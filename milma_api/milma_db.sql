-- SQL script to create the milma_db and tables manually

CREATE DATABASE IF NOT EXISTS milma_db;
USE milma_db;

CREATE TABLE farmer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    village VARCHAR(100),
    contact VARCHAR(100),
    bank_account VARCHAR(100)
);

CREATE TABLE milk_collection (
    id INT AUTO_INCREMENT PRIMARY KEY,
    farmer_id INT NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    volume_litres FLOAT,
    fat_percentage FLOAT,
    snf_percentage FLOAT,
    FOREIGN KEY (farmer_id) REFERENCES farmer(id)
);

CREATE TABLE payment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    collection_id INT NOT NULL,
    amount FLOAT,
    status VARCHAR(50),
    date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (farmer_id) REFERENCES farmer(id)
);
