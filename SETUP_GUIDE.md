# GitHub Repository Setup Guide

Complete step-by-step guide to set up your Nepali Date Converter API Examples repository for maximum SEO and discoverability.

## 📊 Repository Information

### Repository Name
```
nepali-date-converter-api-examples
```

### Short Description (for GitHub)
```
🗓️ Ready-to-use code examples for converting between Gregorian (AD) and Bikram Sambat (BS) Nepali dates. Free REST API with JavaScript, Python, PHP examples. No auth required. CORS enabled.
```

### Website URL
```
https://sudhanparajuli.com.np/code-examples
```

### Topics/Tags (Add all 15)
```
nepali-date
bs-to-ad
ad-to-bs
bikram-sambat
nepali-calendar
date-converter
rest-api
api-examples
javascript
python
php
nepal
nepali-developers
code-snippets
date-conversion
```

---

## 🚀 Step-by-Step Setup

### Step 1: Create Repository on GitHub

1. Go to [github.com/new](https://github.com/new)
2. Enter repository name: `nepali-date-converter-api-examples`
3. Add description (use the short description above)
4. Select **Public**
5. Check **Add a README file**
6. Choose **MIT License**
7. Click **Create repository**

### Step 2: Clone Repository Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/nepali-date-converter-api-examples.git

# Navigate to directory
cd nepali-date-converter-api-examples
```

### Step 3: Create Directory Structure

```bash
# Create all necessary directories
mkdir -p .github/workflows
mkdir -p .github/ISSUE_TEMPLATE
mkdir -p docs
mkdir -p examples/{javascript,python,php,widget,java,csharp,ruby,go}
mkdir -p tools
mkdir -p tests
mkdir -p assets
```

### Step 4: Add Core Files

Create these essential files in the root directory:

#### 1. README.md
*(Use the comprehensive README.md artifact already created)*

#### 2. LICENSE
```bash
# MIT License is already added via GitHub, but you can verify/update it
```

#### 3. CONTRIBUTING.md
*(Use the CONTRIBUTING.md artifact already created)*

#### 4. CODE_OF_CONDUCT.md
```bash
# Create CODE_OF_CONDUCT.md
cat > CODE_OF_CONDUCT.md << 'EOF'
# Contributor Covenant Code of Conduct

## Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints
* Gracefully accepting constructive criticism
* Focusing on what is best for the community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery
* Trolling, insulting/derogatory comments, and personal attacks
* Public or private harassment
* Publishing others' private information without permission

## Enforcement

Project maintainers are responsible for clarifying standards and may take appropriate action in response to unacceptable behavior.

## Attribution

This Code of Conduct is adapted from the Contributor Covenant, version 1.4.
EOF
```

### Step 5: Add Example Files

#### JavaScript Examples

```bash
# Create examples/javascript/README.md
cat > examples/javascript/README.md << 'EOF'
# JavaScript Examples

Examples for using the Nepali Date Converter API with JavaScript.

## Available Examples

- **fetch-api.js** - Using native Fetch API
- **axios-example.js** - Using Axios library
- **jquery-example.js** - Using jQuery
- **nodejs-example.js** - Node.js server-side usage
- **react-component.jsx** - React component
- **vue-component.vue** - Vue.js component

## Quick Start

```javascript
async function convertADToBS(year, month, day) {
  const response = await fetch(`https://sudhanparajuli.com.np/api/ad-to-bs/${year}/${month}/${day}`);
  const data = await response.json();
  return data.result;
}

// Usage
convertADToBS(2024, 10, 15).then(result => console.log(result));
```

See individual files for detailed examples.
EOF
```

#### Python Examples

```bash
# Create examples/python/README.md
cat > examples/python/README.md << 'EOF'
# Python Examples

Examples for using the Nepali Date Converter API with Python.

## Prerequisites

```bash
pip install requests
```

## Available Examples

- **requests_example.py** - Using requests library (recommended)
- **urllib_example.py** - Using urllib (no dependencies)
- **async_example.py** - Async/await with aiohttp
- **batch_converter.py** - Batch conversion script
- **django_integration.py** - Django integration

## Quick Start

```python
import requests

def convert_ad_to_bs(year, month, day):
    url = f"https://sudhanparajuli.com.np/api/ad-to-bs/{year}/{month}/{day}"
    response = requests.get(url)
    data = response.json()
    return data['result']

# Usage
result = convert_ad_to_bs(2024, 10, 15)
print(result)
```

See individual files for detailed examples.
EOF
```

#### PHP Examples

```bash
# Create examples/php/README.md
cat > examples/php/README.md << 'EOF'
# PHP Examples

Examples for using the Nepali Date Converter API with PHP.

## Available Examples

- **file_get_contents.php** - Simple file_get_contents (no dependencies)
- **curl_example.php** - cURL implementation
- **guzzle_example.php** - Guzzle HTTP client
- **laravel_service.php** - Laravel service class

## Quick Start

```php
<?php
function convertADToBS($year, $month, $day) {
    $url = "https://sudhanparajuli.com.np/api/ad-to-bs/{$year}/{$month}/{$day}";
    $response = file_get_contents($url);
    $data = json_decode($response, true);
    return $data['result'];
}

// Usage
$result = convertADToBS(2024, 10, 15);
print_r($result);
?>
```

See individual files for detailed examples.
EOF
```

### Step 6: Add Documentation

```bash
# Create docs/QUICK_START.md
cat > docs/QUICK_START.md << 'EOF'
# Quick Start Guide

Get started with the Nepali Date Converter API in 5 minutes.

## Choose Your Language

- [JavaScript](#javascript)
- [Python](#python)
- [PHP](#php)

## JavaScript

```javascript
// Convert AD to BS
const response = await fetch('https://sudhanparajuli.com.np/api/ad-to-bs/2024/10/15');
const data = await response.json();
console.log(data.result); // { year: 2081, month: 6, day: 29 }
```

## Python

```python
import requests

