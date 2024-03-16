from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import os


# Function to download the PDF file
def download_pdf(pdf_url, download_path):
    response = requests.get(pdf_url)
    with open(download_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded file: {download_path}")


# Setup Chrome WebDriver
service = Service(executable_path="/usr/local/bin/chromedriver")  # Update this path
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the website
    driver.get("https://mib.gov.in/documents/online-reoprts")

    # Find all PDF links on the page
    pdf_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")

    if pdf_links:
        # Assuming the first PDF link is the latest
        latest_pdf_url = pdf_links[0].get_attribute('href')
        latest_pdf_filename = latest_pdf_url.split('/')[-1]

        # Download the latest PDF file
        download_pdf(latest_pdf_url, latest_pdf_filename)
    else:
        print("No PDF files found.")
finally:
    driver.quit()


