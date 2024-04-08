
# Expense Tracker | Rumi press 

Welcome to the Rumi Expense Tracker project. This project was executed with the objective of automating the business processes at Rumi Press, one of the largest book distribution houses in the EdTech industry. Previously, the team at Rumi Press had been utilizing spreadsheets to track their book distribution process. Recognizing the need for a more efficient and secure system, we implemented a Django based web-application tailored to their needs.

The project had several objectives, including tracking book distribution expenses, increasing data security and availability, and customizing and automating business processes. To accomplish these objectives, the following tasks were executed:

- Development of a CRUD* view to manage book categories such as Business Analytics, Python, Data Science, and Math.
- Development of a CRUD* view to add book information such as the title, author, publishing date, book category, and distribution expenses.
- Importation of existing data from spreadsheets to the web app.
- Development of a report view that enables the team to view the distribution expenses of books according to their categories.
- CRUD: Create, Read, Update, Delete

This project is a testament to the application of efficient web development practices to create practical solutions for businesses. The details of the project, including the technology used, features, access management, and user interface, are documented in the following sections.


## Technology Stack

* **Frontend:**
    * HTML
    * CSS
    * JavaScript (JS)
    * Bootstrap 5 (for responsive design and UI components)
    * Font Awesome icons (for visual appeal and interactivity)
    * Chart.js (for data visualization)
* **Backend:**
    * Python
    * Django (high-level web framework for efficient development)

## Key Features

* **Dashboard:**

    * Provides a centralized view of key metrics and insights.
    * Includes charts for expense visualization, expense summary, and average expense.
    * Displays a list of book categories with corresponding numbers of books, total, and average expenses.
* **Book Management:**
    * **View Book List:** Manage extensive book databases efficiently with pagination.
    * **Filter Books:** Narrow down book searches by ID, Author, Publisher, or other relevant criteria.
    * **CRUD Operations:**
        * **Create/Add Books:** Manually add new books or import data from existing Excel files.
        * **Edit Books:** Update book information as needed.
        * **Delete Books:** Remove books from the system while maintaining data integrity.
    * **Book Categories:** Create and manage custom book categories for better organization.

* **User Management:**

    * **View User List:** Administer user accounts effectively with a comprehensive user list.
    * **CRUD Users:**
        * Create new user accounts with appropriate permissions.
        * Edit user details for profile management.
        * Delete user accounts when necessary.
    * **Modal for Admins:** Dedicated user management interface for administrators.

## Access Management
* **Authentication**
   * **Single-Factor Authentication(SFA):** Secure login using username and password combinations.
   * **Account Reset:** Enables users to reset forgotten passwords. Reset credentials are delivered via email for secure recovery.
* **Authorization**
    * **User Groups:** Defines user roles and permissions.
    * **User Group: User:** Read-only access to all data models (cannot modify data).
    * **User Group: Admin:** Full CRUD privileges on all data models (can create, read, update, and delete data).

## User Interface (UI)

* **Modern Design:** Utilizes Bootstrap 5 for a clean, responsive, and mobile-friendly UI that adapts to different screen sizes.
* **Interactive Icons:** Font Awesome icons enhance user experience with intuitive visual cues.






---

This project exemplifies the power of effective web development practices in creating practical solutions for real-world business challenges. It demonstrates how well-chosen technologies and well-defined processes can lead to increased efficiency, improved data management, and ultimately, a competitive advantage.


**Note:** This project was completed as part of a Coursera project.

