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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-10-20 19:03:02.766018'),(2,'auth','0001_initial','2020-10-20 19:03:02.834661'),(3,'admin','0001_initial','2020-10-20 19:03:02.967621'),(4,'admin','0002_logentry_remove_auto_add','2020-10-20 19:03:03.005804'),(5,'admin','0003_logentry_add_action_flag_choices','2020-10-20 19:03:03.013717'),(6,'contenttypes','0002_remove_content_type_name','2020-10-20 19:03:03.055039'),(7,'auth','0002_alter_permission_name_max_length','2020-10-20 19:03:03.082205'),(8,'auth','0003_alter_user_email_max_length','2020-10-20 19:03:03.102456'),(9,'auth','0004_alter_user_username_opts','2020-10-20 19:03:03.109626'),(10,'auth','0005_alter_user_last_login_null','2020-10-20 19:03:03.132800'),(11,'auth','0006_require_contenttypes_0002','2020-10-20 19:03:03.134811'),(12,'auth','0007_alter_validators_add_error_messages','2020-10-20 19:03:03.142988'),(13,'auth','0008_alter_user_username_max_length','2020-10-20 19:03:03.170229'),(14,'auth','0009_alter_user_last_name_max_length','2020-10-20 19:03:03.197604'),(15,'auth','0010_alter_group_name_max_length','2020-10-20 19:03:03.215879'),(16,'auth','0011_update_proxy_permissions','2020-10-20 19:03:03.222918'),(17,'auth','0012_alter_user_first_name_max_length','2020-10-20 19:03:03.248332'),(18,'pokewiki','0001_initial','2020-10-20 19:03:03.318024'),(19,'sessions','0001_initial','2020-10-20 19:03:03.385567'),(20,'users','0001_initial','2020-10-20 19:03:03.422074'),(21,'pokewiki','0002_auto_20201020_1942','2020-10-20 19:42:38.815878'),(22,'pokewiki','0003_auto_20201020_1943','2020-10-20 19:43:51.830883'),(23,'pokewiki','0004_auto_20201020_2010','2020-10-20 20:11:34.890743'),(24,'pokewiki','0005_a_relation_is_hidden','2020-10-20 23:51:41.782369'),(25,'pokewiki','0006_m_relation_m_table','2020-10-24 01:22:51.370648'),(26,'pokewiki','0007_m_table_gen','2020-10-24 01:26:48.006767'),(27,'pokewiki','0008_auto_20201024_0209','2020-10-24 02:09:33.476529'),(28,'pokewiki','0009_auto_20201024_0210','2020-10-24 02:20:31.639042'),(29,'pokewiki','0010_auto_20201024_0220','2020-10-24 02:20:31.656314'),(30,'pokewiki','0011_auto_20201024_0220','2020-10-24 02:21:03.005240'),(31,'pokewiki','0012_auto_20201024_0221','2020-10-24 02:22:01.299128'),(32,'pokewiki','0013_auto_20201024_0222','2020-10-24 02:22:32.874059'),(33,'pokewiki','0014_auto_20201025_0217','2020-10-25 02:17:41.365940'),(34,'pokewiki','0015_auto_20201025_0235','2020-10-25 02:37:41.996543');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-25 23:45:44