response = requests.get('https://sudhanparajuli.com.np/api/ad-to-bs/2024/10/15')
data = response.json()
print(data['result'])  # {'year': 2081, 'month': 6, 'day': 29}
```

## PHP

```php
<?php
$url = "https://sudhanparajuli.com.np/api/ad-to-bs/2024/10/15";
$response = file_get_contents($url);
$data = json_decode($response, true);
print_r($data['result']);
?>
```

That's it! No authentication needed.
EOF
```

### Step 7: Add GitHub Actions (Optional)

```bash
# Create .github/workflows/docs-check.yml
cat > .github/workflows/docs-check.yml << 'EOF'
name: Documentation Check

on:
  pull_request:
    branches: [ main ]
  push:
    branches: [ main ]

jobs:
  check-links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Check Markdown links
        uses: gaurav-nelson/github-action-markdown-link-check@v1
        with:
          use-quiet-mode: 'yes'
EOF
```

### Step 8: Add Issue Templates

```bash
# Create .github/ISSUE_TEMPLATE/bug_report.md
cat > .github/ISSUE_TEMPLATE/bug_report.md << 'EOF'
---
name: Bug Report
about: Report a bug or issue
title: '[BUG] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear description of the bug.

**To Reproduce**
Steps to reproduce:
1. 
2. 
3. 

**Expected behavior**
What you expected to happen.

**Code snippet**
```language
// Your code here
```

**Environment:**
- Programming Language: 
- Version: 
- OS: 
EOF
```

```bash
# Create .github/ISSUE_TEMPLATE/feature_request.md
cat > .github/ISSUE_TEMPLATE/feature_request.md << 'EOF'
---
name: Feature Request
about: Suggest a new feature or example
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

**Feature Description**
Clear description of the feature.

**Use Case**
Why would this be useful?

**Example**
If applicable, provide example code or usage.
EOF
```

### Step 9: Commit and Push

```bash
# Add all files
git add .

# Commit
git commit -m "feat: initial repository setup with examples and documentation

- Add comprehensive README with examples
- Add JavaScript, Python, PHP example directories
- Add API documentation
- Add contributing guidelines
- Add issue templates
- Add GitHub Actions workflow"

# Push to GitHub
git push origin main
```

### Step 10: Configure Repository Settings

#### On GitHub Website:

1. **Go to Settings > General**
   - Add website: `https://sudhanparajuli.com.np/code-examples`
   - Add description
   - Add topics (all 15 tags)

2. **Go to Settings > Options**
   - Enable: ✅ Issues
   - Enable: ✅ Wiki (optional)
   - Enable: ✅ Discussions (optional)

3. **Go to Settings > Pages** (Optional)
   - Source: Deploy from `main` branch `/docs` folder
   - This creates a documentation website

4. **Add Social Preview Image**
   - Settings > General > Social preview
   - Upload 1280x640px image

### Step 11: Create Banner Image

Create a banner image (1280x640px) with:
- Repository name
- API examples tagline
- Code snippet preview
- "Free & Open Source" badge

Upload to `assets/banner.png` and set as social preview.

---

## 📈 SEO Optimization Checklist

### ✅ Repository Level
- [ ] Descriptive repository name with keywords
- [ ] SEO-friendly description under 160 characters
- [ ] 10-15 relevant topics/tags
- [ ] Website URL added
- [ ] License specified (MIT)
- [ ] Social preview image added

### ✅ README.md
- [ ] Clear H1 title with keywords
- [ ] Table of contents
- [ ] Code examples with syntax highlighting
- [ ] Links to documentation
- [ ] Badges (license, API status, etc.)
- [ ] Quick start section
- [ ] Multiple language examples

### ✅ Documentation
- [ ] API reference with examples
- [ ] Quick start guide
- [ ] FAQ section
- [ ] Troubleshooting guide
- [ ] Contributing guidelines

### ✅ Code Examples
- [ ] Well-commented code
- [ ] Multiple programming languages
- [ ] Error handling examples
- [ ] Real-world use cases
- [ ] Copy-paste ready snippets

### ✅ Community
- [ ] Issue templates
- [ ] Pull request template
- [ ] Code of conduct
- [ ] Contributing guidelines
- [ ] License file

---

## 🎯 Post-Setup Tasks

### Week 1
- [ ] Share on social media (Twitter, LinkedIn, Reddit)
- [ ] Post in developer communities
- [ ] Submit to awesome-lists
- [ ] Add to personal portfolio

### Week 2
- [ ] Respond to issues/questions
- [ ] Add more language examples
- [ ] Create demo GIF/video
- [ ] Write a blog post

### Month 1
- [ ] Monitor analytics
- [ ] Gather feedback
- [ ] Add requested features
- [ ] Update documentation

---

## 🔗 Useful Links

- **GitHub Docs**: https://docs.github.com
- **Markdown Guide**: https://guides.github.com/features/mastering-markdown/
- **GitHub Actions**: https://docs.github.com/en/actions
- **Open Source Guides**: https://opensource.guide/

---

## 🆘 Troubleshooting

### Issue: Can't push to repository
**Solution:** Check your authentication (SSH key or personal access token)

### Issue: Social preview not showing
**Solution:** Wait 24 hours, images are cached by GitHub

### Issue: Topics not appearing
**Solution:** Refresh page, may take a few minutes to update

---

**Setup complete! Your repository is now optimized for SEO and discovery! 🎉**
