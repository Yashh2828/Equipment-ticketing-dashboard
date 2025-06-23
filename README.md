# UPMRC-equipment-ticketing-dashboard
# 🛠️ Equipment Fault Ticketing System (Flask + MongoDB)

This is a web-based Ticket/Problem Raising System designed for internal use by employees in an organization. The system supports login/signup, role-based dashboards, equipment issue tracking, and ticket lifecycle management.

##  Features

###  Authentication
- Login and Signup system
- Role-based access control:
  - **End User**: Raises tickets
  
###  Dashboards
- **End User Dashboard**: 
  - View own profil
  - Add assigned equipment
  - Raise new issue tickets
  - Track ticket status (Open, In-Progress, Closed, Verified)

### 🎫 Ticket System
- Raise issues with assigned equipment
- Admins can accept/resolve tickets
- End Users verify if the ticket is actually resolved
- Equipment tracking by serial/model number

### 🧩 Technology Stack
- **Backend**: Python (Flask), PyMongo
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: MongoDB
- **Templating**: Jinja2 (Flask templates)



