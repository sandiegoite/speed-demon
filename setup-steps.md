1. Make sure python3 is installed.
2. Make sure that you have a virtualenv program installed to use / work with virtual environments.
3. Clone the project from github: ```git clone ...```
4. Run ```virtualenv -p python3 venv``` in order to create a virtual environment for building / running the project.
5. Then run . ./venv/bin/activate (in linux to activate the virtual environment)...to test type "python" and make sure that the right python version comes up.
6. Run ```pip install -r requirements.txt``` from the directory of the cloned project.
7. Then set the environment variable FLASK_APP to "app.py" using ```set FLASK_APP=hello.py``` in windows CLI
8. Then run ```flask run```.

These steps are what I did but can be skipped for future people copying the project:
1. ```pip install flask``` (installing flask)
2. ```pip freeze > requirements.txt``` (setting up the initial requirements.txt [dependency tree] for the project)
3. ```git init``` (starting up git version control for the project)
4. Created a .gitignore file (to ignore files that shouldn't be version controlled)
5. Did an initial commit of the project.
6. Pushed it to github.
