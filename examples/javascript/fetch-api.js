/**
 * Nepali Date Converter - Fetch API Examples
 * 
 * These examples show how to use the Nepali Date Converter API
 * with the native Fetch API in JavaScript.
 */

// ============================================
// 1. BASIC AD TO BS CONVERSION
// ============================================

async function convertADToBS(year, month, day) {
  const url = `https://sudhanparajuli.com.np/api/ad-to-bs/${year}/${month}/${day}`;
  
  try {
    const response = await fetch(url);
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
    console.log('Converted date:', result);
    // Use result.year, result.month, result.day
  }
});


// ============================================
// 2. BASIC BS TO AD CONVERSION
// ============================================

async function convertBSToAD(year, month, day) {
  const url = `https://sudhanparajuli.com.np/api/bs-to-ad/${year}/${month}/${day}`;
  
  try {
    const response = await fetch(url);
    const data = await response.json();
    
    if (data.success) {
      console.log(`BS ${year}-${month}-${day} = AD ${data.result.year}-${data.result.month}-${data.result.day}`);
      return data.result;
    } else {
      throw new Error(data.error || 'Conversion failed');
    }
  } catch (error) {
    console.error('Error converting BS to AD:', error);
    return null;
  }
}

// Example usage
convertBSToAD(2081, 6, 29).then(result => {
  if (result) {
    console.log('Converted date:', result);
  }
});


// ============================================
// 3. CONVERT TODAY'S DATE
// ============================================

async function convertTodayToBS() {
  const today = new Date();
  const year = today.getFullYear();
  const month = today.getMonth() + 1; // JavaScript months are 0-indexed
  const day = today.getDate();
  
  console.log(`Converting today's date: ${year}-${month}-${day}`);
  return await convertADToBS(year, month, day);
}

// Example usage
convertTodayToBS().then(bsDate => {
  if (bsDate) {
    console.log(`Today in BS: ${bsDate.year}/${bsDate.month}/${bsDate.day}`);
  }
});


// ============================================
// 4. WITH RETRY LOGIC
// ============================================

async function convertWithRetry(year, month, day, type = 'ad-to-bs', maxRetries = 3) {
  const url = `https://sudhanparajuli.com.np/api/${type}/${year}/${month}/${day}`;
  
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url);
      const data = await response.json();
      
      if (data.success) {
        return data.result;
      } else {
        throw new Error(data.error);
      }
    } catch (error) {
      console.log(`Attempt ${attempt} failed:`, error.message);
      
      if (attempt === maxRetries) {
        console.error('All retry attempts failed');
        return null;
      }
      
      // Wait before retrying (exponential backoff)
      await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
    }
  }
}

// Example usage
convertWithRetry(2024, 10, 15, 'ad-to-bs').then(result => {
  console.log('Result with retry:', result);
});


// ============================================
// 5. WITH CACHING
// ============================================

class DateConverterCache {
  constructor() {
    this.cache = new Map();
  }
  
  generateKey(year, month, day, type) {
    return `${type}-${year}-${month}-${day}`;
  }
  
  async convert(year, month, day, type = 'ad-to-bs') {
    const key = this.generateKey(year, month, day, type);
    
    // Check cache first
    if (this.cache.has(key)) {
      console.log('Returning cached result');
      return this.cache.get(key);
    }
    
    // Make API call
    const url = `https://sudhanparajuli.com.np/api/${type}/${year}/${month}/${day}`;
    
    try {
      const response = await fetch(url);
      const data = await response.json();
      
      if (data.success) {
        // Store in cache
        this.cache.set(key, data.result);
        return data.result;
      } else {
        throw new Error(data.error);
      }
    } catch (error) {
      console.error('Conversion error:', error);
      return null;
    }
  }
  
  clearCache() {
    this.cache.clear();
    console.log('Cache cleared');
  }
  
  getCacheSize() {
    return this.cache.size;
  }
}

// Example usage
const converter = new DateConverterCache();

converter.convert(2024, 10, 15, 'ad-to-bs').then(result => {
  console.log('First call:', result);
});

// This will use cached result
converter.convert(2024, 10, 15, 'ad-to-bs').then(result => {
  console.log('Second call (cached):', result);
});


// ============================================
// 6. BATCH CONVERSION
// ============================================

