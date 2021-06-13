# some stock information of taiwan enterprise
###### tags: `README.md`
this is just a exercise of scrapy
but I don't use the framework 'scrapy'
### language:python
### module:BeautifulSoup+selenium
> ### Input:
> The id of stock in taiwan.
> Here, I used ["3711", "2330", "2454", "5287"] as input
> ### Output: 
> Here, I got a **stocks.csv** file, which records
> ![](https://i.imgur.com/g6VSMYn.png)
> the elements in first row are the indice that I want
> 
</br></br></br>
*NOTE*:Please check that **stock.py** is in the default paths of webdriver or you will get an error with:

```
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

```
