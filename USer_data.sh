#!/bin/bash
# Only Linux 2 version
sudo su
yum update -y
yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service
echo "Hello World from $(hostname -f)" > /var/www/html/index.html
echo "Healthy"> /var/www/html/health.html