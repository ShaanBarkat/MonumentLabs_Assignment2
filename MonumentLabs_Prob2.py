#Monument Labs - Assignment 2 ~ Shaan Barkat

import MySQLdb
from intercom.client import Client

#DROP TABLE IF EXISTS `user`;
#CREATE TABLE `user` (
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#  `name` text NOT NULL,
#  `email` varchar(120) NOT NULL
#  PRIMARY KEY (`id`),
#  UNIQUE KEY `email` (`email`)
#) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#based off table spec

db = MySQLdb.connect(host=HOST, user=User, passwd=Passwd, db=DB)
#placeholders

intercom = Client(personal_access_token = input("Access Token here: ")
#according to the api, intercom needs a personal access code

cursor = db.cursor()
#cursor allows for the data to be selected from the table spec
                  
for row in cursor.fetchall():
    intercome.users.create(id=row[0], email=row[2], name=row[1])
    #allows for user to be created, using API

    #redundant and repeating users not accounted for,
    #barebones implemenation
