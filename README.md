 Python Script for Automation

 Jenkins install and access jenkins 
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 sudo apt-get update
 
 sudo apt install default-jdk
 
 java --version
 
 sudo wget -O /usr/share/keyrings/jenkins-keyring.asc   https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
 
 echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]"   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
 
 sudo apt update -y
 
 sudo apt install jenkins -y
 
 sudo systemctl start jenkins
 
 sudo systemctl status jenkins

 Pre-requsites: For jenkins pipeline
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Python install first

sudo apt install python3-pip -y

python3 --version

sudo apt update

sudo apt install python3-venv


Docker Install
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

sudo apt install docker.io

sudo systemctl start docker

sudo usermod -aG docker jenkins

sudo systemctl restart jenkins

sudo -u jenkins docker ps



