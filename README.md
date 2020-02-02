# mkwrs parser
Quick web scraper to collect all total times from [this page (mkwrs.com)](https://mkwrs.com/mkwii/wrs.php) using [scrapy](https://github.com/scrapy/scrapy).

## How to use it
### Requirements
You need python 2.7/ 3.5 or above and scrapy.
Install scrapy :

    pip install Scrapy
For more info to install scrapy, [check this](https://docs.scrapy.org/en/latest/intro/install.html).



### Run the program
- Download the ZIP file and extract it on your computer.
- Open the command prompt from the root and type :
	- `scrapy crawl mkwrs_parser -s FEED_URI=export/mydata.csv -s FEED_FORMAT=csv` for CSV export
	- `scrapy crawl reddit -s FEED_URI=export/mydata.csv -s FEED_FORMAT=json` for JSON export
- You can now find you exported data in /export/ folder

### Edit the program
You can edit the time period for export and change the output time format in /mkwrs/spiders/mkwrs_parser.py
