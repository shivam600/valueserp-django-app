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
python -m venv venv
# Activate the virtual environment
# On Mac/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
pip install -r requirements.txt


### 3. Set Environment Variables

Create a .env file in the project root and add:

DJANGO_SECRET_KEY=your-secret-key

Note: For local development, you can use any placeholder secret key.


### 4. Apply Migrations
python manage.py migrate


### 5. Run the Development Server
python manage.py runserver

###  6. Open in Browser

Go to: http://127.0.0.1:8000/

Enter your ValueSERP API key and queries.

Click Search to see results.


📥 Using the CSV Download Feature

After performing a search, results are displayed in a table.

Click the "Download CSV" button.

A CSV file containing all search results will be downloaded to your local machine.
