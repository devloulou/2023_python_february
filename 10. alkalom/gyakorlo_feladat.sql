CREATE TABLE webshop_data (
    product_id INT NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    product_description TEXT,
    price DECIMAL(10,2) NOT NULL,
    category_id INT NOT NULL,
    category_name VARCHAR(255) NOT NULL,
    order_id INT NOT NULL,
    user_id INT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    order_date DATE NOT NULL,
    PRIMARY KEY (product_id, order_id)
);

INSERT INTO webshop_data (product_id, product_name, product_description, price, category_id, category_name, order_id, user_id, user_name, user_email, order_date)
VALUES
(1, 'Laptop', 'Dell XPS 13', 1499.99, 1, 'Számítástechnika', 1, 1, 'Kovács Béla', 'kovacs.bela@gmail.com', '2022-01-01'),
(2, 'Okostelefon', 'Samsung Galaxy S21', 999.99, 2, 'Mobiltelefon', 2, 2, 'Nagy László', 'nagy.laszlo@gmail.com', '2022-01-02'),
(3, 'Asztali számítógép', 'Apple iMac', 2199.99, 1, 'Számítástechnika', 3, 3, 'Tóth Lilla', 'toth.lilla@gmail.com', '2022-01-03'),
(4, 'Bluetooth hangszóró', 'JBL Charge 5', 199.99, 3, 'Audió és video', 4, 4, 'Kiss Gábor', 'kiss.gabor@gmail.com', '2022-01-04'),
(5, 'E-book olvasó', 'Amazon Kindle Paperwhite', 129.99, 4, 'E-könyv olvasók', 5, 5, 'Szabó Anna', 'szabo.anna@gmail.com', '2022-01-05'),
(1, 'Laptop', 'Dell XPS 13', 1499.99, 1, 'Számítástechnika', 6, 2, 'Nagy László', 'nagy.laszlo@gmail.com', '2022-01-07'),
(3, 'Asztali számítógép', 'Apple iMac', 2199.99, 1, 'Számítástechnika', 7, 1, 'Kovács Béla', 'kovacs.bela@gmail.com', '2022-01-09'),
(5, 'E-book olvasó', 'Amazon Kindle Paperwhite', 129.99, 4, 'E-könyv olvasók', 8, 4, 'Kiss Gábor', 'kiss.gabor@gmail.com', '2022-01-10'),
(2, 'Okostelefon', 'Samsung Galaxy S21', 999.99, 2, 'Mobiltelefon', 9, 3, 'Tóth Lilla', 'toth.lilla@gmail.com', '2022-01-12'),
(4, 'Bluetooth hangszóró', 'JBL Charge 5', 199.99, 3, 'Audió és video', 10, 5, 'Szabó Anna', 'szabo.anna@gmail.com', '2022-01-14');


-- Nagy László
INSERT INTO webshop_data (product_id, product_name, product_description, price, category_id, category_name, order_id, user_id, user_name, user_email, order_date)
VALUES
(2, 'Smartphone', 'iPhone 13 Pro', 1299.99, 2, 'Mobiltelefonok', 6, 3, 'Nagy László', 'nagy.laszlo@gmail.com', '2022-02-15'),
(4, 'Tablet', 'iPad Pro', 1099.99, 2, 'Mobiltelefonok', 7, 3, 'Nagy László', 'nagy.laszlo@gmail.com', '2022-02-17'),
(6, 'Smartwatch', 'Apple Watch Series 7', 699.99, 3, 'Okosórák', 8, 3, 'Nagy László', 'nagy.laszlo@gmail.com', '2022-02-19');
