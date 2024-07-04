# Inside API

## Table of Contents

- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/inside-api.git
    cd inside-api
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment**:

    - On Windows:

        ```bash
        .\.venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source .venv/bin/activate
        ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

## Running the Project

1. **Start the development server**:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/admin` to access the Django admin interface.

## API Endpoints

### Authentication

- **Registration**: `/auth/registration/`
- **Login**: `/auth/login/`

### Profile

- **Get Profile**: `/api/profiles/`
- **Update Profile**: `/api/profiles/{id}/`
- **Patch Profile**: `/api/profiles/{id}/`

### Suggestion

- **Create Suggestion**: `/api/suggestions/`
- **Get Suggestion**: `/api/suggestions/{id}/`
- **Save Suggestion**: `/api/suggestions/{id}/save/`
- **Get Saved Suggestions**: `/api/suggestions/saved/`

