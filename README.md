# news-website-2820 mini project
# NewsPortal - Django News Website

A professional news portal built with Django, featuring article management, categorization, and responsive design.

## Team Members
- Akshat Vijesh - Lead Developer (akshat24beit@student.mes.ac.in)
- Mohit Kharunkar - Testing and sample fixture (mohit24beit@student.mes.ac.in)
- Vedant Ingale - 

## Features
- ✅ Article management with images
- ✅ Category filtering
- ✅ Author tracking
- ✅ Sorting by date, title, and author
- ✅ Responsive design
- ✅ About page

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Akshatvijesh26/news-website-2820.git
cd news-website-2820/newsportal
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Create superuser for admin access
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Access the application
- **Website:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Admin Credentials
- **Username:** admin
- **Password:** [your admin password]

## Important: Loading Sample Articles
**To view the website with our pre-published articles, run:**
```bash
git pull origin main
```
This ensures you have the latest database with all sample articles and images we've created for demonstration.

## Technologies Used
- Django 5.2
- Python 3.12
- Bootstrap 5
- SQLite3

## Project Structure
```
newsportal/
├── myapp/              # Main application
├── newsportal/         # Project settings
├── media/              # Uploaded images
├── db.sqlite3          # Database
└── manage.py           # Django management
```
##Website Appearance

<img width="1891" height="1015" alt="image" src="https://github.com/user-attachments/assets/037c90ed-1726-445c-8183-96d5acd180d7" />

<img width="1242" height="949" alt="image" src="https://github.com/user-attachments/assets/d2c90d4f-49e5-423f-9ce4-f5edbb6b59ad" />

## The features
✅ Article management
✅ Category filtering
✅ Image uploads
✅ Sorting functionality
✅ Author attribution
✅ Responsive navbar
✅ About page with team info

# What Makes This Project Strong:
Full-stack - Backend + Frontend + Database
CRUD operations - Create, Read via admin
Relationships - Foreign keys (Category, Author)
File handling - Media uploads
Clean code - Well-structured
Professional design - Not just functional, looks good
GitHub ready - Professor can clone and run

## Administrative operations
We used admin.py module to have a user authenticated and safe website operation that 
-can add articles
-can add categories
-add images, authors, date(automated)

  <img width="599" height="442" alt="image" src="https://github.com/user-attachments/assets/02952119-bd26-4656-8bba-2d7ac55316d3" />  

  <img width="1898" height="966" alt="image" src="https://github.com/user-attachments/assets/18c0ee05-5b79-4f11-bbaf-283c07db730b" />
          
  <img width="1907" height="973" alt="image" src="https://github.com/user-attachments/assets/c9c42fb9-5fd3-4f25-8619-2885d58463ab" />
    This window is used to create and save articles, here we have the options to add category,image,author and set date automatically
    
## Challenges we faced
-Design Challenges

Visual Balance – The site looked too flashy at first, so we switched to a minimal flat layout with red accents.

Information Hierarchy – Article cards were cluttered; we added color-coded metadata, badges, and better spacing.

Image Handling – Some posts had missing images; we used fixed-height containers, red placeholders, and object-fit.

Responsive Design – Made layouts work across devices with Bootstrap grid and media queries.

Performance – Fixed N+1 query issue using select_related() for faster database queries.

## Major issue we faced
-When we tried to add a base template using the extends feature, it caused multiple file errors and conflicts in our project structure. We faced issues with linking CSS, paths, and block inheritance, which made several pages break. Since fixing everything would’ve taken too long and caused more confusion, we decided to start over and use single templates instead. This helped us keep the project stable and ensured all pages worked properly.

## comments by team members on their contribution
# Akshat Vijesh ITA320
-I learned how web applications are developed from start to finish. I understood how the frontend and backend connect and how everything integrates together. We used HTML and Bootstrap for the layout and design, Python Django for backend logic, and SQLite for handling the database. I also worked with Pillow for image processing and learned how to manage routes, templates, and static files. Overall, I got a clear idea of how to integrate different technologies to build a complete web application. I also learned how its not necessary to download any additional packs for applying cosmetics to the UI. simply linking the files work. same case for hosting images , we can link via google apis in html code for this. i think ive gained substantial footing on web development and github operations by working on this mini project.
# Mohit Kharunkar
-I worked on testing and creating sample fixtures. My main goal was to make sure all parts of the website — articles, categories, authors, and images — worked properly.I tested every page using django tools to checkCRUD functions, links, and forms were running smoothly .I also created sample data for different categories like politic, Sports, and infotianment etc to make the website look real and easy to test .I also manage news-related information directly through the Django admin panel, which helped in testing data entry and verifying that content updates appeared correctly on the website.Through this project, I understood how Django connects the backend and frontend to manage data effectively. I learned to use the admin panel with a superuser key to add news content and saw how testing ensures smooth website performance.
