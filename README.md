# some stock information of taiwan enterprises
###### tags: `beautifulSoup`,`selenium`,`python`
this is just a exercise of scrapy
but I don't use the framework 'scrapy'
### language:python
### module:BeautifulSoup+selenium
> ### goal: 
> enter https://tw.stock.yahoo.com/ (yahoo stock)
> and scrapy some enterprises stock information(eg:climax, Opening Price...etc) in Taiwan(See the Input below).
> ### Input:
> The id of stock in taiwan.
> Here, I used ["3711", "2330", "2454", "5287"] as input
> ### Output: 
> You will get a csv file.
> The **1st row** is the stock information I need.
> The **2nd row** is the corresponding values of the **first row** of enterprise1.
> The **3rd row** is the corresponding values of the **first row** of enterprise2,
> and so on.
> Here, I got a **stocks.csv** file, which records
> ![](https://i.imgur.com/g6VSMYn.png)
> the elements in first row are the indice that I want
> 
</br></br></br>
*NOTE*:Please check that **stock.py** is in the default paths of webdriver or you will get an error with:

```
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

```





