--
-- Create model Customer
--
CREATE TABLE `accounts_customer` (`id` varchar(50) NOT NULL PRIMARY KEY, `name` varchar(255) NOT NULL, `email` varchar(254) NOT NULL UNIQUE, `password` varchar(255) NOT NULL);
