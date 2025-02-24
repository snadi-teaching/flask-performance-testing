
## How to run

### Create virtual environment and install dependencies

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the back end

```
python app.py
```

### Run the front end

In a **different terminal**, navigate to the project's directory and run

```
source .venv/bin/activate
python frontend.py
```

## Exploring the current app

Go to your browser.

If you go to [http://localhost:8000](http://localhost:8000), you should see the front end of your app. The landing page is a page that lists the current available pages (Add student, List students)

Click on the different links, and explore the pages.

Go to the source code and try to map which parts of the code trigger the different functionality you see.

## Your Task

Add another page for deleting a student. This page will communicate with the backend.

Try to think about what you need systematically:

1. You need the html page that will contain the form for deleting a student (hint: we need to enter the email of the student we will delete). This will go into the templates/ folder

2. You need to specify what will happen when that forms gets submitted. This is the code that will go into the js/student.js script. It should be something similar to adding a student (i.e., you need to call the write backend endpoint)

3. You need to add a frontend url for this page. This will be another function and route in your frontend.py file

4. Finally, add a link for this page on the index.html page

Thus, in summary, you will need to edit/add the following files

- create a new `delete_student.html` page in frontend/templates
- add new javascript code for handling the submission of the delete student form in `frontend/static/js/students.js`
- add the new frontend endpoint/url for delete student in `frontend/frontend.py`
- add needed link in `index.html`