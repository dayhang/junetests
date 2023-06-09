from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Specify the path to the chromedriver executable
driver_path = "chromedriver"

# Create a Chrome webdriver instance
chrome_options = Options()
chrome_options.add_argument("--headless")  # Uncomment this line if you want to run the script without opening a browser window
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Open the Google login page
driver.get("https://accounts.google.com")

# Find the email input field and enter your email address
email_input = driver.find_element_by_xpath('//input[@type="email"]')
email_input.send_keys("your-email@gmail.com")

# Click the Next button
next_button = driver.find_element_by_xpath('//div[@id="identifierNext"]')
next_button.click()

# Find the password input field and enter your password
password_input = driver.find_element_by_xpath('//input[@type="password"]')
password_input.send_keys("your-password")

# Press Enter to submit the form
password_input.send_keys(Keys.ENTER)

# Wait for the page to load (you can adjust the time if needed)
driver.implicitly_wait(10)

# Verify that the login was successful
if "My Account" in driver.title:
    print("Login successful!")
else:
    print("Login failed.")

# Close the webdriver
