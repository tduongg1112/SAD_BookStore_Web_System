--
-- Create model Book
--
CREATE TABLE `books_book` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(255) NOT NULL, `author` varchar(255) NOT NULL, `price` double precision NOT NULL, `stock` integer NOT NULL);
