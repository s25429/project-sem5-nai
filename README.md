# project-sem5-nai

> ¯\\\_(ツ)\_/¯


## Setup

## Local git integration with Github

If you cannot push or pull anything from github repository to your local project folder, add those lines while in the root directory of the project.
```bash
git config user.name "<name and surname>"
git config user.emal "<your email address>"
```

Overwrite `<...>` with your actual data and it should work fine now.

This will store your user data for this project locally. On your first push or pull you might need to log in to your Github account via a browser.

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

---

### Virtualenv setup

Creates a vritual environment with name 'venv'. A folder named 'venv' appears where all packages will be installed.
```bash
virtualenv venv
```

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

---

### Bugs, issues and caveats

__Q__: _I have some packages that I don't use and cannot get rid of them easily._\
__A__: If you install some packages only to uninstall them, Python will not uninstall packages that the other package dependent on (dependencies). You cannot uninstall them easily, but virtual environments are relatively cheap and so you can just deactive your virtualenv, delete the `venv/` folder and make a new one, then install all previously required packages, but now without your unused one.

__Q__: _My code editor does not want to resolve/find a package._\
__A__: That usually happens with bad virtualenv integration with an editor. Simply restart it and it should go away. If it does not, you might need to link your created virtualenv to the editor. Easiest way to do it is to make a virtualenv again and wait for a popup asking you to do it. Modern code editors do it that way, like VS Code.


## Usage

### Starting the website

Website is built using Python's __flask__ package. To start the website follow those instructions.
```bash
cd client
python main.py  # For windows
python3 main.py  # For mac & linux
```