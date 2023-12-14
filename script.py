import concurrent.futures
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Constants for the script
MAX_RETRIES = 3
CHUNKS = 10
TIMEOUT = 3
START_RANGE = 600
END_RANGE = 750
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html',
    'Connection': 'keep-alive',
}
ALLOW_REDIRECTS = False

# Function to fetch the content of a webpage
def fetch_page_content(url):
    try:
        response = requests.get(url, timeout=TIMEOUT, headers=HEADERS, allow_redirects=ALLOW_REDIRECTS)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return None

# Function to find active sites based on specified meta tag names
def find_active_sites(meta_tag_names):
    active_sites = []
    base_url = "https://dizipal{}.com"

    # Using ThreadPoolExecutor for concurrent execution
    with concurrent.futures.ThreadPoolExecutor() as executor:
        site_urls = [base_url.format(i) for i in range(START_RANGE, END_RANGE)]
        # Divide the site URLs into chunks for parallel processing
        for chunk_start in tqdm(range(0, len(site_urls), CHUNKS), desc="Processing Chunks"):
            chunk = site_urls[chunk_start:chunk_start + CHUNKS]
            with tqdm(total=len(chunk), desc="Processing Sites", leave=False) as site_progress:
                # Use executor.map to parallelize the site checking
                results = executor.map(lambda site_url: check_site(site_url, meta_tag_names, site_progress), chunk)
                # Collect the results and display active sites
                active_sites.extend(result for result in results if result)
                site_progress.close()

    return active_sites

# Function to check if a site is active based on meta tag names and keywords in the title
def check_site(site_url, meta_tag_names, site_progress):
    for attempt in range(MAX_RETRIES):
        page_content = fetch_page_content(site_url)

        if not page_content:
            continue

        soup = BeautifulSoup(page_content, 'html.parser')
        found_tags = [meta for meta_tag_name in meta_tag_names for meta in soup.find_all("meta", {"name": meta_tag_name})]

        if len(found_tags) == len(meta_tag_names):
            title_tag = soup.find('title')
            title = title_tag.text if title_tag else "Title not found"

            # Check if keywords are present in the title
            if any(keyword in title for keyword in ["Dizipal", "DizipalX"]):
                site_progress.update(1)
                print("----------------------------------------------")
                print(f"Active site: {site_url} - Title: {title}")
                print("----------------------------------------------")
                return site_url, title

    site_progress.update(1)
    return None

# Main function to orchestrate the script
def main():
    try:
        # Specify meta tag names to search for
        meta_tag_names = ["description", "viewport"]
        active_sites = find_active_sites(meta_tag_names)

        # Display the active sites, if any
        if active_sites:
            print("\nActive sites:")
            for site, title in active_sites:
                print(f"{site} - Title: {title}")
        else:
            print("No active sites found.")

    except KeyboardInterrupt:
        print("\nProcess terminated by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
