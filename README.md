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

## Installation

Run these commands in order from your Frappe bench directory (`~/frappe-bench`):

1. **Get the app**:
   Since this is a custom repo, clone it into your apps directory:
   ```bash
   cd ~/frappe-bench/apps
   git clone https://github.com/ss-sevesh/hawc-crm-frappe-app.git hawc_crm
   ```

2. **Install the app**:
   ```bash
   cd ~/frappe-bench
   bench --site hawc.localhost install-app hawc_crm
   ```

3. **Migrate the database**:
   ```bash
   bench migrate
   ```

4. **Clear cache and restart**:
   ```bash
   bench --site hawc.localhost clear-cache
   bench restart
   ```

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
