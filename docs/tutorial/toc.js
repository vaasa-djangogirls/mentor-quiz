(function () {
  if (document.body.dataset.chapter === 'index') {
    return;
  }

  const slugCache = new Set();

  function slugify(text) {
    const base = text
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9\s-]/g, '')
      .replace(/\s+/g, '-');
    let slug = base || 'section';
    let counter = 1;
    while (slugCache.has(slug)) {
      counter += 1;
      slug = `${base || 'section'}-${counter}`;
    }
    slugCache.add(slug);
    return slug;
  }

  function buildTOC() {
    const main = document.querySelector('main');
    if (!main) {
      return;
    }

    const content = main.querySelector('.page') || main;
    const headings = Array.from(
      content.querySelectorAll('h2, h3, h4, h5, h6')
    ).filter((heading) => heading.textContent.trim().length > 0);

    if (!headings.length) {
      return;
    }

    headings.forEach((heading) => {
      if (!heading.id) {
        heading.id = slugify(heading.textContent);
      }
    });

    const panelId = `page-toc-${document.body.dataset.chapter || 'page'}`;

    const toc = document.createElement('aside');
    toc.className = 'page-toc';

    const toggle = document.createElement('button');
    toggle.className = 'page-toc__toggle';
    toggle.type = 'button';
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', panelId);
    toggle.setAttribute('aria-label', 'Toggle page outline');
    toggle.innerHTML = '<span class="icon" aria-hidden="true">▸</span><span class="label">On this page</span>';

    const panel = document.createElement('div');
    panel.className = 'page-toc__panel';
    panel.id = panelId;

    const list = document.createElement('ul');
    list.className = 'page-toc__list';

    const stack = [{ level: 1, list }];

    headings.forEach((heading) => {
      const level = Number(heading.tagName.slice(1));
      while (stack.length && level <= stack[stack.length - 1].level) {
        stack.pop();
      }
      const parentList = stack[stack.length - 1].list;
      const item = document.createElement('li');
      item.className = `toc-level toc-level-${level}`;
      const link = document.createElement('a');
      link.href = `#${heading.id}`;
      link.textContent = heading.textContent.trim();
      item.appendChild(link);
      parentList.appendChild(item);

      const subList = document.createElement('ul');
      subList.className = 'page-toc__sublist';
      item.appendChild(subList);
      stack.push({ level, list: subList });
    });

    list.querySelectorAll('ul').forEach((subList) => {
      if (!subList.children.length) {
        subList.remove();
      }
    });

    panel.appendChild(list);
    toc.appendChild(toggle);
    toc.appendChild(panel);

    const insertionPoint = main.querySelector('.page');
    if (insertionPoint) {
      main.insertBefore(toc, insertionPoint);
    } else {
      main.insertBefore(toc, main.firstChild);
    }

    toggle.addEventListener('click', () => {
      const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!isExpanded));
      toc.classList.toggle('open', !isExpanded);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildTOC);
  } else {
    buildTOC();
  }
})();
