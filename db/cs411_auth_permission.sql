-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: localhost    Database: cs411
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add team_table',1,'add_team_table'),(2,'Can change team_table',1,'change_team_table'),(3,'Can delete team_table',1,'delete_team_table'),(4,'Can view team_table',1,'view_team_table'),(5,'Can add profile_table',2,'add_profile_table'),(6,'Can change profile_table',2,'change_profile_table'),(7,'Can delete profile_table',2,'delete_profile_table'),(8,'Can view profile_table',2,'view_profile_table'),(9,'Can add a_table',3,'add_a_table'),(10,'Can change a_table',3,'change_a_table'),(11,'Can delete a_table',3,'delete_a_table'),(12,'Can view a_table',3,'view_a_table'),(13,'Can add s_table',4,'add_s_table'),(14,'Can change s_table',4,'change_s_table'),(15,'Can delete s_table',4,'delete_s_table'),(16,'Can view s_table',4,'view_s_table'),(17,'Can add t_table',5,'add_t_table'),(18,'Can change t_table',5,'change_t_table'),(19,'Can delete t_table',5,'delete_t_table'),(20,'Can view t_table',5,'view_t_table'),(21,'Can add t_relation',6,'add_t_relation'),(22,'Can change t_relation',6,'change_t_relation'),(23,'Can delete t_relation',6,'delete_t_relation'),(24,'Can view t_relation',6,'view_t_relation'),(25,'Can add f_table',7,'add_f_table'),(26,'Can change f_table',7,'change_f_table'),(27,'Can delete f_table',7,'delete_f_table'),(28,'Can view f_table',7,'view_f_table'),(29,'Can add a_relation',8,'add_a_relation'),(30,'Can change a_relation',8,'change_a_relation'),(31,'Can delete a_relation',8,'delete_a_relation'),(32,'Can view a_relation',8,'view_a_relation'),(33,'Can add log entry',9,'add_logentry'),(34,'Can change log entry',9,'change_logentry'),(35,'Can delete log entry',9,'delete_logentry'),(36,'Can view log entry',9,'view_logentry'),(37,'Can add permission',10,'add_permission'),(38,'Can change permission',10,'change_permission'),(39,'Can delete permission',10,'delete_permission'),(40,'Can view permission',10,'view_permission'),(41,'Can add group',11,'add_group'),(42,'Can change group',11,'change_group'),(43,'Can delete group',11,'delete_group'),(44,'Can view group',11,'view_group'),(45,'Can add user',12,'add_user'),(46,'Can change user',12,'change_user'),(47,'Can delete user',12,'delete_user'),(48,'Can view user',12,'view_user'),(49,'Can add content type',13,'add_contenttype'),(50,'Can change content type',13,'change_contenttype'),(51,'Can delete content type',13,'delete_contenttype'),(52,'Can view content type',13,'view_contenttype'),(53,'Can add session',14,'add_session'),(54,'Can change session',14,'change_session'),(55,'Can delete session',14,'delete_session'),(56,'Can view session',14,'view_session'),(57,'Can add m_table',15,'add_m_table'),(58,'Can change m_table',15,'change_m_table'),(59,'Can delete m_table',15,'delete_m_table'),(60,'Can view m_table',15,'view_m_table'),(61,'Can add m_relation',16,'add_m_relation'),(62,'Can change m_relation',16,'change_m_relation'),(63,'Can delete m_relation',16,'delete_m_relation'),(64,'Can view m_relation',16,'view_m_relation');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-25 23:45:43
