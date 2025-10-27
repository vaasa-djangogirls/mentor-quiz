(function () {
  const chapters = [
    { slug: 'index', file: 'index.html', title: 'Contents' },
    { slug: '001-cover', file: '001-cover.html', title: 'Cover' },
    { slug: '003-introduction', file: '003-introduction.html', title: 'Introduction' },
    { slug: '004-installation', file: '004-installation.html', title: 'Installation' },
    { slug: '006-how-the-internet-works', file: '006-how-the-internet-works.html', title: 'How the Internet works' },
    { slug: '007-introduction-to-command-line', file: '007-introduction-to-command-line.html', title: 'Introduction to command line' },
    { slug: '008-python-installation', file: '008-python-installation.html', title: 'Python installation' },
    { slug: '009-code-editor', file: '009-code-editor.html', title: 'Code editor' },
    { slug: '010-introduction-to-python', file: '010-introduction-to-python.html', title: 'Introduction to Python' },
    { slug: '011-what-is-django', file: '011-what-is-django.html', title: 'What is Django?' },
    { slug: '012-django-installation', file: '012-django-installation.html', title: 'Django installation' },
    { slug: '013-your-first-django-project', file: '013-your-first-django-project.html', title: 'Your first Django project!' },
    { slug: '014-django-models', file: '014-django-models.html', title: 'Django models' },
    { slug: '015-django-admin', file: '015-django-admin.html', title: 'Django admin' },
    { slug: '016-deploy', file: '016-deploy.html', title: 'Deploy!' },
    { slug: '017-django-urls', file: '017-django-urls.html', title: 'Django URLs' },
    { slug: '018-django-views-time-to-create', file: '018-django-views-time-to-create.html', title: 'Django views – time to create!' },
    { slug: '019-introduction-to-html', file: '019-introduction-to-html.html', title: 'Introduction to HTML' },
    { slug: '020-django-orm-querysets', file: '020-django-orm-querysets.html', title: 'Django ORM (Querysets)' },
    { slug: '021-dynamic-data-in-templates', file: '021-dynamic-data-in-templates.html', title: 'Dynamic data in templates' },
    { slug: '022-django-templates', file: '022-django-templates.html', title: 'Django templates' },
    { slug: '023-css-make-it-pretty', file: '023-css-make-it-pretty.html', title: 'CSS – make it pretty' },
    { slug: '024-template-extending', file: '024-template-extending.html', title: 'Template extending' },
    { slug: '025-extend-your-application', file: '025-extend-your-application.html', title: 'Extend your application' },
    { slug: '026-django-forms', file: '026-django-forms.html', title: 'Django Forms' },
    { slug: '027-what-s-next', file: '027-what-s-next.html', title: "What's next?" }
  ];

  const icons = {
    menu: '≡',
    home: '⌂',
    contents: '≣',
    prev: '←',
    next: '→'
  };

  function createElement(tag, attrs = {}, children = []) {
    const el = document.createElement(tag);
    Object.entries(attrs).forEach(([key, value]) => {
      if (value === null || value === undefined) {
        return;
      }
      if (key === 'className') {
        el.className = value;
      } else if (key === 'text') {
        el.textContent = value;
      } else {
        el.setAttribute(key, value);
      }
    });
    children.forEach((child) => {
      if (typeof child === 'string') {
        el.appendChild(document.createTextNode(child));
      } else if (child) {
        el.appendChild(child);
      }
    });
    return el;
  }


  function attachBackToTop() {
    if (document.querySelector('.back-to-top')) {
      return;
    }
    const button = createElement('button', {
      className: 'back-to-top',
      type: 'button',
      'aria-label': 'Back to top'
    }, [
      createElement('span', { className: 'icon', 'aria-hidden': 'true', text: '↑' })
    ]);
    button.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    const handleScroll = () => {
      if (window.scrollY > 280) {
        button.classList.add('visible');
      } else {
        button.classList.remove('visible');
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
    document.body.appendChild(button);
  }

  function buildNav(chapterSlug) {
    const index = chapters.findIndex((ch) => ch.slug === chapterSlug);
    if (index === -1) {
      return null;
    }

    const chapter = chapters[index];
    const isContentsPage = chapter.slug === 'index';
    const prev = chapters[index - 1] || null;
    const next = chapters[index + 1] || null;

    const drawerId = `nav-panel-${chapter.slug}`;

    const nav = createElement('nav', {
      className: 'book-nav',
      'data-chapter': chapter.slug
    });

    const toggle = createElement('button', {
      className: 'nav-toggle',
      type: 'button',
      'aria-expanded': 'false',
      'aria-controls': drawerId,
      'data-target': drawerId,
      'aria-label': 'Toggle menu'
    }, [
      createElement('span', { className: 'icon', 'aria-hidden': 'true', text: icons.menu }),
      createElement('span', { className: 'label', text: 'Menu' })
    ]);

    const links = createElement('div', { className: 'nav-links' });

    function navLink(href, label, icon, extraClass = '') {
      const commonChildren = [
        createElement('span', { className: 'icon', 'aria-hidden': 'true', text: icon }),
        createElement('span', { className: 'label', text: label })
      ];
      if (!href) {
        return createElement('span', {
          className: `nav-link disabled ${extraClass}`.trim(),
          'aria-disabled': 'true'
        }, commonChildren);
      }
      return createElement('a', { className: `nav-link ${extraClass}`.trim(), href }, commonChildren);
    }

    links.appendChild(navLink('../index.html', 'Home', icons.home, 'home'));
    const contentsHref = isContentsPage ? null : 'index.html';
    links.appendChild(navLink(contentsHref, 'Contents', icons.contents, 'contents'));
    links.appendChild(navLink(prev ? prev.file : null, 'Previous', icons.prev, 'previous'));
    links.appendChild(navLink(next ? next.file : null, 'Next', icons.next, 'next'));

    const panel = createElement('div', {
      className: 'nav-panel',
      id: drawerId,
      'aria-hidden': 'true'
    });

    function buildGroup(title, items, currentFile) {
      const ul = createElement('ul', { className: 'nav-panel__list' });
      items.forEach(({ href, label, icon }) => {
        const children = [];
        if (icon) {
          children.push(createElement('span', { className: 'icon', 'aria-hidden': 'true', text: icon }));
        }
        children.push(label);
        const isCurrent = href && href === currentFile;
        let link;
        if (!href) {
          link = createElement('span', { className: 'nav-panel__link disabled', 'aria-disabled': 'true' }, children);
        } else {
          link = createElement('a', {
            className: `nav-panel__link${isCurrent ? ' is-active' : ''}`,
            href
          }, children);
        }
        const item = createElement('li', {}, [link]);
        ul.appendChild(item);
      });
      const group = createElement('div', { className: 'nav-panel__group' }, [
        createElement('h3', { className: 'nav-panel__title', text: title }),
        ul
      ]);
      return group;
    }

    const shortcuts = [
      { href: '../index.html', label: 'Home', icon: icons.home },
      { href: contentsHref, label: 'Contents', icon: icons.contents }
    ];
    if (prev) {
      shortcuts.push({ href: prev.file, label: 'Previous', icon: icons.prev });
    }
    if (next) {
      shortcuts.push({ href: next.file, label: 'Next', icon: icons.next });
    }

    panel.appendChild(buildGroup('Shortcuts', shortcuts, chapter.file));
    panel.appendChild(buildGroup('Chapters', chapters.map((ch) => ({ href: ch.file, label: ch.title })), chapter.file));

    nav.appendChild(toggle);
    nav.appendChild(links);

    return { nav, panel, toggle };
  }

  function attachNav() {
    const slug = document.body.dataset.chapter;
    if (!slug) {
      return;
    }

    const header = document.querySelector('header.book-header');
    const main = document.querySelector('main');
    if (!header || !main) {
      return;
    }

    const built = buildNav(slug);
    if (!built) {
      return;
    }

    const { nav, panel, toggle } = built;

    header.insertAdjacentElement('afterend', nav);
    nav.insertAdjacentElement('afterend', panel);

    const drawer = panel;

    function closeDrawer() {
      drawer.classList.remove('open');
      drawer.setAttribute('aria-hidden', 'true');
      toggle.setAttribute('aria-expanded', 'false');
      document.removeEventListener('keydown', onKeyDown);
      document.removeEventListener('click', onDocumentClick, true);
    }

    function openDrawer() {
      drawer.classList.add('open');
      drawer.setAttribute('aria-hidden', 'false');
      toggle.setAttribute('aria-expanded', 'true');
      document.addEventListener('keydown', onKeyDown);
      document.addEventListener('click', onDocumentClick, true);
      const firstLink = drawer.querySelector('a');
      if (firstLink) {
        firstLink.focus();
      }
    }

    function onKeyDown(event) {
      if (event.key === 'Escape') {
        closeDrawer();
        toggle.focus();
      }
    }

    function onDocumentClick(event) {
      if (!drawer.contains(event.target) && event.target !== toggle && !toggle.contains(event.target)) {
        closeDrawer();
      }
    }

    toggle.addEventListener('click', () => {
      const isOpen = drawer.classList.contains('open');
      if (isOpen) {
        closeDrawer();
      } else {
        openDrawer();
      }
    });

    drawer.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeDrawer);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachNav);
  } else {
    attachNav();
  }
})();
