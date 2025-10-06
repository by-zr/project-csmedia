# CSMedia - Social Media Platform

CSMedia is a Django-based social media platform that allows users to create profiles, share posts, interact with friends, and build social connections. The application features user authentication, friend management, post creation with images, commenting, and liking functionality.

> **Note**: This is a learning project built to explore Django web development, social media concepts, and modern web technologies. It serves as a foundation for understanding full-stack development principles and social platform architecture.

## 🚀 Features

### Core Functionality
- **User Authentication**: Django Allauth integration for secure user registration and login
- **User Profiles**: Customizable user profiles with avatars, bio, and personal information
- **Social Posts**: Create and share text posts with optional image uploads
- **Friend System**: Send, receive, and manage friend requests
- **Interactions**: Like posts and add comments
- **User Discovery**: Find and connect with other users

### Technical Features
- **Django 4.1.7**: Modern web framework with robust features
- **SQLite Database**: Lightweight database for development and testing
- **Image Upload**: Support for PNG, JPG, and JPEG image formats
- **Responsive UI**: Semantic UI framework for modern, responsive design
- **Static File Management**: Organized static and media file handling

## 🔮 Future Implementations

### Planned Features
- **Real-time Messaging**: WebSocket integration for instant messaging between users
- **Advanced Search**: Full-text search with filtering and sorting capabilities
- **Content Moderation**: Automated and manual content review system
- **Push Notifications**: Email and browser notifications for user interactions
- **Mobile App**: React Native or Flutter mobile application
- **API Development**: RESTful API for third-party integrations
- **Analytics Dashboard**: User engagement and platform usage statistics

### Technical Enhancements
- **Database Migration**: PostgreSQL or MySQL for production scalability
- **Caching Layer**: Redis integration for improved performance
- **CDN Integration**: Cloud storage for media files and static assets
- **Docker Deployment**: Containerized application for easy deployment
- **CI/CD Pipeline**: Automated testing and deployment workflows
- **Security Enhancements**: Rate limiting, CSRF protection, and security headers
- **Testing Suite**: Comprehensive unit and integration tests
- **Documentation**: API documentation and developer guides

### Advanced Features
- **AI Integration**: Content recommendation and sentiment analysis
- **Video Support**: Video upload and streaming capabilities
- **Live Streaming**: Real-time video broadcasting
- **Story Feature**: Temporary content sharing (24-hour stories)
- **Group Management**: Create and manage user groups and communities
- **Event System**: Create and manage social events
- **Marketplace**: Buy and sell items within the platform
- **Gamification**: Points, badges, and achievement systems

## 📁 Project Structure

```
CSMedia/
├── Src/                          # Main source code
│   ├── CSMedia/                  # Main Django project
│   │   ├── settings.py           # Django configuration
│   │   ├── urls.py              # Main URL routing
│   │   └── views.py             # Home page view
│   ├── CSMediaPosts/            # Posts application
│   │   ├── models.py            # Post, Comment, Like models
│   │   ├── views.py             # Post-related views
│   │   ├── forms.py             # Post and comment forms
│   │   └── templates/           # Post templates
│   ├── CSMediaProfiles/         # User profiles application
│   │   ├── models.py            # Profile and relationship models
│   │   ├── views.py             # Profile management views
│   │   ├── forms.py             # Profile forms
│   │   └── templates/           # Profile templates
│   ├── CSMediaTemplates/        # Base templates
│   │   ├── base.html            # Main template
│   │   └── Main/                # Home page templates
│   ├── CSMediaStatic/           # Static files
│   │   ├── style.css            # Custom styles
│   │   └── main.js              # JavaScript functionality
│   ├── manage.py                # Django management script
│   └── db.sqlite3               # SQLite database
├── Static_CDN/                  # Static and media files
│   ├── Static_Root/             # Collected static files
│   └── Media_Root/              # User uploaded media
├── Lib/                         # Python virtual environment
└── Scripts/                     # Virtual environment scripts
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.11.2 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd CSMedia
   ```

2. **Activate the virtual environment**
   ```bash
   # On Windows
   Scripts\activate
   
   # On macOS/Linux
   source Scripts/activate
   ```

3. **Install dependencies** (if not already installed)
   ```bash
   pip install django==4.1.7
   pip install django-allauth
   pip install Pillow
   ```

4. **Navigate to the source directory**
   ```bash
   cd Src
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## 🎯 Usage

### Getting Started
1. **Home Page**: Visit the main page to see navigation options
2. **User Registration**: Create a new account or login with existing credentials
3. **Profile Setup**: Customize your profile with personal information and avatar
4. **Create Posts**: Share text posts with optional images
5. **Connect with Friends**: Send friend requests and manage your social network

### Available Pages
- **Home** (`/`): Main landing page with navigation
- **Posts** (`/CSMediaPosts/`): View and create social media posts
- **My Profile** (`/CSMediaProfiles/myprofile`): Manage your profile settings
- **All Users** (`/CSMediaProfiles/everyone`): Browse all registered users
- **Find New Friends** (`/CSMediaProfiles/toinvite`): Discover users to connect with
- **Pending Requests** (`/CSMediaProfiles/pendingrequest`): Manage friend requests
- **Admin Panel** (`/admin/`): Django administration interface

## 🗄️ Database Models

### CSMediaProfile
- User profile information (name, bio, avatar)
- Friend relationships
- Profile statistics (posts, likes, friends count)

### CSMediaPost
- Text content and optional images
- Author relationship
- Like and comment tracking
- Timestamps for creation and updates

### CSMediaComment
- Comment text and author
- Associated post
- Creation timestamps

### CSMediaLike
- Like/unlike functionality
- User and post relationships
- Like status tracking

### CSMediaRelationship
- Friend request management
- Sender/receiver relationships
- Request status (Send/Accepted)

## 🎨 UI Framework

The application uses **Semantic UI** for modern, responsive design:
- Clean and intuitive interface
- Mobile-friendly responsive design
- Pre-built UI components
- Custom CSS for branding and styling

## 🔧 Configuration

### Key Settings
- **Database**: SQLite for development
- **Static Files**: Organized in Static_CDN directory
- **Media Files**: User uploads stored in Media_Root
- **Authentication**: Django Allauth for social login support
- **File Upload**: Image validation for posts and avatars

### Environment Variables
The application uses Django's default settings. For production deployment, consider:
- Setting `DEBUG = False`
- Configuring a production database
- Setting up proper static file serving
- Configuring email settings for user verification

## 🚀 Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

## 📝 API Endpoints

The application provides the following main URL patterns:
- `/` - Home page
- `/CSMediaPosts/` - Posts application
- `/CSMediaProfiles/` - Profiles application
- `/admin/` - Django admin interface

## 🐛 Troubleshooting

### Common Issues

1. **Virtual Environment Not Activated**
   - Ensure you've activated the virtual environment before running commands

2. **Database Migration Errors**
   - Delete `db.sqlite3` and run migrations again
   - Check for any model conflicts

3. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_URL and STATIC_ROOT settings

4. **Image Upload Issues**
   - Ensure Pillow is installed: `pip install Pillow`
   - Check MEDIA_ROOT and MEDIA_URL settings



---

**Built with ❤️ using Django and Semantic UI**
