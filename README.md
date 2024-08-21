# AA-GGY Cabs

AA-GGY Cabs is a comprehensive cab booking system designed to streamline urban transportation. This project leverages a robust RDBMS and modern web technologies to manage taxi services efficiently. It caters to customers, drivers, and administrators, providing a seamless experience for all stakeholders involved.

## Project Scope

Taxis play a crucial role in urban transportation, serving various needs from commuting to leisure. Despite the industry’s growth, there remains a significant demand for more efficient solutions. AA-GGY Cabs aims to address this by offering a cab booking system that manages customer and driver information, ride bookings, fare calculations, and more, creating an efficient platform for both drivers and passengers.

## Features

- **User Authentication:** Secure login/signup for customers.
- **Ride Booking:** Customers can book rides by entering pickup and destination locations, including an estimated time.
- **Fare Calculation:** Calculates ride fares based on distance, traffic, and time, including adjustments for traffic delays.
- **User Management:** Stores and manages customer and driver profiles.
- **Ride Tracking:** Provides information on ride status, time, fare, and details.
- **Reviews and Ratings:** Allows customers to rate drivers and provide feedback.
- **Admin Controls:** Admins can access personal information, manage accounts, and resolve fare discrepancies.
- **Parking Management:** Cabs return to the nearest parking location after a ride, making it available for the next customer.

## Technical Requirements

- **Backend:** Python, Flask, Java
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL
- **Additional Technologies:** Java

## Constraints

- **Admin Privileges:** Admins can access personal information but cannot alter ratings or reviews.
- **Customer Capabilities:** Customers can track the driver, cancel rides, and rate drivers.
- **Driver Access:** Drivers can view customer details necessary for the ride.
- **Fare Adjustments:** Only admins can make adjustments to fare discrepancies.
