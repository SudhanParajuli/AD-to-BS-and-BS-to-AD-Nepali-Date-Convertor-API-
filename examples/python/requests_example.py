"""
Nepali Date Converter - Python Examples using requests library

This module provides various examples of using the Nepali Date Converter API
with the Python requests library.

Requirements:
    pip install requests
"""

import requests
import json
from datetime import datetime
from typing import Optional, Dict, List, Tuple
import time


# ============================================
# 1. BASIC AD TO BS CONVERSION
# ============================================

def convert_ad_to_bs(year: int, month: int, day: int) -> Optional[Dict]:
    """
    Convert Gregorian (AD) date to Bikram Sambat (BS) date.
    
    Args:
        year: AD year (1943-2042)
        month: Month (1-12)
        day: Day (1-31)
    
    Returns:
        Dictionary with converted date or None if failed
    """
    url = f"https://sudhanparajuli.com.np/api/ad-to-bs/{year}/{month}/{day}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        data = response.json()
        
        if data.get('success'):
            bs_date = data['result']
            print(f"AD {year}-{month}-{day} = BS {bs_date['year']}-{bs_date['month']}-{bs_date['day']}")
            return bs_date
        else:
            print(f"Error: {data.get('error', 'Unknown error')}")
            return None
            
    except requests.Timeout:
        print("Request timed out")
        return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


# ============================================
# 2. BASIC BS TO AD CONVERSION
# ============================================

def convert_bs_to_ad(year: int, month: int, day: int) -> Optional[Dict]:
    """
    Convert Bikram Sambat (BS) date to Gregorian (AD) date.
    
    Args:
        year: BS year (2000-2099)
        month: Month (1-12)
        day: Day (1-32)
    
    Returns:
        Dictionary with converted date or None if failed
    """
    url = f"https://sudhanparajuli.com.np/api/bs-to-ad/{year}/{month}/{day}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('success'):
            ad_date = data['result']
            print(f"BS {year}-{month}-{day} = AD {ad_date['year']}-{ad_date['month']}-{ad_date['day']}")
            return ad_date
        else:
            print(f"Error: {data.get('error', 'Unknown error')}")
            return None
            
    except requests.Timeout:
        print("Request timed out")
        return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


# ============================================
# 3. CONVERT TODAY'S DATE
# ============================================

def convert_today_to_bs() -> Optional[Dict]:
    """Convert today's date from AD to BS."""
    today = datetime.now()
    print(f"Converting today's date: {today.strftime('%Y-%m-%d')}")
    
    return convert_ad_to_bs(today.year, today.month, today.day)


# ============================================
# 4. WITH RETRY LOGIC
# ============================================

def convert_with_retry(
    year: int, 
    month: int, 
    day: int, 
    conversion_type: str = 'ad-to-bs',
    max_retries: int = 3
) -> Optional[Dict]:
    """
    Convert date with automatic retry on failure.
    
    Args:
        year: Year value
        month: Month value
        day: Day value
        conversion_type: Either 'ad-to-bs' or 'bs-to-ad'
        max_retries: Maximum number of retry attempts
    
    Returns:
        Converted date dictionary or None
    """
    url = f"https://sudhanparajuli.com.np/api/{conversion_type}/{year}/{month}/{day}"
    
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('success'):
                return data['result']
            else:
                print(f"Attempt {attempt}: {data.get('error')}")
                
        except requests.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            
            if attempt < max_retries:
                # Exponential backoff
                wait_time = 2 ** attempt
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("All retry attempts failed")
                return None
    
    return None


# ============================================
# 5. WITH CACHING
# ============================================

class DateConverterCache:
    """Date converter with built-in caching."""
    
    def __init__(self):
        self.cache = {}
    
    def _generate_key(self, year: int, month: int, day: int, conv_type: str) -> str:
        """Generate cache key."""
        return f"{conv_type}-{year}-{month}-{day}"
    
    def convert(
        self, 
        year: int, 
        month: int, 
        day: int, 
        conversion_type: str = 'ad-to-bs'
    ) -> Optional[Dict]:
        """
        Convert date with caching.
        
        Args:
            year: Year value
            month: Month value
            day: Day value
            conversion_type: Either 'ad-to-bs' or 'bs-to-ad'
        
        Returns:
            Converted date dictionary or None
        """
        key = self._generate_key(year, month, day, conversion_type)
        
        # Check cache first
        if key in self.cache:
            print("Returning cached result")
            return self.cache[key]
        
        # Make API call
        url = f"https://sudhanparajuli.com.np/api/{conversion_type}/{year}/{month}/{day}"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('success'):
                # Store in cache
                self.cache[key] = data['result']
                return data['result']
            else:
                print(f"Error: {data.get('error')}")
                return None
                
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None
    
    def clear_cache(self):
        """Clear the cache."""
        self.cache.clear()
        print("Cache cleared")
    
    def get_cache_size(self) -> int:
        """Get number of cached items."""
        return len(self.cache)


