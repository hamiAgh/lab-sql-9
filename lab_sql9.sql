USE Sakila;
#In this lab we will find the customers who were active in consecutive months of May and June. Follow the steps to complete the analysis.
#Create a table rentals_may to store the data from rental table with information for the month of May.
#Insert values in the table rentals_may using the table rental, filtering values only for the month of May.

CREATE TABLE rentals_may AS
SELECT rental_id, substring(rental_date, 6, 2) AS rental_month, inventory_id, customer_id, return_date, staff_id, last_update
FROM rental
WHERE substring(rental_date, 6, 2)=05;
  
SELECT * FROM rentals_may;
  
#Create a table rentals_june to store the data from rental table with information for the month of June.
#Insert values in the table rentals_june using the table rental, filtering values only for the month of June.

CREATE TABLE rentals_june AS
SELECT rental_id, substring(rental_date, 6, 2) AS rental_month, inventory_id, customer_id, return_date, staff_id, last_update
FROM rental
WHERE substring(rental_date, 6, 2)=06;
  
SELECT * FROM rentals_june;

#Check the number of rentals for each customer for May.
SELECT rental_month, customer_id, COUNT(rental_id) AS num_rental FROM rentals_may GROUP BY rental_month, customer_id;
SELECT customer_id, COUNT(rental_id) AS num_rental FROM rentals_may GROUP BY customer_id HAVING customer_id=130;

#Check the number of rentals for each customer for June.
SELECT rental_month, customer_id, COUNT(rental_id) AS num_rental FROM rentals_june GROUP BY rental_month, customer_id;
SELECT customer_id, COUNT(rental_id) AS num_rental FROM rentals_june GROUP BY customer_id HAVING customer_id=130;