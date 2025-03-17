

# In-Class Exercise 1: Static Application Security Testing (SAST)

In this exercise, you will practice running Static Application Security Testing (SAST) tools to analyze the security of the given Flask application. This is the same repo we used before with a front end and backend but I dockerized it. You will use three different SAST tools to scan the codebase for vulnerabilities:

- **[Bandit](https://bandit.readthedocs.io/en/latest/)**: A tool for finding common security issues in Python code.
- **[Trivy](https://trivy.dev/latest/)**: A tool that scans container images for vulnerabilities.
- **[Checkov](https://www.checkov.io)**: A static code analysis tool for Infrastructure as Code (IaC), such as Terraform or CloudFormation.

## Prerequisites

Bandit and Checkov can be installed through pip and are already in the provided requirements.txt file (see creating virtual environment and installing dependencies below). You should run the steps below in a virtual environment with the dependencies installed.

Trivy needs to be installed by following the [instructions relevant to your OS](https://github.com/aquasecurity/trivy). For MacOS, you can use `brew install trivy`

## Instructions

### Step 1: Scan the application with Bandit

Run Bandit on the Python files in your backend

```bash
bandit -r server
```

and then run it on your front end

```bash
bandit -r frontend
```

### Step 2: Scan for Vulnerabilities with Trivy
 
 Run 

```
trivy fs --scanners vuln,secret,misconfig .
```


### Step 4: Scan Infrastructure Code with Checkov

Checkov considers Dockerfiles while scanning infrastructure code files.

```bash
checkov -d  .
```

### Step 5: Review Results and Fix Issues

Review the findings from all three tools and answer the following questions. Put your answers on brightspace

1. Which vulnerabilities are common between the tools?
2. Are there vulnerabilities that only one tool seems to detect?
3. Pick one vulnerability and fix it based on the provided error message. You can search for how this error can be fixed or even ask ChatGPT. Rescan using the respective tool to make sure it's fixed

# In-Class Exercise 2: Dynamic Application Security Testing (DAST)

1. Follow the instructions on [https://www.zaproxy.org/getting-started/](https://www.zaproxy.org/getting-started/) to download OWASP ZAP (hopefully you did this before class already)
2. Make sure you have your application running using `docker compose up`. Double check that it works in the browser
3. Open ZAP and follow the run automated scan instructions [https://www.zaproxy.org/getting-started/](https://www.zaproxy.org/getting-started/). Basically, you want to click on "Automated Scan" and enter "http://127.0.0.1:800" in the "URL to Attack" box and then click "Attack". It will take a minute or so before you see the summary of teh results in the bottom left.


# Running the app

If you just want to run the app, follow these instructions

## Running the app with docker

```
docker compose up --build -d
```

## Running the app without docker

### Create virtual environment and install dependencies

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the back end

```
cd server
python app.py
```

### Run the front end

In a **different terminal**, navigate to the project's directory and run

```
source .venv/bin/activate
cd frontend
python frontend.py
```

