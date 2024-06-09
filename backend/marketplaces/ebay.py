# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as webdriver


import time

class Ebay():
    def __init__(self):
        self.username = "snip7171"
        self.password = "snapsell123!"
        
    def upload_item(self, url, item, description):
        pass
    
    def upload_item_selenium(self, url, item, description):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--use_subprocess")
        chrome_options.add_argument("--disable-popup-blocking")
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        try:
            # Open eBay login page
            driver.get("https://www.ebay.com/signin")
            time.sleep(1)
            print("here1")
            username = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "userid"))
            )
            print("here2")
            # Log in to eBay
            # username = driver.find_element(By.ID, "userid")
            # username.send_keys(self.username)
            username.send_keys(self.username)
            driver.find_element(By.ID, "signin-continue-btn").click()
            time.sleep(5)  # Wait for password field to appear

            password = driver.find_element(By.ID, "pass")
            password.send_keys(self.password)
            driver.find_element(By.ID, "sgnBt").click()
            time.sleep(15)  # Wait for login to complete

            # Navigate to the create listing page
            driver.get("https://www.ebay.com/sl/sell")

            # Wait for the page to load
            time.sleep(5)

            # Start creating a listing
            # Fill in the title
            title = driver.find_element(By.NAME, "title")
            title.send_keys("Sample Item")

            # Fill in the category
            category = driver.find_element(By.XPATH, "//button[contains(text(),'Select a category')]")
            category.click()
            time.sleep(2)
            category_input = driver.find_element(By.XPATH, "//input[@placeholder='Search categories']")
            category_input.send_keys("Electronics")
            category_input.send_keys(Keys.RETURN)
            time.sleep(2)
            first_category = driver.find_element(By.XPATH, "//div[@role='option'][1]")
            first_category.click()

            # Fill in other details like condition, price, and description
            time.sleep(2)
            condition = driver.find_element(By.XPATH, "//button[contains(text(),'Condition')]")
            condition.click()
            new_condition = driver.find_element(By.XPATH, "//button[contains(text(),'New')]")
            new_condition.click()

            price = driver.find_element(By.NAME, "price")
            price.send_keys("10.00")

            description = driver.find_element(By.XPATH, "//textarea[@name='description']")
            description.send_keys("This is a sample item description.")

            # Add a photo
            photo_upload = driver.find_element(By.XPATH, "//input[@type='file']")
            photo_upload.send_keys("/path/to/your/image.jpg")
            time.sleep(5)  # Wait for image to upload

            # Submit the form to create the listing
            submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'List it')]")
            submit_button.click()

            print("Listing created successfully!")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the WebDriver
            driver.quit()
