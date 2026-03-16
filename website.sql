CREATE DATABASE website;

USE website;

CREATE TABLE content (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255),
description TEXT
);

INSERT INTO content (title, description) VALUES
('Apple', 'Information about apples'),
('Banana', 'Bananas are yellow fruit'),
('Orange', 'Citrus fruit high in vitamin C'),
('Laptop', 'Portable computer device'),
('Phone', 'Modern smartphone technology');