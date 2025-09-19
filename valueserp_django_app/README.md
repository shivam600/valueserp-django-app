# 🔍 ValueSERP Django App (Sample)

This is a minimal Django app that integrates with the **[ValueSERP API](https://app.valueserp.com/)**, allowing multiple queries and exporting search results as CSV.

---

## ✨ Features
- Accepts up to 5 queries and a ValueSERP API key.
- Calls the ValueSERP API for each query and parses search results.
- Displays results in a table.
- Allows CSV download (stored in session).

---

## ⚙️ Setup (Local)

### 1. Clone the Repository
```bash
git clone https://github.com/shivam600/valueserp-django-app.git
cd valueserp-django-app


### 2. Create a Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows
pip install -r requirements.txt




### 3. Set Environment Variables

DJANGO_SECRET_KEY (optional, for local development you can skip or use a placeholder)

You can also create a .env file in the project root:

DJANGO_SECRET_KEY=your-secret-key



###6. Open in Browser

Go to: http://127.0.0.1:8000/

Enter your ValueSERP API key and queries, then click Search.