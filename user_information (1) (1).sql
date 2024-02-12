-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 22, 2023 at 12:49 PM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cism`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_information`
--

CREATE TABLE `user_information` (
  `sr no.` int(11) NOT NULL,
  `field` varchar(250) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `age` bigint(5) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `city` varchar(150) NOT NULL,
  `address` varchar(200) NOT NULL,
  `username` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `mobile_No` bigint(12) NOT NULL,
  `email` varchar(150) NOT NULL,
  `user_createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_type` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_information`
--

INSERT INTO `user_information` (`sr no.`, `field`, `first_name`, `last_name`, `age`, `gender`, `city`, `address`, `username`, `password`, `mobile_No`, `email`, `user_createtime`, `user_type`) VALUES
(1, 'admin', 'admin', 'admin', 0, 'Male', 'jaipur', 'jaipur', 'adm_12', '1234567', 6367844774, 'adm@gmail.com', '2023-09-18 07:58:52', ''),
(2, 'ADMIN', 'praveen', 'kumar', 20, 'Male', 'jaipur', 'jaipur', 'user', '123', 1234567895, 'praveen@gmail.com', '2023-09-20 07:59:40', ''),
(3, 'ADMIN', 'kamal', 'kumar', 20, 'Male', 'JAIPUR', 'jaipur', 'USER1', '123', 1234566, 'kamal@gmail.com', '2023-09-20 08:02:43', ''),
(4, 'STUDENT', 'gss', 'qwe', 36, 'Male', 'jwedfdf', 'aS', 'gss', '1234567', 6367844, 'r\'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$\'', '2023-09-21 06:33:55', ''),
(5, 'STUDENT', 'sad', 'sad', 0, 'Male', 'sad', 'asd', 'asd', '1234567', 0, 'weqr', '2023-09-21 06:35:09', ''),
(6, 'STUDENT', 'huji', 'uiujo', 78, 'Male', 'sdgd', 'fdhhdfh', 'hjk', '1234567', 0, 'anitadhawan@gmail.com', '2023-09-21 06:38:55', ''),
(7, 'STUDENT', 'dfg', 'dfg', 0, 'Male', 'asd', 'asd', 'dfdfg', '12345678', 0, 'sad', '2023-09-22 09:11:00', ''),
(8, 'STUDENT', 'sadasd', 'asd', 0, 'Male', 'asd', 'asd', 'asdasd', '125864', 0, 'asd', '2023-09-22 09:12:06', ''),
(9, 'STUDENT', 'dsfg', 'sdf', 0, 'Male', 'sdf', 'sdf', 'sdf', 'sdf', 0, 'dsf', '2023-09-22 09:16:29', ''),
(10, 'STUDENT', 'fdsf', 'sdf', 0, 'Male', 'sdf', 'sdf', 'wqewqe', '1234567', 0, 'sdf', '2023-09-22 09:20:03', ''),
(11, 'STUDENT', 'gfdg', 'dfgfdg', 0, 'Male', 'sfa', 'sad', 'dfg', '1234567', 0, 'sad', '2023-09-22 09:23:10', ''),
(12, 'STUDENT', 'ASD', 'SADASD', 0, 'Male', 'SAD', 'ASDSAD', 'ASDASDAS', '1234567', 0, 'ASD', '2023-09-22 09:35:44', ''),
(13, 'STUDENT', 'ASDF', 'DSF', 0, 'Male', 'SDF', 'SDF', '456', '1234567', 0, 'SDF', '2023-09-22 09:40:24', ''),
(14, 'STUDENT', 'SAD', 'ASD', 0, 'Male', 'ASD', 'ASD', 'SAD', 'SADSAD', 0, 'SAD', '2023-09-22 09:41:28', ''),
(15, 'STUDENT', 'asd', 'asd', 0, 'Male', 'asd', 'asdasd', 'sadasd', '6367844774', 6367844774, 'ads@gmail.com', '2023-09-22 09:52:33', ''),
(16, 'STUDENT', 'werasdrfds', 'sdf', 0, 'Male', 'asd', 'asd', 'sdfsdf', '1234567', 6367844774, 'rohit@gmail.com', '2023-09-22 09:59:52', ''),
(17, 'STUDENT', 'Gaurav', 'kumar', 18, 'Male', 'jaipur', 'jaipur', 'g1234', 'g123345', 6367844774, 'sahil@gmail.com', '2023-09-22 10:01:24', ''),
(18, 'STUDENT', 'dfg', 'fdg', 0, 'Male', 'sdf', 'sdfdsf', 'dfg455', '1234567', 6367844774, 'rohit@gmail.com', '2023-09-22 10:05:18', ''),
(19, 'STUDENT', 'dfg', 'fdg', 0, 'Male', 'g', 'dfg', 'dfg545694', '147852', 6367844774, 'rohit@gmail.com', '2023-09-22 10:06:41', ''),
(20, 'ADMIN', 'Rohit', 'Bairwa', 19, 'Male', 'jaipur', 'jaipur', 'rohit123', '1234567', 6367844774, 'rohit@gmail.com', '2023-09-22 10:15:58', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_information`
--
ALTER TABLE `user_information`
  ADD PRIMARY KEY (`sr no.`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_information`
--
ALTER TABLE `user_information`
  MODIFY `sr no.` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
