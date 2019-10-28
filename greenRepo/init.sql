create database greenrepo;
create user 'greenlab'@'localhost' identified by 'Greens1234'
GRANT ALL PRIVILEGES ON greenrepo.* to 'greenlab'@'localhost';
