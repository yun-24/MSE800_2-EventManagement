# **Event Application**

This project is a Django-based web application designed to manage and participate in events. 
Users can sign up, log in, create events, and view a list of upcoming events.

## **Features**

- User authentication (sign up, log in, log out)
- Event creation, listing, and detail view

## **Technologies Used**

- **Backend**: Django, SQLite
- **Frontend**: HTML, CSS

## **Installation**

### **Prerequisites**

- Python 3.x
- Django

### **Steps**

1. **Clone the repository**:

    ```shell
    git clone <repository_url>
    cd event_management
    ```

2. **Install dependencies**:

    ```shell
    pip install -r requirements.txt
    ```

3. **Apply migrations**:

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

4**Run the development server**:

    ```shell
    python manage.py runserver
    ```

5**Access the application**:

   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## **Usage**

- **Sign Up**: Create a new account to access the application.
- **Log In**: Log in with your credentials to create and manage events.
- **Create Event**: Navigate to `/events/new/` to create a new event.
- **View Events**: Visit the homepage to view the list of upcoming

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