# ============================================
# 6. BATCH CONVERSION
# ============================================

def convert_batch_dates(
    dates: List[Tuple[int, int, int]], 
    conversion_type: str = 'ad-to-bs',
    delay: float = 0.1
) -> List[Dict]:
    """
    Convert multiple dates in batch.
    
    Args:
        dates: List of (year, month, day) tuples
        conversion_type: Either 'ad-to-bs' or 'bs-to-ad'
        delay: Delay between requests in seconds
    
    Returns:
        List of result dictionaries
    """
    results = []
    
    for year, month, day in dates:
        url = f"https://sudhanparajuli.com.np/api/{conversion_type}/{year}/{month}/{day}"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('success'):
                results.append({
                    'input': {'year': year, 'month': month, 'day': day},
                    'output': data['result'],
                    'success': True
                })
            else:
                results.append({
                    'input': {'year': year, 'month': month, 'day': day},
                    'error': data.get('error'),
                    'success': False
                })
                
        except requests.RequestException as e:
            results.append({
                'input': {'year': year, 'month': month, 'day': day},
                'error': str(e),
                'success': False
            })
        
        # Be respectful to the API
        time.sleep(delay)
    
    return results


# ============================================
# 7. DATE VALIDATION
# ============================================

def is_valid_ad_date(year: int, month: int, day: int) -> bool:
    """Validate AD date before API call."""
    if not (1943 <= year <= 2042):
        return False
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31):
        return False
    
    # Check if date is valid using datetime
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False


def is_valid_bs_date(year: int, month: int, day: int) -> bool:
    """Validate BS date before API call."""
    if not (2000 <= year <= 2099):
        return False
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 32):
        return False
    
    return True


def convert_with_validation(
    year: int, 
    month: int, 
    day: int, 
    conversion_type: str = 'ad-to-bs'
) -> Optional[Dict]:
    """Convert date with input validation."""
    # Validate before making API call
    is_valid = (is_valid_ad_date(year, month, day) if conversion_type == 'ad-to-bs' 
                else is_valid_bs_date(year, month, day))
    
    if not is_valid:
        print(f"Invalid date: {year}-{month}-{day}")
        return None
    
    url = f"https://sudhanparajuli.com.np/api/{conversion_type}/{year}/{month}/{day}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        return data['result'] if data.get('success') else None
        
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


# ============================================
# 8. SESSION-BASED REQUESTS
# ============================================

