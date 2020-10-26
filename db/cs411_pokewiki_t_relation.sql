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
-- Table structure for table `pokewiki_t_relation`
--

DROP TABLE IF EXISTS `pokewiki_t_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokewiki_t_relation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Normal` double NOT NULL,
  `Fire` double NOT NULL,
  `Water` double NOT NULL,
  `Grass` double NOT NULL,
  `Flying` double NOT NULL,
  `Fighting` double NOT NULL,
  `Poison` double NOT NULL,
  `Electric` double NOT NULL,
  `Ground` double NOT NULL,
  `Rock` double NOT NULL,
  `Psychic` double NOT NULL,
  `Ice` double NOT NULL,
  `Bug` double NOT NULL,
  `Ghost` double NOT NULL,
  `Steel` double NOT NULL,
  `Dragon` double NOT NULL,
  `Dark` double NOT NULL,
  `Fairy` double NOT NULL,
  `t_id` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `t_id` (`t_id`),
  CONSTRAINT `pokewiki_t_relation_t_id_fc170a94_fk_pokewiki_t_table_t_name` FOREIGN KEY (`t_id`) REFERENCES `pokewiki_t_table` (`t_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokewiki_t_relation`
--

LOCK TABLES `pokewiki_t_relation` WRITE;
/*!40000 ALTER TABLE `pokewiki_t_relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `pokewiki_t_relation` ENABLE KEYS */;
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
