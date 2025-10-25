#!/usr/bin/env python3
"""Generate the quiz question bank JSON for the Django Girls coach quiz."""

from __future__ import annotations

import json
from pathlib import Path


def q(prompt: str, options: list[str], answer_index: int, explanation: str | None = None) -> dict:
    return {
        "prompt": prompt,
        "options": options,
        "answerIndex": answer_index,
        **({"explanation": explanation} if explanation else {}),
    }


QUESTION_BANK = [
    {
        "id": "introduction",
        "title": "Introduction",
        "tutorialPath": "../tutorial/003-introduction.html",
        "questions": [
            q(
                "What primary outcome does the Django Girls Tutorial promise once you finish it?",
                [
                    "You will have a small blog application online",
                    "You will have learned how to deploy a machine learning model",
                    "You will have written a fully featured social network",
                    "You will have mastered every Python standard library module",
                ],
                0,
            ),
            q(
                "Why do the authors emphasize that programming is not as hard as it seems?",
                [
                    "Because the tutorial automates every step so you never write code",
                    "Because with patient explanations, intimidating topics become approachable",
                    "Because the web workshop is only for people who already know JavaScript",
                    "Because the tutorial takes less than an hour to complete",
                ],
                1,
            ),
            q(
                "What tone does the tutorial set for newcomers at the beginning?",
                [
                    "Welcoming and encouraging",
                    "Competitive and test-focused",
                    "Strict and exam oriented",
                    "Formal and academic",
                ],
                0,
            ),
            q(
                "Which Creative Commons license covers the Django Girls Tutorial?",
                [
                    "CC BY-SA 4.0",
                    "CC BY-ND 2.0",
                    "CC0",
                    "GPLv3",
                ],
                0,
            ),
            q(
                "What format does the tutorial suggest you will build during the workshop?",
                [
                    "A blog-style web application",
                    "A command-line calculator",
                    "A desktop note-taking app",
                    "A multiplayer game server",
                ],
                0,
            ),
            q(
                "Why does the tutorial highlight videos being produced for at-home learners?",
                [
                    "To ensure only workshop attendees can learn",
                    "To support readers who cannot join an in-person event",
                    "To replace all written instructions with video",
                    "To promote unrelated courses",
                ],
                1,
            ),
            q(
                "What does the introduction encourage you to feel about technology?",
                [
                    "It is exciting and you can learn to love it",
                    "It is too complex to start with",
                    "It requires advanced mathematics first",
                    "It is only for professional engineers",
                ],
                0,
            ),
            q(
                "Which organization maintains the tutorial?",
                [
                    "Django Girls",
                    "Python Software Foundation",
                    "Linux Foundation",
                    "Mozilla",
                ],
                0,
            ),
            q(
                "What is a suggested mindset when approaching the tutorial?",
                [
                    "Treat it as an adventure and stay curious",
                    "Rush to the end without reading explanations",
                    "Memorize every detail before trying code",
                    "Avoid asking questions until you master everything",
                ],
                0,
            ),
            q(
                "What is one way the tutorial invites participants to contribute back?",
                [
                    "By opening pull requests or issues on GitHub",
                    "By keeping their improvements private",
                    "By paying a licensing fee",
                    "By rewriting the tutorial in another framework without permission",
                ],
                0,
            ),
        ],
    },
    {
        "id": "installation",
        "title": "Installation",
        "tutorialPath": "../tutorial/004-installation.html",
        "questions": [
            q(
                "Which operating systems does the tutorial explicitly provide installation instructions for?",
                [
                    "Windows, macOS, and Linux",
                    "Windows and Android only",
                    "macOS and iOS only",
                    "Linux and ChromeOS only",
                ],
                0,
            ),
            q(
                "Why does the tutorial ask you to install Python and Django locally?",
                [
                    "So you can write and run code directly on your own computer",
                    "So you can avoid ever using the terminal",
                    "So you can skip deploying the project",
                    "So you can uninstall other programming languages",
                ],
                0,
            ),
            q(
                "What package manager does the tutorial recommend for Windows users to install Python?",
                [
                    "The official Python installer from python.org",
                    "Homebrew",
                    "apt-get",
                    "MacPorts",
                ],
                0,
            ),
            q(
                "What is the main reason for installing a virtual environment tool?",
                [
                    "To isolate project dependencies from the system Python",
                    "To enable offline browsing of documentation",
                    "To back up the hard drive automatically",
                    "To improve graphics performance",
                ],
                0,
            ),
            q(
                "Which command-line tool does the tutorial suggest you verify after installation?",
                [
                    "python --version",
                    "node --version",
                    "java --version",
                    "ruby --version",
                ],
                0,
            ),
            q(
                "Why is Git installed during the setup steps?",
                [
                    "To manage source code versions and collaborate",
                    "To draw wireframes for the project",
                    "To compile C extensions manually",
                    "To host databases locally",
                ],
                0,
            ),
            q(
                "What does the tutorial recommend using to store your project code online?",
                [
                    "GitHub",
                    "Dropbox",
                    "Google Drive",
                    "A USB stick",
                ],
                0,
            ),
            q(
                "Which browser tool is suggested for editing or copying commands accurately?",
                [
                    "Using copy & paste carefully from the tutorial snippets",
                    "Downloading a browser extension",
                    "Printing the commands and typing from paper",
                    "Using voice dictation",
                ],
                0,
            ),
            q(
                "Why does the tutorial mention administrator or sudo privileges?",
                [
                    "Because some installations need elevated permissions",
                    "Because the tutorial modifies BIOS settings",
                    "Because the tutorial installs system-wide themes",
                    "Because the tutorial encrypts the disk",
                ],
                0,
            ),
            q(
                "What should you do if a command fails during installation?",
                [
                    "Read the error message, double-check spelling, and ask a coach for help",
                    "Ignore it and continue without fixing",
                    "Restart the computer immediately without reading the error",
                    "Assume the tutorial is outdated and stop",
                ],
                0,
            ),
        ],
    },
    {
        "id": "how-the-internet-works",
        "title": "How the Internet works",
        "tutorialPath": "../tutorial/006-how-the-internet-works.html",
        "questions": [
            q(
                "Which components are described as working together when you visit a website?",
                [
                    "Browser, server, and internet connection",
                    "Router, printer, and monitor",
                    "Keyboard, mouse, and CPU fan",
                    "Camera, microphone, and speakers",
                ],
                0,
            ),
            q(
                "What is the role of a web server in the tutorial's explanation?",
                [
                    "It receives requests and sends back responses such as HTML pages",
                    "It renders graphics directly on the user's screen",
                    "It manufactures physical cables",
                    "It encrypts Wi-Fi networks automatically",
                ],
                0,
            ),
            q(
                "Which protocol is highlighted as the common language between browsers and servers?",
                [
                    "HTTP",
                    "FTP",
                    "SMTP",
                    "SSH",
                ],
                0,
            ),
            q(
                "What does DNS help you do according to the tutorial?",
                [
                    "Translate human-readable domain names into IP addresses",
                    "Compress images before uploading",
                    "Write SQL queries for databases",
                    "Design responsive layouts",
                ],
                0,
            ),
            q(
                "Which statement best describes an IP address in the tutorial?",
                [
                    "A numeric label that identifies a device on a network",
                    "A password used to login to a router",
                    "A secret key you share only with friends",
                    "A programming language for the internet",
                ],
                0,
            ),
            q(
                "What happens when you type a URL into the browser bar?",
                [
                    "The browser creates an HTTP request and asks a server for a resource",
                    "The browser installs new software on your computer",
                    "The browser edits the server configuration",
                    "The browser sends your password to the ISP",
                ],
                0,
            ),
            q(
                "Why are packets important in networking as described in the tutorial?",
                [
                    "They break data into small pieces that can travel across the internet reliably",
                    "They store user passwords securely",
                    "They act as backup power supplies",
                    "They provide hardware acceleration",
                ],
                0,
            ),
            q(
                "Which example does the tutorial use to show how many systems work together on the internet?",
                [
                    "Requesting a web page through a browser",
                    "Sending a text message on a phone",
                    "Printing a document",
                    "Editing a spreadsheet offline",
                ],
                0,
            ),
            q(
                "What metaphor does the tutorial use to help explain a request/response cycle?",
                [
                    "Ordering a coffee and receiving it from a barista",
                    "Building a house with bricks",
                    "Driving a car on a highway",
                    "Solving a jigsaw puzzle",
                ],
                0,
            ),
            q(
                "What is one takeaway from this chapter for new web developers?",
                [
                    "Understanding the basics of how requests reach servers helps you reason about web apps",
                    "You never need to know how browsers talk to servers",
                    "Only network engineers worry about HTTP",
                    "Front-end code runs on the server only",
                ],
                0,
            ),
        ],
    },
    {
        "id": "introduction-to-command-line",
        "title": "Introduction to command line",
        "tutorialPath": "../tutorial/007-introduction-to-command-line.html",
        "questions": [
            q(
                "What is the command line primarily used for in the tutorial?",
                [
                    "Running commands to interact with your computer using text",
                    "Designing user interfaces visually",
                    "Recording audio notes for the project",
                    "Editing photos for the website",
                ],
                0,
            ),
            q(
                "What does the command pwd display?",
                [
                    "The current working directory",
                    "The number of files in a folder",
                    "The current Python version",
                    "The password for your user account",
                ],
                0,
            ),
            q(
                "Which command do you use to list files in a directory on most systems?",
                [
                    "ls",
                    "open",
                    "dircreate",
                    "env",
                ],
                0,
            ),
            q(
                "What is the purpose of the cd command?",
                [
                    "To change directories",
                    "To compile code",
                    "To copy files",
                    "To delete directories",
                ],
                0,
            ),
            q(
                "Why does the tutorial emphasize careful typing in the terminal?",
                [
                    "Because small typos can cause commands to fail",
                    "Because the terminal randomly changes characters",
                    "Because the terminal has autocorrect",
                    "Because every command runs twice",
                ],
                0,
            ),
            q(
                "Which key shortcut is highlighted to stop a running command?",
                [
                    "Ctrl + C",
                    "Ctrl + S",
                    "Alt + F4",
                    "Shift + Enter",
                ],
                0,
            ),
            q(
                "What command creates a new directory?",
                [
                    "mkdir",
                    "rmdir",
                    "touch",
                    "nano",
                ],
                0,
            ),
            q(
                "What symbol represents your home directory in many shells?",
                [
                    "~",
                    "#",
                    "@",
                    "%",
                ],
                0,
            ),
            q(
                "Which of these is a benefit of learning terminal basics according to the tutorial?",
                [
                    "Many developer tools expect you to use the command line",
                    "You can uninstall the operating system",
                    "You can skip learning version control",
                    "You can avoid writing code altogether",
                ],
                0,
            ),
            q(
                "Why does the tutorial ask you to practice simple navigation commands?",
                [
                    "To build confidence before running project commands later",
                    "To memorize every possible terminal command",
                    "To learn how to customize your desktop wallpaper",
                    "To obtain administrator access to other computers",
                ],
                0,
            ),
        ],
    },
    {
        "id": "python-installation",
        "title": "Python installation",
        "tutorialPath": "../tutorial/008-python-installation.html",
        "questions": [
            q(
                "What version of Python does the tutorial expect you to install?",
                [
                    "Python 3 (the latest stable 3.x release)",
                    "Python 2.5",
                    "Python 1.0",
                    "Micropython",
                ],
                0,
            ),
            q(
                "Why is it important to add Python to your PATH during installation?",
                [
                    "So you can run python from any directory in the terminal",
                    "So Python can access your camera",
                    "So you can uninstall other languages",
                    "So the installer can update your BIOS",
                ],
                0,
            ),
            q(
                "What tool does the tutorial recommend for creating virtual environments?",
                [
                    "python -m venv",
                    "virtualbox",
                    "conda",
                    "docker",
                ],
                0,
            ),
            q(
                "Which command activates a virtual environment on Windows?",
                [
                    "env\\Scripts\\activate",
                    "source env/bin/activate",
                    "./activate.sh",
                    "activate_env.exe",
                ],
                0,
            ),
            q(
                "Which command activates a virtual environment on macOS or Linux?",
                [
                    "source env/bin/activate",
                    "env\\Scripts\\activate",
                    "launchctl env",
                    "python activate",
                ],
                0,
            ),
            q(
                "What package installer does the tutorial use to install Django and other packages?",
                [
                    "pip",
                    "npm",
                    "gem",
                    "composer",
                ],
                0,
            ),
            q(
                "Why does the tutorial show how to upgrade pip?",
                [
                    "To ensure you have the latest features and bug fixes when installing packages",
                    "To enable pip to run offline",
                    "To remove the need for a virtual environment",
                    "To compile packages faster",
                ],
                0,
            ),
            q(
                "Which command verifies the currently installed Django version?",
                [
                    "python -m django --version",
                    "django-admin version",
                    "pip list django",
                    "django --help version",
                ],
                0,
            ),
            q(
                "Why does the tutorial instruct you to deactivate the virtual environment when done?",
                [
                    "To return to your system Python and avoid accidental package installs",
                    "To delete the project files",
                    "To reset your terminal prompt",
                    "To upgrade your operating system",
                ],
                0,
            ),
            q(
                "What is the benefit of installing Python before the workshop begins?",
                [
                    "You spend workshop time creating instead of troubleshooting setup",
                    "You can avoid learning the command line",
                    "You can skip the tutorial entirely",
                    "You can run Django projects on a tablet",
                ],
                0,
            ),
        ],
    },
    {
        "id": "code-editor",
        "title": "Code editor",
        "tutorialPath": "../tutorial/009-code-editor.html",
        "questions": [
            q(
                "Why does the tutorial recommend using a dedicated code editor instead of a word processor?",
                [
                    "Code editors understand programming languages and avoid formatting issues",
                    "Word processors automatically run your code",
                    "Code editors require no learning curve",
                    "Word processors are faster for editing large files",
                ],
                0,
            ),
            q(
                "Which feature is highlighted as helpful in a code editor for new developers?",
                [
                    "Syntax highlighting",
                    "3D rendering",
                    "Built-in music player",
                    "Automatic spreadsheet creation",
                ],
                0,
            ),
            q(
                "Why does the tutorial suggest enabling automatic indentation?",
                [
                    "Because Python relies on indentation to define code blocks",
                    "Because it makes your code colorful",
                    "Because it lets you avoid learning loops",
                    "Because it prevents runtime errors entirely",
                ],
                0,
            ),
            q(
                "Which editors does the tutorial mention as good options?",
                [
                    "Visual Studio Code, Atom, and Sublime Text",
                    "Microsoft Word and LibreOffice",
                    "Photoshop and GIMP",
                    "GarageBand and Audacity",
                ],
                0,
            ),
            q(
                "What is a common shortcut for saving files that the tutorial encourages remembering?",
                [
                    "Ctrl/Command + S",
                    "Ctrl/Command + Q",
                    "Ctrl/Command + Z",
                    "Ctrl/Command + P",
                ],
                0,
            ),
            q(
                "Why is it important to know where your editor stores files?",
                [
                    "So you can find them later to run or commit",
                    "So you can delete the entire project",
                    "So you can move them to your desktop for backups",
                    "So you can email them to yourself automatically",
                ],
                0,
            ),
            q(
                "Which tip helps avoid mixed line endings when collaborating?",
                [
                    "Configuring the editor to use UTF-8 and consistent newline settings",
                    "Disabling autosave",
                    "Using multiple editors at the same time",
                    "Copying code into a spreadsheet first",
                ],
                0,
            ),
            q(
                "What does the tutorial recommend doing if the editor auto-completion surprises you?",
                [
                    "Slow down and learn what the editor inserted before running code",
                    "Disable the editor and switch to a word processor",
                    "Ignore the change and continue coding",
                    "Install a browser extension instead",
                ],
                0,
            ),
            q(
                "Why is opening the project folder in your editor useful?",
                [
                    "It keeps all files organized and visible in one place",
                    "It automatically deploys the project to production",
                    "It encrypts your code",
                    "It prevents syntax errors",
                ],
                0,
            ),
            q(
                "What habit does the tutorial encourage before running your program?",
                [
                    "Saving your changes so your latest code executes",
                    "Restarting your computer",
                    "Clearing your browser cache",
                    "Unplugging from the internet",
                ],
                0,
            ),
        ],
    },
    {
        "id": "introduction-to-python",
        "title": "Introduction to Python",
        "tutorialPath": "../tutorial/010-introduction-to-python.html",
        "questions": [
            q(
                "What Python function prints output to the screen?",
                [
                    "print()",
                    "echo()",
                    "say()",
                    "display()",
                ],
                0,
            ),
            q(
                "How is a string value defined in Python?",
                [
                    "Characters wrapped in quotes",
                    "Numbers without quotes",
                    "By using curly braces only",
                    "By prefixing with a # symbol",
                ],
                0,
            ),
            q(
                "Which symbol is used for comments in Python?",
                [
                    "#",
                    "//",
                    "<!-- -->",
                    "/* */",
                ],
                0,
            ),
            q(
                "What does the tutorial say about indentation in Python?",
                [
                    "It is significant and defines code blocks",
                    "It is optional and just for style",
                    "It must always be tabs, never spaces",
                    "It resets variables automatically",
                ],
                0,
            ),
            q(
                "Which data structure stores an ordered collection of items?",
                [
                    "List",
                    "Dictionary",
                    "Set",
                    "Tuple",
                ],
                0,
            ),
            q(
                "How do you define a function in Python?",
                [
                    "Using the def keyword followed by the function name",
                    "Using the function keyword",
                    "Typing func and the name",
                    "By writing the name with parentheses only",
                ],
                0,
            ),
            q(
                "What does the tutorial teach about loops?",
                [
                    "They let you repeat actions, such as iterating over a list",
                    "They remove the need for functions",
                    "They change integers into strings automatically",
                    "They are only available in JavaScript",
                ],
                0,
            ),
            q(
                "Which keyword starts a conditional block in Python?",
                [
                    "if",
                    "when",
                    "switch",
                    "check",
                ],
                0,
            ),
            q(
                "What is the value of len([1, 2, 3])?",
                [
                    "3",
                    "2",
                    "1",
                    "0",
                ],
                0,
            ),
            q(
                "Why does the tutorial encourage experimentation in the Python shell?",
                [
                    "It helps you quickly test concepts and see immediate feedback",
                    "It replaces the need to write scripts",
                    "It lets you skip saving files",
                    "It is required before learning Django",
                ],
                0,
            ),
        ],
    },
    {
        "id": "what-is-django",
        "title": "What is Django?",
        "tutorialPath": "../tutorial/011-what-is-django.html",
        "questions": [
            q(
                "How does the tutorial describe Django?",
                [
                    "A high-level Python web framework",
                    "A low-level operating system kernel",
                    "A JavaScript front-end library",
                    "A database engine",
                ],
                0,
            ),
            q(
                "What is one benefit of using a web framework like Django?",
                [
                    "It handles common tasks so you can focus on your application logic",
                    "It removes the need to learn Python fundamentals",
                    "It automatically writes your project requirements",
                    "It only works for static sites",
                ],
                0,
            ),
            q(
                "Which architectural pattern does Django encourage?",
                [
                    "Model-View-Template (MVT)",
                    "Model-View-Controller (MVC)",
                    "Event-Driven Architecture",
                    "Entity-Component-System",
                ],
                0,
            ),
            q(
                "What is Django best suited for according to the tutorial?",
                [
                    "Building web applications quickly and cleanly",
                    "Designing mobile operating systems",
                    "Rendering 3D games",
                    "Compiling C programs",
                ],
                0,
            ),
            q(
                "What does the tutorial highlight about Django's community?",
                [
                    "It is large, friendly, and provides extensive documentation",
                    "It is closed and private",
                    "It only accepts expert developers",
                    "It is focused on proprietary plugins",
                ],
                0,
            ),
            q(
                "Which part of a web app does Django help you manage?",
                [
                    "Server-side logic and database interactions",
                    "GPU rendering pipelines",
                    "Mobile push notifications",
                    "Desktop window management",
                ],
                0,
            ),
            q(
                "What is one reason Django is great for beginners?",
                [
                    "It provides batteries-included features like admin and authentication",
                    "It requires writing assembly code first",
                    "It only runs on supercomputers",
                    "It has no documentation to read",
                ],
                0,
            ),
            q(
                "Why does the tutorial compare Django to a builder's toolkit?",
                [
                    "Because it offers reusable components to assemble applications faster",
                    "Because it includes 3D printing instructions",
                    "Because it builds houses literally",
                    "Because it sells physical hardware",
                ],
                0,
            ),
            q(
                "What does the tutorial suggest you can create with Django?",
                [
                    "Blogs, news sites, social networks, and many other web apps",
                    "Only command-line utilities",
                    "Only mobile games",
                    "Only desktop spreadsheets",
                ],
                0,
            ),
            q(
                "How does Django help enforce security best practices?",
                [
                    "It includes protections like CSRF mitigation and secure password handling",
                    "It disables HTTPS entirely",
                    "It automatically shares user data publicly",
                    "It encourages storing passwords in plain text",
                ],
                0,
            ),
        ],
    },
    {
        "id": "django-installation",
        "title": "Django installation",
        "tutorialPath": "../tutorial/012-django-installation.html",
        "questions": [
            q(
                "Which command installs Django inside your virtual environment?",
                [
                    "pip install django",
                    "django install pip",
                    "sudo install django",
                    "python setup.py django",
                ],
                0,
            ),
            q(
                "Why does the tutorial stress activating your virtual environment before installing packages?",
                [
                    "So packages are isolated to your project environment",
                    "So packages install system-wide for all users",
                    "So you can skip using pip",
                    "So you can upgrade your OS",
                ],
                0,
            ),
            q(
                "Which command verifies that Django installed correctly?",
                [
                    "python -m django --version",
                    "django-admin help",
                    "pip freeze django",
                    "django check",
                ],
                0,
            ),
            q(
                "What does the tutorial recommend doing after installing Django?",
                [
                    "Creating a new Django project to ensure everything works",
                    "Uninstalling the virtual environment",
                    "Reading the entire Django source code",
                    "Switching to a different framework immediately",
                ],
                0,
            ),
            q(
                "Which command creates a new Django project skeleton?",
                [
                    "django-admin startproject mysite",
                    "django-admin create mysite",
                    "django-admin init mysite",
                    "django-admin build mysite",
                ],
                0,
            ),
            q(
                "What does manage.py allow you to do?",
                [
                    "Run various Django management commands within your project",
                    "Compile front-end assets automatically",
                    "Configure your operating system",
                    "Edit HTML templates graphically",
                ],
                0,
            ),
            q(
                "Why does the tutorial ask you to run python manage.py runserver after installation?",
                [
                    "To confirm the development server starts without errors",
                    "To deploy the app to production",
                    "To migrate the database automatically",
                    "To package the project into a zip file",
                ],
                0,
            ),
            q(
                "What URL does the Django development server use by default?",
                [
                    "http://127.0.0.1:8000/",
                    "http://localhost:3000/",
                    "http://0.0.0.0:5000/",
                    "http://django.local/",
                ],
                0,
            ),
            q(
                "Which keyboard shortcut stops the development server?",
                [
                    "Ctrl + C",
                    "Ctrl + D",
                    "Ctrl + Z",
                    "Ctrl + X",
                ],
                0,
            ),
            q(
                "What file keeps track of installed packages for sharing with teammates?",
                [
                    "requirements.txt",
                    "packages.lock",
                    "dependencies.json",
                    "modules.md",
                ],
                0,
            ),
        ],
    },
    {
        "id": "your-first-django-project",
        "title": "Your first Django project!",
        "tutorialPath": "../tutorial/013-your-first-django-project.html",
        "questions": [
            q(
                "Which command creates a new Django app inside your project?",
                [
                    "python manage.py startapp blog",
                    "python manage.py newapp blog",
                    "django-admin createapp blog",
                    "django-admin blog start",
                ],
                0,
            ),
            q(
                "Where do you register a new app so Django knows about it?",
                [
                    "In the INSTALLED_APPS list inside settings.py",
                    "In urls.py under urlpatterns",
                    "In manage.py",
                    "In requirements.txt",
                ],
                0,
            ),
            q(
                "What Python command applies changes to the database schema?",
                [
                    "python manage.py migrate",
                    "python manage.py make",
                    "python manage.py collectstatic",
                    "python manage.py compile",
                ],
                0,
            ),
            q(
                "Why does the tutorial ask you to set TIME_ZONE in settings.py?",
                [
                    "So dates and times are displayed correctly for your region",
                    "So the server restarts automatically at midnight",
                    "So migrations run faster",
                    "So static files download quicker",
                ],
                0,
            ),
            q(
                "What is the purpose of urls.py in a Django project?",
                [
                    "It maps URL patterns to views",
                    "It configures database connections",
                    "It defines CSS styles",
                    "It stores environment variables",
                ],
                0,
            ),
            q(
                "Which template engine is enabled by default in Django settings?",
                [
                    "Django Templates",
                    "Jinja2",
                    "Mustache",
                    "Handlebars",
                ],
                0,
            ),
            q(
                "What does the tutorial instruct you to do after creating a superuser?",
                [
                    "Log into the admin site to verify credentials",
                    "Delete the admin app",
                    "Share the password publicly",
                    "Disable the admin site",
                ],
                0,
            ),
            q(
                "Where does Django store SQLite database files by default?",
                [
                    "In the project root as db.sqlite3",
                    "In the templates directory",
                    "In the static folder",
                    "On a remote server automatically",
                ],
                0,
            ),
            q(
                "Why does the tutorial encourage meaningful commit messages during setup?",
                [
                    "They make it easier to understand history and debug issues",
                    "They automatically deploy the code",
                    "They speed up the server",
                    "They encrypt the repository",
                ],
                0,
            ),
            q(
                "Which command shows pending migrations that haven't been applied?",
                [
                    "python manage.py showmigrations",
                    "python manage.py checkmigrations",
                    "python manage.py migrations list",
                    "python manage.py status",
                ],
                0,
            ),
        ],
    },
    {
        "id": "django-models",
        "title": "Django models",
        "tutorialPath": "../tutorial/014-django-models.html",
        "questions": [
            q(
                "What is a Django model?",
                [
                    "A Python class that defines the structure of database data",
                    "A CSS class for styling templates",
                    "A JavaScript object for UI state",
                    "A command-line tool for deployment",
                ],
                0,
            ),
            q(
                "Which base class must your model inherit from?",
                [
                    "django.db.models.Model",
                    "django.core.models.Base",
                    "django.models.BaseModel",
                    "django.forms.ModelForm",
                ],
                0,
            ),
            q(
                "What does makemigrations do?",
                [
                    "Creates migration files based on model changes",
                    "Applies migrations to the database",
                    "Deletes the database",
                    "Backs up the project",
                ],
                0,
            ),
            q(
                "Why do you run python manage.py migrate after makemigrations?",
                [
                    "To apply the migration files and update the database schema",
                    "To reset the admin password",
                    "To install third-party apps",
                    "To push code to GitHub",
                ],
                0,
            ),
            q(
                "What field type should you use for storing large text content?",
                [
                    "models.TextField",
                    "models.IntegerField",
                    "models.BooleanField",
                    "models.DateTimeField",
                ],
                0,
            ),
            q(
                "How do you link a model to a user account?",
                [
                    "Using models.ForeignKey(User, on_delete=...)",
                    "Using models.UserField()",
                    "Using models.OneToOneField(Post)",
                    "Using models.ManyToManyField(Text)",
                ],
                0,
            ),
            q(
                "What method allows you to specify how objects appear in the Django admin list?",
                [
                    "__str__",
                    "__repr__",
                    "__display__",
                    "__print__",
                ],
                0,
            ),
            q(
                "Why does the tutorial emphasize using timezone-aware DateTime fields?",
                [
                    "To avoid issues when displaying dates across different regions",
                    "To make queries faster",
                    "To disable timezone conversions",
                    "To store dates as strings",
                ],
                0,
            ),
            q(
                "Which command opens a Django shell for interacting with models?",
                [
                    "python manage.py shell",
                    "python manage.py console",
                    "django-admin shell",
                    "python shell manage.py",
                ],
                0,
            ),
            q(
                "What is the benefit of creating migrations frequently?",
                [
                    "They capture incremental changes and make team collaboration smoother",
                    "They remove the need for database backups",
                    "They automatically generate documentation",
                    "They deploy the project to production",
                ],
                0,
            ),
        ],
    },
    {
        "id": "django-admin",
        "title": "Django admin",
        "tutorialPath": "../tutorial/015-django-admin.html",
        "questions": [
            q(
                "What purpose does the Django admin site serve?",
                [
                    "It allows trusted users to manage database content through a web interface",
                    "It publishes the site to the internet",
                    "It renders front-end templates",
                    "It replaces the need for migrations",
                ],
                0,
            ),
            q(
                "How do you make a model appear in the admin interface?",
                [
                    "Register it in admin.py with admin.site.register(Model)",
                    "Add it to INSTALLED_APPS",
                    "Create a template with the model name",
                    "Enable ADMIN=True in settings.py",
                ],
                0,
            ),
            q(
                "Why does the tutorial recommend customizing ModelAdmin classes?",
                [
                    "To control list display, search fields, and ordering",
                    "To deploy the admin with SSL",
                    "To migrate data between environments",
                    "To manage static files automatically",
                ],
                0,
            ),
            q(
                "What command creates a superuser for admin access?",
                [
                    "python manage.py createsuperuser",
                    "python manage.py makeuser",
                    "django-admin adduser",
                    "python manage.py admin",
                ],
                0,
            ),
            q(
                "Which URL path is used to load the admin site by default?",
                [
                    "/admin/",
                    "/dashboard/",
                    "/manage/",
                    "/cms/",
                ],
                0,
            ),
            q(
                "What does list_display do in a ModelAdmin?",
                [
                    "Defines which fields are shown in the change list table",
                    "Sets the default template for a model",
                    "Controls database indexing",
                    "Configures caching",
                ],
                0,
            ),
            q(
                "Why is it important to create meaningful __str__ methods for models viewed in admin?",
                [
                    "So entries are readable and recognizable in dropdowns and lists",
                    "So models can be exported to CSV",
                    "So admin will auto-translate field names",
                    "So admins can upload images",
                ],
                0,
            ),
            q(
                "Which decorator or function is used to register models with a custom admin class?",
                [
                    "@admin.register(Model)",
                    "@admin.model(Model)",
                    "admin.include(Model)",
                    "@register.admin(Model)",
                ],
                0,
            ),
            q(
                "What does search_fields allow you to do?",
                [
                    "Add a search box that filters results by specific model fields",
                    "Change the admin site title",
                    "Schedule background jobs",
                    "Serve static files",
                ],
                0,
            ),
            q(
                "Why should admin accounts use strong passwords?",
                [
                    "They can edit critical data, so compromising them puts the site at risk",
                    "They have limited permissions, so security is optional",
                    "They cannot change any settings",
                    "They only access comments",
                ],
                0,
            ),
        ],
    },
    {
        "id": "deploy",
        "title": "Deploy!",
        "tutorialPath": "../tutorial/016-deploy.html",
        "questions": [
            q(
                "What is deployment in the context of the tutorial?",
                [
                    "Making your site available on the internet for others to visit",
                    "Running the development server locally",
                    "Designing wireframes for your application",
                    "Installing Python on your computer",
                ],
                0,
            ),
            q(
                "Which hosting platform does the tutorial recommend for beginners?",
                [
                    "PythonAnywhere",
                    "AWS Lambda",
                    "Microsoft Azure",
                    "DigitalOcean",
                ],
                0,
            ),
            q(
                "Why do you collect static files before deployment?",
                [
                    "To gather CSS and JS assets into one place for the production server",
                    "To delete unused templates",
                    "To minify database migrations",
                    "To back up the SQLite database",
                ],
                0,
            ),
            q(
                "What management command bundles static assets?",
                [
                    "python manage.py collectstatic",
                    "python manage.py collectmedia",
                    "python manage.py bundleassets",
                    "python manage.py build",
                ],
                0,
            ),
            q(
                "Why does the tutorial guide you to configure allowed hosts?",
                [
                    "To specify which domain names can serve your Django project",
                    "To block all traffic",
                    "To enable debugging",
                    "To automatically renew SSL certificates",
                ],
                0,
            ),
            q(
                "What is the purpose of setting DEBUG = False in production?",
                [
                    "To prevent detailed error pages from exposing sensitive information",
                    "To disable static files",
                    "To speed up the development server",
                    "To reload templates automatically",
                ],
                0,
            ),
            q(
                "Which command uploads your code to PythonAnywhere when using git?",
                [
                    "git push",
                    "git deploy",
                    "git upload",
                    "git release",
                ],
                0,
            ),
            q(
                "Why do you run migrations on the hosting platform after deployment?",
                [
                    "Because the production database needs the same schema as development",
                    "Because it resets your local database",
                    "Because it deletes old migrations",
                    "Because it compiles CSS files",
                ],
                0,
            ),
            q(
                "What is a good practice after deploying your site?",
                [
                    "Visit the live URL to ensure everything works as expected",
                    "Immediately shut down the server",
                    "Delete the repository",
                    "Turn DEBUG back on",
                ],
                0,
            ),
            q(
                "Why does the tutorial celebrate deployment as a milestone?",
                [
                    "Because sharing a working app with the world is an exciting accomplishment",
                    "Because deployment means development ends permanently",
                    "Because deployment is the easiest step in the process",
                    "Because deployment removes the need for backups",
                ],
                0,
            ),
        ],
    },
    {
        "id": "django-urls",
        "title": "Django URLs",
        "tutorialPath": "../tutorial/017-django-urls.html",
        "questions": [
            q(
                "What does a URL pattern map to in Django?",
                [
                    "A view function or class that handles the request",
                    "A database table",
                    "A static file",
                    "A JavaScript component",
                ],
                0,
            ),
            q(
                "Where are project-level URL patterns typically defined?",
                [
                    "In the urls.py file of the project directory",
                    "In settings.py",
                    "In models.py",
                    "In admin.py",
                ],
                0,
            ),
            q(
                "Which function is commonly used to define URL patterns?",
                [
                    "path()",
                    "url()",
                    "route()",
                    "link()",
                ],
                0,
            ),
            q(
                "How do you include URL patterns from an app inside the project urls.py?",
                [
                    "Using include('app.urls') in the urlpatterns list",
                    "By copying all app URLs into the project file",
                    "By adding the app name to INSTALLED_APPS",
                    "By referencing the app in settings.ALLOWED_HOSTS",
                ],
                0,
            ),
            q(
                "What is the advantage of naming URL patterns?",
                [
                    "You can reference them in templates and redirect calls without hardcoding paths",
                    "It prevents the URL from ever changing",
                    "It automatically translates URLs",
                    "It disables debugging",
                ],
                0,
            ),
            q(
                "What does the tutorial suggest using for dynamic URL segments like post IDs?",
                [
                    "Path converters such as path('post/<int:pk>/')",
                    "Query strings only",
                    "Environment variables",
                    "Hard-coded HTML links",
                ],
                0,
            ),
            q(
                "Which helper builds URLs in templates based on their names?",
                [
                    "The url template tag (e.g., {% url 'post_detail' pk=post.pk %})",
                    "The static template tag",
                    "The include tag",
                    "The load tag",
                ],
                0,
            ),
            q(
                "Why is URL organization important for larger projects?",
                [
                    "It keeps routes manageable and avoids conflicts between apps",
                    "It removes the need for tests",
                    "It automatically documents the API",
                    "It speeds up the database",
                ],
                0,
            ),
            q(
                "What does the tutorial recommend doing after changing URL patterns?",
                [
                    "Run the server and click through links to ensure they resolve correctly",
                    "Delete the migrations",
                    "Deactivate the virtual environment",
                    "Switch to a different framework",
                ],
                0,
            ),
            q(
                "Why is using include() helpful when building modular apps?",
                [
                    "It lets each app define its own URL structure without cluttering the main file",
                    "It merges templates automatically",
                    "It disables admin URLs",
                    "It generates models dynamically",
                ],
                0,
            ),
        ],
    },
    {
        "id": "django-views",
        "title": "Django views – time to create!",
        "tutorialPath": "../tutorial/018-django-views-time-to-create.html",
        "questions": [
            q(
                "What does a Django view do?",
                [
                    "It receives HTTP requests and returns HTTP responses",
                    "It defines database tables",
                    "It stores CSS styles",
                    "It configures URL routes",
                ],
                0,
            ),
            q(
                "Which function renders templates with context data?",
                [
                    "render(request, template_name, context)",
                    "display(request, template_name, context)",
                    "template(request, context)",
                    "return_template(template_name)",
                ],
                0,
            ),
            q(
                "What is the purpose of returning redirect(...) in a view?",
                [
                    "To send the user to a different URL after processing",
                    "To reload the same template",
                    "To clear the database",
                    "To stop the server",
                ],
                0,
            ),
            q(
                "Why does the tutorial introduce class-based views later?",
                [
                    "They provide reusable patterns for common tasks",
                    "They replace models entirely",
                    "They remove the need for URL patterns",
                    "They only work with REST APIs",
                ],
                0,
            ),
            q(
                "What HTTP methods are commonly handled in Django views?",
                [
                    "GET and POST",
                    "FTP and SSH",
                    "PUT and DELETE only",
                    "SMTP and POP3",
                ],
                0,
            ),
            q(
                "Why does the tutorial encourage keeping view functions small?",
                [
                    "Small views are easier to maintain and test",
                    "View size affects HTML rendering speed",
                    "Large views cannot access the database",
                    "Small views automatically cache responses",
                ],
                0,
            ),
            q(
                "What is the role of context in render()?",
                [
                    "It passes data to the template for display",
                    "It configures middleware",
                    "It loads static files",
                    "It sets environment variables",
                ],
                0,
            ),
            q(
                "Which decorator restricts access to authenticated users?",
                [
                    "@login_required",
                    "@staff_only",
                    "@superuser",
                    "@authenticated",
                ],
                0,
            ),
            q(
                "Why does the tutorial stress returning HttpResponse or render from views?",
                [
                    "A view must return an HTTP response object for Django to send to the browser",
                    "It automatically saves data to the database",
                    "It closes the server socket",
                    "It refreshes the admin site",
                ],
                0,
            ),
            q(
                "What is a good practice after writing a new view?",
                [
                    "Hook it into urls.py and test it in the browser",
                    "Delete the template files",
                    "Restart your operating system",
                    "Disable static file serving",
                ],
                0,
            ),
        ],
    },
    {
        "id": "introduction-to-html",
        "title": "Introduction to HTML",
        "tutorialPath": "../tutorial/019-introduction-to-html.html",
        "questions": [
            q(
                "What does HTML stand for?",
                [
                    "HyperText Markup Language",
                    "HighText Machine Language",
                    "Hyperlink and Text Markup Layer",
                    "Home Tool Markup Language",
                ],
                0,
            ),
            q(
                "What is the purpose of HTML tags?",
                [
                    "They provide structure and meaning to content on a web page",
                    "They apply dynamic server logic",
                    "They execute Python code in the browser",
                    "They style the page with colors",
                ],
                0,
            ),
            q(
                "Which HTML tag creates a link to another page?",
                [
                    "<a>",
                    "<link>",
                    "<p>",
                    "<div>",
                ],
                0,
            ),
            q(
                "What attribute sets the destination URL of a link?",
                [
                    "href",
                    "src",
                    "alt",
                    "class",
                ],
                0,
            ),
            q(
                "How do you create an ordered list in HTML?",
                [
                    "Using <ol> with <li> items",
                    "Using <ul> with <li> items only",
                    "Using <list> tags",
                    "Using <order> tags",
                ],
                0,
            ),
            q(
                "What element is used to insert an image?",
                [
                    "<img>",
                    "<picture>",
                    "<image>",
                    "<src>",
                ],
                0,
            ),
            q(
                "Why does the tutorial talk about semantic HTML?",
                [
                    "Semantic tags make content more accessible and meaningful",
                    "Semantic tags change the color scheme",
                    "Semantic tags run Python scripts",
                    "Semantic tags require no closing tags",
                ],
                0,
            ),
            q(
                "Which tag defines the main heading of a page?",
                [
                    "<h1>",
                    "<main>",
                    "<title>",
                    "<header>",
                ],
                0,
            ),
            q(
                "What does the <head> section of an HTML document contain?",
                [
                    "Metadata like title, links, and scripts",
                    "Only visible text for the page",
                    "Server-side Python code",
                    "Database queries",
                ],
                0,
            ),
            q(
                "Why is indentation still recommended in HTML?",
                [
                    "It keeps code readable even though whitespace is mostly ignored",
                    "It changes how the browser renders the HTML",
                    "It is required to deploy the site",
                    "It replaces CSS styling",
                ],
                0,
            ),
        ],
    },
    {
        "id": "django-orm-querysets",
        "title": "Django ORM (Querysets)",
        "tutorialPath": "../tutorial/020-django-orm-querysets.html",
        "questions": [
            q(
                "What does ORM stand for?",
                [
                    "Object-Relational Mapping",
                    "Organized Resource Management",
                    "Object Runtime Module",
                    "Online Resource Monitor",
                ],
                0,
            ),
            q(
                "What does Post.objects.all() return?",
                [
                    "A queryset containing all Post objects",
                    "A single Post instance",
                    "A dictionary of Post fields",
                    "An SQL string",
                ],
                0,
            ),
            q(
                "How do you filter posts by author using the ORM?",
                [
                    "Post.objects.filter(author=some_user)",
                    "Post.objects.where(author=some_user)",
                    "Post.filter(author=some_user)",
                    "Post.objects.query(author__match=some_user)",
                ],
                0,
            ),
            q(
                "Why does the tutorial show ordering querysets?",
                [
                    "To display data in a predictable order for users",
                    "To randomize results every time",
                    "To automatically cache results",
                    "To remove duplicates from the database",
                ],
                0,
            ),
            q(
                "Which queryset method returns a single object or raises DoesNotExist?",
                [
                    "get()",
                    "first()",
                    "filter()",
                    "values()",
                ],
                0,
            ),
            q(
                "What does the tutorial caution about when using get()?",
                [
                    "Make sure the lookup is unique, or it could raise MultipleObjectsReturned",
                    "It deletes the object automatically",
                    "It always returns None if missing",
                    "It converts the result to JSON",
                ],
                0,
            ),
            q(
                "How do you limit a queryset to objects published up to now?",
                [
                    "Post.objects.filter(published_date__lte=timezone.now())",
                    "Post.objects.filter(published_date__gte=timezone.now())",
                    "Post.objects.filter(published_date__contains=timezone.now())",
                    "Post.objects.filter(published_date=timezone.now())",
                ],
                0,
            ),
            q(
                "Why are querysets lazy in Django?",
                [
                    "They delay database access until the data is needed, improving performance",
                    "They never hit the database",
                    "They run on a background thread",
                    "They store results in HTML",
                ],
                0,
            ),
            q(
                "Which method converts a queryset into a list of dictionaries?",
                [
                    "values()",
                    "list()",
                    "dict()",
                    "serialize()",
                ],
                0,
            ),
            q(
                "What is the benefit of chaining queryset filters?",
                [
                    "It refines queries step by step without hitting the database immediately",
                    "It duplicates results for testing",
                    "It automatically creates indexes",
                    "It updates records in place",
                ],
                0,
            ),
        ],
    },
    {
        "id": "dynamic-data-in-templates",
        "title": "Dynamic data in templates",
        "tutorialPath": "../tutorial/021-dynamic-data-in-templates.html",
        "questions": [
            q(
                "How do you display a variable from the view context in a template?",
                [
                    "{{ variable_name }}",
                    "{% variable_name %}",
                    "[[ variable_name ]]",
                    "<% variable_name %>",
                ],
                0,
            ),
            q(
                "What is the purpose of template tags like {% for %}?",
                [
                    "To add logic such as loops or conditionals in templates",
                    "To run Python code directly",
                    "To import CSS files",
                    "To execute SQL queries",
                ],
                0,
            ),
            q(
                "Which filter capitalizes the first letter of a string?",
                [
                    "{{ text|capfirst }}",
                    "{{ text|capitalize }}",
                    "{{ text|upperfirst }}",
                    "{{ text|titlecase }}",
                ],
                0,
            ),
            q(
                "Why does the tutorial encourage keeping logic minimal in templates?",
                [
                    "Templates should focus on presentation while views handle business logic",
                    "Templates cannot access variables",
                    "Templates run faster without HTML",
                    "Templates are compiled into SQL",
                ],
                0,
            ),
            q(
                "How do you perform an if statement in a template?",
                [
                    "{% if condition %} ... {% endif %}",
                    "{{ if condition }} ... {{ endif }}",
                    "<if condition> ... </if>",
                    "[% if condition %]",
                ],
                0,
            ),
            q(
                "What will happens if you try to access an attribute that doesn't exist in the template?",
                [
                    "Django renders an empty string by default",
                    "The template crashes with a Python exception",
                    "The server stops running",
                    "The template automatically creates the attribute",
                ],
                0,
            ),
            q(
                "Which tag loads additional template libraries like static?",
                [
                    "{% load static %}",
                    "{{ load static }}",
                    "<load static>",
                    "{% import static %}",
                ],
                0,
            ),
            q(
                "How can you use the length of a list in a condition?",
                [
                    "{% if posts|length > 0 %}",
                    "{% if len(posts) > 0 %}",
                    "{% if posts.length > 0 %}",
                    "{% if posts.count > 0 %}",
                ],
                0,
            ),
            q(
                "Why does the tutorial emphasize escaping user content?",
                [
                    "To protect against cross-site scripting by default",
                    "To minify HTML automatically",
                    "To translate text into multiple languages",
                    "To store data in cookies",
                ],
                0,
            ),
            q(
                "What does the safe filter do?",
                [
                    "It marks a string as trusted so HTML tags are rendered",
                    "It validates form inputs",
                    "It sanitizes user passwords",
                    "It adds CSRF tokens",
                ],
                0,
            ),
        ],
    },
    {
        "id": "django-templates",
        "title": "Django templates",
        "tutorialPath": "../tutorial/022-django-templates.html",
        "questions": [
            q(
                "Where does Django look for templates by default inside an app?",
                [
                    "In the app's templates/app_name/ directory",
                    "In the project root",
                    "In the static directory",
                    "In settings.py",
                ],
                0,
            ),
            q(
                "What does the tutorial suggest to avoid template name conflicts between apps?",
                [
                    "Namespace templates by placing them inside a folder named after the app",
                    "Use random file extensions",
                    "Avoid creating multiple apps",
                    "Store templates in the static folder",
                ],
                0,
            ),
            q(
                "Which setting defines directories Django searches for templates globally?",
                [
                    "TEMPLATES in settings.py",
                    "STATICFILES_DIRS",
                    "MEDIA_ROOT",
                    "INSTALLED_APPS",
                ],
                0,
            ),
            q(
                "Why is the base.html template useful?",
                [
                    "It provides a common layout that other templates can extend",
                    "It stores database migrations",
                    "It holds form submission logic",
                    "It configures URL routes",
                ],
                0,
            ),
            q(
                "How do you reference a static file in a template?",
                [
                    "{% load static %} ... <img src=\"{% static 'path/to/file.png' %}\">",
                    "<img src=\"/static/path/to/file.png\"> without loading",
                    "Use {{ static('file.png') }} without loading",
                    "Hardcode the server IP address",
                ],
                0,
            ),
            q(
                "What is the advantage of using template inheritance?",
                [
                    "It reduces duplication by letting child templates fill predefined blocks",
                    "It speeds up database queries",
                    "It auto-generates forms",
                    "It enforces authentication",
                ],
                0,
            ),
            q(
                "Which block is typically used to inject unique content into a layout?",
                [
                    "{% block content %} ... {% endblock %}",
                    "{% block head %}",
                    "{% block script %}",
                    "{% block csrf %}",
                ],
                0,
            ),
            q(
                "Why does the tutorial recommend keeping templates organized?",
                [
                    "Large projects remain manageable when templates follow a consistent structure",
                    "The development server starts faster",
                    "The admin site loads more quickly",
                    "The ORM generates fewer queries",
                ],
                0,
            ),
            q(
                "What does {% extends 'base.html' %} do?",
                [
                    "It tells Django to use base.html as the parent template",
                    "It imports CSS files automatically",
                    "It renders raw Python code",
                    "It adds context variables",
                ],
                0,
            ),
            q(
                "Where should you place reusable snippets like navigation bars?",
                [
                    "In separate templates that can be included with {% include %}",
                    "In models.py",
                    "In manage.py",
                    "In urls.py",
                ],
                0,
            ),
        ],
    },
    {
        "id": "css-make-it-pretty",
        "title": "CSS – make it pretty",
        "tutorialPath": "../tutorial/023-css-make-it-pretty.html",
        "questions": [
            q(
                "What does CSS stand for?",
                [
                    "Cascading Style Sheets",
                    "Creative Styling System",
                    "Computer Styled Sections",
                    "Colorful Selective Syntax",
                ],
                0,
            ),
            q(
                "How do you link a CSS file in an HTML template?",
                [
                    "<link rel=\"stylesheet\" href=\"{% static 'css/style.css' %}\">",
                    "<css href=\"style.css\">",
                    "<style src=\"style.css\">",
                    "<script src=\"style.css\"></script>",
                ],
                0,
            ),
            q(
                "What selector targets all paragraph elements?",
                [
                    "p { ... }",
                    "#p { ... }",
                    ".p { ... }",
                    "*p { ... }",
                ],
                0,
            ),
            q(
                "Why does the tutorial encourage experimenting with colors and spacing?",
                [
                    "To build intuition for how CSS rules change the look and feel",
                    "To slow down the page load intentionally",
                    "To replace the need for templates",
                    "To learn database queries",
                ],
                0,
            ),
            q(
                "Which property changes the background color of an element?",
                [
                    "background-color",
                    "color",
                    "border-color",
                    "font-color",
                ],
                0,
            ),
            q(
                "What does margin control?",
                [
                    "The space outside an element",
                    "The inner padding of an element",
                    "The font size",
                    "The text color",
                ],
                0,
            ),
            q(
                "How do you apply a style only to elements with a specific class?",
                [
                    ".classname { ... }",
                    "#classname { ... }",
                    "classname { ... }",
                    "$classname { ... }",
                ],
                0,
            ),
            q(
                "What is the purpose of @font-face or using Google Fonts?",
                [
                    "To include custom typefaces in your design",
                    "To compress HTML files",
                    "To speed up database queries",
                    "To inline images",
                ],
                0,
            ),
            q(
                "Why is it useful to use browser developer tools when styling?",
                [
                    "You can inspect elements and tweak CSS live to see instant results",
                    "You can edit Python code directly",
                    "You can disable HTTPS",
                    "You can auto-generate migrations",
                ],
                0,
            ),
            q(
                "What property controls the font size of text?",
                [
                    "font-size",
                    "font-style",
                    "text-size",
                    "type-size",
                ],
                0,
            ),
        ],
    },
    {
        "id": "template-extending",
        "title": "Template extending",
        "tutorialPath": "../tutorial/024-template-extending.html",
        "questions": [
            q(
                "What problem does template inheritance solve?",
                [
                    "Avoiding repetition by sharing base layouts across pages",
                    "Running migrations faster",
                    "Configuring database replicas",
                    "Generating REST APIs automatically",
                ],
                0,
            ),
            q(
                "Which tag do child templates use to reuse a base template?",
                [
                    "{% extends 'base.html' %}",
                    "{% import 'base.html' %}",
                    "{{ extends 'base.html' }}",
                    "<extends base>",
                ],
                0,
            ),
            q(
                "How do you define a replaceable section in a base template?",
                [
                    "{% block content %}{% endblock %}",
                    "{% area content %}",
                    "{{ block content }}",
                    "<block content></block>",
                ],
                0,
            ),
            q(
                "Why is {% block title %} beneficial?",
                [
                    "It lets each page set a custom <title> while sharing the same head",
                    "It auto-generates navigation menus",
                    "It adjusts the server hostname",
                    "It configures static files",
                ],
                0,
            ),
            q(
                "What happens if a child template omits a block defined in the parent?",
                [
                    "The parent block content is used by default",
                    "The page crashes with an error",
                    "The page renders blank",
                    "Django stops the server",
                ],
                0,
            ),
            q(
                "Which tag combines inheritance with reusable fragments?",
                [
                    "{% include 'partial.html' %}",
                    "{% partial 'fragment.html' %}",
                    "{{ include 'fragment.html' }}",
                    "<include fragment>",
                ],
                0,
            ),
            q(
                "Why does the tutorial warn against deep inheritance chains?",
                [
                    "Too many layers make templates hard to follow and maintain",
                    "Django does not allow inheritance",
                    "It slows down SQL queries",
                    "It prevents caching",
                ],
                0,
            ),
            q(
                "How can you provide default content that child templates can override?",
                [
                    "Place fallback HTML inside the block in the base template",
                    "Use JavaScript to swap content later",
                    "Store defaults in settings.py",
                    "Load context processors",
                ],
                0,
            ),
            q(
                "What is an advantage of keeping base.html minimal?",
                [
                    "It keeps inheritance flexible and avoids forcing every page to load unnecessary sections",
                    "It disables template caching",
                    "It speeds up migrations",
                    "It renders admin automatically",
                ],
                0,
            ),
            q(
                "Which statement reflects the tutorial's advice on template organization?",
                [
                    "Plan a small set of base templates that reflect your layout variations",
                    "Create one unique base template per page",
                    "Avoid using includes",
                    "Use plain HTML without blocks",
                ],
                0,
            ),
        ],
    },
    {
        "id": "extend-your-application",
        "title": "Extend your application",
        "tutorialPath": "../tutorial/025-extend-your-application.html",
        "questions": [
            q(
                "What new feature does the tutorial add in this chapter?",
                [
                    "A post detail page that shows full articles",
                    "A user authentication system",
                    "Real-time chat functionality",
                    "Automatic payment processing",
                ],
                0,
            ),
            q(
                "Which function retrieves a single object or returns 404 if not found?",
                [
                    "get_object_or_404()",
                    "get_or_return()",
                    "object_or_404()",
                    "fetch_or_404()",
                ],
                0,
            ),
            q(
                "Why does the tutorial add links from the post list to the detail view?",
                [
                    "To let users navigate between summaries and full content",
                    "To update the admin site automatically",
                    "To trigger background jobs",
                    "To delete old posts",
                ],
                0,
            ),
            q(
                "What does the slug or primary key in the URL represent?",
                [
                    "A unique identifier used to look up the correct post",
                    "A CSS class",
                    "A database index name",
                    "A file path to an image",
                ],
                0,
            ),
            q(
                "Which template displays the detailed blog post?",
                [
                    "post_detail.html",
                    "detail_post.html",
                    "post_full.html",
                    "single_post.html",
                ],
                0,
            ),
            q(
                "Why does the tutorial add published_date filtering when listing posts?",
                [
                    "To show only posts that have been published",
                    "To hide posts with images",
                    "To sort alphabetically",
                    "To paginate results automatically",
                ],
                0,
            ),
            q(
                "What is the benefit of using reverse() or reverse_lazy()?",
                [
                    "They construct URLs from their named patterns without hardcoding paths",
                    "They render templates faster",
                    "They serialize models",
                    "They delete outdated migrations",
                ],
                0,
            ),
            q(
                "Why does the tutorial remind you to run tests after adding new views?",
                [
                    "To ensure everything still works before deploying",
                    "To migrate the database automatically",
                    "To create new superusers",
                    "To clear static files",
                ],
                0,
            ),
            q(
                "What context does the detail view send to the template?",
                [
                    "A single post object to display",
                    "A list of all posts",
                    "The entire settings file",
                    "Only the post's author name",
                ],
                0,
            ),
            q(
                "Why is linking between pages emphasized?",
                [
                    "Good navigation makes the blog usable and encourages exploration",
                    "It reduces the HTML file size",
                    "It locks content behind authentication",
                    "It disables caching",
                ],
                0,
            ),
        ],
    },
    {
        "id": "django-forms",
        "title": "Django Forms",
        "tutorialPath": "../tutorial/026-django-forms.html",
        "questions": [
            q(
                "What is the purpose of Django forms in the tutorial?",
                [
                    "They handle user input safely and validate data before saving",
                    "They compile CSS automatically",
                    "They manage database migrations",
                    "They replace the admin site",
                ],
                0,
            ),
            q(
                "Which class lets you create a form tied to a model?",
                [
                    "forms.ModelForm",
                    "forms.FormModel",
                    "models.Form",
                    "forms.BaseForm",
                ],
                0,
            ),
            q(
                "Why is CSRF protection important for forms?",
                [
                    "It prevents malicious sites from submitting forms on behalf of users",
                    "It encrypts the database",
                    "It resizes images",
                    "It speeds up queries",
                ],
                0,
            ),
            q(
                "What does form.save(commit=False) allow you to do?",
                [
                    "Modify the instance before saving it to the database",
                    "Discard user input automatically",
                    "Save the form twice",
                    "Export data to CSV",
                ],
                0,
            ),
            q(
                "Which template tag inserts the CSRF token into a form?",
                [
                    "{% csrf_token %}",
                    "{% token %}",
                    "{{ csrf }}",
                    "{% csrf %}",
                ],
                0,
            ),
            q(
                "Why does the tutorial use the POST method for creating posts?",
                [
                    "POST transmits data securely and doesn't expose it in the URL",
                    "POST automatically creates database tables",
                    "POST refreshes the template",
                    "POST caches the page",
                ],
                0,
            ),
            q(
                "What does form.is_valid() check?",
                [
                    "Whether submitted data matches the form's validation rules",
                    "Whether the form has a template",
                    "Whether the server is online",
                    "Whether static files are collected",
                ],
                0,
            ),
            q(
                "How do you display form fields in a template quickly?",
                [
                    "{{ form.as_p }}",
                    "{{ form.render }}",
                    "{% include form %}",
                    "{{ form.html }}",
                ],
                0,
            ),
            q(
                "Why does the tutorial redirect after a successful form submission?",
                [
                    "To follow the Post/Redirect/Get pattern and avoid duplicate submissions",
                    "To clear the database",
                    "To reload static files",
                    "To sign the user out",
                ],
                0,
            ),
            q(
                "What advantage does ModelForm provide over manually creating forms?",
                [
                    "It automatically builds form fields from model definitions",
                    "It manages user authentication",
                    "It compresses CSS files",
                    "It runs database backups",
                ],
                0,
            ),
        ],
    },
    {
        "id": "whats-next",
        "title": "What's next?",
        "tutorialPath": "../tutorial/027-what-s-next.html",
        "questions": [
            q(
                "What does the tutorial encourage you to do after finishing the project?",
                [
                    "Continue learning and building by tackling new features or ideas",
                    "Stop coding entirely",
                    "Switch to a different career immediately",
                    "Delete your project repository",
                ],
                0,
            ),
            q(
                "Which community does the tutorial suggest joining to stay connected?",
                [
                    "The global Django Girls community and local groups",
                    "Only paid enterprise forums",
                    "Unrelated gaming communities",
                    "Closed-source mailing lists",
                ],
                0,
            ),
            q(
                "Why is contributing to open source recommended?",
                [
                    "It helps you learn collaboratively and give back to the community",
                    "It guarantees paid work immediately",
                    "It replaces the need for practice",
                    "It locks your code behind licenses",
                ],
                0,
            ),
            q(
                "What mindset does the tutorial promote about debugging and errors?",
                [
                    "Errors are normal; keep experimenting and asking questions",
                    "Errors mean you should quit coding",
                    "Errors only happen to beginners",
                    "Errors can be ignored safely",
                ],
                0,
            ),
            q(
                "Which suggestion helps you deepen your knowledge?",
                [
                    "Read Django documentation and try official tutorials",
                    "Memorize every line of the tutorial",
                    "Avoid new technologies",
                    "Only watch videos, never write code",
                ],
                0,
            ),
            q(
                "Why does the tutorial highlight teaching others?",
                [
                    "Explaining concepts reinforces your own understanding and supports newcomers",
                    "Teaching is only for experts",
                    "Teaching replaces practicing",
                    "Teaching is mandatory for certification",
                ],
                0,
            ),
            q(
                "What kind of projects does the tutorial encourage you to build next?",
                [
                    "Projects that solve problems you care about or help your community",
                    "Only projects identical to the example blog",
                    "Only closed-source projects",
                    "Only projects assigned by others",
                ],
                0,
            ),
            q(
                "How can attending meetups or conferences help you?",
                [
                    "You meet fellow developers, learn new skills, and find mentors",
                    "They replace the need for online resources",
                    "They guarantee job offers immediately",
                    "They eliminate the need to practice",
                ],
                0,
            ),
            q(
                "What is the tutorial's advice about keeping your code on GitHub?",
                [
                    "Use GitHub to showcase your progress and track history",
                    "Delete repositories after each session",
                    "Keep everything private forever",
                    "Avoid version control for small projects",
                ],
                0,
            ),
            q(
                "How should you approach the journey of becoming a coach or mentor?",
                [
                    "Keep learning, stay kind, and support others just as you were supported",
                    "Focus solely on perfect scores",
                    "Work alone without collaboration",
                    "Avoid giving feedback to learners",
                ],
                0,
            ),
        ],
    },
]


def main() -> None:
    output = Path("docs/quiz/questions.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    data = {"sections": QUESTION_BANK}
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
