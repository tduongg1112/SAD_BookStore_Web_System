--
-- Create model BookModel
--
CREATE TABLE `clean_book` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(255) NOT NULL, `author` varchar(255) NOT NULL, `price` double precision NOT NULL, `stock` integer NOT NULL);
--
-- Create model CartModel
--
CREATE TABLE `clean_cart` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_at` datetime(6) NOT NULL);
--
-- Create model CustomerModel
--
CREATE TABLE `clean_customer` (`id` varchar(50) NOT NULL PRIMARY KEY, `name` varchar(255) NOT NULL, `email` varchar(254) NOT NULL UNIQUE, `password` varchar(255) NOT NULL);
--
-- Create model CartItemModel
--
CREATE TABLE `clean_cartitem` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `quantity` integer NOT NULL, `book_id` bigint NOT NULL, `cart_id` bigint NOT NULL);
--
-- Add field customer to cartmodel
--
ALTER TABLE `clean_cart` ADD COLUMN `customer_id` varchar(50) NOT NULL UNIQUE , ADD CONSTRAINT `clean_cart_customer_id_f807b3e8_fk_clean_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `clean_customer`(`id`);
ALTER TABLE `clean_cartitem` ADD CONSTRAINT `clean_cartitem_book_id_53e1178e_fk_clean_book_id` FOREIGN KEY (`book_id`) REFERENCES `clean_book` (`id`);
ALTER TABLE `clean_cartitem` ADD CONSTRAINT `clean_cartitem_cart_id_9b7abfa8_fk_clean_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `clean_cart` (`id`);
