from time import sleep
import pprint as pp
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from parsel import Selector

import parameters


_DRIVER_CHROME = None

# Instaniate webdriver using path to chromedriver
_DRIVER_CHROME = webdriver.Chrome(parameters.google_chrome_driver)


def linkedin_login():

    # Go to Linkedin home page
    _DRIVER_CHROME.get(parameters.linkedin_url)
    sleep(1)

    # locate and populate login id text box
    username = _DRIVER_CHROME.find_element_by_name('session_key')
    username.send_keys(parameters.linkedin_login_id)
    sleep(1)

    # locate and populate password text box
    password = _DRIVER_CHROME.find_element_by_name('session_password')
    password.send_keys(parameters.linkedin_password)
    sleep(1)

    # locate submit button and click
    log_in_button = _DRIVER_CHROME.find_element_by_class_name('sign-in-form__submit-btn')
    log_in_button.click()
    sleep(5)

    print('LinkedIn login OK!')


def google_search():

    # Go to Google home page
    _DRIVER_CHROME.get(parameters.google_url)
    sleep(3)

    # Submit query string defined in parameters.py
    query = _DRIVER_CHROME.find_element_by_name('q')
    query.send_keys(parameters.google_query)
    sleep(1)

    query.send_keys(Keys.RETURN)
    sleep(3)

    # Submit query string defined in parameters.py
    linkedin_urls = []

    while len(linkedin_urls) < parameters.google_scrape_limit:

        # Locate DIV web elements that contains the LinkedIn profiles
        results_div = _DRIVER_CHROME.find_elements_by_class_name('r')

        # Extract the url link embedded with the DIV element
        urls = [div.find_element_by_tag_name('a').get_attribute('href') for div in results_div]

        # Calculate scrape limit to determine if more LinkedIn urls are needed
        limit_available = parameters.google_scrape_limit - len(linkedin_urls)

        # If limit is reached, stop scrapping LinkedIn urls
        if limit_available <= 0:
            break
        else:
            # If available limit is more than the number of urls scrapped on current page
            if limit_available > len(urls):

                # Add all urls that were scrapped
                linkedin_urls.extend(urls)

                # Clicked on next page to scrape more urls
                next_page = _DRIVER_CHROME.find_element_by_id('pnnext')
                next_page.click()
                sleep(3)

            else:
                # If available limit is less than the number of urls scrapped on current page
                # i.e. scrape limit has been reached
                linkedin_urls.extend(urls[0:limit_available])
                break

    print(f'Scrapped {len(linkedin_urls)} LinkedIn urls from Google Search using query={parameters.google_query}')
    pp.pprint(linkedin_urls)

    return linkedin_urls


def linkedin_scrape(linkedin_urls):

    profiles = []

    for url in linkedin_urls:

        _DRIVER_CHROME.get(url)
        sleep(5)

        selector = Selector(text=_DRIVER_CHROME.page_source)

        # Use xpath to extract the exact class containing the profile name
        name = selector.xpath('//*[starts-with(@class, "inline")]/text()').extract_first()

        if name:
            name = name.strip()

        # Use xpath to extract the exact class containing the profile position
        position = selector.xpath('//*[starts-with(@class, "mt1")]/text()').extract_first()

        if position:

            position = position.strip()

            position = position[0:position.find(' at ')]

        # Use xpath to extract the exact class containing the profile company
        company = selector.xpath('//*[starts-with(@class, "text-align-left")]/text()').extract_first()

        if company:
            company = company.strip()

        profiles.append([name, position, company, url])
        print(f'{len(profiles)}: {name}, {position}, {company}, {url}')

    return profiles


def save_to_csv(profiles):

    with open(parameters.file_name, 'w', newline='\n', encoding='utf-8') as f:

        # Open CVS file for writing profile information
        writer = csv.writer(f)

        # Write header row
        writer.writerow(['Name', 'Position', 'Company', 'URL'])

        # Write each profile as a row
        for profile in profiles:
            writer.writerow(profile)


linkedin_urls = google_search()

linkedin_login()

profiles = linkedin_scrape(linkedin_urls)

save_to_csv(profiles)

_DRIVER_CHROME.quit()
