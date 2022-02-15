-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 02, 2022 at 05:22 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `id_anggota` char(10) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `alamat` text DEFAULT NULL,
  `nohp` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `anggota`
--

INSERT INTO `anggota` (`id_anggota`, `nama`, `alamat`, `nohp`) VALUES
('1', 'Jovi', 'Bandung', '081313162548'),
('2', 'Nisa', 'Bandung', '081313162548'),
('3', 'Dera', 'bandung', '081313162548'),
('4', 'Julian', 'Bandung', '081313162548');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `kodeBuku` varchar(10) NOT NULL,
  `judulBuku` varchar(200) NOT NULL,
  `penerbit` varchar(100) NOT NULL,
  `penulis` varchar(100) NOT NULL,
  `tahunTerbit` varchar(20) NOT NULL,
  `posisiRak` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`kodeBuku`, `judulBuku`, `penerbit`, `penulis`, `tahunTerbit`, `posisiRak`) VALUES
('KB001', 'Malin Kundang', 'Bentang Pustaka ', 'Andrea Hirata', '2005', 'KR001'),
('KB002', 'Kancil', 'Pustaka Sandro Jaya', 'Rahimsyah AR., MB.', '2011', 'KR001'),
('KB003', 'PHP', 'GAGAS MEDIA', 'RADITYA DIKA', '2006', 'KR002'),
('KB004', 'SEPATU DAHLAN', 'NOURA BOOKS', 'KHRISNA PABICHARA', '2012', 'KR003');

-- --------------------------------------------------------

--
-- Table structure for table `petugas`
--

CREATE TABLE `petugas` (
  `id_petugas` char(9) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `alamat` text DEFAULT NULL,
  `jamTugas` varchar(50) DEFAULT NULL,
  `nohp` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `petugas`
--

INSERT INTO `petugas` (`id_petugas`, `nama`, `alamat`, `jamTugas`, `nohp`) VALUES
('1', 'Stein', 'Bandung', 'Jam 12 - 6', '081313162548'),
('2', 'Drevilia', 'Bandung', 'Jam 7 - 12', '081313162548');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` char(10) NOT NULL,
  `id_anggota` char(10) NOT NULL,
  `kodeBuku` char(10) NOT NULL,
  `tglpinjam` varchar(20) DEFAULT NULL,
  `tglkembali` varchar(20) DEFAULT NULL,
  `keterangan` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id_transaksi`, `id_anggota`, `kodeBuku`, `tglpinjam`, `tglkembali`, `keterangan`) VALUES
('1', '1', 'KB001', '2', '5', 'sudah dikembalikan'),
('2', '2', 'KB003', '10', '15', 'sudah dikembalikan'),
('3', '3', 'KB002', '17', '20', 'sudah dikembalikan'),
('4', '4', 'KB004', '25', '27', 'belum dikembalikan'),
('5', '1', 'KB003', '28', '31', 'sudah dikembalikan'),
('6', '3', 'KB002', '29', '5', 'belum dikembalikan');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`id_anggota`);

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`kodeBuku`);

--
-- Indexes for table `petugas`
--
ALTER TABLE `petugas`
  ADD PRIMARY KEY (`id_petugas`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`,`id_anggota`,`kodeBuku`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
