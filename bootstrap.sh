#!/usr/bin/env bash

apt-get update

#apt-get install -y apache2
#rm -rf /var/www
#ln -fs /vagrant /var/www

apt-get install -y unzip
apt-get install -y git-core
apt-get install -y python-pip 
apt-get install -y python-mysqldb
pip install virtualenv
pip install Django==1.6.5
pip install boto
#pip install mysql-python==1.2.3

# Install eb (elastic beanstalk) cli tools
wget -O /home/vagrant/AWS-ElasticBeanstalk-CLI-2.6.2.zip https://s3.amazonaws.com/elasticbeanstalk/cli/AWS-ElasticBeanstalk-CLI-2.6.2.zip
unzip /home/vagrant/AWS-ElasticBeanstalk-CLI-2.6.2.zip
echo "export PATH=\$PATH:/home/vagrant/AWS-ElasticBeanstalk-CLI-2.6.2/eb/linux/python2.7" >> /home/vagrant/.profile

echo -e "\n\n\n" | ssh-keygen -t rsa -C "psivah@yahoo.com"