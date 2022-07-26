/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - online election
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`online election` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online election`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(100) NOT NULL AUTO_INCREMENT,
  `workers_category` varchar(200) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`workers_category`) values (2,'PLUMBER'),(3,'driver'),(4,'electrician'),(6,'PAINTER'),(7,'cardriveer');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(100) NOT NULL AUTO_INCREMENT,
  `from_id` varchar(200) DEFAULT NULL,
  `to_id` varchar(200) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`message`,`date`) values (1,'7','17','xjcxgk','2022-05-07'),(2,'7','17','xjcxgk','2022-05-07'),(3,'7','17',' kchivho','2022-05-07'),(4,'17','7','ghj','2022-05-07'),(5,'17','7','hkchhigih','2022-05-07'),(6,'17','7','gxgcgc','2022-05-07'),(7,'17','7','gh','2022-05-07'),(8,'17','7','cnfzj','2022-05-07'),(9,'17','7','fgh','2022-05-07'),(10,'17','7','hh','2022-05-07'),(11,'17','7','hello ','2022-05-07'),(12,'17','7','hyy','2022-05-07'),(13,'17','7','hy','2022-05-07'),(14,'7','','GAS','2022-05-07'),(15,'17','7','ahaag','2022-05-07'),(16,'17','7','hello','2022-05-07'),(17,'7','','','2022-05-07'),(18,'7','','hgh','2022-05-07'),(19,'7','','','2022-05-07'),(20,'7','','aa','2022-05-07'),(21,'7','','','2022-05-07'),(22,'20','','b','2022-05-12'),(23,'20','','hy','2022-05-12'),(24,'20','','sdf','2022-05-12'),(25,'','','hi','2022-05-12'),(26,'17','','hi','2022-05-12'),(27,'17','','hi','2022-05-12'),(28,'17','','hoiiiiii','2022-05-12'),(29,'20','17','hhj','2022-05-12'),(30,'17','7','jjk','2022-05-12'),(31,'17','20','kxkx','2022-05-12'),(32,'17','20','hyy','2022-05-12'),(33,'17','20','hhh','2022-05-12'),(34,'17','20','heloo','2022-05-12'),(35,'17','20','how are you?','2022-05-12');

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `complaint_and_reply` */

insert  into `complaint_and_reply`(`complaint_id`,`cuser_id`,`complaints`,`date`,`reply`,`reply_date`) values (1,17,'bad','2022-04-30','pending','0000-00-00'),(2,17,'????rhj','2022-05-02','pending','0000-00-00'),(3,17,'????huv','2022-05-02','pending','0000-00-00'),(4,17,'dig','2022-05-02','pending','0000-00-00'),(5,17,'yoo','2022-05-02','pending','0000-00-00'),(6,17,'theere pora','2022-05-07','sdv','2022-05-12'),(7,17,'yjx','2022-05-12','pending','0000-00-00');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(100) NOT NULL AUTO_INCREMENT,
  `f_uid` int(100) NOT NULL,
  `feedback` char(255) NOT NULL,
  `date` varchar(100) NOT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`f_uid`,`feedback`,`date`) values (1,2,'highly recomended','2010-09-21'),(2,17,'vrygood','2022-03-14'),(3,17,'ji','2022-03-21'),(4,17,'hello','2022-03-21'),(5,17,'','2022-03-21'),(6,17,'','2022-03-21'),(7,17,'','2022-03-21'),(8,17,'','2022-03-21'),(9,17,'','2022-03-21'),(10,17,'hh','2022-03-21'),(11,17,'hhhh','2022-04-30'),(12,17,'not bad','2022-05-02'),(13,17,'hello','2022-05-02'),(14,17,'cnn h','2022-05-02'),(15,17,'ruis','2022-05-02'),(16,17,'pora','2022-05-07'),(17,17,'','2022-05-07'),(18,17,'','2022-05-07'),(19,17,'dfh','2022-05-07'),(20,17,'dkc','2022-05-12');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `u_type` varchar(100) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`u_type`) values (1,'admin','admin','admin'),(4,'wrfw','7234','pending'),(6,'thanzeerthansi96@gmail.com','6802','pending'),(7,'gokul.ramesh2k@gmail.com','117','worker'),(8,'sangeerth123@gmail.com','1478','worker'),(9,'gokul.ramesh2k@gmail.com','7946','worker'),(10,'thasneem.musthafa.889@gmail.com','2623','user'),(11,'thasneem.musthafa.889@gmail.com','5618','user'),(12,'GOKUL@GMAIL.COM','5713','user'),(13,'sangeerth123@gmail.com','195','user'),(14,'sangeerth123@gmail.com','2800','user'),(15,'gokul.ramesh2k@gmail.com','3276','user'),(16,'sangeerth123@gmail.com','8893','user'),(17,'thasneem.musthafa.889@gmail.com','4321','user'),(18,'arjunan@gmail.com','6685','worker'),(19,'thasneem.musthafa.889@gmail.com','4357','worker'),(20,'athira@gmail.com','2890','worker'),(25,'jhgh@gfcfv','1694','pending'),(26,'2000/02/05','abcd','user'),(27,'0788','ncjdk','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(100) NOT NULL AUTO_INCREMENT,
  `notification` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`notification`,`date`) values (1,'helloooo','2022-01-08'),(2,'exciting offers only for you..join now','2022-01-08'),(3,'','2022-01-13'),(4,'poda mone','2022-01-15'),(5,'x','2022-01-15'),(6,'hello','2022-01-15'),(7,'poda mone','2022-01-17'),(8,'sdv','2022-05-12');

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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `ratings_and_reviews` */

insert  into `ratings_and_reviews`(`rating_id`,`rating`,`review`,`date`,`worker_id`,`user_id`) values (1,'5','good','2022-04-30',7,17),(2,'3.0','gooood','2022-04-30',7,17),(3,'pending','hhj','2022-04-30',7,17),(4,'pending','hkkl','2022-04-30',7,17),(5,'5.0','sangee','2022-05-02',7,17),(6,'5.0','gh','2022-05-02',7,17),(7,'4.5','gooid','2022-05-02',7,17),(8,'1.0','pora','2022-05-02',7,17),(9,'3.5','xg','2022-05-02',7,17),(10,'4.0','ghj','2022-05-07',7,17),(11,'5.0','ggihgy','2022-05-07',7,17),(12,'pending','dd','2022-05-07',7,17),(13,'3.0','dd','2022-05-07',7,17),(14,'3.0','ndjdj','2022-05-13',7,17);

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `service_id` int(100) NOT NULL AUTO_INCREMENT,
  `service_type` varchar(200) DEFAULT NULL,
  `charges` varchar(200) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `service` */

insert  into `service`(`service_id`,`service_type`,`charges`,`worker_id`) values (1,'fixing pipe','3500',20),(2,'broken','30',8),(7,'plumbing','450',20),(8,'','',20);

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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`u_name`,`hname`,`place`,`post`,`pin`,`age`,`email`,`gender`,`photo`,`phone_number`) values (15,'sds','reemas','pnr','pnr',32145,20,'gokul.ramesh2k@gmail.com','MALE',NULL,'8281857487'),(16,'sds','reemas','pnr','pnr',32145,12,'sangeerth123@gmail.com','MALE','/static/userpic/220129-165048.jpg','8281857487'),(17,'mmm','ree','pnr','pnr',32145,32,'thasneem.musthafa.889@gmail.com','MALE','/static/userpic/220129-165819.jpg','8281857487'),(26,'bbb','bbb','kannur','kannur',0,0,'2000/02/05','9797','/static/userpic/220513-140945.jpg','abcd'),(27,'xjx','ndj','hdj','jxjd',0,0,'0788','95956','/static/userpic/220513-141215.jpg','ncjdk');

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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `work_request` */

insert  into `work_request`(`request_id`,`user_ID`,`Service_id`,`description`,`status`,`date`) values (2,17,7,'cvb','completed','2022-04-30'),(4,17,9,'vn','pending','2022-05-02'),(6,17,8,'n','pending','2022-05-07'),(7,17,19,'vn','pending','2022-05-07'),(8,17,18,'vb','pending','2022-05-07'),(9,17,7,'','pending','2022-05-13');

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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `worker` */

insert  into `worker`(`user_id`,`name`,`home`,`place`,`post`,`pin`,`age`,`photo`,`phone_number`,`category`,`experience`,`gender`,`email`) values (7,'gokul','gokulam','kanhiram','chokli',670691,'0000-00-00','/static/pic/220129-170629.jpg','8592972557','Painter','3 years','Female','gokul.ramesh2k@gmail.com'),(8,'sangeerth','samgeertham','kuruva','kannur',670625,'0000-00-00','/static/pic/220122-150131.jpg','6238301369','Helper','2 years','Male','sangeerth123@gmail.com'),(9,'gokl','gklm','chokli','cjokli',6352,'0000-00-00','/static/pic/220129-141040.jpg','965','Carpenter','2year','Others','gokul.ramesh2k@gmail.com'),(18,'arjun','ajunm','mahe','mhe',362,'0000-00-00','/static/pic/220129-170904.jpg','78965412','Electrician','2 years','Male','arjunan@gmail.com'),(19,'thasneem','reemas','pnr','qq',20,'0000-00-00','/static/pic/220129-171805.jpg','55555555','Gardener','12','Male','thasneem.musthafa.889@gmail.com'),(20,'athira','kannur','kannur','mmm',0,'0000-00-00','/static/pic/220512-112648.jpg','9898765434567','Gardener','0','Female','athira@gmail.com'),(25,'athira','hgf','jht','hf',0,'0000-00-00','/static/pic/220512-104213.jpg','6733333333','Plumber','fdgj','Female','jhgh@gfcfv');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
