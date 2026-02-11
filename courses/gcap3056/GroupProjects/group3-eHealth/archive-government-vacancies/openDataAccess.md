# Open Data Access Report: Government Job Vacancies API

**Date:** January 29, 2026  
**Subject:** Analysis of DATA.GOV.HK API for Government Job Vacancies

---

## 1. Executive Summary

Yes, government job openings are available through API access on DATA.GOV.HK. The Civil Service Bureau provides a comprehensive JSON API that is updated **hourly** with all current government vacancy advertisements. This report documents the API structure, available data fields, and potential use cases.

---

## 2. Data Source Overview

### 2.1 Dataset Information

| Attribute | Value |
|-----------|-------|
| **Dataset Name** | Data on Recruitment Advertisements for Government Vacancies |
| **Provider** | Civil Service Bureau |
| **Portal** | DATA.GOV.HK |
| **Category** | Miscellaneous |
| **Update Frequency** | Hourly |
| **Authentication Required** | No |
| **Cost** | Free |

### 2.2 Portal URL

**Main Dataset Page:**  
https://data.gov.hk/en-data/dataset/hk-csb-csb-gov-vacancies

---

## 3. API Endpoints

### 3.1 Available Data Resources

| Language | API Endpoint | Format |
|----------|--------------|--------|
| **English** | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json | JSON |
| **Traditional Chinese** | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-tc.json | JSON |
| **Simplified Chinese** | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-sc.json | JSON |

### 3.2 API Properties

| Property | Value |
|----------|-------|
| Response Format | JSON |
| Response Encoding | UTF-8 |
| Authentication | Not required |
| Rate Limiting | Not documented (appears unrestricted) |
| CORS | Enabled (can be called from browser) |

---

## 4. Data Structure

### 4.1 Top-Level Structure

```json
{
  "common": [
    {
      "vacancies": [ /* Array of job vacancy objects */ ]
    },
    {
      "timestamp": "2026-01-29 15:00:00"  // JSON creation time (HK timezone)
    },
    {
      "language": "en"  // en | tc | sc
    }
  ]
}
```

### 4.2 Vacancy Object Fields

The following table lists all 37 data fields available for each vacancy:

| # | Field Name | Type | Description |
|---|------------|------|-------------|
| 1 | `jobid` | Number | Unique system identifier |
| 2 | `deptnamejve` | String | Recruiting department/bureau |
| 3 | `division` | String | Division/Section/Unit |
| 4 | `jobnature` | String | Job classification category |
| 5 | `jobname` | String | Job title |
| 6 | `ernotes` | String | Supplementary notes on entry requirements |
| 7 | `depturl` | String | Department website URL |
| 8 | `enqaddr` | String | Enquiry office address |
| 9 | `iscs` | Boolean | Is civil service vacancy (Y/N) |
| 10 | `appnotes` | String | General application notes |
| 11 | `benefit` | String | Fringe benefits |
| 12 | `enqtel` | String | Enquiry telephone number |
| 13 | `expfrom` | Number | Min. years of experience required |
| 14 | `expto` | Number | Max. years of experience (null = no ceiling) |
| 15 | `pubdate` | Date | Advertising date (yyyy-MM-dd) |
| 16 | `enddate` | Datetime | Application closing date |
| 17 | `appmethod` | String | How to apply |
| 18 | `appterm` | String | Terms of appointment |
| 19 | `attachfilename` | String | Attachment filename (if any) |
| 20 | `duties` | String | Job duties description |
| 21 | `isgf340` | Boolean | Can apply via G.F.340 system (Y/N) |
| 22 | `newspaper` | String | Newspapers advertised and dates |
| 23 | `entreq` | String | Entry requirements |
| 24 | `entrypay` | String | Salary range description |
| 25 | `ccym` | String | Currency for monthly salary (HKD/RMB/USD/EUR) |
| 26 | `ccyh` | String | Currency for hourly salary |
| 27 | `ccyd` | String | Currency for daily salary |
| 28 | `minpaym` | Number | Monthly salary (numeric) |
| 29 | `minpayh` | Number | Hourly salary (numeric) |
| 30 | `minpayd` | Number | Daily salary (numeric) |
| 31 | `isonlineform` | Boolean | Uses departmental online form (Y/N) |
| 32 | `onlineformurl` | String | Departmental online form URL |
| 33 | `isapplyemail` | Boolean | Can apply via email (Y/N) |
| 34 | `applyemail` | String | Application email address |
| 35 | `issubmitdocument` | Boolean | Can submit attachments online (Y/N) |
| 36 | `submitdocumentlink` | String | Link/email for document submission |
| 37 | `academic` | Array | Academic requirements list |

