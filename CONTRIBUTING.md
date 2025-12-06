# Contributing to Amazon SP-API Django

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Issues

- Check if the issue already exists in the [Issues](https://github.com/Vishnu-Singh/amazon-sp-api-django/issues) section
- Provide detailed information about the issue:
  - Steps to reproduce
  - Expected behavior
  - Actual behavior
  - Environment details (OS, Python version, Docker version)
  - Error messages or logs

### Suggesting Enhancements

- Open an issue with the "enhancement" label
- Clearly describe the feature and its use case
- Explain why this enhancement would be useful

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes**:
   - Follow the existing code style
   - Add docstrings to new functions and classes
   - Update documentation if needed
3. **Test your changes**:
   ```bash
   python manage.py test
   python manage.py check
   ```
4. **Commit your changes** with clear commit messages
5. **Push to your fork** and submit a pull request

## 📋 Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/amazon-sp-api-django.git
cd amazon-sp-api-django

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with test credentials

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## 🎨 Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Use type hints where appropriate

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test feeds

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 📝 Documentation

- Update README.md if you add new features
- Add docstrings to new functions and classes
- Update QUICKSTART.md if setup process changes
- Include examples in docstrings where helpful

## 🔍 Code Review Process

1. All pull requests require review before merging
2. Address any feedback from reviewers
3. Ensure all CI checks pass
4. Keep pull requests focused on a single feature or fix

## 🌳 Branch Naming

- `feature/description` - For new features
- `fix/description` - For bug fixes
- `docs/description` - For documentation updates
- `refactor/description` - For code refactoring

## 📦 Adding New API Endpoints

When adding new Amazon SP-API endpoints:

1. **Identify the correct app** (e.g., `feeds`, `orders`, etc.)
2. **Add the view** in `views.py`:
   ```python
   class NewEndpointView(View):
       def __init__(self, **kwargs):
           super().__init__(**kwargs)
           self.client = AmazonSPAPIClient()
       
       def get(self, request, *args, **kwargs):
           # Implementation
           pass
   ```
3. **Add the URL** in `urls.py`:
   ```python
   path('new-endpoint/', NewEndpointView.as_view(), name='new-endpoint'),
   ```
4. **Update documentation** in README.md
5. **Add tests** if applicable

## 🐛 Debugging

```bash
# Enable debug logging
DEBUG=True python manage.py runserver

# Check for issues
python manage.py check

# Run deployment checks
python manage.py check --deploy
```

## 🚀 Release Process

1. Update version in relevant files
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. Tag the release with semantic versioning (e.g., v1.0.0)

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## 💬 Questions?

- Open an issue for questions
- Check existing issues and pull requests
- Review the README.md and QUICKSTART.md

## 🙏 Thank You!

Your contributions help make this project better for everyone!
