# A Simple LinkedIn Scrapper
A simple python script that scrapes LinkedIn profiles from a Google Search.
It performs the scrapping in 5 steps:
1. Searches for relevant LinkedIn profiles using Google Search with the specified query string.
2. Collects the LinkedIn URLs from the Google Search result pages.
3. Performs a LinkedIn login using credentials provided.
4. Using the URLs collected earlier, visit the LinkedIn profile pages and scrape profile information.
5. Stores the scraped profile information in a CSV file.

### Installation

- The dependencies of the python script are listed in requirements.txt
- Included in this repository is a Windows x32 Chrome version 80 executable of 
[ChromeDriver](https://chromedriver.chromium.org/home). ChromeDriver is used by Selenium to automate the scrapping 
workflow. If you're on a Linux/Unix platform or have a different version of Chrome, you'll have to download the 
relevant version [here](https://chromedriver.chromium.org/downloads). 
- To install the scrapper, create a directory/folder. Copy `scrapper.py`, `parameters.py` and your correct version of 
ChromeDriver into the created directory/folder.
- The ChromeDriver executable can be in a separate location. If so, you'll need to set its path in `parameters.py`.

### Configuration

- All configurable parameters can be found in `parameters.py`.
- The LinkedIn parameters that you need to change are the `linkedin_login_id` and `linkedin_password`. 
- These credentials are needed for the automated LinkedIn login by Selenium, that will allow for more profile 
information to be scraped.
- Technically, scrapping can also be done without the login.  However, without the login, the web page source will be 
different. This script only does scrapping from the 'logined' profile page.
- `google_chrome_driver` contains the path to your appropriate ChromeDriver executable.
- `google_query` contains the query string to be used with Google Search to query LinkedIn profiles of interest.
`site:linkedin.com/in/` tells Google Search to look for LinkedIn profiles, `"Head of Data"` is the job position/title 
of the profile, `Singapore` is the location.
- You customized the search by adding more job positions, like "Data Scientists", to the query string, connected by the
`AND` operator. For more information on how to construct Google Search queries, refer to the 
[Search Query Language](https://developers.google.com/issue-tracker/concepts/search-query-language) documentation.
- You can configure the scrapper to search of LinkedIn jobs by using `site:linkedin.com/jobs/` and the job title of 
your interest.
- `google_scrape_limit` limits the number of LinkedIn profiles scraped.
- `file_name` contains the path of the CVS file which the scraped LinkedIn profiles will be saved. If a file of the 
same name exist, it will be overwritten.

### Execution

- Open a terminal/command prompt window, navigate to the directory/folder created to store the scrapper.
- Execute the command line ```python scrapper.py```

### Credits

[Use Selenium & Python to scrape LinkedIn profiles](https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/)
, by David Craven