### 4.3 Job Nature Categories

The `jobnature` field can contain one of the following values:

| Code | Category |
|------|----------|
| (a) | Accounting, Finance, Audit and Taxation |
| (b) | Administrative, Executive and General Support Services |
| (c) | Agriculture, Fisheries and Food |
| (d) | Commerce and Investment |
| (e) | Communications and Technology |
| (f) | Culture, Leisure and Sports |
| (g) | Disciplined |
| (h) | Education and Training |
| (i) | Engineering |
| (j) | Environment and Natural Conservation |
| (k) | Healthcare and Hygienic Services |
| (l) | Housing and Estate Management |
| (m) | Labour and Social Services |
| (n) | Legal and Judicial Services |
| (o) | Logistics and Transport |
| (p) | Observatory, Aviation and Marine |
| (q) | Planning, Land and Works |
| (r) | Public Relations and Media |
| (s) | Research and Statistics |
| (t) | Others |

---

## 5. Sample Data

### 5.1 Example Vacancy Object

```json
{
  "jobid": 12345,
  "jobname": "Medical and Health Officer",
  "deptnamejve": "Department of Health",
  "division": "Primary Healthcare Office",
  "jobnature": "Healthcare and Hygienic Services",
  "iscs": "N",
  "pubdate": "2026-01-15",
  "enddate": "2099-12-31 23:59:00",
  "entreq": "Candidates should possess a medical qualification registrable in Hong Kong...",
  "duties": "Successful candidate will be deployed to perform licensing and regulatory function...",
  "ccym": "HKD$",
  "minpaym": 85000,
  "appmethod": "Apply online through the G.F. 340 Online Application System...",
  "isgf340": "Y",
  "academic": ["Professional Qualification"],
  "enqtel": "2961 8609",
  "enqaddr": "Room 1807, 18/F, Wu Chung House, 213 Queen's Road East, Wan Chai",
  "benefit": "Paid leave, medical and dental benefits, housing assistance"
}
```

**Note:** When `enddate` is `2099-12-31 23:59:00`, it means applications are accepted year-round until further notice.

### 5.2 Attachment Download URL Pattern

For vacancies with attachments:
```
https://csboa.csb.gov.hk/csboa/jve/JVE_003_download.action?jobid=[jobid]
```

---

## 6. Historical Data Access

### 6.1 Historical Data API

DATA.GOV.HK provides access to historical versions of the data:

**API Specification:**  
https://data.gov.hk/en/help/api-spec#api-for-retrieval-of-historical-data

**Features:**
- Download previous versions of vacancy data
- Specify date ranges
- Download monthly/daily archives
- Add to download queue for batch processing

---

## 7. Usage Examples

### 7.1 Fetch All Current Vacancies (JavaScript)

```javascript
async function fetchGovVacancies() {
  const response = await fetch(
    'https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json'
  );
  const data = await response.json();
  
  const vacancies = data.common[0].vacancies;
  const timestamp = data.common[1].timestamp;
  
  console.log(`Found ${vacancies.length} vacancies`);
  console.log(`Data updated: ${timestamp}`);
  
  return vacancies;
}
```

### 7.2 Filter by Department (JavaScript)

```javascript
function filterByDepartment(vacancies, deptName) {
  return vacancies.filter(v => 
    v.deptnamejve.toLowerCase().includes(deptName.toLowerCase())
  );
}

// Example: Find all Health Department vacancies
const healthJobs = filterByDepartment(vacancies, 'Health');
```

### 7.3 Filter by Salary Range (JavaScript)

```javascript
function filterBySalary(vacancies, minSalary, maxSalary) {
  return vacancies.filter(v => {
    const salary = v.minpaym;
    if (!salary) return false;
    return salary >= minSalary && salary <= maxSalary;
  });
}

// Example: Find jobs with monthly salary 30,000 - 50,000 HKD
const midRangeJobs = filterBySalary(vacancies, 30000, 50000);
```

