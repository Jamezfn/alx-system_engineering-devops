0. Install MySQL
To install MySQL 5.7 on your web-01 and web-02 servers, you can follow these steps. Note that the commands should be executed on both servers. Here’s a step-by-step guide:

Step 1: Update the Package List
Ensure your package list is up-to-date.
	sudo apt-get update

Step 2: Install MySQL 5.7
Add the MySQL APT repository.
	sudo apt-get install -y wget
	wget https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb
	sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb

1. Let us in!
Create MySQL User with Specific Permissions

Log in to MySQL:
	sudo mysql -u root -p

Create the user holberton_user with the required permissions:
	CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
	GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
	FLUSH PRIVILEGES;

Verify the grants for holberton_user:
	mysql -u holberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost';"

Step 4: Configure SSH for Both Servers
Ensure SSH Key Access for web-02
	1. Copy your SSH key to web-02:
		ssh-copy-id ubuntu@<web-02-ip-address>
	2. Verify you can SSH into web-02 without a password:
		ssh ubuntu@<web-02-ip-address>

