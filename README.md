

# In-Class Exercise: Static Application Security Testing (SAST)

In this exercise, you will practice running Static Application Security Testing (SAST) tools to analyze the security of the given Flask application. This is the same repo we used before with a front end and backe end. You will use three different SAST tools to scan the codebase for vulnerabilities:

- **[Bandit](https://bandit.readthedocs.io/en/latest/)**: A tool for finding common security issues in Python code.
- **[Trivy](https://trivy.dev/latest/)**: A tool that scans container images for vulnerabilities.
- **[Checkov](https://www.checkov.io)**: A static code analysis tool for Infrastructure as Code (IaC), such as Terraform or CloudFormation.

## Prerequisites

Bandit and Checkov can be installed through pip and are already in the provided requirements.txt file (see creating virtual environment and installing dependencies below)

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

Review the results and check the provided links to solve the issues. Re-run and make sure the issues are gone.

### Step 2: Scan for Vulnerabilities with Trivy

If the project is containerized (e.g., using Docker), you will need to scan the Docker image. First, build the Docker image:

```bash
docker build -t flask-security-app .
```

Now, use Trivy to scan the image for vulnerabilities:

```bash
trivy image flask-security-app
```

Trivy will analyze the container image and report any vulnerabilities in the installed software packages.

### Step 4: Scan Infrastructure Code with Checkov

If the project includes any Infrastructure as Code (IaC) files (e.g., Terraform files), run Checkov on those files. For example, if there are Terraform files in the `infrastructure/` folder, run:

```bash
checkov -d infrastructure/
```

Checkov will scan the IaC files for potential security issues, such as misconfigurations in cloud infrastructure.

### Step 5: Review Results and Fix Issues

Review the findings from all three tools and attempt to fix any security issues. For each issue, document:

- The nature of the vulnerability.
- How you addressed the vulnerability.
- If applicable, commit your changes to the repo.

### Step 6: Submit Your Work

Once you've completed the exercise and fixed any issues, submit your updated code and a short report summarizing the issues found and the actions you took to resolve them.

## Deliverables

1. The fixed code with security improvements.
2. A brief report (1-2 pages) summarizing the vulnerabilities found and how you fixed them.

## Notes

- Focus on fixing the most critical security vulnerabilities first.
- If you encounter any issues or need clarification, feel free to reach out for help.



## Running the app

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

