# UjuziPortfoliyo project

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Related Projects](#related-projects)
- [Contributing](#contributing)
- [License](#licensing)

## Introduction
This is a web application that allows users to create a professional portfolio with a profile page, blog page, project page, and more. Users can manage their portfolios through a user dashboard and share their portfolio links with others. The application is built with Django and provides a seamless experience for both users and visitors.

[Deployed Site](https://your-deployed-site-link.com) | [Final Project Blog Article](https://your-blog-link.com) | [Author's LinkedIn](https://www.linkedin.com/in/your-linkedin-profile/)

## Features
- User Registration and Authentication
- User Dashboard for managing profile, blogs, projects, skills, and technologies
- Add, Edit, Delete, and View Blogs and Projects
- Profile management with profile photo, bio, and social links
- Skill and Technology management
- Contact form for visitors to send messages
- Email notifications for registration and contact form
- Responsive and user-friendly UI
- Dynamic forms with Django Crispy Forms
- Secure environment variable management

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Database**: PostgreSQL
- **Storage**: -
- **Email**: SMTP configuration for email notifications
- **Deployment**: -
- **Containers**: - Docker

## Installation
1. Clone the repository

   ```bash
   git clone https://github.com/sarahwonago/UjuziPortfoliyo
   cd ujuziportfoliyoproject
2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies

   ```bash
    pip install -r requirements.txt

4. Set up the database

   ```bash
    python manage.py migrate
   
5. Create the superuser and run the development server

   ```bash
    python manage.py createsuperuser
    python manage.py runserver

   
### Prerequisites
- Python 3.x
- Django 5.x
- PostgreSQL or SQLite
- Docker
- SMTP server for email notifications

## Usage

- Open your browser and go to http://127.0.0.1:8000/.
- Register a new user account or log in if you already have one.
- Explore the dashboard to add and manage your blogs, projects, skills, and technologies.
- Share your portfolio link with others.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

### Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request
  
## Related Projects
Here are a few related projects you might find interesting:

  -DevShowcase

## Licensing
Distributed under the MIT License. See LICENSE for more information.