### 7.4 Python Example

```python
import requests
import json

def fetch_gov_vacancies():
    url = 'https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json'
    response = requests.get(url)
    data = response.json()
    
    vacancies = data['common'][0]['vacancies']
    timestamp = data['common'][1]['timestamp']
    
    print(f"Found {len(vacancies)} vacancies")
    print(f"Data updated: {timestamp}")
    
    return vacancies

# Filter civil service vs non-civil service
def separate_by_type(vacancies):
    civil_service = [v for v in vacancies if v['iscs'] == 'Y']
    non_civil_service = [v for v in vacancies if v['iscs'] == 'N']
    return civil_service, non_civil_service
```

---

## 8. Potential Applications

### 8.1 For Students/Developers

| Application | Description |
|-------------|-------------|
| **Job Alert Bot** | Telegram/Discord bot that notifies when matching jobs are posted |
| **Salary Analysis** | Dashboard showing salary trends across departments |
| **Career Explorer** | Tool to explore career paths within government |
| **Accessibility Analyzer** | Check job requirements accessibility for different demographics |

### 8.2 For Researchers

| Application | Description |
|-------------|-------------|
| **Hiring Trends** | Analyze which departments are hiring most |
| **Qualification Analysis** | Study academic requirements across job types |
| **Salary Benchmarking** | Compare government vs private sector pay |
| **Historical Tracking** | Track vacancy patterns over time |

### 8.3 Improvement Ideas for Official App

| Feature | How API Enables It |
|---------|-------------------|
| Better Search | Use structured data for faceted search |
| Salary Filters | Filter using `minpaym`, `minpayh`, `minpayd` fields |
| Department Browse | Group by `deptnamejve` field |
| Category Browse | Group by `jobnature` field |
| Experience Filter | Use `expfrom` and `expto` fields |
| Real-time Updates | Poll API hourly for new vacancies |

---

## 9. Limitations & Considerations

### 9.1 Technical Limitations

| Limitation | Details |
|------------|---------|
| No Pagination | Entire dataset returned in single response |
| No Query Parameters | Cannot filter server-side; must download all data |
| No WebSocket | No real-time push notifications via API |
| Update Delay | Hourly updates (not real-time) |

### 9.2 Data Limitations

| Limitation | Details |
|------------|---------|
| No Application Status | Cannot track applications via API |
| No User Profiles | API is read-only vacancy data |
| No Saved Searches | Must implement client-side |
| Text-Heavy | Many fields contain long text (not structured) |

---

## 10. Documentation & Support

### 10.1 Official Documentation

| Resource | URL |
|----------|-----|
| Data Dictionary (PDF) | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-data-dictionary-en.pdf |
| DATA.GOV.HK API Spec | https://data.gov.hk/en/help/api-spec |
| Dataset Page | https://data.gov.hk/en-data/dataset/hk-csb-csb-gov-vacancies |

### 10.2 Contact Information

| Contact | Value |
|---------|-------|
| Maintainer | Civil Service Bureau |
| Phone | 2810 2639 |
| Email | csbjoa@csb.gov.hk |

---

## 11. Conclusion

The DATA.GOV.HK open data portal provides **excellent API access** to government job vacancies. The data is:

- **Comprehensive** - 37 data fields per vacancy
- **Current** - Updated hourly
- **Accessible** - No authentication required
- **Well-documented** - Official data dictionary available
- **Multi-lingual** - English, Traditional Chinese, Simplified Chinese

This API could be leveraged to build improved job search experiences, analysis tools, or integrations that address many of the limitations identified in the current Government Vacancies mobile app.

---

## Appendix: Quick Reference

### API Endpoints

```
# English
GET https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json

# Traditional Chinese
GET https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-tc.json

# Simplified Chinese
GET https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-sc.json
```

### Response Structure

```
data.common[0].vacancies  → Array of job objects
data.common[1].timestamp  → Last update time
data.common[2].language   → Data language (en/tc/sc)
```

---

*Report prepared by exploring DATA.GOV.HK open data portal and testing API endpoints*
