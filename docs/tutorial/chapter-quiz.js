(function () {
  const containers = Array.from(document.querySelectorAll('.chapter-quiz[data-section-id]'));
  if (!containers.length) {
    return;
  }

  function shuffle(list) {
    const arr = list.slice();
    for (let i = arr.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  function createEl(tag, className, text) {
    const el = document.createElement(tag);
    if (className) {
      el.className = className;
    }
    if (text !== undefined) {
      el.textContent = text;
    }
    return el;
  }

  function prepareQuestions(section) {
    const questionOrder = shuffle(section.questions || []);
    return questionOrder.map((question) => {
      const paired = question.options.map((option, index) => ({
        text: option,
        isCorrect: index === question.answerIndex
      }));
      const shuffled = shuffle(paired);
      const answerIndex = shuffled.findIndex((opt) => opt.isCorrect);
      return {
        prompt: question.prompt,
        options: shuffled.map((opt) => opt.text),
        answerIndex
      };
    });
  }

  function getScoreMeta(percentage) {
    if (percentage >= 80) {
      return { cls: 'chapter-quiz__score--high', message: "Fantastic! You're on top of this chapter." };
    }
    if (percentage >= 50) {
      return { cls: 'chapter-quiz__score--mid', message: 'Good progress—review a few spots and try again.' };
    }
    return { cls: 'chapter-quiz__score--low', message: 'No worries! Revisit the content and give it another go.' };
  }

  function setupQuiz(container, section) {
    const app = container.querySelector('.chapter-quiz__app');
    if (!app) {
      return;
    }

    function renderError(message) {
      app.innerHTML = '';
      app.appendChild(createEl('p', 'chapter-quiz__error', message));
    }

    const state = {
      questions: prepareQuestions(section),
      records: [],
      index: 0
    };

    function resetState() {
      state.questions = prepareQuestions(section);
      state.records = [];
      state.index = 0;
    }

    function renderIntro() {
      app.innerHTML = '';
      const card = createEl('div', 'chapter-quiz__card');
      card.appendChild(createEl('p', 'chapter-quiz__meta', `${state.questions.length} practice questions`));
      const title = createEl('h3', 'chapter-quiz__question', 'Ready for a quick check-in?');
      card.appendChild(title);
      card.appendChild(createEl('p', 'chapter-quiz__tip', 'Answer each question, then review which ones to revisit.'));
      const actions = createEl('div', 'chapter-quiz__actions chapter-quiz__actions--center');
      const btn = createEl('button', 'chapter-quiz__button chapter-quiz__button--primary', 'Start quiz');
      btn.type = 'button';
      btn.addEventListener('click', () => {
        resetState();
        renderQuestion();
      });
      actions.appendChild(btn);
      card.appendChild(actions);
      app.appendChild(card);
    }

    function renderQuestion() {
      const question = state.questions[state.index];
      if (!question) {
        renderError('This quiz is unavailable right now.');
        return;
      }

      app.innerHTML = '';
      const form = document.createElement('form');
      form.className = 'chapter-quiz__card';

      form.appendChild(createEl('p', 'chapter-quiz__meta', `Question ${state.index + 1} of ${state.questions.length}`));
      form.appendChild(createEl('h3', 'chapter-quiz__question', question.prompt));

      const fieldset = createEl('fieldset', 'chapter-quiz__options');
      question.options.forEach((optionText, optionIndex) => {
        const label = createEl('label', 'chapter-quiz__option');
        const input = document.createElement('input');
        input.type = 'radio';
        input.name = 'answer';
        input.value = String(optionIndex);
        label.appendChild(input);
        const text = document.createElement('span');
        text.textContent = optionText;
        label.appendChild(text);
        fieldset.appendChild(label);
      });
      form.appendChild(fieldset);

      const alert = createEl('div', 'chapter-quiz__alert', 'Choose an answer before continuing.');
      form.appendChild(alert);

      const actions = createEl('div', 'chapter-quiz__actions');
      const submit = createEl(
        'button',
        'chapter-quiz__button chapter-quiz__button--primary',
        state.index === state.questions.length - 1 ? 'See results' : 'Next question'
      );
      submit.type = 'submit';
      actions.appendChild(submit);
      form.appendChild(actions);

      form.addEventListener('submit', (event) => {
        event.preventDefault();
        const formData = new FormData(form);
        const selected = formData.get('answer');
        if (selected === null) {
          alert.style.display = 'block';
          return;
        }
        alert.style.display = 'none';
        const selectedIndex = Number(selected);
        const record = {
          prompt: question.prompt,
          options: question.options,
          answerIndex: question.answerIndex,
          selectedIndex,
          isCorrect: selectedIndex === question.answerIndex
        };
        state.records.push(record);
        if (state.index === state.questions.length - 1) {
          renderResults();
        } else {
          state.index += 1;
          renderQuestion();
        }
      });

      app.appendChild(form);
      container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function renderResults() {
      const total = state.records.length;
      const correct = state.records.filter((record) => record.isCorrect).length;
      const percentage = total ? Math.round((correct / total) * 100) : 0;
      const meta = getScoreMeta(percentage);

      app.innerHTML = '';
      const card = createEl('div', 'chapter-quiz__card');

      const score = createEl('div', `chapter-quiz__score ${meta.cls}`);
      score.appendChild(createEl('p', null, `You answered ${correct} of ${total} correctly (${percentage}%).`));
      score.appendChild(createEl('p', null, meta.message));
      card.appendChild(score);

      const reviewList = createEl('div', 'chapter-quiz__review');
      state.records.forEach((record, index) => {
        const item = createEl(
          'article',
          `chapter-quiz__review-item ${record.isCorrect ? 'correct' : 'incorrect'}`
        );
        item.appendChild(createEl('h4', null, `Question ${index + 1}`));

        const prompt = createEl('p');
        const promptLabel = createEl('strong', null, 'Prompt: ');
        prompt.appendChild(promptLabel);
        prompt.append(record.prompt);
        item.appendChild(prompt);

        const yourAnswer = createEl('p');
        const yourLabel = createEl('strong', null, 'Your answer: ');
        yourAnswer.appendChild(yourLabel);
        yourAnswer.append(record.options[record.selectedIndex] || 'No answer selected');
        item.appendChild(yourAnswer);

        const correctAnswer = createEl('p');
        const correctLabel = createEl('strong', null, 'Correct answer: ');
        correctAnswer.appendChild(correctLabel);
        correctAnswer.append(record.options[record.answerIndex]);
        item.appendChild(correctAnswer);

        const statusText = record.isCorrect ? 'Correct! Nicely done.' : 'Incorrect. Worth another look.';
        const status = createEl('p', null, statusText);
        item.appendChild(status);

        reviewList.appendChild(item);
      });
      card.appendChild(reviewList);

      const actions = createEl('div', 'chapter-quiz__actions chapter-quiz__actions--center');
      const retry = createEl('button', 'chapter-quiz__button chapter-quiz__button--primary', 'Retake quiz');
      retry.type = 'button';
      retry.addEventListener('click', () => {
        resetState();
        renderQuestion();
      });
      actions.appendChild(retry);
      const reviewChapter = createEl('button', 'chapter-quiz__button chapter-quiz__button--secondary', 'Back to start');
      reviewChapter.type = 'button';
      reviewChapter.addEventListener('click', () => {
        resetState();
        renderIntro();
        container.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
      actions.appendChild(reviewChapter);
      card.appendChild(actions);

      app.appendChild(card);
      container.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    renderIntro();
  }

  function handleData(container, sectionId, data) {
    const app = container.querySelector('.chapter-quiz__app');
    const sections = Array.isArray(data.sections) ? data.sections : [];
    const section = sections.find((item) => item.id === sectionId);
    if (!section || !Array.isArray(section.questions) || !section.questions.length) {
      if (app) {
        app.innerHTML = '';
        app.appendChild(createEl('p', 'chapter-quiz__error', 'No quiz questions available yet for this chapter.'));
      }
      return;
    }
    setupQuiz(container, section);
  }

  const dataPromise = fetch('../quiz/questions.json')
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Failed to load questions.json: ${response.status}`);
      }
      return response.json();
    })
    .catch((error) => {
      console.error('Failed to fetch chapter quiz data', error);
      return Promise.reject(error);
    });

  containers.forEach((container) => {
    const sectionId = container.dataset.sectionId;
    if (!sectionId) {
      return;
    }
    const app = container.querySelector('.chapter-quiz__app');
    dataPromise
      .then((data) => {
        handleData(container, sectionId, data);
      })
      .catch(() => {
        if (app) {
          app.innerHTML = '';
          app.appendChild(
            createEl(
              'p',
              'chapter-quiz__error',
              'We could not load the quiz questions. Please refresh and try again.'
            )
          );
        }
      });
  });
})();
