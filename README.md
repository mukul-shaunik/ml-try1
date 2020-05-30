<h1># ml-cnn-model</h1>

**This task is to automate the process of a perfect model creation by changing the hyperparams based on accuracy rate of model**

Pre-requisite:
1. Jenkins 
2. Docker
3. Github
4. Machine learning model python file

<h3>Building and starting the container from dockerfile:</h3>

1. Copy dockerfile2 in rhel8 system. Trying to improve dockerfile. Docker image is smaller with dockerfile but has some performance issues.

2. Run : docker build -t keras:latest <path/to/dockerfile>

3. We need to create a volume attachment also for the docker so that we can put the files in that volume to be run in the docker.

4. docker run -d -it --name cnntrainer -v <path/to/host/sourcedir>:<path/to/dockerhost/targetdir> keras:latest

5. After to inspect whether the volume is attached or not use.

6. docker inspect cnntrainer : Look for Mounts section, your volume attachement will be present there.

7. In <path/to/host/sourcedir> put the python model file

 

<h3>Jenkins setup:</h3>
1. Install Java first : sudo yum install java-1.8.0-openjdk-devel

2. Enable Jenkins Repo : curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo

3. sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key

4. Install Jenkins : sudo yum install jenkins

5. Start Jenkins : sudo systemctl start jenkins

6. Access Jenkins : http://localhost:8080

7. Provide the first time password from : sudo cat /var/lib/jenkins/secrets/initialAdminPassword

8. Install Plugins and start using Jenkins



<h4>Task 1 :: Setting up webhook that triggers the job when ever code is pushed to github repo.</h4>

![Setting up git repo in jenkins](https://github.com/mukul-shaunik/ml-try1/blob/master/task1_1.png)

![Create webhook in github](https://github.com/mukul-shaunik/ml-try1/blob/master/task1_2.png)


<h3>Task 2 :: Decide the container image based on code pattern.</h3>

![code for deciding the which image to be used](https://github.com/mukul-shaunik/ml-try1/blob/master/task2_1.png)


<h3>Task 3 :: Train the model using the pulled code, initial params and run the container using image name decided in task 2</h3>

![Run the container with python model and params](https://github.com/mukul-shaunik/ml-try1/blob/master/task3_2.png)


<h3>Task 4 :: Retrain model if accuracy is less then 80%</h3>

![change the params and re trigger the task 3](https://github.com/mukul-shaunik/ml-try1/blob/master/task4_1.png)

