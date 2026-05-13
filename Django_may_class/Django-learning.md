# Django Learning Guide: Step by Step

A comprehensive roadmap to master Django web framework.

---

## Prerequisites

Before starting Django, ensure you have:

- **Python fundamentals** - variables, data types, functions, classes, OOP concepts
- **Basic HTML/CSS** - forms, templates, styling
- **Basic command line** - navigating directories, running commands
- **Virtual environments** - understanding why and how to isolate projects

---

## Phase 1: Django Fundamentals (Week 1-2)

### 1.1 Installation & Setup
- Install Django: `pip install django`
- Create a project: `django-admin startproject myproject`
- Create an app: `python manage.py startapp myapp`
- Run the server: `python manage.py runserver`

### 1.2 Project Structure
Understand the generated files:
- `manage.py` - command-line utility
- `settings.py` - configuration
- `urls.py` - URL routing
- `wsgi.py` / `asgi.py` - deployment entry points

### 1.3 MTV Architecture
- **Model** - database layer (data structure)
- **Template** - presentation layer (HTML with Django template language)
- **View** - business logic (handles requests and returns responses)

---

## Phase 2: Models & Databases (Week 2-3)

### 2.1 Creating Models
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
```

### 2.2 Key Field Types to Learn
- `CharField`, `TextField`, `IntegerField`, `FloatField`
- `BooleanField`, `DateField`, `DateTimeField`
- `ForeignKey`, `ManyToManyField`, `OneToOneField`
- `EmailField`, `URLField`, `FileField`, `ImageField`

### 2.3 Migrations
- `python manage.py makemigrations` - create migrations
- `python manage.py migrate` - apply migrations
- **Important:** Always run both commands after model changes

### 2.4 Django ORM
- QuerySet API: `Model.objects.all()`, `.filter()`, `.get()`, `.exclude()`
- Lookups: `__exact`, `__contains`, `__gt`, `__lt`, `__in`
- CRUD operations: Create, Read, Update, Delete

---

## Phase 3: Views & URLs (Week 3-4)

### 3.1 Function-Based Views (FBV)
```python
from django.shortcuts import render, get_object_or_404

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})
```

### 3.2 URL Configuration
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
]
```

### 3.3 Class-Based Views (CBV)
- `View` - base class
- `TemplateView` - render a template
- `ListView`, `DetailView` - display model data
- `CreateView`, `UpdateView`, `DeleteView` - handle forms

### 3.4 URL Patterns & Naming
- Named URLs for `reverse()` and `{% url %}` template tag
- URL namespacing for apps
- URL converters: `int`, `str`, `slug`, `uuid`

---

## Phase 4: Templates (Week 4-5)

### 4.1 Template Syntax
- Variables: `{{ variable }}`
- Tags: `{% tag %}`
- Filters: `{{ variable|filter }}`
- Comments: `{# comment #}` or `{% comment %}`

### 4.2 Template Inheritance
```html
<!-- base.html -->
<html>
<body>
    {% block content %}{% endblock %}
</body>
</html>

<!-- article.html -->
{% extends 'base.html' %}
{% block content %}
    <h1>{{ article.title }}</h1>
{% endblock %}
```

### 4.3 Built-in Tags & Filters
- `{% if %}`, `{% for %}`, `{% include %}`
- `{% static %}` for static files
- `|date`, `|truncatewords`, `|lower`, `|upper`

### 4.4 Context Processors
- Add global data to all templates
- Common use: user info, site settings

---

## Phase 5: Forms (Week 5-6)

### 5.1 Django Forms
```python
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
```

### 5.2 Form Handling in Views
- Display form: `form = ArticleForm()`
- Validate: `if form.is_valid()`
- Save: `form.save()`

### 5.3 CSRF Protection
- Always use `{% csrf_token %}` in forms
- Django provides built-in CSRF middleware

### 5.4 Form Validation
- `clean_<fieldname>()` for field-specific validation
- `clean()` for cross-field validation
- Custom validators

---

## Phase 6: Admin Interface (Week 6)

### 6.1 Admin Setup
- Create superuser: `python manage.py createsuperuser`
- Register models in `admin.py`

### 6.2 Customizing Admin
```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'content']
```

---

## Phase 7: Authentication & Authorization (Week 7)

### 7.1 Built-in Auth System
- User model: `django.contrib.auth.models.User`
- Login/logout views
- `@login_required` decorator

### 7.2 Registration
- Use `UserCreationForm` or `UserRegisterForm`
- Password hashing is automatic

### 7.3 Custom User Model
- Extend `AbstractUser` or `AbstractBaseUser`
- Set `AUTH_USER_MODEL` in settings