class DateConverter:
    """Date converter using persistent session."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Nepali-Date-Converter-Python/1.0'
        })
        self.base_url = "https://sudhanparajuli.com.np/api"
    
    def convert(
        self, 
        year: int, 
        month: int, 
        day: int, 
        conversion_type: str = 'ad-to-bs'
    ) -> Optional[Dict]:
        """Convert date using session."""
        url = f"{self.base_url}/{conversion_type}/{year}/{month}/{day}"
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return data['result'] if data.get('success') else None
            
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None
    
    def close(self):
        """Close the session."""
        self.session.close()


# ============================================
# 9. FORMATTING HELPERS
# ============================================

def format_nepali_date(date_dict: Dict, format_str: str = 'YYYY/MM/DD') -> str:
    """
    Format Nepali date dictionary.
    
    Args:
        date_dict: Dictionary with year, month, day keys
        format_str: Format string (YYYY, MM, DD)
    
    Returns:
        Formatted date string
    """
    if not date_dict:
        return ''
    
    year = str(date_dict['year'])
    month = str(date_dict['month']).zfill(2)
    day = str(date_dict['day']).zfill(2)
    
    return (format_str
            .replace('YYYY', year)
            .replace('MM', month)
            .replace('DD', day))


def format_ad_date(date_dict: Dict, format_str: str = 'YYYY-MM-DD') -> str:
    """Format AD date dictionary."""
    return format_nepali_date(date_dict, format_str)


# ============================================
# 10. ERROR HANDLING WRAPPER
# ============================================

class ConversionError(Exception):
    """Custom exception for conversion errors."""
    pass


def safe_convert(
    year: int, 
    month: int, 
    day: int, 
    conversion_type: str = 'ad-to-bs'
) -> Dict:
    """
    Convert date with comprehensive error handling.
    
    Raises:
        ConversionError: If conversion fails
    """
    url = f"https://sudhanparajuli.com.np/api/{conversion_type}/{year}/{month}/{day}"
    
    try:
        response = requests.get(url, timeout=10)
        
        # Check HTTP status
        if response.status_code == 400:
            raise ConversionError("Invalid date provided")
        elif response.status_code == 404:
            raise ConversionError("API endpoint not found")
        elif response.status_code >= 500:
            raise ConversionError("Server error occurred")
        
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('success'):
            return data['result']
        else:
            raise ConversionError(data.get('error', 'Unknown error'))
            
    except requests.Timeout:
        raise ConversionError("Request timed out")
    except requests.ConnectionError:
        raise ConversionError("Connection error")
    except requests.RequestException as e:
        raise ConversionError(f"Request failed: {e}")


# ============================================
# USAGE EXAMPLES
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("Nepali Date Converter - Python Examples")
    print("=" * 60)
    
    # Example 1: Basic conversion
    print("\n1. Basic AD to BS Conversion:")
    result = convert_ad_to_bs(2024, 10, 15)
    
    # Example 2: BS to AD
    print("\n2. Basic BS to AD Conversion:")
    result = convert_bs_to_ad(2081, 6, 29)
    
    # Example 3: Convert today's date
    print("\n3. Convert Today's Date:")
    today_bs = convert_today_to_bs()
    
    # Example 4: With retry
    print("\n4. Conversion with Retry:")
    result = convert_with_retry(2024, 10, 15, 'ad-to-bs', max_retries=3)
    
    # Example 5: Using cache
    print("\n5. Using Cache:")
    converter = DateConverterCache()
    result1 = converter.convert(2024, 10, 15, 'ad-to-bs')  # API call
    result2 = converter.convert(2024, 10, 15, 'ad-to-bs')  # Cached
    print(f"Cache size: {converter.get_cache_size()}")
    
    # Example 6: Batch conversion
    print("\n6. Batch Conversion:")
    dates_to_convert = [
        (2024, 1, 1),
        (2024, 6, 15),
        (2024, 12, 31)
    ]
    batch_results = convert_batch_dates(dates_to_convert, 'ad-to-bs')
    
    for result in batch_results:
        if result['success']:
            inp = result['input']
            out = result['output']
            print(f"✓ {inp['year']}/{inp['month']}/{inp['day']} → "
                  f"{out['year']}/{out['month']}/{out['day']}")
        else:
            inp = result['input']
            print(f"✗ {inp['year']}/{inp['month']}/{inp['day']}: {result['error']}")
    
    # Example 7: With validation
    print("\n7. With Validation:")
    valid_result = convert_with_validation(2024, 10, 15, 'ad-to-bs')
    invalid_result = convert_with_validation(2024, 13, 1, 'ad-to-bs')
    
    # Example 8: Using session
    print("\n8. Using Session:")
    converter = DateConverter()
    result = converter.convert(2024, 10, 15, 'ad-to-bs')
    converter.close()
    
    # Example 9: Formatting
    print("\n9. Date Formatting:")
    bs_date = convert_ad_to_bs(2024, 10, 15)
    if bs_date:
        print(f"Format 1: {format_nepali_date(bs_date, 'YYYY/MM/DD')}")
        print(f"Format 2: {format_nepali_date(bs_date, 'DD-MM-YYYY')}")
        print(f"Format 3: {format_nepali_date(bs_date, 'YYYY.MM.DD')}")
    
    # Example 10: Error handling
    print("\n10. Safe Conversion with Error Handling:")
    try:
        result = safe_convert(2024, 10, 15, 'ad-to-bs')
        print(f"Success: {result}")
    except ConversionError as e:
        print(f"Conversion failed: {e}")
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
