/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - get_me_help
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`get_me_help` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `get_me_help`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(100) NOT NULL AUTO_INCREMENT,
  `workers_category` varchar(200) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `category` */

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(100) NOT NULL AUTO_INCREMENT,
  `from_id` varchar(200) DEFAULT NULL,
  `to_id` varchar(200) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `complaint_and_reply` */

DROP TABLE IF EXISTS `complaint_and_reply`;

CREATE TABLE `complaint_and_reply` (
  `complaint_id` int(100) NOT NULL AUTO_INCREMENT,
  `cuser_id` int(100) NOT NULL,
  `complaints` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `reply_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint_and_reply` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(100) NOT NULL AUTO_INCREMENT,
  `f_uid` int(100) NOT NULL,
  `feedback` char(255) NOT NULL,
  `date` varchar(100) NOT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `u_type` varchar(100) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into 'login'(`login_id`,`username`,`password`,`u_type`) values (1,'admin','admin','admin');
insert  into 'login'(`login_id`,`username`,`password`,`u_type`) values (2,'Ak','test','admin');
insert  into 'logjn'('login_id','username','password','u_type') values (3,'gokul.ramesh2k@gmail.com','abcd','user'); 

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(100) NOT NULL AUTO_INCREMENT,
  `notification` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

/*Table structure for table `ratings_and_reviews` */

DROP TABLE IF EXISTS `ratings_and_reviews`;

CREATE TABLE `ratings_and_reviews` (
  `rating_id` int(100) NOT NULL AUTO_INCREMENT,
  `rating` varchar(200) DEFAULT NULL,
  `review` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `worker_id` int(100) DEFAULT NULL,
  `user_id` int(100) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ratings_and_reviews` */

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `service_id` int(100) NOT NULL AUTO_INCREMENT,
  `service_type` varchar(200) DEFAULT NULL,
  `charges` varchar(200) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `service` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(100) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(100) DEFAULT NULL,
  `hname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` int(100) DEFAULT NULL,
  `age` int(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

/*Table structure for table `work_request` */

DROP TABLE IF EXISTS `work_request`;

CREATE TABLE `work_request` (
  `request_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_ID` int(100) DEFAULT NULL,
  `Service_id` int(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `work_request` */

/*Table structure for table `worker` */

DROP TABLE IF EXISTS `worker`;

CREATE TABLE `worker` (
  `user_id` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `home` varchar(200) DEFAULT NULL,
  `place` varchar(200) DEFAULT NULL,
  `post` varchar(200) DEFAULT NULL,
  `pin` int(100) DEFAULT NULL,
  `age` date DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `phone_number` varchar(200) DEFAULT NULL,
  `category` varchar(200) DEFAULT NULL,
  `experience` varchar(200) DEFAULT NULL,
  `gender` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `worker` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
