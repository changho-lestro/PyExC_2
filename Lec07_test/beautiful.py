import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Configuration
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/HTML"

# 2. Function to fetch HTML content
def fetch_html_content(url):
    """
    Fetches the HTML content from a given URL.
    Args:
        url (str): The URL of the web page.
    Returns:
        str: The HTML content of the page, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        print(f"Successfully fetched content from: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

# 3. Function to parse HTML with Beautiful Soup
def parse_html_with_beautifulsoup(html_content):
    """
    Parses HTML content using BeautifulSoup.
    Args:
        html_content (str): The HTML content as a string.
    Returns:
        BeautifulSoup object: A parse tree representation of the HTML.
    """
    if not html_content:
        return None
    soup = BeautifulSoup(html_content, 'html.parser')
    print("HTML content successfully parsed by BeautifulSoup.")
    return soup

# 4. Function to extract specific data
def extract_data(soup):
    """
    Extracts specific data points from the parsed Wikipedia page.
    Args:
        soup (BeautifulSoup object): The parsed HTML content.
    Returns:
        dict: A dictionary containing the extracted data.
    """
    if not soup:
        return {}

    extracted_data = {
        "page_title": "",
        "sections": [],
        "paragraphs": [],
        "external_links": []
    }

    # Extract Page Title
    page_title_tag = soup.find('h2')
    if page_title_tag:
        extracted_data["page_title"] = page_title_tag.get_text(strip=True)
        print(f"Extracted Page Title: {extracted_data['page_title']}")

    # Extract Top-Level Headings (h2)
    for h2_tag in soup.find_all('h4'):
        headline_span = h2_tag.find('span', class_='mw-headline')
        if headline_span:
            extracted_data["sections"].append(headline_span.get_text(strip=True))
    print(f"Extracted {len(extracted_data['sections'])} sections.")

    # Extract Paragraphs from the main content
    content_div = soup.find('div', class_='mw-parser-output')
    if content_div:
        for p_tag in content_div.find_all('p', limit=5): # Get first 5 paragraphs
            paragraph_text = p_tag.get_text(strip=True)
            if paragraph_text:
                extracted_data["paragraphs"].append(paragraph_text)
    print(f"Extracted {len(extracted_data['paragraphs'])} paragraphs.")

    # Extract External Links from the main content
    if content_div:
        for a_tag in content_div.find_all('a', href=True):
            link = a_tag['href']
            # Filter for external links (often start with // or http, and not internal wiki links)
            if link.startswith(('http://', 'https://')) and "wikipedia.org" not in link:
                extracted_data["external_links"].append(link)
    print(f"Extracted {len(extracted_data['external_links'])} external links.")

    return extracted_data

# 5. Function to create Pandas DataFrames
def create_dataframes(data):
    """
    Creates Pandas DataFrames from the extracted data.
    Args:
        data (dict): The dictionary containing extracted data.
    Returns:
        tuple: A tuple containing (sections_df, links_df).
    """
    if not data:
        print("No data to create DataFrames.")
        return pd.DataFrame(), pd.DataFrame()

    sections_df = pd.DataFrame(data["sections"], columns=["Section Title"])
    print("\n--- Sections DataFrame ---")
    print(sections_df.head())

    links_df = pd.DataFrame(data["external_links"], columns=["External Link URL"])
    print("\n--- External Links DataFrame ---")
    print(links_df.head())

    # You can also create a DataFrame for paragraphs if needed
    # paragraphs_df = pd.DataFrame(data["paragraphs"], columns=["Paragraph Text"])

    return sections_df, links_df

# Main execution flow
if __name__ == "__main__":
    WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/HTML"
    html_doc = fetch_html_content(WIKIPEDIA_URL)

    h4_data=soup.find_all('h4')
    for h4 in h4_data:
        print(h4.get_text(strip=True))

    if html_doc:
        soup = parse_html_with_beautifulsoup(html_doc)
        if soup:
            extracted_data = extract_data(soup)
            if extracted_data:
                sections_df, links_df = create_dataframes(extracted_data)
                print("\nData collection and DataFrame creation complete!")
            else:
                print("No data extracted from the page.")
        else:
            print("Failed to parse HTML content.")
    else:
        print("Failed to fetch HTML content.")
