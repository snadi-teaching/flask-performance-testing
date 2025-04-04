
# Performance Testing with JMeter

The goal of this exercise is to guide you through designing a performance test plan for your Flask application using JMeter. Note that this can also apply to any other web application.

Remember that our current simple demo application is for a student management system. We don't really have a lot going on in this system but it will serve the demo purpose.

## Run JMeter

To run JMeter, run the jmeter.bat (for Windows) or jmeter (for Unix) file. These files are found in the bin directory. See [https://jmeter.apache.org/usermanual/get-started.html](https://jmeter.apache.org/usermanual/get-started.html) for more details.

## Walk through the steps of the performance testing process

### 1.  Decide on the testing environment

In an ideal world, we have some test environment that we can deploy to and it is as close as possible to our production environment. We are in a class setting so we are far from the ideal world :-) 

For our purposes, our test environment will be our local computer. While you can use your deployment machine, it will likely be very slow and digital ocean might block the high number of requests.

### 2.  Identify performance metrics

You have multiple performance metrics on Slide 20 in the lecture. Think of which performance metrics make sense here. For the purposes of the demo, we will choose response time, latency, and error rate.

Other metrics are also applicable.

### 3. Plan and design the performance test (take into account diff. user types, data, scenarios etc)

Given our simple system, we only have limited functionality. We will select the following three main use cases: adding a student, listing students, deleting a student. So these provide three different use cases and we can assume that we have multiple users of the system who may each be doing one or more of these actions at the same time.

Note: In a real setting, you would have more complicated use cases and scenarios that actually depend on each other (e.g., doing an action depends on the success of the authentication endpoint). In the jobboard case, one example is a company user logs in and creates a new post while another example is a job seeker logs in and checks the status of their job applications. Examples of specific checkpoints you want to verify (e.g., checkpoint 1: user logged in sucessfully and within a short amount of time, checkpoint 2: post is created successfully and in a short amount of time). JMeter allows the addition of assertions. The [following link](https://www.baeldung.com/jmeter-session-cookie-management) describes how to handle authentication, cookies and session management between tests. You will need this to set up proper scenarios in your tests.

### 4. Configure the test environment

We don't have much to configure here since we are running on our local machine but let's now fire up the application by running `docker compose up --build -d`

Make sure you can access [http://127.0.0.1:6969](http://127.0.0.1:6969). Note that we are running the performance tests on the backend.

### 5. Implement the tests

We will use JMeter to implement the tests. In this exercise, we will focus on baseline testing where our goal is to understand how our system behaves in normal circumstances. The parameters of the tests would differ if we are doing stress testing for example where we want to overwhelm the system with requests.

1. **Create a Test Plan** name your test plan "Baseline Testing"
2. **Create a Thread Group** to simulate multiple users. Right click on the test plan you just created then choose Add --> Threads (Users) --> Thread Group
3. **Fill in the thread group details** as this screenshot:

![alt text](/docs/imgs/threadgrp.png)

Remember that baseline testing is about establishing some measure you can compare to later. In this case, we will execute the user case as a single user. Since we have only one user here, the ramp up won't make a difference (no parallel users). However, taking a single measurement is not reliable so we want to repeat the requests multiple times to be able to later have a median etc. I chose 30 for feasiblity for the demo.

4. **Add HTTP Requests.** Ok, in this thread group, as its name indicates, the scenario is we have the user add a student and then list all students so we want to tell Jmeter the requests that do that (i.e., what will happen in this test). Right click the thread group, then click "Add --> Sampler --> HTTPRequest" and fill it in as follows:

![alt text](/docs/imgs/addstudent.png)

Repeat this step to add another HTTPRequest for this thread group but for viewing students (you will not need to include body data for viewing students).

For the add student request, we will also specify the content type by following these steps:

- Select your HTTP Request sampler in the Test Plan.
- Right-click on it → Add → Config Element → HTTP Header Manager.
- In the HTTP Header Manager, click Add and then set the following:

    Name: Content-Type
    Value: application/json 

Your configuration would look like this:
![alt text](/docs/imgs/HTTPHeaderManager.jpg)

Note: in this simple exercise, we are repeatedly posting the same data to the DB. This is not a problem here since we don't ensure unique emails, ids etc per users. In your real system, this won't work as you can't have multiple users with the same id/email. See [docs/resources/SimulatingMultiplUsers.md](docs/resources/SimulatingMultiplUsers.md) for starting points on how to tell Jmeter to use different data with each request.

4. **Add Listeners** to capture test results (e.g., Summary Report, View Results Tree).

Right-click on Thread Group > Add > Listener > View Results in Table.

Repeat to add an aggregate report.

Your configuration should look like this:

![alt text](/docs/imgs/reports.png)

### 5. Execute tests

Click on the green start mark.

### 6. Analyze, report, retest  

Look at the output of the tests. In this case, we simply have a baseline so it gives us an idea of how are system performs under very ideal circumstances.

# Saving reports & re-running performance tests

Once you create a test plan, you can save it as a `.jmx` file from Jmeter and then you can use the command line to run this plan multiple times. 

For example, the test plan we created above is in the `plans/` folder of this repo. We can re-run the above performance test as (this assumes you in the jmeter bin directory):

`./jmeter -n -t <path to jmx plan file> -l <path to a jtl results file you want to save results to>`

e.g.,

`./jmeter -n -t /Users/bob/Downloads/BaselineTest.jmx -l /Users/bob/Downloads/BaselineTestResults.jtl`

Then, you can generate a visual report for this:

`./jmeter -g <path_to_output_file>.jtl -e -o <path_to_report_directory>`

e.g., 


`./jmeter -g /Users/bob/Downloads/BaselineTestResults.jtl -e -o /Users/bob/Downloads/JmeterResults/`


## Submit to Brightspace

Take a screenshot of your Jmeter results (any of the listeners) as well as your html report and upload it to brightspace.