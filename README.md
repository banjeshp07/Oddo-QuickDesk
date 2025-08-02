# 📮 QuickDesk - Simple Helpdesk System for Odoo

QuickDesk is a custom helpdesk module built for the **Odoo x CGC Hackathon 2025**.  
It allows users to raise support tickets, assign them to agents, and track their status through resolution.

---

## 🎯 What QuickDesk Does

- Users can create tickets with a subject, description, and category
- Each ticket is assigned to a support agent
- Agents can update ticket status: Open → In Progress → Resolved → Closed
- Clean form and list views for managing tickets
- Access rights applied: normal users, support agents, and admins

---

## 🛠️ Tech Used

- **Odoo 16**
- **Python**
- **XML (for views)**
- **PostgreSQL (backend database)**

---

## 📸 Features in Action

- Go to *QuickDesk → Tickets*
- Click **Create** to log a new issue
- Choose agent, write description, set status
- View all tickets in a list
- Each user sees only their own tickets (based on rights)

---

## 🔧 How to Install (Dev Mode)

```bash
# Clone the repo into your custom_addons directory
git clone https://github.com/banjeshp07/Oddo-QuickDesk.git

# Start Odoo server
python odoo-bin -c odoo.conf

# Open browser → http://localhost:8069
# Enable Developer Mode → Update App List
# Search "QuickDesk" → Install
