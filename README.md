# project-sem5-nai

> Group university project for 5th semester from Artificial Intelligence Tools.


## Table of Contents

- [Overview](#overview)
- [Models Used](#models-used)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [Bugs, issues and caveats](#bugs-issues-and-caveats)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)


## Overview

This is a group university project that aims to implement and measure three AI models based on their effectiveness in Named Entity Recognition, specifically Person Recognition.


## Models Used

- dslim's Bert Base NER @ [huggingface.co](https://huggingface.co/dslim/bert-base-NER)
- explosion's SpaCy @ [spacy.io](https://spacy.io/)
- OpenAI's ChatGPT API @ [openai.com](https://openai.com/chatgpt)


## Technologies Used

- Python 3.10+
- Flask 3.0.1
- fransformers 4.37.2
- pytorch 2.2.0
- openai 1.10.0
- python-dotenv 1.0.1
- spacy 3.7.2 \
... more in [requirements.txt](./requirements.txt)


## Installation

### Cloning

Clone repository to your local machine and open it.
```bash
git clone https://github.com/s25429/project-sem5-nai.git
cd project-sem5-nai
```

---

### Local git integration with Github (for contributors)

If you cannot push or pull anything from github repository to your local project folder, add those lines while in the root directory of the project.
```bash
git config user.name "<name and surname>"
git config user.emal "<your email address>"
```

Overwrite `<...>` with your actual data and it should work fine now.

This will store your user data for this project locally. On your first push or pull you might need to log in to your Github account via a browser.

---

### Virtualenv installation

```bash
# For windows
pip install virtualenv
virtualenv --version  # Check if installed correctly

# For mac & linux (hopefully)
sudo apt install python3-virtualenv
sudo pip3 install virtualenv
virtualenv --version  # Chech if installed correctly
```

There is a possibility of virtualenv not being added to PATH automatically. In this case `virtualenv --version` will not work, but `python -m virtualenv --version` should work. 

In this case, change every insance of `virtualenv...` with `python -m virtualenv...` or `python3 -m virtualenv...`.

---

### Virtualenv setup

Creates a vritual environment with name 'venv'. A folder named 'venv' appears where all packages will be installed.
```bash
virtualenv venv
```

When using VS Code, you will get notified if you want to use current virtual environment in the editor. You can select Yes.

Activate venv before installing any python packages or running any python scripts. One of those should work. Once it is activated, at the very front or at the top of command line you will see virtual environment name: (venv).
```bash
venv\Scripts\activate
venv\Scripts\activate.bat
sudo ./venv/Scripts/activate
venv/Scripts/activate
source venv/bin/activate
source venv/Scripts/activate  # This works for Git Bash for Windows
```

To check if virtual environment works, we can check our installed python packages. If you had some installed previously, now upon checking the list, they will be gone and only some default ones will show up.
```bash
# For windows
pip list  # Shows me only three: pip, setuptools and wheel

# For mac & linux
sudo pip3 list  # Shows me only three: pip, setuptools and wheel
```

Now you can install packages "locally" and run python scripts without worry of some global packages interfering.

To deactivate virtual environment run of the following.
```bash
venv\Scripts\deactivate.bat
sudo ./venv/Scripts/deactivate
deactivate  # This works for Git Bash for Windows
```

---

### Setting up and using requirements.txt

Pipe installed "locally" packages (in virtual environment) to a requirements.txt file.
```bash
# For windows
pip freeze --local > requirements.txt

# For mac & linux
sudo pip3 freeze --local > requirements.txt
```

To install all required packaged for this project, run this.
```bash
# For windows
pip install -r requirements.txt

# For mac & linux
sudo pip3 install -r requirements.txt
```

---

### Installing packages (if not done by requirements.txt)

If you have troubles with installing packages from requirements.txt, you can install them manually like so.
```bash
# For windows
pip install [package-name] [package-name-2] ...

# For mac & linux
sudo pip3 install [package-name-1] [package-name-2] ...
```


## Usage

First, add your OpenAI's private API key to `.env`. Create `.env` file in the root of the project with contents below.
```bash
OPENAI_KEY=<your_key>
```

Next, convert Jupyter files in `models/` into standard Python script files.
```bash
cd models

# For windows
scripts\convert_ipynb_to_py.bat

# For mac & linux
./scripts/convert_ipynb_to_py.sh

cd ..
```

You might need to give admin priviliges to the script and/or give executive privileges: `chmod a+x convert_ipynb_to_py.sh`.

Once `.py` files are generated, you can launch __Flask__ server.
```bash
# For windows
python main.py

# For mac & linux
python3 main.py
```

This will run the web server on your network. Details will be shown in console, but for basic usage you can get there with `http://127.0.0.1:8123`.


## Metrics

`put metrics file here`


## Bugs, issues and caveats

__Q__: _`virtualenv` is not recognnized as a command?_ \
__A__: Try `python -m virtualenv`.

__Q__: _Function `process_message from models.raw.bert` does not exist?_ \
__A__: Make sure that you generate `.py` files from Jupyter files. Check [Usage](#usage) section for details.

__Q__: _ChatGPT does not work?_ \
__A__: Make sure that you added `OPENAI_KEY` private key for OpenAI's API to `.env`. Check [Usage](#usage) section for details.

__Q__: _I have some packages that I don't use and cannot get rid of them easily._\
__A__: If you install some packages only to uninstall them, Python will not uninstall packages that the other package dependent on (dependencies). You cannot uninstall them easily, but virtual environments are relatively cheap and so you can just deactive your virtualenv, delete the `venv/` folder and make a new one, then install all previously required packages, but now without your unused one.

__Q__: _My code editor does not want to resolve/find a package._\
__A__: That usually happens with bad virtualenv integration with an editor. Simply restart it and it should go away. If it does not, you might need to link your created virtualenv to the editor. Easiest way to do it is to make a virtualenv again and wait for a popup asking you to do it. Modern code editors do it that way, like VS Code.


## Contributing

No contributions outside of project authors and lecturers will be accepted.


## License

This project is licensed under the [MIT License](./LICENSE).


## Authors

- Weronika Szydlik <s24301@pjwstk.edu.pl>
- Alicja Wieloch <s24274@pjwstk.edu.pl>
- Cezary Ciślak <s25429@pjwstk.edu.pl>
- Jakub Dębkowski <s24579@pjwstk.edu.pl>
- Bartosz Grzanka <s24953@pjwstk.edu.pl>