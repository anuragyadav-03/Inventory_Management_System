-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 04, 2023 at 08:45 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
CREATE TABLE IF NOT EXISTS `inventory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `stock` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`id`, `name`, `stock`, `price`) VALUES
(1, 'ParleG', 500, 10),
(2, 'Maria', 498, 5),
(3, 'Echlair', 500, 2),
(4, 'DairyMilk', 80, 20),
(5, 'GoodDay', 30, 10),
(6, 'Kurkure', 60, 10),
(7, 'Coke', 50, 40),
(8, 'Sprite', 30, 60),
(9, 'Namkeen', 30, 5),
(10, 'PanCake', 40, 5),
(11, 'Saon papdi', 190, 5),
(12, 'jal geera ', 899, 1);

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
CREATE TABLE IF NOT EXISTS `test` (
  `full_name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`full_name`, `email`, `username`, `password`) VALUES
('abcwe', 'wqf', 'abc', 'abc'),
('Anurag Yadav', 'ay79007@gmail.com', 'mindblaze', '123'),
('jdsn', ' cnlkwenl', 'aaa', 'aaa'),
('mjgm', 'mjjjjv', 'bbb', 'bbb'),
('drg', 'sdv', 'ccc', 'ccc'),
('amit', 'amityadav63@gmail.co', 'amit63', 'amit63'),
('ankit', 'abc', 'ankit', 'ankit'),
('Bhagwandas Gupta', 'bhagwandasgupta777@g', 'bhagwandas', 'bhagwandas');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
  `product_name` varchar(20) NOT NULL,
  `quantity` int NOT NULL,
  `price` int NOT NULL,
  `date` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
