# Django Girls Coach Quiz

[Website](https://vaasa-djangogirls.github.io/mentor-quiz)

An **interactive web quiz** inspired by the [Django Girls Tutorial](https://tutorial.djangogirls.org/), designed to help potential coaches evaluate their readiness to become Django Girls coaches.  
This project aims to make self-assessment fun, educational, and aligned with the spirit of open knowledge and community learning.

---

## Features

- Static HTML version of the Django Girls tutorial (`docs/tutorial/`)
- Landing page with quick links to the tutorial and future quiz (`docs/index.html`)
- Placeholder area for the interactive mentor readiness quiz (`docs/quiz/`)
- Fully compliant with the [CC BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/)

---

## About Django Girls

[Django Girls](https://djangogirls.org/) is a global initiative that helps women learn programming by building their first web application using Python and Django.  
The official tutorial is available at [tutorial.djangogirls.org](https://tutorial.djangogirls.org/) and is released under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

---

## License

This project is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license.

> Portions of the content are adapted from the [Django Girls Tutorial](https://tutorial.djangogirls.org/), used under the CC BY-SA 4.0 license.  
> Changes and adaptations have been made for the purpose of creating an interactive quiz experience.

Read the full license text here:  
[https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Regenerate the tutorial HTML

The EPUB distributed with this repository can be re-converted at any time:

```bash
python3 convert_epub.py django-girls-tutorial_en.epub --force
```

The converter writes the HTML version of the book to `docs/tutorial/` and updates supporting assets.

## Publish on GitHub Pages

1. Commit the `docs/` directory alongside the code and push it to GitHub.
2. In the repository settings on GitHub, enable **Pages** and select the **Deploy from branch** option with the branch you pushed and the `/docs` folder.
3. Wait for GitHub Pages to build the site, then visit the published URL.  
   The landing page will appear at `/` with links to:
   - `/tutorial/index.html` – the full Django Girls tutorial split into chapters.
   - `/quiz/index.html` – a “coming soon” placeholder for the coach quiz.

---

## Contributing

Contributions are welcome!
Please make sure any new content or code you add is also shared under the same **CC BY-SA 4.0** license.

---

## Attribution

- Based on the [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- Created by [Amir Mojiri](https://github.com/amirmojiry)

---

**If you find this project useful, please consider starring the repository!**
