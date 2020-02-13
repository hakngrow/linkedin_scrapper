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
- Included in this repository is a Windows x32 Chrome version 80 executable of [ChromeDriver](https://chromedriver.chromium.org/home). ChromeDriver is used by Selenium to automate the scrapping workflow. If you're on a Linux/Unix platform or have a different version of Chrome, you'll have to download the relevant version [here](https://chromedriver.chromium.org/downloads). 
- To install the scrapper, create a directory/folder. Copy scrapper.py, parameters.py and your correct version of ChromeDriver into the created dircetory/folder.
- The ChromeDriver executable can be in a separate location. If so, you'll need to set its path in parameters.py

### Configuration

- Open a terminal/command prompt window, navigate to the just created directory/folder.
- Execute the command line 'python scrapper.py'.

All configurable parameters are set in the parameters.py file.

