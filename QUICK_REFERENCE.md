# Django Template Quick Reference

## 🎯 What Changed

### Before
- **1 file**: `home.html` (95 lines with inline CSS)
- Hardcoded styles, mixed concerns
- No reusability

### After
- **8 files**: Organized, modular structure
- Separated CSS, JS, and HTML
- Reusable components

---

## 📁 New File Structure

```
static/
├── css/style.css          # 107 lines of organized CSS
└── js/main.js             # JavaScript functionality

templates/
├── base.html              # Master template with blocks
├── home.html              # Clean 12-line template
└── includes/
    ├── header.html        # Reusable header
    ├── navigation.html    # Reusable nav with auth logic
    └── footer.html        # Reusable footer
```

---

## 🚀 Quick Commands

```bash
# Collect static files (run after changes to CSS/JS)
python manage.py collectstatic --noinput

# Run development server
python manage.py runserver

# Check for issues
python manage.py check
```

---

## 📝 Common Tasks

### Add a New Page

1. Create `templates/about.html`:
```django
{% extends 'base.html' %}

{% block title %}About{% endblock %}

{% block content %}
    <section>
        <h2>About Us</h2>
        <p>Content here...</p>
    </section>
{% endblock %}
```

2. Add view in `django_project/views.py`:
```python
def about(request):
    return render(request, 'about.html')
```

3. Add URL in `django_project/urls.py`:
```python
path('about/', views.about, name='about'),
```

### Add Custom CSS for a Page

1. Create `static/css/about.css`
2. In your template:
```django
{% block extra_css %}
    <link rel="stylesheet" href="{% static 'css/about.css' %}">
{% endblock %}
```

### Add Custom JavaScript for a Page

1. Create `static/js/about.js`
2. In your template:
```django
{% block extra_js %}
    <script src="{% static 'js/about.js' %}"></script>
{% endblock %}
```

### Update Navigation Links

Edit `templates/includes/navigation.html` - changes appear site-wide!

### Update Styles Site-Wide

Edit `static/css/style.css` - changes apply to all pages!

---

## 🎨 Template Blocks Available

In `base.html`, you can override these blocks:

| Block | Purpose | Required |
|-------|---------|----------|
| `{% block title %}` | Page title | No |
| `{% block extra_css %}` | Page-specific CSS | No |
| `{% block content %}` | Main content | **Yes** |
| `{% block extra_js %}` | Page-specific JS | No |

---

## ✨ Benefits Achieved

✅ **Clean Code**: No more inline styles  
✅ **Reusable**: Header, nav, footer used everywhere  
✅ **Maintainable**: Update once, changes everywhere  
✅ **Performance**: Browser caches CSS/JS  
✅ **Scalable**: Easy to add new pages  
✅ **Best Practices**: Follows Django conventions  
✅ **Professional**: Industry-standard structure  

---

## 🔗 Key Template Tags Used

```django
{% load static %}                      # Load static files system
{% static 'css/style.css' %}          # Generate static file URL
{% extends 'base.html' %}             # Inherit from base
{% block content %}{% endblock %}     # Define/override blocks
{% include 'includes/header.html' %}  # Include partial
{% url 'view_name' %}                 # Generate URL
{% now "Y" %}                         # Current year
{% if user.is_authenticated %}        # Conditional logic
```

---

## 📚 Next Steps

1. ✅ Static files configured
2. ✅ Templates restructured
3. ✅ Components created
4. ✅ collectstatic executed

**You can now:**
- Visit `http://localhost:8000/` to see the result
- Create new pages using the same pattern
- Modify `static/css/style.css` to update styles
- Edit `templates/includes/navigation.html` to update navigation

**To run the server:**
```bash
python manage.py runserver
```

Then visit: http://127.0.0.1:8000/
