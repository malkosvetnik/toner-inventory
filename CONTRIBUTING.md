# Contributing to Toner Inventory System

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- **Clear title** describing the problem
- **Steps to reproduce** the bug
- **Expected behavior** vs **actual behavior**
- **Screenshots** if applicable
- **Environment** (OS, Python version)

### Suggesting Features

Feature requests are welcome! Please:
- Check if the feature is already requested
- Clearly describe the feature and its benefits
- Explain your use case

### Pull Requests

1. **Fork** the repository
2. **Create a branch** for your feature (`git checkout -b feature/amazing-feature`)
3. **Make your changes** following the code style
4. **Test thoroughly** - ensure nothing breaks
5. **Commit** with clear messages (`git commit -m 'Add amazing feature'`)
6. **Push** to your branch (`git push origin feature/amazing-feature`)
7. **Open a Pull Request** with detailed description

## Development Setup

```bash
# Clone your fork
git clone https://github.com/malkosvetnik/toner-inventory.git
cd toner-inventory

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python toner_app_multilang.py
```

## Code Style

- Follow **PEP 8** Python style guide
- Use **meaningful variable names** (Serbian or English)
- Add **comments** for complex logic
- Keep functions **focused and small**
- Write **docstrings** for classes and functions

## Testing

Before submitting a PR:
- [ ] Test all basic operations (add/edit/delete)
- [ ] Test search functionality
- [ ] Test export/print features
- [ ] Test on clean database
- [ ] Check for any error messages

## Areas for Contribution

We especially welcome contributions in:
- 🌐 **Translations** - Add new languages
- 📊 **Reports** - New export formats
- 🎨 **UI/UX** - Design improvements
- 🐛 **Bug Fixes** - Always appreciated!
- 📖 **Documentation** - Improve README, add guides

## Questions?

Feel free to open an issue with the `question` label!

Thank you for contributing! 🙏
