📌 Event Management System

(Frappe Framework)

📖 Project Overview

This project is a Frappe-based Event Management Web Application developed as part of a Developer Hiring Test.

The application helps event planners to:

Create and manage events

Register attendees

Sell tickets

Track event capacity and revenue

Import events using CSV files

Generate basic analytical reports

The system is designed for single-role usage (Event Planner) and focuses on core business logic, avoiding complex permission management.

🛠️ Tech Stack

Backend: Frappe Framework (Python)

Database: MariaDB (via Frappe)

Frontend: Frappe Desk UI

Version Control: Git & GitHub

🗂️ DocTypes Used
1️⃣ Event Detail

Stores all event-related information.

Fields:

Event Title

Description

Event Date

Location

Capacity

Ticket Price

Tickets Sold

Remaining Capacity

2️⃣ Attendee

Stores attendee information and links them to events.

Fields:

Attendee Name

Email

Phone

Event (Link to Event Detail)

3️⃣ Ticket Sale

Handles ticket sales and revenue tracking.

Fields:

Event (Link to Event Detail)

Attendee

Quantity

Total Price

✅ Features Implemented
🔹 Base Event System (CRUD)

Create, Read, Update, Delete Events

Create, Read, Update, Delete Attendees

Create, Read, Update, Delete Ticket Sales

🔹 Event Management

Create events with required fields

Update and delete events

Search and filter events by:

Event Title

Event Date

🔹 Attendee Management

Register attendees for events

Update attendee details

Link attendees to specific events

🔹 Ticket Sales

Auto-calculate Total Price (Ticket Price × Quantity)

Auto-update Tickets Sold

Auto-calculate Remaining Capacity

Prevent ticket sales when event capacity is exceeded

🔹 CSV Import (Data Import)

Import Event records using CSV files

Supported CSV fields:

Event Title

Description

Event Date

Location

Capacity

Ticket Price

Implemented using Frappe Data Import Tool

🔹 Reports

Event-wise total tickets sold

Event-wise revenue calculation

Implemented using Frappe Report Builder

🧪 How to Test the Application
▶️ Run the Application
bench start


Open in browser:

http://127.0.0.1:8001/app

▶️ Test Ticket Sales Logic

Create an Event with Capacity and Ticket Price

Create a Ticket Sale with a Quantity

Verify:

Tickets Sold increases

Remaining Capacity decreases

Total Price is calculated automatically

Try exceeding capacity → system blocks the sale

▶️ Test CSV Import

Go to Data Import

Select Event Detail

Download the CSV template

Upload the filled CSV file

Verify imported events in the Event list

▶️ Test Reports

Open Event Ticket Sales Report

Verify:

Total tickets sold per event

Revenue per event

📸 Screenshots Included (For Submission)
Event Creation
<img width="1288" height="666" alt="Event Creation" src="https://github.com/user-attachments/assets/0e5db7cd-5d30-4db5-8e0f-7c0aa879f6a4" />
Attendee List
<img width="1337" height="588" alt="Attendee List" src="https://github.com/user-attachments/assets/d6b99807-27ed-46e4-aeda-dc66a07cbc30" /> <img width="1304" height="672" alt="Attendee Detail" src="https://github.com/user-attachments/assets/78982d1e-471f-4fd3-8d26-2989d92f4c1c" />
Ticket Sale Entry
<img width="1288" height="669" alt="Ticket Sale" src="https://github.com/user-attachments/assets/622e52a6-f17e-4aca-b058-34473b17bc8d" />
CSV Import Success
<img width="1289" height="671" alt="CSV Import" src="https://github.com/user-attachments/assets/e642b8c6-8620-4d4e-8dc6-2afd4e98fa12" />
🧠 Key Learning Outcomes

DocType design and relationships in Frappe

Server-side business logic using Python

Capacity validation and automation

CSV data import handling

Report creation using Report Builder

🚀 Future Enhancements (Optional)

React frontend integration

User authentication and roles

Dashboard with charts

Email notifications

Online payment gateway integration

👤 Author

Narasimma Rathakrishnan
Event Management System using Frappe Framework
