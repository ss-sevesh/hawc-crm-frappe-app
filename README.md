# HAWC CRM

A complete CRM application built as a custom Frappe app. Designed to handle Leads, Deals, and Activity Logs with custom REST APIs, Role-based permissions, and Workspace dashboards.

## Features
- **Lead Management**: Track potential customers with statuses and sources.
- **Deal Pipeline**: Convert qualified leads to deals, track values and stages.
- **Activity Logging**: Log calls, emails, and meetings.
- **Automations**: Auto-create deals when leads are qualified, notify managers when deals are won.
- **Custom REST APIs**: 5 custom endpoints for integration.
- **Role-based Access**: CRM Admin, CRM Manager, and CRM Sales Rep roles.

## Tech Stack
- **Framework**: Frappe (version-15)
- **Language**: Python 3.11+, JavaScript
- **Database**: MariaDB 10.6+
- **Cache**: Redis 7+

## Installation (Docker)

This app is fully Dockerized for easy setup. You do not need to install Frappe natively.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ss-sevesh/hawc-crm-frappe-app.git
   cd hawc-crm-frappe-app
   ```

2. **Start the environment**:
   ```bash
   docker compose up -d
   ```
   *This will spin up MariaDB, Redis, and a Frappe container. It will automatically initialize a new bench, install the app, and start the development server.*

3. **Access the CRM**:
   Wait a few minutes for the setup script to finish, then go to:
   **http://localhost:8000**
   
   **Default Login:**
   - **Username:** Administrator
   - **Password:** admin

## Role Setup Guide

1. Log into your Frappe Desk as Administrator.
2. Go to **Role List**. You will see three new roles: `CRM Admin`, `CRM Manager`, `CRM Sales Rep`.
3. Go to **User List** and assign these roles to the appropriate users.
   - Sales Reps will only see Leads/Deals assigned to them.
   - Managers have full read/write access.
   - Admins have full system access.



## Video Demo
A demonstration video of this application in action will be uploaded to the `demo_video/` directory.

## License
MIT
