from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to the WebDriver
driver_path = 'path/to/chromedriver'  # Update with the actual path to your WebDriver

# Initialize the Selenium WebDriver
driver = webdriver.Chrome(driver_path)

# Define the URL for the production terminal
url = 'https://your-production-terminal-url.com'

try:
    # Navigate to the URL
    driver.get(url)

    # Wait for the page to load and for the login elements to be available
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

    # Locate and fill in login details
    username = driver.find_element(By.ID, 'username')
    password = driver.find_element(By.ID, 'password')

    username.send_keys('your_username')  # Replace with actual username
    password.send_keys('your_password')  # Replace with actual password
    password.send_keys(Keys.RETURN)

    # Wait for the terminal selection page to load and select the Mob API Terminal
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Mob API Terminal'))
    )

    # Click on the Mob API Terminal link
    mob_api_terminal_link = driver.find_element(By.LINK_TEXT, 'Mob API Terminal')
    mob_api_terminal_link.click()

    # Wait for the Ruby Rails console to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'console_input'))
    )

    # Execute the Ruby command in the Rails console
    console_input = driver.find_element(By.ID, 'console_input')
    ruby_command = 'puts "Hello from Ruby console!"'  # Replace with your Ruby code
    console_input.send_keys(ruby_command)
    console_input.send_keys(Keys.RETURN)

    # Optional: Wait for some time to view the output
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()