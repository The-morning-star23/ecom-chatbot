# E-commerce Sales Chatbot

## Project Summary

This project implements an interactive sales chatbot designed to enhance the user shopping experience on an e-commerce platform. It enables customers to perform product searches, explore product details, and facilitates the purchase journey via a conversational interface.

The solution consists of a responsive React.js frontend that communicates with a Flask-based RESTful backend API. The backend handles user authentication, processes product search queries, and interacts with a MySQL database containing a mock inventory of 100 diverse products across categories such as electronics, books, and textiles.

The chatbot interface is intuitive and responsive, supporting desktop, tablet, and mobile devices. It features session management to maintain user state, a conversation reset option, and persistent chat history for later retrieval and analysis.

The backend system ensures secure user login with hashed passwords and session tokens, fault-tolerant API handling, and efficient SQL querying for product data retrieval.

This project demonstrates the integration of modern frontend and backend technologies to deliver a modular, maintainable, and scalable e-commerce chatbot solution.

---

## Technology Stack

- **Frontend:** React.js, HTML5, CSS3  
- **Backend:** Python, Flask  
- **Database:** MySQL (via MySQL Workbench)  
- **Authentication:** Flask sessions, bcrypt for password hashing  
- **Tools:** VS Code, PowerShell, npm, pip

---

## Features

- Responsive chatbot UI compatible with multiple devices  
- Secure user authentication and session management  
- Product search and filtering by name and category  
- Display of product cards with images, prices, and details  
- Conversation reset functionality  
- Persistent chat session tracking  

---

## Project Structure

ecommerce-chatbot/
│
├── backend/
│ ├── app.py
│ ├── models.py
│ ├── database.py
│ ├── requirements.txt
│ ├── config.py
│ └── data/
│ └── populate_db.sql
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ ├── App.js
│ │ ├── index.js
│ │ ├── api.js
│ │ └── styles.css
│ ├── package.json
│
│
└── README.md

---

## Setup and Installation

### Backend Setup

1. Navigate to the backend directory:

cd backend
Create and activate a Python virtual environment:
python -m venv venv
.\venv\Scripts\activate    # Windows PowerShell
source venv/bin/activate   # macOS/Linux
Install required Python packages:
    pip install -r requirements.txt
Configure your MySQL database and update credentials in config.py.


Populate the MySQL database with mock data:
    mysql -u your_username -p your_database_name < data/populate_db.sql

Run the Flask backend server:
    python app.py


### Brontend Setup

2. Navigate to the frontend directory:

cd frontend
Install npm dependencies:
    npm install
Start the React development server:
    npm start
Open your browser and go to http://localhost:3000




Sample Queries
Search by product name:
"Product 10"
Displays product matching "Product 10".

Search by category:
"Electronics"
Lists all products categorized under electronics.

Keyword search:
"Book"
Finds products with “Book” in their name or category.

Results and Demonstration
The chatbot interface presents matched products as responsive cards, each showing:

Product image

Name

Price

Category

User sessions maintain the chat state, allowing seamless multi-query interactions. Users can reset conversations at any time using the reset button.

Future Improvements
Integrate Natural Language Processing (NLP) for enhanced query understanding

Add shopping cart and checkout functionalities

Implement JWT-based authentication for improved security

Extend chatbot capabilities to handle voice commands

Contact and Support
For questions or contributions, please reach out via the GitHub repository or email.