async function convertBatchDates(dates, type = 'ad-to-bs') {
  const results = [];
  
  for (const date of dates) {
    const { year, month, day } = date;
    const url = `https://sudhanparajuli.com.np/api/${type}/${year}/${month}/${day}`;
    
    try {
      const response = await fetch(url);
      const data = await response.json();
      
      if (data.success) {
        results.push({
          input: date,
          output: data.result,
          success: true
        });
      } else {
        results.push({
          input: date,
          error: data.error,
          success: false
        });
      }
    } catch (error) {
      results.push({
        input: date,
        error: error.message,
        success: false
      });
    }
    
    // Small delay to be respectful to the API
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  
  return results;
}

// Example usage
const datesToConvert = [
  { year: 2024, month: 1, day: 1 },
  { year: 2024, month: 6, day: 15 },
  { year: 2024, month: 12, day: 31 }
];

convertBatchDates(datesToConvert, 'ad-to-bs').then(results => {
  console.log('Batch conversion results:', results);
  
  results.forEach(result => {
    if (result.success) {
      console.log(`✓ ${result.input.year}/${result.input.month}/${result.input.day} → ${result.output.year}/${result.output.month}/${result.output.day}`);
    } else {
      console.log(`✗ ${result.input.year}/${result.input.month}/${result.input.day}: ${result.error}`);
    }
  });
});


// ============================================
// 7. DATE VALIDATION BEFORE CONVERSION
// ============================================

function isValidADDate(year, month, day) {
  // Basic validation
  if (month < 1 || month > 12) return false;
  if (day < 1 || day > 31) return false;
  if (year < 1943 || year > 2042) return false;
  
  // Check days in month
  const daysInMonth = new Date(year, month, 0).getDate();
  if (day > daysInMonth) return false;
  
  return true;
}

function isValidBSDate(year, month, day) {
  // Basic validation for BS dates
  if (month < 1 || month > 12) return false;
  if (day < 1 || day > 32) return false;
  if (year < 2000 || year > 2099) return false;
  
  return true;
}

async function convertWithValidation(year, month, day, type = 'ad-to-bs') {
  // Validate before making API call
  const isValid = type === 'ad-to-bs' 
    ? isValidADDate(year, month, day)
    : isValidBSDate(year, month, day);
  
  if (!isValid) {
    console.error('Invalid date provided');
    return null;
  }
  
  const url = `https://sudhanparajuli.com.np/api/${type}/${year}/${month}/${day}`;
  
  try {
    const response = await fetch(url);
    const data = await response.json();
    
    return data.success ? data.result : null;
  } catch (error) {
    console.error('Conversion error:', error);
    return null;
  }
}

// Example usage
convertWithValidation(2024, 13, 1, 'ad-to-bs').then(result => {
  // Will return null due to invalid month
  console.log('Invalid date result:', result);
});

convertWithValidation(2024, 10, 15, 'ad-to-bs').then(result => {
  // Will return converted date
  console.log('Valid date result:', result);
});


// ============================================
// 8. DOM INTEGRATION EXAMPLE
// ============================================

// HTML:
// <input type="date" id="adDate" />
// <button id="convertBtn">Convert to BS</button>
// <p id="result"></p>

function setupDateConverter() {
  const adDateInput = document.getElementById('adDate');
  const convertBtn = document.getElementById('convertBtn');
  const resultP = document.getElementById('result');
  
  if (!adDateInput || !convertBtn || !resultP) {
    console.error('Required DOM elements not found');
    return;
  }
  
  convertBtn.addEventListener('click', async () => {
    const dateValue = adDateInput.value;
    
    if (!dateValue) {
      resultP.textContent = 'Please select a date';
      return;
    }
    
    const [year, month, day] = dateValue.split('-').map(Number);
    
    resultP.textContent = 'Converting...';
    
    const result = await convertADToBS(year, month, day);
    
    if (result) {
      resultP.textContent = `BS Date: ${result.year}/${result.month}/${result.day}`;
      resultP.style.color = 'green';
    } else {
      resultP.textContent = 'Conversion failed';
      resultP.style.color = 'red';
    }
  });
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', setupDateConverter);
} else {
  setupDateConverter();
}


// ============================================
// 9. PROMISE.ALL FOR PARALLEL CONVERSION
// ============================================

async function convertMultipleDatesParallel(dates, type = 'ad-to-bs') {
  const promises = dates.map(({ year, month, day }) => {
    const url = `https://sudhanparajuli.com.np/api/${type}/${year}/${month}/${day}`;
    return fetch(url).then(res => res.json());
  });
  
  try {
    const results = await Promise.all(promises);
    return results.map((data, index) => ({
      input: dates[index],
      output: data.success ? data.result : null,
      error: data.error || null,
      success: data.success
    }));
  } catch (error) {
    console.error('Batch conversion error:', error);
    return [];
  }
}

// Example usage
const parallelDates = [
  { year: 2024, month: 1, day: 1 },
  { year: 2024, month: 6, day: 15 },
  { year: 2024, month: 12, day: 31 }
];

convertMultipleDatesParallel(parallelDates, 'ad-to-bs').then(results => {
  console.log('Parallel conversion results:', results);
});


// ============================================
// 10. FORMATTING HELPER
// ============================================

function formatNepaliDate(bsDate, format = 'YYYY/MM/DD') {
  if (!bsDate) return '';
  
  const { year, month, day } = bsDate;
  
  // Pad with zeros
  const mm = String(month).padStart(2, '0');
  const dd = String(day).padStart(2, '0');
  
  return format
    .replace('YYYY', year)
    .replace('MM', mm)
    .replace('DD', dd);
}

// Example usage
convertADToBS(2024, 10, 15).then(result => {
  if (result) {
    console.log(formatNepaliDate(result, 'YYYY/MM/DD')); // 2081/06/29
    console.log(formatNepaliDate(result, 'YYYY-MM-DD')); // 2081-06-29
    console.log(formatNepaliDate(result, 'DD/MM/YYYY')); // 29/06/2081
  }
});
