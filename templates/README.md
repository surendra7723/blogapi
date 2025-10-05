# Django Template Structure Guide

## Project Structure

```
blogapi/
├── static/
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   └── js/
│       └── main.js            # Main JavaScript file
├── templates/
│   ├── base.html              # Base template (extends by all pages)
│   ├── home.html              # Home page (extends base.html)
│   └── includes/              # Reusable template fragments
│       ├── header.html
│       ├── navigation.html
│       └── footer.html
```

## Template Inheritance

### Base Template (`base.html`)
The foundation for all pages. Contains:
- HTML structure
- Meta tags
- Static file loading
- Common CSS/JS files
- Blocks for content and extra CSS/JS

### Page Templates (e.g., `home.html`)
Extend the base template using:
```django
{% extends 'base.html' %}
```

### Include Templates (`includes/`)
Reusable components that can be included in any template:
```django
{% include 'includes/header.html' %}
```

## Using Static Files

### In Templates
```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/main.js' %}"></script>
```

### Collecting Static Files
For production deployment:
```bash
python manage.py collectstatic
```

## Creating New Pages

1. **Create a new template** that extends base:
```django
{% extends 'base.html' %}

{% block title %}Page Title{% endblock %}

{% block content %}
    <!-- Your content here -->
{% endblock %}
```

2. **Add page-specific CSS** (optional):
```django
{% block extra_css %}
    <link rel="stylesheet" href="{% static 'css/page-specific.css' %}">
{% endblock %}
```

3. **Add page-specific JavaScript** (optional):
```django
{% block extra_js %}
    <script src="{% static 'js/page-specific.js' %}"></script>
{% endblock %}
```

## Benefits of This Structure

✅ **Separation of Concerns**: HTML, CSS, and JS in separate files  
✅ **Reusability**: Include fragments prevent code duplication  
✅ **Maintainability**: Easy to update styles across all pages  
✅ **Performance**: Browser can cache static files  
✅ **Scalability**: Easy to add new pages following the same pattern  
✅ **Best Practices**: Follows Django's recommended structure

## Common Template Tags

### Template Inheritance
- `{% extends 'base.html' %}` - Inherit from base template
- `{% block content %}{% endblock %}` - Define content blocks
- `{% include 'includes/header.html' %}` - Include partial template

### Static Files
- `{% load static %}` - Load static tag library
- `{% static 'css/style.css' %}` - Generate static file URL

### URLs
- `{% url 'view_name' %}` - Generate URL from view name
- `{% url 'view_name' arg1 arg2 %}` - URL with arguments

### Template Variables
- `{{ variable }}` - Output variable value
- `{% if condition %}{% endif %}` - Conditional logic
- `{% for item in list %}{% endfor %}` - Loops

## Next Steps

1. Run `python manage.py collectstatic` to collect static files
2. Test the home page by visiting `http://localhost:8000/`
3. Create additional pages following the same pattern
4. Add more CSS/JS files as needed for specific features
