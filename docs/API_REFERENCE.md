# API Reference - Nepali Date Converter

Complete API documentation for converting between AD (Gregorian) and BS (Bikram Sambat) dates.

## Base URL

```
https://sudhanparajuli.com.np/api/
```

## Authentication

No authentication required. The API is free and open for public use.

## Rate Limiting

- Please be respectful with request volume
- Cache results when possible
- No hard rate limits currently enforced
- For high-volume usage, consider implementing your own converter

## Endpoints

### 1. Convert AD to BS

Convert a Gregorian (AD) date to Bikram Sambat (BS) date.

#### Endpoint
```
GET /api/ad-to-bs/{year}/{month}/{day}
```

#### Parameters

| Parameter | Type | Required | Description | Valid Range |
|-----------|------|----------|-------------|-------------|
| year | integer | Yes | AD year | 1943-2042 |
| month | integer | Yes | AD month | 1-12 |
| day | integer | Yes | AD day | 1-31 |

#### Request Example

```bash
curl https://sudhanparajuli.com.np/api/ad-to-bs/2024/10/15
```

#### Success Response

**Status Code:** `200 OK`

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

---

### 2. Convert BS to AD

Convert a Bikram Sambat (BS) date to Gregorian (AD) date.

#### Endpoint
```
GET /api/bs-to-ad/{year}/{month}/{day}
```

#### Parameters

| Parameter | Type | Required | Description | Valid Range |
|-----------|------|----------|-------------|-------------|
| year | integer | Yes | BS year | 2000-2099 |
| month | integer | Yes | BS month | 1-12 |
| day | integer | Yes | BS day | 1-32 |

#### Request Example

```bash
curl https://sudhanparajuli.com.np/api/bs-to-ad/2081/6/29
```

#### Success Response

**Status Code:** `200 OK`

```json
{
  "success": true,
  "input": {
    "year": 2081,
    "month": 6,
    "day": 29,
    "type": "BS"
  },
  "result": {
    "year": 2024,
    "month": 10,
    "day": 15,
    "type": "AD"
  }
}
```

---

## Error Responses

### Invalid Date Format

**Status Code:** `400 Bad Request`

```json
{
  "error": "Invalid date: month must be between 1 and 12"
}
```

### Date Out of Range

**Status Code:** `400 Bad Request`

```json
{
  "error": "Date out of supported range"
}
```

### Invalid Day for Month

**Status Code:** `400 Bad Request`

```json
{
  "error": "Invalid date: day 32 does not exist in month 6"
}
```

### Server Error

**Status Code:** `500 Internal Server Error`

```json
{
  "error": "Internal server error"
}
```

---

## Response Fields

### Success Response Structure

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Always `true` for successful conversions |
| `input` | object | The input date provided |
| `input.year` | integer | Year from request |
| `input.month` | integer | Month from request |
| `input.day` | integer | Day from request |
| `input.type` | string | Calendar type: "AD" or "BS" |
| `result` | object | The converted date |
| `result.year` | integer | Converted year |
| `result.month` | integer | Converted month |
| `result.day` | integer | Converted day |
| `result.type` | string | Calendar type: "BS" or "AD" |

### Error Response Structure

| Field | Type | Description |
|-------|------|-------------|
| `error` | string | Human-readable error message |

---

## Date Ranges

### AD (Gregorian) Support
- **Minimum:** January 1, 1943 (1943/1/1)
- **Maximum:** December 31, 2042 (2042/12/31)

### BS (Bikram Sambat) Support
- **Minimum:** Baisakh 1, 2000 (2000/1/1)
- **Maximum:** Chaitra 32, 2099 (2099/12/32)

---

## CORS (Cross-Origin Resource Sharing)

CORS is enabled for all origins:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

You can make requests directly from web browsers without proxy servers.

---

## HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success - Request completed successfully |
| 400 | Bad Request - Invalid parameters or date out of range |
| 404 | Not Found - Invalid endpoint |
| 500 | Internal Server Error - Server-side error |
| 503 | Service Unavailable - API temporarily unavailable |

---

## Usage Examples

### JavaScript (Fetch)

