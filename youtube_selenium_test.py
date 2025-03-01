from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver (ChromeDriver Required)
driver = webdriver.Chrome()  # Requires chromedriver installed in PATH
driver.get("https://www.youtube.com/")
driver.maximize_window()

# Search
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Latest Tech Review")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Click on First Video
first_video = driver.find_element(By.XPATH, "(//a[@id='video-title'])[1]")
first_video.click()
time.sleep(5)

# Check Video Play
video_element = driver.find_element(By.TAG_NAME, "video")
if video_element.get_attribute("paused") == "false":
    print("Test Passed: Video is playing successfully.")
else:
    print("Test Failed: Video is not playing.")

# Close browser
driver.quit()

""" It is added for demonstration purposes and has NOT been executed. """
