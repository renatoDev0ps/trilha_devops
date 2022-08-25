#!/bin/bash

echo "Installing Jenkins and dependencies..."
yum install -y epel-release yum-utils git wget unzip net-tools telnet java-11-openjdk-devel stress
# curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo
# sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo wget --no-check-certificate -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum install jenkins -y
sudo systemctl daemon-reload
service jenkins start

### Instalacao do docker e docker-compose
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io -y
sudo systemctl start docker
sudo systemctl enable docker

sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
sudo systemctl daemon-reload
sudo systemctl restart docker

usermod -aG docker jenkins
chown jenkins:docker /var/run/docker.sock

# instalacao sonar scanner
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472-linux.zip
sudo mkdir -p /opt/sonar-scanner
sudo unzip sonar-scanner-cli-4.6.2.2472-linux.zip -d /opt/
sudo mv /opt/sonar-scanner-4.6.2.2472-linux/* /opt/sonar-scanner
chown -R jenkins:jenkins /opt/sonar-scanner
echo 'export PATH=$PATH:/opt/sonar-scanner/bin' | sudo tee -a /etc/profile

# instalacao do nodejs
curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
yum install nodejs -y

# instalacao do kubectl
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0775 kubectl /usr/local/bin/kubectl