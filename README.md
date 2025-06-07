
---

# 2️⃣ Detailed Project Report

### Suggested Sections and Content

---

### Title: Development of an E-commerce Sales Chatbot

**1. Introduction**

The goal was to develop a chatbot that helps users navigate and shop on an e-commerce platform. The chatbot supports product search and discovery with a conversational UI, integrated with a backend server and a product inventory database.

---

**2. Technology Stack**

- **Backend:** Flask (Python microframework), Flask-MySQLdb to connect to MySQL
- **Frontend:** ReactJS with components for chat UI and login
- **Database:** MySQL Workbench storing 100 mock product entries with fields like name, description, price, category, and image URL
- **Tools:** VS Code, PowerShell terminal, npm for frontend package management

---

**3. Architecture**

- **Frontend** handles user interactions, login, and chat interface.
- **Backend API** processes user queries, fetches relevant product data, and manages sessions.
- **Database** stores users and product details.
- Communication uses REST APIs secured by session-based authentication.

---

**4. Implementation Details**

- Backend built with Flask and modular blueprints for auth and products.
- Passwords hashed with bcrypt.
- Products queried by name using SQL LIKE operator.
- Frontend React uses Axios for API calls and maintains login state.
- Chatbot UI accepts search queries and displays product cards with images and prices.
- Responsive design suitable for desktop and mobile devices.

---

**5. Sample Queries and Results**

- Query: `"Product 15"`
- Result: Displays the product card with name, description, price, category, and image.

- Query: `"Electronics"`
- Result: List of products filtered by the category containing "Electronics".

---

**6. Challenges Faced**

- Managing session continuity between React frontend and Flask backend.
- Handling CORS and secure cookie sharing.
- Populating database with meaningful yet mock product data.
- Building an intuitive chat UI without complex NLP.

---

**7. Learnings**

- Integration of Flask with React and MySQL for a full-stack application.
- Handling authentication and session management in Flask with React.
- Designing simple yet user-friendly chatbots for e-commerce.
- Writing clean, modular code for scalability and maintenance.

---

**8. Future Enhancements**

- Adding natural language understanding for better query parsing.
- Shopping cart and checkout integration.
- Persistent chat history storage and analytics.
- User registration and password recovery flows.

---

# 3️⃣ Presentation Outline (Example slide content)

---

### Slide 1: Title Slide  
**Development of an E-commerce Sales Chatbot**  
Shubh Kumar  
Date: [Insert Date]

---

### Slide 2: Project Overview  
- Objective: Build a chatbot for e-commerce product search and purchase assistance  
- Key features: Login, search, session continuity, product display

---

### Slide 3: Technology Stack  
- Backend: Flask, MySQL  
- Frontend: ReactJS  
- Database: MySQL Workbench  
- Tools: VS Code, PowerShell

---

### Slide 4: Architecture Diagram  
(Sketch or diagram showing React frontend, Flask backend, MySQL DB, API interaction)

---

### Slide 5: Implementation Details  
- REST API design and endpoints  
- User authentication flow  
- Product search and display UI components

---

### Slide 6: Challenges & Solutions  
- Session management between frontend & backend  
- Data seeding of 100 products  
- CORS & security handling

---

### Slide 7: Demo & Sample Queries  
- Demonstrate login  
- Search “Product 10”, “Electronics”  
- Show product cards & info

---

### Slide 8: Learnings & Future Work  
- Full-stack integration experience  
- Clean modular codebase  
- Plan: NLP chatbot, checkout features

---

### Slide 9: Thank You  
- Questions?

---

# Summary

| Deliverable                  | What to Include                                              |
|-----------------------------|--------------------------------------------------------------|
| **GitHub Repo**              | Full source code, README.md with setup and summary           |
| **Project Report (Word/PDF)**| Detailed tech stack, architecture, challenges, sample queries |
| **Presentation (PPT/PDF)**    | Slides per outline above including diagrams and demo points   |

---
