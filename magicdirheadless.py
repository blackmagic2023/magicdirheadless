import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ANSI escape codes for colors
class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

def check_directory_exists(url, directory, pbar):
    full_url = url + "/" + directory
    response = requests.head(full_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        if directory in soup.get_text():
            print(colors.GREEN + f"Directory '{directory}' exists at {full_url}" + colors.END)
            pbar.update(1)
            return

    # Use headless browser for additional verification
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(full_url)
    if driver.current_url != full_url:
        print(colors.RED + f"Directory '{directory}' does not exist at {full_url}" + colors.END)
        pbar.update(1)
    else:
        print(colors.GREEN + f"Directory '{directory}' exists at {full_url}" + colors.END)
        pbar.update(1)
    driver.quit()

def main():
    website = input("Enter the website URL: ")
    directory_file = input("Enter the path to the txt file containing list of directories: ")

    try:
        with open(directory_file, 'r') as file:
            directories = file.read().splitlines()
    except FileNotFoundError:
        print("Error: Directory file not found.")
        return

    num_threads = int(input("Enter the number of threads to use (default is system specs): "))

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        with tqdm(total=len(directories), desc="Scanning directories") as pbar:
            for directory in directories:
                executor.submit(check_directory_exists, website, directory, pbar)

if __name__ == "__main__":
    main()
