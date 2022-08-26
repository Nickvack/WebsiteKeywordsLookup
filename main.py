import time
import pandas as pd
import requests
import re

"""
All of the above are the required packages for this project to work. I will 
use Selenium as the websearch engine, pandas as the file manager and Regex for the keyword lookup. 
"""

# This dictionary will store the results from each website, to later be saved on a CSV file.
output = {
    "Website": [],
    "Results": []
}


# This class will manage everything related to the files (reading, creating and editing)
class FileManager:

    def __init__(self):
        self.keywords = None
        self.websites = None

    # Read both "websites" and "keywords" CSV files
    def read_files(self):
        self.websites = pd.read_csv('websites.csv').stack().explode()
        self.keywords = pd.read_csv('keywords.csv').stack().explode()

    # Saves results in both CSV and XLSX files
    def ouput_file(self, output_dict):
        pd.DataFrame(output_dict).to_excel('Output.xlsx', header=True, index=False)
        pd.DataFrame(output_dict).to_csv('Output.csv', header=True, index=False)


# This class will manage the web search based on the websites and keywords CSV files
class WebSearch:

    # Naming all the variables we'll need for the scraper to work
    def __init__(self):
        self.status = None
        self.req = None
        self.session = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/99.0.4844.74 Safari/537.36 ',
        }
        self.driver = None
        self.service = None
        self.count = 0

    """will go through all the websites and search for each keyword on the "Keywords" File. If the page is not 
    secure it will search it with "http" instead of "https", if it doesn't get resultes like this it will output
    a "Not found" on the results."""

    def open_website(self, website_list, keywords_list, output_dict):

        self.session = requests.session()

        for website in website_list:
            output_dict['Website'].append(website)

            try:

                self.req = self.session.get('https://' + website + '/', headers=self.headers, verify=False)
                self.status = self.req.status_code
                self.count += 1

                # Default time to wait between each page, the number is the amount of seconds between each search.
                time.sleep(3)

                found_word = 'N'

                for word in keywords_list:

                    search = re.search(word, self.req.text)

                    if search is not None:
                        found_word = 'Y'

                    else:
                        pass

                output_dict['Results'].append(found_word)

            # This starts the run again for the website with http instead of https
            except:

                try:
                    self.req = self.session.get('http://' + website + '/', headers=self.headers, verify=False)
                    self.status = self.req.status_code
                    self.count += 1

                    time.sleep(3)

                    found_word = 'N'

                    for word in keywords_list:

                        search = re.search(word, self.req.text)

                        if search is not None:
                            found_word = 'Y'

                        else:
                            pass

                    output_dict['Results'].append(found_word)

                # Page doesn't exist, this is the output
                except:
                    output_dict['Results'].append('Not Found')


# This last part runs the entire script.
file_manager = FileManager()

file_manager.read_files()

web_searcher = WebSearch()

web_searcher.open_website(file_manager.websites, file_manager.keywords, output)

file_manager.ouput_file(output)
