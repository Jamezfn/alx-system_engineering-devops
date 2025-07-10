-- Primary server new use
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replicapw';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
