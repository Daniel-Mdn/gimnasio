-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: aplicaciongym
-- ------------------------------------------------------
-- Server version	5.7.29-log

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
-- Table structure for table `ejercicio`
--

DROP TABLE IF EXISTS `ejercicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ejercicio` (
  `id_ejercicio` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) DEFAULT NULL,
  `descripcion` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id_ejercicio`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ejercicio`
--

LOCK TABLES `ejercicio` WRITE;
/*!40000 ALTER TABLE `ejercicio` DISABLE KEYS */;
INSERT INTO `ejercicio` VALUES (1,'Sentadilla','Se puede realizar con barra o en maquina'),(2,'Sentadilla Bulgara','Se puede realizar una sola mancuerna o dos'),(3,'Gemelos piernas rectas','Se puede realizar en maquina, barras o mancuernas'),(5,'Press banca inclinado','Se puede realizar con maquinas, barras o mancuernas'),(6,'Cruce de polea alta','Se realiza en poleas'),(7,'Curl de biseps','Se realiza con mancuerna, barra o polea'),(8,'Extensiones de triseps','Se realiza en polea'),(9,'Extensiones de cuadriceps','Se realiza en maquina'),(10,'Curl de isquios','Se realiza en maquina'),(11,'Gemelos sentado','Se realiza en maquina'),(12,'Jalon al pecho','Se realiza en maquina'),(13,'Press de hombros','Se realiza con maquina, mancuernas o barra'),(14,'Peso muerto','Se realiza con barra'),(15,'Remo horizontal','Se realiza en maquina'),(16,'Remo al menton','Se realiza en poleas'),(17,'Vuelos laterales','Se realiza con mancuernas o polea');
/*!40000 ALTER TABLE `ejercicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entrenador`
--

DROP TABLE IF EXISTS `entrenador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entrenador` (
  `id_entrenador` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `dni` varchar(45) DEFAULT NULL,
  `cargo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_entrenador`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entrenador`
--

LOCK TABLES `entrenador` WRITE;
/*!40000 ALTER TABLE `entrenador` DISABLE KEYS */;
/*!40000 ALTER TABLE `entrenador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial_rutina`
--

DROP TABLE IF EXISTS `historial_rutina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_rutina` (
  `id_historial` int(11) NOT NULL AUTO_INCREMENT,
  `id_rutina` int(11) NOT NULL,
  `id_ejerc` int(11) NOT NULL,
  `fecha_realizacion` date DEFAULT NULL,
  `peso` int(11) DEFAULT NULL,
  `repeticiones` int(11) DEFAULT NULL,
  `descanso` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_historial`,`id_rutina`),
  KEY `gistorial_rutina_rutina_idx` (`id_rutina`),
  CONSTRAINT `gistorial_rutina_rutina` FOREIGN KEY (`id_rutina`) REFERENCES `rutina` (`id_rutina`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_rutina`
--

LOCK TABLES `historial_rutina` WRITE;
/*!40000 ALTER TABLE `historial_rutina` DISABLE KEYS */;
INSERT INTO `historial_rutina` VALUES (27,1,1,'2021-11-10',20,12,90),(28,1,1,'2021-11-10',20,12,90),(29,1,1,'2021-11-10',15,14,90),(30,1,2,'2021-11-10',10,15,90),(31,1,2,'2021-11-10',10,15,90),(32,1,3,'2021-11-10',20,10,90),(33,1,3,'2021-11-10',25,12,90),(34,1,3,'2021-11-10',30,13,90),(35,1,5,'2021-11-10',20,12,150),(36,1,5,'2021-11-10',20,12,120),(37,1,5,'2021-11-10',20,10,120),(38,1,6,'2021-11-10',10,15,90),(39,1,6,'2021-11-10',10,15,90),(40,1,7,'2021-11-10',8,12,90),(41,1,7,'2021-11-10',10,12,90),(42,1,7,'2021-11-10',12,12,90),(43,1,8,'2021-11-10',15,10,90),(44,1,8,'2021-11-10',15,10,90),(45,1,8,'2021-11-10',15,10,90),(46,2,5,'2021-11-10',20,12,60),(47,2,5,'2021-11-10',20,12,120),(48,2,5,'2021-11-10',25,12,120),(49,2,7,'2021-11-10',15,10,120),(50,2,7,'2021-11-10',15,10,120),(51,2,7,'2021-11-10',15,10,120),(52,2,8,'2021-11-10',15,10,120),(53,2,8,'2021-11-10',15,10,120),(54,2,8,'2021-11-10',15,10,120),(55,2,9,'2021-11-10',20,15,90),(56,2,9,'2021-11-10',20,15,90),(57,2,9,'2021-11-10',20,15,90),(58,2,10,'2021-11-10',15,12,120),(59,2,10,'2021-11-10',15,12,120),(60,2,10,'2021-11-10',15,12,120),(61,2,11,'2021-11-10',15,20,90),(62,2,11,'2021-11-10',15,20,90),(63,2,12,'2021-11-10',25,20,60),(64,2,12,'2021-11-10',25,20,60),(65,2,12,'2021-11-10',25,20,60),(66,2,13,'2021-11-10',15,12,120),(67,2,13,'2021-11-10',15,12,120),(68,2,13,'2021-11-10',15,12,120);
/*!40000 ALTER TABLE `historial_rutina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial_usuario`
--

DROP TABLE IF EXISTS `historial_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_usuario` (
  `id_historial_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) NOT NULL,
  `imc` int(11) DEFAULT '0',
  `metabolismo_basal` int(11) DEFAULT '0',
  `porcentaje_grasa` int(11) DEFAULT '0',
  `fecha_historial` date DEFAULT NULL,
  PRIMARY KEY (`id_historial_usuario`,`id_usuario`),
  KEY `historia_usuario_usuario_fk_idx` (`id_usuario`),
  CONSTRAINT `historial_usuario_usuario_fk` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_usuario`
--

LOCK TABLES `historial_usuario` WRITE;
/*!40000 ALTER TABLE `historial_usuario` DISABLE KEYS */;
INSERT INTO `historial_usuario` VALUES (1,14,27,1968,-13,'2021-11-18'),(2,14,26,1911,-14,'2021-11-18');
/*!40000 ALTER TABLE `historial_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prueba`
--

DROP TABLE IF EXISTS `prueba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prueba` (
  `id_prueba` int(11) NOT NULL,
  `descripcion` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_prueba`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prueba`
--

LOCK TABLES `prueba` WRITE;
/*!40000 ALTER TABLE `prueba` DISABLE KEYS */;
/*!40000 ALTER TABLE `prueba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rutina`
--

DROP TABLE IF EXISTS `rutina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rutina` (
  `id_rutina` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `estado` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_rutina`,`fecha`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rutina`
--

LOCK TABLES `rutina` WRITE;
/*!40000 ALTER TABLE `rutina` DISABLE KEYS */;
INSERT INTO `rutina` VALUES (1,'2021-11-09','Full Body Dia 1','Creada'),(2,'2021-11-10','Full body Dia 2','Creada');
/*!40000 ALTER TABLE `rutina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rutina_ejercicio`
--

DROP TABLE IF EXISTS `rutina_ejercicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rutina_ejercicio` (
  `fecha_rutina` date NOT NULL,
  `id_rutina` int(11) NOT NULL,
  `id_ejercicio` int(11) NOT NULL,
  `descanso` int(11) DEFAULT NULL,
  `repeticiones` int(11) DEFAULT NULL,
  `peso` int(11) DEFAULT NULL,
  `series` int(11) DEFAULT NULL,
  PRIMARY KEY (`fecha_rutina`,`id_rutina`,`id_ejercicio`),
  KEY `rutina_ejercicio_rutina_idx` (`id_rutina`),
  KEY `rutina_ejercicio_ejercicio_idx` (`id_ejercicio`),
  CONSTRAINT `rutina_ejercicio_ejercicio` FOREIGN KEY (`id_ejercicio`) REFERENCES `ejercicio` (`id_ejercicio`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `rutina_ejercicio_rutina` FOREIGN KEY (`id_rutina`) REFERENCES `rutina` (`id_rutina`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rutina_ejercicio`
--

LOCK TABLES `rutina_ejercicio` WRITE;
/*!40000 ALTER TABLE `rutina_ejercicio` DISABLE KEYS */;
INSERT INTO `rutina_ejercicio` VALUES ('2021-11-10',1,1,90,12,20,3),('2021-11-10',1,2,90,15,10,2),('2021-11-10',1,3,90,12,20,3),('2021-11-10',1,5,120,12,20,3),('2021-11-10',1,6,90,15,10,2),('2021-11-10',1,7,90,10,8,3),('2021-11-10',1,8,90,10,15,3),('2021-11-10',2,5,120,12,20,3),('2021-11-10',2,7,120,10,15,3),('2021-11-10',2,8,120,10,15,3),('2021-11-10',2,9,90,15,20,3),('2021-11-10',2,10,120,12,15,3),('2021-11-10',2,11,90,20,15,2),('2021-11-10',2,12,60,20,25,3),('2021-11-10',2,13,120,12,15,3);
/*!40000 ALTER TABLE `rutina_ejercicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `apellido` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `mail` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `contra` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `sexo` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `altura` double DEFAULT NULL,
  `peso` double DEFAULT NULL,
  `cintura` double DEFAULT NULL,
  `cuello` double DEFAULT NULL,
  `caderas` double DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `usuario_UNIQUE` (`usuario`),
  UNIQUE KEY `mail_UNIQUE` (`mail`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (14,'Danwife','Daniel','Medina','danielmedina012@gmail.com','Alexander1','Masculino','2021-11-04',177,80,80,61,75),(15,'Juan','Juan','Ruiz','juan012@gmail.com','123','Masculino','1999-07-15',180,80,80,40,75);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_rutina`
--

DROP TABLE IF EXISTS `usuario_rutina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_rutina` (
  `id_usuario` int(11) NOT NULL,
  `id_rutina` int(11) NOT NULL,
  `fecha_rutina` date DEFAULT NULL,
  PRIMARY KEY (`id_usuario`,`id_rutina`),
  KEY `usuario_rutina_rutina_fk_idx` (`id_rutina`),
  CONSTRAINT `usuario_rutina_rutina_fk` FOREIGN KEY (`id_rutina`) REFERENCES `rutina` (`id_rutina`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `usuario_rutina_usuario_fk` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_rutina`
--

LOCK TABLES `usuario_rutina` WRITE;
/*!40000 ALTER TABLE `usuario_rutina` DISABLE KEYS */;
INSERT INTO `usuario_rutina` VALUES (14,1,'2021-11-10'),(14,2,'2021-11-10');
/*!40000 ALTER TABLE `usuario_rutina` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-18 17:34:55
