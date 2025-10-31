# NewsPortal - Django News Website

A professional news portal built with Django, featuring article management, categorization, and responsive design. This project demonstrates full-stack web development with modern design principles and robust backend functionality.

![Website Preview](https://github.com/user-attachments/assets/037c90ed-1726-445c-8183-96d5acd180d7)

## 🎯 Features

- **Article Management** - Complete CRUD operations through Django admin
- **Category Filtering** - Organize news by Politics, Sports, Entertainment, and more
- **Author Tracking** - Attribution and author-based article organization
- **Image Uploads** - Media handling with Pillow integration
- **Sorting Functionality** - Sort articles by date, title, and author
- **Responsive Design** - Mobile-friendly interface built with Bootstrap 5
- **Admin Dashboard** - Secure administrative interface for content management
- **About Page** - Team information and project details

## 👥 Team Members

- **Akshat Vijesh** - Lead Developer (akshat24beit@student.mes.ac.in)
- **Mohit Kharunkar** - Testing & Sample Fixtures (mohit24beit@student.mes.ac.in)
- **Vedant Ingale** - Documentation & Deployment (vedant24beit@student.mes.ac.in)

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Akshatvijesh26/news-website-2820.git
cd news-website-2820/newsportal
```

2. **Create and activate virtual environment**
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create superuser for admin access**
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

5. **Load sample data (recommended)**
```bash
git pull origin main
```
This ensures you have the latest database with pre-published articles and images.

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the application**
- **Main Website:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## 🛠️ Technologies Used

- **Backend:** Django 5.2
- **Language:** Python 3.12
- **Frontend:** HTML5, Bootstrap 5
- **Database:** SQLite3
- **Image Processing:** Pillow

## 📁 Project Structure

```
newsportal/
├── myapp/              # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View logic
│   ├── urls.py         # URL routing
│   └── admin.py        # Admin configuration
├── newsportal/         # Project settings
│   ├── settings.py     # Configuration
│   └── urls.py         # Root URL config
├── media/              # Uploaded images
├── static/             # CSS, JS files
├── templates/          # HTML templates
├── db.sqlite3          # SQLite database
├── manage.py           # Django management
└── requirements.txt    # Python dependencies
```

## 📸 Screenshots

### Homepage
![Homepage](https://github.com/user-attachments/assets/037c90ed-1726-445c-8183-96d5acd180d7)

### Article View
![Article View](https://github.com/user-attachments/assets/d2c90d4f-49e5-423f-9ce4-f5edbb6b59ad)

### Admin Panel
![Admin Panel](https://github.com/user-attachments/assets/02952119-bd26-4656-8bba-2d7ac55316d3)

### Article Management
![Article Management](https://github.com/user-attachments/assets/18c0ee05-5b79-4f11-bbaf-283c07db730b)

### Creating Articles
![Creating Articles](https://github.com/user-attachments/assets/c9c42fb9-5fd3-4f25-8619-2885d58463ab)

## 💼 Admin Operations

The admin panel provides secure, authenticated access to:
- Add and manage articles
- Create and organize categories
- Upload and manage images
- Add author information
- Automatic date tracking

Access the admin panel at `/admin/` with your superuser credentials.

## 🎨 Design Decisions

- **Minimal Flat Layout:** Clean design with red accent colors for professional appearance
- **Color-Coded Metadata:** Easy identification of article information with badges
- **Fixed-Height Containers:** Consistent image display with object-fit properties
- **Responsive Grid:** Bootstrap-based layout adapts to all screen sizes
- **Optimized Queries:** Used `select_related()` to prevent N+1 query issues

## 🧪 Testing

The project includes comprehensive testing for:
- CRUD operations on all models
- Category filtering and sorting functionality
- Image upload and display
- Form validation
- Admin panel operations
- Responsive design across devices

## 🚧 Challenges & Solutions

### Design Balance
**Challenge:** Initial design was too flashy  
**Solution:** Switched to minimal flat layout with strategic red accents

### Information Hierarchy
**Challenge:** Cluttered article cards  
**Solution:** Implemented color-coded metadata, badges, and improved spacing

### Image Handling
**Challenge:** Missing images broke layout  
**Solution:** Added fixed-height containers with red placeholders and object-fit CSS

### Template Issues
**Challenge:** Base template inheritance caused file conflicts  
**Solution:** Opted for single templates to maintain stability

### Performance
**Challenge:** Slow database queries  
**Solution:** Implemented `select_related()` for optimized foreign key queries

## 📚 What We Learned

This project provided hands-on experience with:
- Full-stack web development (frontend + backend + database)
- Django framework and MTV architecture
- Database relationships and foreign keys
- File handling and media uploads
- Version control with Git and GitHub
- Team collaboration and project management
- Testing and quality assurance
- Deployment and documentation

This is an academic project, but suggestions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📧 Contact

For questions or feedback, reach out to any team member:
- Akshat Vijesh: akshat24beit@student.mes.ac.in
- Mohit Kharunkar: mohit24beit@student.mes.ac.in
- Vedant Ingale: vedant24beit@student.mes.ac.in

---

**Course:** ITA320  
**Institution:** MES College  
**Year:** 2024