### 7.4 Permissions
- `@permission_required` decorator
- `user.has_perm()` method
- Groups for role-based access

---

## Phase 8: Advanced Topics (Week 8-10)

### 8.1 Signals
- `pre_save`, `post_save`, `pre_delete`, `post_delete`
- Decouple components

### 8.2 Middleware
- Request/response processing
- Custom middleware classes

### 8.3 Class-Based Views Deep Dive
- Mixins
- Method flowchart (dispatch, http_method_not_allowed, etc.)

### 8.4 Pagination
- `Paginator` class
- `paginate_by` in ListView

### 8.5 Sending Email
- Configure SMTP settings
- `send_mail()` function

### 8.6 Caching
- Per-site, per-view, template fragment caching
- Redis/Memcached integration

---

## Phase 9: REST API with Django REST Framework (Week 10-12)

### 9.1 Installation
- `pip install djangorestframework`
- Add to `INSTALLED_APPS`

### 9.2 Serializers
- ModelSerializer for quick serialization
- Custom serializers for complex data

### 9.3 ViewSets & Routers
- `ModelViewSet` for full CRUD
- `ReadOnlyModelViewSet` for read-only

### 9.4 Authentication
- Token authentication
- JWT authentication (with `djangorestframework-simplejwt`)

### 9.5 Permissions
- `IsAuthenticated`, `IsAdminUser`
- Custom permission classes

---

## Phase 10: Deployment (Week 12)

### 10.1 Production Settings
- `DEBUG = False`
- `ALLOWED_HOSTS`
- `SECRET_KEY` from environment variable
- Static files: `collectstatic`

### 10.2 Deployment Options
- **Heroku** - beginner-friendly, free tier discontinued
- **Railway** / **Render** - modern PaaS alternatives
- **VPS** - DigitalOcean, Linode (more control)
- **AWS** / **GCP** / **Azure** - enterprise scale

### 10.3 WSGI/ASGI Servers
- Gunicorn (WSGI)
- Uvicorn (ASGI for async)

### 10.4 Web Server
- Nginx as reverse proxy
- Static file serving

---

## Key Things to Pay Attention To

### Security
1. **Never commit SECRET_KEY** to version control
2. **CSRF protection** - always include `{% csrf_token %}`
3. **SQL injection** - Django ORM prevents this, avoid raw SQL
4. **XSS** - Django auto-escapes HTML in templates
5. **Clickjacking** - use `XFrameOptionsMiddleware`
6. **HTTPS** - always use in production

### Best Practices
1. **Virtual environments** - always use them
2. **requirements.txt** - track dependencies
3. **.gitignore** - exclude sensitive files
4. **Settings** - use separate settings for dev/production
5. **Testing** - write tests from the start
6. **Code organization** - follow Django conventions

### Common Pitfalls
1. **Forgetting migrations** after model changes
2. **Circular imports** - use lazy imports
3. **N+1 queries** - use `select_related()` / `prefetch_related()`
4. **Not handling static files** correctly in production
5. **Ignoring migrations conflicts** - resolve properly

---

## Recommended Resources

### Official Documentation
- https://docs.djangoproject.com/ - comprehensive and well-written

### Tutorials
- Django Girls Tutorial - beginner-friendly
- Mozilla Developer Network Django Tutorial
- William Vincent's Django tutorials

### Books
- "Django for Beginners" - William Vincent
- "Two Scoops of Django" - advanced patterns
- "Django 4 By Example" - practical projects

### Video Courses
- Django tutorials on YouTube (Corey Schafer)
- Udemy Django courses

---

## Practice Projects (By Difficulty)

### Beginner
1. **Personal Blog** - CRUD, templates, admin
2. **To-Do List** - forms, authentication
3. **URL Shortener** - redirects, models

### Intermediate
4. **E-commerce Store** - cart, checkout, orders
5. **Social Media Clone** - users, posts, likes, comments
6. **Job Board** - postings, applications, filtering

### Advanced
7. **REST API for Mobile App** - DRF, authentication
8. **Real-time Chat** - WebSockets, Channels
9. **CMS (Content Management System)** - custom admin, permissions

---

## Weekly Learning Schedule Suggestion

| Week | Focus Area |
|------|------------|
| 1-2 | Setup, models, basic views |
| 3-4 | URLs, templates, templates inheritance |
| 5-6 | Forms, admin, validation |
| 7 | Authentication, authorization |
| 8 | Advanced ORM, pagination |
| 9 | Signals, middleware |
| 10-12 | REST API with DRF |
| 12+ | Deployment, real projects |

---

Happy Learning! Remember: **Build projects alongside learning** - nothing beats hands-on experience.