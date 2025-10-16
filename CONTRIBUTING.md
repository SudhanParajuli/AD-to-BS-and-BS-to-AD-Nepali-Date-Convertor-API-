# Contributing to Nepali Date Converter API Examples

First off, thank you for considering contributing to this project! 🎉

We love receiving contributions from our community. This document provides guidelines to make the contribution process easy and effective for everyone involved.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs **actual behavior**
- **Code samples** if applicable
- **Environment details** (OS, language version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear use case** for the enhancement
- **Step-by-step description** of the suggested enhancement
- **Why this enhancement would be useful** to most users

### Adding Code Examples

We especially welcome contributions of code examples in different programming languages! If you'd like to add an example:

1. Choose a language not yet covered or improve an existing example
2. Follow our code style guidelines (see below)
3. Include clear comments explaining the code
4. Add error handling
5. Test your code thoroughly
6. Update the relevant README.md file

### Improving Documentation

Documentation improvements are always welcome! This includes:

- Fixing typos or unclear explanations
- Adding more detailed examples
- Improving the FAQ section
- Translating documentation (if applicable)

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/nepali-date-converter-api-examples.git
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** following our guidelines
5. **Test your changes** thoroughly
6. **Commit your changes** with clear commit messages
7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Submit a Pull Request** through GitHub

## 📝 Contribution Guidelines

### Code Examples

When adding code examples:

- ✅ Use clear, descriptive variable names
- ✅ Include comprehensive error handling
- ✅ Add comments explaining complex logic
- ✅ Provide multiple examples (simple and advanced)
- ✅ Test all examples before submitting
- ✅ Follow the language's standard conventions
- ✅ Include dependencies/requirements if any

### Documentation

When contributing to documentation:

- ✅ Use clear, concise language
- ✅ Include code examples where appropriate
- ✅ Use proper Markdown formatting
- ✅ Check spelling and grammar
- ✅ Update the table of contents if needed
- ✅ Link to related documentation where helpful

### File Organization

Place your contributions in the appropriate directory:

```
examples/
├── [language-name]/
│   ├── README.md           # Overview of examples
│   ├── example1.ext        # Simple example
│   ├── example2.ext        # Advanced example
│   └── requirements.txt    # Dependencies (if applicable)
```

## 🎨 Style Guidelines

### Code Style

#### JavaScript
```javascript
// Use async/await for cleaner code
async function convertDate(year, month, day) {
  try {
    const response = await fetch(`https://api.example.com/${year}/${month}/${day}`);
    const data = await response.json();
    return data.result;
  } catch (error) {
    console.error('Error:', error);
    return null;
  }
}
```

#### Python
```python
# Follow PEP 8 style guide
def convert_date(year, month, day):
    """Convert date with proper documentation."""
    try:
        response = requests.get(f"https://api.example.com/{year}/{month}/{day}")
        response.raise_for_status()
        return response.json()['result']
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
```

#### PHP
```php
<?php
// Use descriptive function names and proper error handling
function convertDate($year, $month, $day) {
    $url = "https://api.example.com/{$year}/{$month}/{$day}";
    $response = file_get_contents($url);
    
    if ($response === FALSE) {
        return null;
    }
    
    return json_decode($response, true)['result'];
}
?>
```

### Documentation Style

- Use **Markdown** for all documentation
- Use **heading hierarchy** properly (H1 → H2 → H3)
- Include **code blocks** with language specification
- Add **emojis** sparingly for visual appeal
- Keep **line length** under 120 characters
- Use **lists** for better readability

### README Template for New Languages

```markdown
# [Language Name] Examples

Examples for using the Nepali Date Converter API with [Language Name].

## Prerequisites

- [Language] version X.X or higher
- [Required package] (if any)

## Installation

```bash
# Installation commands
```

## Basic Example

```[language]
// Your code here
```

## Advanced Example

```[language]
// More complex code here
```

## Error Handling

```[language]
// Error handling example
```

## Additional Resources

- [Official Documentation](link)
- [Language Guide](link)
```

## 💬 Commit Messages

Write clear, meaningful commit messages:

### Format
```
type(scope): short description

Longer description if needed

Fixes #issue_number
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting)
- **refactor**: Code refactoring
- **test**: Adding tests
- **chore**: Maintenance tasks

### Examples
```bash
feat(python): add async example with aiohttp

Add asynchronous date conversion example using aiohttp library.
Includes error handling and batch processing example.

Fixes #45
```

```bash
docs(readme): fix typo in installation section

Corrected the package name in the installation instructions.
```

## 🔄 Pull Request Process

1. **Update documentation** if you've changed functionality
2. **Add yourself to CONTRIBUTORS.md** if you haven't already
3. **Ensure all tests pass** (if applicable)
4. **Update the README.md** with details of changes if needed
5. **Request review** from maintainers
6. **Address review comments** promptly

### Pull Request Template

When creating a PR, use this template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
How did you test these changes?

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have commented my code where needed
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have tested my changes
```

## 🎯 Priority Areas

We're especially looking for contributions in these areas:

1. **New language examples** (Go, Rust, Swift, Kotlin, etc.)
2. **Framework integrations** (Angular, Svelte, FastAPI, etc.)
3. **Mobile examples** (React Native, Flutter)
4. **Real-world use cases** and tutorials
5. **Performance optimizations**
6. **Better error messages** and handling

## ❓ Questions?

Don't hesitate to ask questions! You can:

- Open an issue with the "question" label
- Reach out to maintainers
- Check our FAQ documentation

## 🙏 Thank You!

Your contributions make this project better for the entire Nepali developer community. We appreciate your time and effort!

---

**Happy Contributing! 🚀**
