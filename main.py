import time
import pandas as pd
import requests

"""
All of the above are the required packages for this project to work. I will 
use Selenium as the websearch engine and pandas as the file manager. 
"""


# This class will manage everything related to the files (reading, creating and editing)
class FileManager:

    def __init__(self):
        self.keywords = None
        self.websites = None

    def read_files(self):
        self.websites = pd.read_csv('websites.csv').stack().explode()
        self.keywords = pd.read_csv('keywords.csv').stack().explode()


# This class will manage the web search based on the websites and keywords files
class WebSearch:

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

    def open_website(self, website_list, keywords_list):

        self.session = requests.session()

        # self.service = ChromeService(executable_path=ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=self.service)

        # path = 'chromedriver.exe'
        # self.driver = webdriver.Chrome(path)

        for website in website_list[:100]:

            # self.driver.get('https://' + website)

            try:

                self.req = self.session.get('https://' + website + '/', headers=self.headers, verify=False)
                self.status = self.req.status_code
                self.count += 1

                time.sleep(3)

                print('https://' + website + '/')
                print(self.status)
                print(self.count)

            except:

                self.req = self.session.get('http://' + website + '/', headers=self.headers, verify=False)
                self.status = self.req.status_code
                self.count += 1

                time.sleep(3)

                print('http://' + website + '/')
                print(self.status)
                print(self.count)

        self.driver


x = FileManager()

x.read_files()

y = WebSearch()

y.open_website(x.websites, x.keywords)

y
