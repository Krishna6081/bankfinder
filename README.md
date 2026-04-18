# Bank Branch Contact Finder

A Django web application for searching bank branch contact numbers and managing branch records (staff only). It includes AJAX live search, CSV/Excel import, Excel export, copy-to-clipboard, flash notifications, optional dark mode, and a Bootstrap 5 responsive UI.

## Stack

- Python 3.11+ (recommended)
- Django 5.x
- SQLite (default)
- Bootstrap 5 (CDN), vanilla JavaScript
- openpyxl (Excel import/export)

## Step-by-step setup

### 1. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
cd d:\OneDrive\Desktop\Numbers
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
cd /path/to/Numbers
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply database migrations

```bash
python manage.py migrate
```

### 4. Create a staff user (for dashboard access)

Only users with **Staff status** can add, edit, delete, import, or export branches. Logged-in users who are **not** staff receive HTTP **403** on those URLs (by design).

```bash
python manage.py createsuperuser
```

When prompted, choose a username and password. In the Django shell you can set `is_staff` if needed:

```bash
python manage.py shell
```

```python
from django.contrib.auth import get_user_model
User = get_user_model()
u = User.objects.get(username="your_username")
u.is_staff = True
u.is_superuser = True  # optional; allows /admin/ too
u.save()
```

Alternatively, use **Django admin** at `/admin/` after `createsuperuser` (superusers are staff by default).

### 5. Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the public search page.

- **Staff login:** [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)
- **Dashboard:** [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/) (requires staff login)
- **Django admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### 6. Try the workflow

1. Log in as staff and open **Dashboard** → **Add branch** (e.g. name `Pune Branch`, contact number, optional address).
2. Open the **home** page, type `Pune` — suggestions appear; click a row — the contact number loads with **Copy number**.
3. Use **Import** with a CSV or `.xlsx` file (headers: `branch_name`, `contact_number`, optional `address`).
4. Use **Export Excel** from the dashboard to download all rows.

## Import file format

**CSV or Excel** first row (headers), case-insensitive, spaces allowed (e.g. `Branch Name` maps to `branch_name`):

| branch_name   | contact_number | address (optional) |
|---------------|----------------|------------------|
| Pune Branch   | +91-20-1111111 | MG Road          |

## Production notes

- Set `DEBUG = False`, configure `ALLOWED_HOSTS`, and use a strong `SECRET_KEY` (environment variable).
- Serve static files with your web server or `collectstatic`.
- Use HTTPS and a production database if deploying beyond local use.

## Project layout

- `bankfinder/` — Django project settings and root URLs
- `branches/` — App: models, views, forms, URLs
- `templates/` — `base.html`, `branches/*.html`, `registration/login.html`
- `static/branches/` — CSS and JavaScript
