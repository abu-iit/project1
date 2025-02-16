from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Path to chromedriver.exe (or make sure it's in your PATH)
#driver = webdriver.Chrome(executable_path="path/to/chromedriver.exe")

# Open a website
driver.get("https://www.google.com")

# Find the search box
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("LLM-based automation agent")
search_box.send_keys(Keys.RETURN)

# Let the page load
time.sleep(3)

# Close the browser
driver.quit()
