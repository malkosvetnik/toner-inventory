# Contributing to Toner Inventory System

First off, thank you for considering contributing to Toner Inventory System! 🎉

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the [existing issues](../../issues) to avoid duplicates.

When creating a bug report, include:
- **Description**: Clear description of the problem
- **Steps to reproduce**: Numbered steps to reproduce the behavior
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Screenshots**: If applicable
- **Environment**: 
  - OS (Windows 10/11, Linux distro, etc.)
  - Python version (if running from source)
  - App version

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as [GitHub issues](../../issues).

When creating an enhancement suggestion, include:
- **Clear title**: Describe the enhancement in the title
- **Detailed description**: Explain the feature and its benefits
- **Use cases**: Provide examples of how it would be used
- **Alternatives**: Describe alternatives you've considered

### 🔧 Pull Requests

1. **Fork** the repository
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly** - make sure nothing breaks
5. **Commit** with clear messages:
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push** to your fork:
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request** with:
   - Clear title describing the change
   - Description of what changed and why
   - Screenshots (if UI changes)
   - Link to related issue (if applicable)

## Development Guidelines

### Code Style

- Follow [PEP 8](https://pep8.org/) for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues: "Fix #123: Description"

### Translation

When adding new UI text:

1. Add to `translations.py`:
   ```python
   'your_key': {'sr': 'Srpski tekst', 'en': 'English text'}
   ```

2. Use in code:
   ```python
   T.get("your_key", self.lang)
   ```

### Testing

Before submitting:
- [ ] Test all affected features
- [ ] Test in both Serbian and English
- [ ] Test edge cases
- [ ] Check for errors in console

## Project Structure

```
toner-inventory/
├── toner_app_multilang.py  # Main application
├── translations.py          # All translations
├── create_icon.py          # Icon generator
├── build_exe.py            # EXE builder
├── screenshots/            # Documentation images
└── docs/                   # Documentation files
```

## Adding New Features

### Example: Adding a new dialog

1. **Create dialog class** (follow existing patterns):
   ```python
   class NewDialog(QDialog):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.lang = parent.lang if parent else 'sr'
           self.init_ui()
   ```

2. **Add translations**:
   ```python
   'dialog_new_title': {'sr': 'Novi Dijalog', 'en': 'New Dialog'}
   ```

3. **Test** both languages

4. **Document** in README if user-facing

## Areas Open for Contribution

### 🌍 **Translations**
- Add more languages (German, French, etc.)
- Improve existing translations

### 📊 **Features**
- Dark mode theme
- Additional statistics/charts
- Barcode scanning
- Email notifications
- Cost tracking

### 🐛 **Bug Fixes**
- Check [open issues](../../issues)
- Fix known bugs

### 📝 **Documentation**
- Improve README
- Add tutorials
- Write use case examples

### 🎨 **UI/UX**
- Improve design
- Add icons
- Better color schemes

## Questions?

- 💬 [Start a discussion](../../discussions)
- 📧 Open an issue
- 🐛 Report bugs in issues

## Code of Conduct

Be respectful and constructive. We want a welcoming community for everyone.

---

**Thank you for contributing!** 🙏