```javascript
async function convertDate(year, month, day, type = 'ad-to-bs') {
  const url = `https://sudhanparajuli.com.np/api/${type}/${year}/${month}/${day}`;
  
  try {
    const response = await fetch(url);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    
    if (data.success) {
      return data.result;
    } else {
      console.error('Conversion failed:', data.error);
      return null;
    }
  } catch (error) {
    console.error('Request failed:', error);
    return null;
  }
}

// Usage
convertDate(2024, 10, 15, 'ad-to-bs').then(result => {
  console.log(result); // { year: 2081, month: 6, day: 29, type: 'BS' }
});
```

### Python (requests)

```python
import requests

def convert_date(year, month, day, conversion_type='ad-to-bs'):
    url = f"https://sudhanparajuli.com.np/api/{conversion_type}/{year}/{month}/{day}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('success'):
            return data['result']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except requests.Timeout:
        print("Request timed out")
        return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Usage
result = convert_date(2024, 10, 15, 'ad-to-bs')
print(result)  # {'year': 2081, 'month': 6, 'day': 29, 'type': 'BS'}
```

### cURL

```bash
# AD to BS
curl -X GET "https://sudhanparajuli.com.np/api/ad-to-bs/2024/10/15" \
  -H "Accept: application/json"

# BS to AD
curl -X GET "https://sudhanparajuli.com.np/api/bs-to-ad/2081/6/29" \
  -H "Accept: application/json"
```

---

## Best Practices

### 1. Input Validation

Always validate dates before making API calls:

```javascript
function isValidDate(year, month, day) {
  if (month < 1 || month > 12) return false;
  if (day < 1 || day > 32) return false;
  if (year < 1943 || year > 2099) return false;
  return true;
}
```

### 2. Error Handling

Implement comprehensive error handling:

```python
try:
    result = convert_date(2024, 10, 15)
    if result:
        print(f"Converted: {result}")
    else:
        print("Conversion failed")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### 3. Caching

Cache frequently used conversions:

```javascript
const cache = new Map();

async function cachedConvert(year, month, day) {
  const key = `${year}-${month}-${day}`;
  
  if (cache.has(key)) {
    return cache.get(key);
  }
  
  const result = await convertDate(year, month, day);
  if (result) {
    cache.set(key, result);
  }
  
  return result;
}
```

### 4. Timeout Handling

Set appropriate timeouts:

```python
response = requests.get(url, timeout=10)  # 10 second timeout
```

### 5. Retry Logic

Implement retry logic for network failures:

```javascript
async function convertWithRetry(year, month, day, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await convertDate(year, month, day);
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
    }
  }
}
```

---

## Common Use Cases

### 1. Current Date Conversion

```javascript
// Get today's date and convert to BS
const today = new Date();
const result = await convertDate(
  today.getFullYear(),
  today.getMonth() + 1,
  today.getDate(),
  'ad-to-bs'
);
```

### 2. Batch Conversion

```python
dates_to_convert = [
    (2024, 1, 1),
    (2024, 6, 15),
    (2024, 12, 31)
]

results = []
for year, month, day in dates_to_convert:
    result = convert_date(year, month, day, 'ad-to-bs')
    if result:
        results.append(result)
```

### 3. Date Range Validation

```javascript
async function isDateInRange(year, month, day) {
  const result = await convertDate(year, month, day, 'ad-to-bs');
  return result !== null;
}
```

---

## Troubleshooting

### Issue: CORS Error in Browser

**Solution:** The API has CORS enabled. If you're still seeing errors, check:
- Your browser's console for specific error messages
- Network tab to verify the request is being sent
- Try a different browser

### Issue: Invalid Date Error

**Solution:** Verify:
- Date is within supported range (1943-2042 for AD)
- Month is between 1-12
- Day is valid for the given month
- All parameters are integers

### Issue: Slow Response Time

**Solution:**
- Implement caching for frequently used dates
- Use connection pooling for multiple requests
- Consider batch processing if converting many dates

### Issue: Rate Limiting

**Solution:**
- Add delays between requests
- Cache results locally
- For high-volume needs, consider self-hosting a converter

---

## Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check the [FAQ](FAQ.md)
- Visit [Troubleshooting Guide](TROUBLESHOOTING.md)

---

## Changelog

### Version 1.0 (Current)
- Initial API release
- Support for AD ↔ BS conversion
- Date range: 1943-2042 (AD), 2000-2099 (BS)
- CORS enabled
- JSON response format

---

**Last Updated:** October 2024
