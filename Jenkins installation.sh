#!/bin/bash

# Exit on any error
set -e

echo "Starting Jenkins, Python, and Docker installation..."

# Update system packages
echo "Updating system packages..."
sudo apt-get update

# Install Java
echo "Installing Java..."
sudo apt install default-jdk -y
java --version

# Install Jenkins
echo "Installing Jenkins..."
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update -y
sudo apt install jenkins -y

# Start Jenkins service
echo "Starting Jenkins service..."
sudo systemctl start jenkins
sudo systemctl status jenkins

# Install Python and dependencies
echo "Installing Python and dependencies..."
sudo apt install python3-pip -y
python3 --version
sudo apt update
sudo apt install python3-venv -y

# Install Docker
echo "Installing Docker..."
sudo apt install docker.io -y
sudo systemctl start docker

# Add Jenkins user to Docker group
echo "Configuring Docker permissions for Jenkins..."
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins

# Verify Docker access for Jenkins user
echo "Verifying Docker access for Jenkins user..."
sudo -u jenkins docker ps

echo "Installation complete!"
echo "Please check Jenkins status and access it through your browser at http://localhost:8080"
echo "You can find the initial admin password at: /var/lib/jenkins/secrets/initialAdminPassword"