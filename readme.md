<!-- Project Description -->
<h1>Project Description</h1>

<p>This project will search for Keywords from each URL on a CSV file and Output a CSV file
with either "Y" if any of the Keywords are in the URL, "N" if none of the keywords are on 
the page and "Not found" if the page is no longer available. This process will take between
3 and 5 seconds per URL on the list.</p>

<h3>Requirements:</h3>

<p>For this project, only two files are required:</p>
<li>websites.csv</li>
<li>keywords.csv</li>

<p>Both files must be located in the same folder as "main.py". Once you have saved both files all you need
to do is run the "main.py" script.</p>

<h4>Libraries used: </h4>

<p>For this project the following libraries were used: </p>

- [Requests][requests]: This library will crawl through the pages on the website.csv file
- [Pandas][pandas_url]: This library is used to read, create and edit files
- [OpenPyxl][openpyxl]: This is an interpreter for XLSX files

<!-- MARKDOWN LINKS -->
[pandas_url]:[https://pandas.pydata.org/docs/index.html]
[requests]:[https://pypi.org/project/requests/]
[openpyxl]:[https://openpyxl.readthedocs.io/en/stable/]