📖 Project Overview

This project is a Frappe-based Event Management Web Application developed as part of a Developer Hiring Test.

The application helps event planners to:

Create and manage events

Register attendees

Sell tickets

Track capacity and revenue

Import events using CSV files

Generate basic reports

The system is designed for single-role usage (Event Planner) and focuses on core business logic, not complex permissions.

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

Stores attendee information.

Fields:

Attendee Name

Email

Phone

Event (Link to Event Detail)

3️⃣ Ticket Sale

Handles ticket selling for events.

Fields:

Event (Link to Event Detail)

Attendee

Quantity

Total Price

✅ Features Implemented
🔹 Base Event System (CRUD)

Create, Read, Update, Delete events

Create, Read, Update, Delete attendees

Create, Read, Update, Delete ticket sales

🔹 Event Management

Create events with required fields

Update and delete events

Search and filter events by:

Event Title

Event Date

🔹 Attendee Management

Register attendees for events

Update attendee details

Link attendees to events

🔹 Ticket Sales

Auto-calculate Total Price (Ticket Price × Quantity)

Auto-update Tickets Sold

Auto-calculate Remaining Capacity

Prevent ticket sales when event capacity is exceeded

🔹 CSV Import (Data Import)

Import Event records using CSV

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

Built using Frappe Report Builder

🧪 How to Test the Application
▶️ Run the Application
bench start


Open in browser:

http://127.0.0.1:8001/app

▶️ Test Ticket Sales Logic

Create an Event with Capacity and Ticket Price

Create a Ticket Sale with Quantity

Verify:

Tickets Sold increases

Remaining Capacity decreases

Total Price is calculated

Try exceeding capacity → system blocks the sale

▶️ Test CSV Import

Go to Data Import

Select Event Detail

Download template

Upload CSV

Verify imported events in Event list

▶️ Test Reports

Open Event Ticket Sales Report

Verify:

Total tickets sold per event

Revenue per event

📸 Screenshots Included (For Submission)

Event creation:
<img width="1288" height="666" alt="Screenshot 2026-01-20 102747" src="https://github.com/user-attachments/assets/0e5db7cd-5d30-4db5-8e0f-7c0aa879f6a4" />


Attendee list

Ticket sale entry

Ticket capacity validation

CSV import success

Report output

🧠 Key Learning Outcomes

DocType design and relationships in Frappe

Server-side business logic using Python

Capacity validation and automation

CSV data import handling

Report creation using Report Builder

🚀 Future Enhancements (Optional)

React frontend integration

User authentication & roles

Dashboard with charts

Email notifications

Online payment gateway integration

👤 Author

Narasimma Rathakrishnan
Event Management System using Frappe Framework

