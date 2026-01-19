--
-- Create model Cart
--
CREATE TABLE `cart_cart` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `customer_id` varchar(50) NOT NULL, `created_at` datetime(6) NOT NULL);
--
-- Create model CartItem
--
CREATE TABLE `cart_cartitem` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `book_id` integer NOT NULL, `quantity` integer NOT NULL, `cart_id` bigint NOT NULL);
ALTER TABLE `cart_cartitem` ADD CONSTRAINT `cart_cartitem_cart_id_370ad265_fk_cart_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `cart_cart` (`id`);
