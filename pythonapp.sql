-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mysql:3306
-- Generation Time: Lis 14, 2025 at 09:20 AM
-- Wersja serwera: 9.5.0
-- Wersja PHP: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `pythonapp`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `miejsca`
--

CREATE TABLE `miejsca` (
  `ID` int NOT NULL,
  `adres` varchar(255) NOT NULL,
  `miasto` varchar(255) NOT NULL,
  `deleted` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Zrzut danych tabeli `miejsca`
--

INSERT INTO `miejsca` (`ID`, `adres`, `miasto`, `deleted`) VALUES
(1, 'Nowa 120', 'Cyganka', 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `organizatorzy`
--

CREATE TABLE `organizatorzy` (
  `ID` int NOT NULL,
  `imie` varchar(255) NOT NULL,
  `nazwisko` varchar(255) NOT NULL,
  `telefon` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `rodzaj`
--

CREATE TABLE `rodzaj` (
  `ID` int NOT NULL,
  `nazwa` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wydarzenia`
--

CREATE TABLE `wydarzenia` (
  `ID` int NOT NULL,
  `id_organizatora` int NOT NULL,
  `id_miejsca` int NOT NULL,
  `id_rodzaju` int NOT NULL,
  `nazwa` varchar(255) NOT NULL,
  `data` varchar(20) NOT NULL,
  `godz_zacz` varchar(10) NOT NULL,
  `godz_zak` varchar(10) NOT NULL,
  `deleted` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Zrzut danych tabeli `wydarzenia`
--

INSERT INTO `wydarzenia` (`ID`, `id_organizatora`, `id_miejsca`, `id_rodzaju`, `nazwa`, `data`, `godz_zacz`, `godz_zak`, `deleted`) VALUES
(1, 1, 2, 3, 'Koncert Jazzowy', '2025-12-15', '19:00:00', '23:00:00', 1);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `miejsca`
--
ALTER TABLE `miejsca`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `organizatorzy`
--
ALTER TABLE `organizatorzy`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `rodzaj`
--
ALTER TABLE `rodzaj`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `wydarzenia`
--
ALTER TABLE `wydarzenia`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `miejsca`
--
ALTER TABLE `miejsca`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `organizatorzy`
--
ALTER TABLE `organizatorzy`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `rodzaj`
--
ALTER TABLE `rodzaj`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `wydarzenia`
--
ALTER TABLE `wydarzenia`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
