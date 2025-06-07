CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  description TEXT,
  price DECIMAL(10,2),
  category VARCHAR(50),
  image_url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert 100 sample products
DELIMITER $$
CREATE PROCEDURE seed_products()
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= 100 DO
    INSERT INTO products(name, description, price, category, image_url)
    VALUES(
      CONCAT('Product ', i),
      CONCAT('Description for product ', i),
      ROUND(RAND()*500 + 10,2),
      ELT( (i % 5) + 1, 'Electronics','Books','Textiles','Gadgets','Accessories'),
      CONCAT('https://picsum.photos/seed/', i, '/200/200')
    );
    SET i = i + 1;
  END WHILE;
END$$
DELIMITER ;

CALL seed_products();
DROP PROCEDURE seed_products;
