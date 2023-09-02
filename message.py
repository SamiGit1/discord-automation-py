import time
from selenium import webdriver #Selenium lets you access webpages for automation purposes.
from selenium.webdriver.common.by import By #Importing By so I can use it to access the input box
from selenium.webdriver.common.keys import Keys #importing keys to pass the content into the input box



email = "email here"
password = "password here"

#Put the channel id
id = "id here"
message = "Content here"

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Navigate to the Discord login page
driver.get("https://discord.com/login")

# Wait for the page to load
time.sleep(5)


driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(email)
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)

# Click the login button
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(10)

# Navigating to the chat
driver.get(f"https://discord.com/channels/@me/{id}")

# Wait for the chat to load
time.sleep(5)
input_selector= "#app-mount > div.appAsidePanelWrapper-ev4hlp > div.notAppAsidePanel-3yzkgB > div.app-3xd6d0 > div > div.layers-OrUESM.layers-1YQhyW > div > div > div > div > div.chat-2ZfjoI > div.content-1jQy2l > main > form > div > div > div > div.textArea-2CLwUE.textAreaSlate-9-y-k2.slateContainer-3x9zil > div > div.markup-eYLPri.editor-H2NA06.slateTextArea-27tjG0.fontSize16Padding-XoMpjI"

# Find the chat input field and send the message
input_box = driver.find_element(By.CSS_SELECTOR, input_selector)
input_box.send_keys(message)
input_box.send_keys(Keys.ENTER)


time.sleep(5)
driver.quit()
