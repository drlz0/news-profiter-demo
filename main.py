import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#url = 'https://www.marketwatch.com/story/microsoft-ramps-up-purchases-of-carbon-removal-credits-with-kenya-deal-opis-222ff61b?mod=dj-newswires'
url = 'https://www.marketwatch.com/story/rivians-stock-is-a-risky-bet-why-this-analyst-now-says-its-one-worth-making-16bbc7b0?mod=home-page'
# Use Selenium to load the page and render dynamic content
options = webdriver.ChromeOptions()
options.headless = True  # Run Chrome in headless mode, so no browser window pops up
driver = webdriver.Chrome(options=options)

driver.get(url)

# Get the page source after dynamic content is loaded
page_source = driver.page_source

# Close the Selenium WebDriver
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the relevant HTML element containing the news content
content = soup.find('div', class_='article__content')
headline = soup.find('h1', class_='article__headline')

# Extract the text from the content
if content:
    title = headline.get_text()
    summary = content.get_text(separator='\n').strip()
    print("Title:", title)
    print("Summary:", summary)
else:
    print("Content not found.")