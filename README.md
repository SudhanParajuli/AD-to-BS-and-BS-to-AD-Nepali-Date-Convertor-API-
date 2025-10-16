# 🗓️ Nepali Date Converter API - Code Examples

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![API Status](https://img.shields.io/badge/API-Online-success)](https://sudhanparajuli.com.np/api/)
[![CORS](https://img.shields.io/badge/CORS-Enabled-blue)](https://sudhanparajuli.com.np/api/)

> **Ready-to-use code snippets for converting between Gregorian (AD) and Bikram Sambat (BS) Nepali dates**

Convert dates between AD (Anno Domini) and BS (Bikram Sambat) calendar systems with a simple, free REST API. Perfect for developers building applications that need Nepali date functionality.

## 🚀 Quick Start

```javascript
// Convert AD to BS
const response = await fetch('https://sudhanparajuli.com.np/api/ad-to-bs/2024/10/15');
const data = await response.json();
console.log(data.result); // { year: 2081, month: 6, day: 29 }
```

## 📚 Table of Contents

- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Code Examples](#code-examples)
  - [JavaScript](#javascript)
  - [Python](#python)
  - [PHP](#php)
  - [Iframe Widget](#iframe-widget)
- [API Response Format](#api-response-format)
- [Common Use Cases](#common-use-cases)
- [Rate Limiting](#rate-limiting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- 🌐 **Free to Use** - No authentication or API keys required
- ⚡ **Fast & Reliable** - Optimized for quick responses
- 🔓 **CORS Enabled** - Use directly from browser applications
- 📖 **Well Documented** - Copy-paste ready code examples
- 🛠️ **Multiple Languages** - JavaScript, Python, PHP, and more
- 📱 **Widget Available** - Embeddable iframe for quick integration
- 🔄 **Bidirectional** - Convert AD→BS and BS→AD

## 🌐 API Endpoints

**Base URL:** `https://sudhanparajuli.com.np/api/`

### Convert AD to BS

```
GET /api/ad-to-bs/{YYYY}/{MM}/{DD}
```

**Example:** `https://sudhanparajuli.com.np/api/ad-to-bs/2024/10/15`

### Convert BS to AD

```
GET /api/bs-to-ad/{YYYY}/{MM}/{DD}
```

**Example:** `https://sudhanparajuli.com.np/api/bs-to-ad/2081/6/29`

## 💻 Code Examples

### JavaScript

#### Using Fetch API

```javascript
async function convertADToBS(year, month, day) {
  try {
    const response = await fetch(
      `https://sudhanparajuli.com.np/api/ad-to-bs/${year}/${month}/${day}`
    );
    const data = await response.json();
    
    if (data.success) {
      console.log(`AD ${year}-${month}-${day} = BS ${data.result.year}-${data.result.month}-${data.result.day}`);
      return data.result;
    } else {
      throw new Error(data.error || 'Conversion failed');
    }
  } catch (error) {
    console.error('Error converting AD to BS:', error);
    return null;
  }
}

// Example usage
convertADToBS(2024, 10, 15).then(result => {
  if (result) {
    document.getElementById('bs-date').textContent = 
      `${result.year}/${result.month}/${result.day}`;
  }
});
```

#### Using jQuery

```javascript
$.get('https://sudhanparajuli.com.np/api/ad-to-bs/2024/1/15')
  .done(function(data) {
    if (data.success) {
      $('#result').text(`${data.result.year}/${data.result.month}/${data.result.day}`);
    }
  })
  .fail(function() {
    console.log('API request failed');
  });
```

[See more JavaScript examples →](./examples/javascript/)

### Python

#### Using requests library

```python
import requests

def convert_ad_to_bs(year, month, day):
    """Convert Gregorian (AD) date to Bikram Sambat (BS) date"""
    url = f"https://sudhanparajuli.com.np/api/ad-to-bs/{year}/{month}/{day}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get('success'):
            bs_date = data['result']
            print(f"AD {year}-{month}-{day} = BS {bs_date['year']}-{bs_date['month']}-{bs_date['day']}")
            return bs_date
        else:
            print(f"Error: {data.get('error', 'Unknown error')}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Example usage
bs_result = convert_ad_to_bs(2024, 10, 15)
```

#### Using urllib (no dependencies)

```python
import urllib.request
import json

def convert_date_api(year, month, day, conversion_type='ad-to-bs'):
    """Convert date using the API without external dependencies"""
    url = f"https://sudhanparajuli.com.np/api/{conversion_type}/{year}/{month}/{day}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if data.get('success'):
                return data['result']
            else:
                print(f"API Error: {data.get('error', 'Unknown error')}")
                return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
ad_to_bs = convert_date_api(2024, 10, 15, 'ad-to-bs')
bs_to_ad = convert_date_api(2081, 6, 29, 'bs-to-ad')
```

[See more Python examples →](./examples/python/)

### PHP

```php
<?php
/**
 * Convert AD date to BS date using the API
 */
function convertADToBS($year, $month, $day) {
    $url = "https://sudhanparajuli.com.np/api/ad-to-bs/{$year}/{$month}/{$day}";
    $response = file_get_contents($url);
    
    if ($response === FALSE) {
        return null;
    }
    
    $data = json_decode($response, true);
    
    if (isset($data['success']) && $data['success']) {
        return $data['result'];
    }
    
    return null;
}

// Example usage
$bs_date = convertADToBS(2024, 10, 15);
if ($bs_date) {
    echo "AD 2024-10-15 = BS {$bs_date['year']}-{$bs_date['month']}-{$bs_date['day']}\n";
}
?>
```

[See more PHP examples →](./examples/php/)

### Iframe Widget

Embed the date converter directly into your website:

```html
<!-- Basic iframe embed -->
<iframe
  src="https://sudhanparajuli.com.np/iframe"
  width="100%"
  height="400"
  frameborder="0"
  title="Nepali Date Converter - AD to BS and BS to AD"
  style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>
```

[See more widget examples →](./examples/widget/)

## 📋 API Response Format

### Successful Response (AD to BS)

```json
{
  "success": true,
  "input": {
    "year": 2024,
    "month": 10,
    "day": 15,
    "type": "AD"
  },
  "result": {
    "year": 2081,
    "month": 6,
    "day": 29,
    "type": "BS"
  }
}
```

### Error Response

```json
{
  "error": "Invalid date: month must be between 1 and 12"
}
```

## 🎯 Common Use Cases

- **Web Applications** - Add Nepali date functionality to your website
- **Mobile Apps** - Integrate BS calendar in Android/iOS apps
- **Data Processing** - Convert historical dates in datasets
- **CMS Integration** - WordPress, Drupal, or custom CMS plugins
- **AI Applications** - Train models with Nepali calendar data
- **Educational Tools** - Teaching calendar systems
- **Financial Systems** - Handle Nepali fiscal year calculations

## ⚡ Rate Limiting

- Be respectful with API requests
- Cache results when possible to reduce load
- For high-volume usage, consider implementing your own converter

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add More Examples** - Share code in other languages
2. **Improve Documentation** - Fix typos, clarify instructions
3. **Report Issues** - Found a bug? Let us know
4. **Share Use Cases** - Tell us how you're using the API

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Best Practices

- ✅ Validate input dates before making API calls
- ✅ Implement proper error handling
- ✅ Cache frequently used conversions
- ✅ Use HTTPS for secure connections
- ✅ Handle network timeouts gracefully
- ✅ Test with edge cases (leap years, month boundaries)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Support

If you find this useful, please:
- ⭐ Star this repository
- 🐛 Report issues
- 📢 Share with others
- 💡 Suggest improvements

## 📧 Contact

For questions or support:
- **Website:** [sudhanparajuli.com.np](https://sudhanparajuli.com.np)
- **API Documentation:** [sudhanparajuli.com.np/code-examples](https://sudhanparajuli.com.np/code-examples)

---

**Made with ❤️ for the Nepali developer community**
