from playwright.sync_api import sync_playwright
import httpx
import os
from bs4 import BeautifulSoup
from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class DiscoveredHansard(BaseModel):
    title: str
    page_url: HttpUrl
    pdf_download_url: Optional[HttpUrl] = None


PARLIAMENT_BASE_URL = "https://parlzim.gov.zw"
HANSARDS_URL = f"{PARLIAMENT_BASE_URL}/national-assembly-hansards"


def discover_hansards(page) -> List[DiscoveredHansard]:
    print(f"Scraping index page: {HANSARDS_URL}")
    discovered = []

    page.goto(HANSARDS_URL, timeout=480000)
    page.wait_for_timeout(5000)

    soup = BeautifulSoup(page.content(), 'lxml')

    selector = ".media"
    hansard_entries = soup.select(selector)

    if not hansard_entries:
        print("No Hansard links found on the page.")
        return []

    print(f"Found {len(hansard_entries)} entries on the first page.")
    for entry in hansard_entries:
        
        title_link = entry.select_one(".package-title a")
        if not title_link:
            continue
        
        title = title_link.text.strip()
        url = title_link.get('href')
        if not url.startswith("http"):
            url = PARLIAMENT_BASE_URL + url
            
            
        pdf_link_element = entry.select_one(".ml-3 a")
        pdf_download_url = None
        
        if pdf_link_element:
            data_url = pdf_link_element.get('data-downloadurl')
            
            pdf_download_url = data_url
            print(pdf_download_url)
        
        discovered.append(DiscoveredHansard(
            title=title, 
            page_url=url,
            pdf_download_url=pdf_download_url
        ))

    return discovered


def download_pdf(page, pdf_url: HttpUrl, output_dir: str = "hansards"):
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = str(pdf_url).split("/")[-1]
    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"
        filename = f"hansard_{os.path.basename(str(pdf_url)).replace('.', '_')}.pdf"
        
    file_path = os.path.join(output_dir, filename)
    
    print(f"Downloading PDF from {pdf_url} to {file_path}")
    try:
        with page.expect_download(timeout=60000) as download_info:
            print(f"DEBUG: PDF URL for Playwright: '{str(pdf_url)}'")
            page.goto(str(pdf_url), timeout=60000)
            
        download = download_info.value
        download_path = download.path()
        
        if download_path and os.path.exists(download_path) and download.suggested_filename:
            download.save_as(file_path)
            print(f"PDF downloaded successfully: {file_path}")
            return file_path
        else:
            print(f"Failed to download PDF: {download.suggested_filename} not found.")
            return None
    except Exception as e:
        print(f"An error occurred while downloading the PDF: {e}")
        return None
    

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()

        print("Starting the scraper...")
        discovered_hansards = discover_hansards(page)

        if discovered_hansards:
            print("\n--- Discovered Hansards ---")
            for i, hansard in enumerate(discovered_hansards, start=1):
                print(f"{i}. {hansard.title} - {hansard.page_url}")
                if hansard.pdf_download_url:
                    print(f"   PDF Download URL: {hansard.pdf_download_url}")
                else:
                    print("   No PDF download link available.")
                    
            print("\n--- Downloading PDFs ---")
            
            
            for hansard_to_process in discovered_hansards[:3]:
                print("-" * 30)
                if hansard_to_process.pdf_download_url:
                    download_path = download_pdf(
                        page,
                        hansard_to_process.pdf_download_url
                        )
                        
                    if download_path:
                        print(f"PDF downloaded to: {download_path}")
                    else:
                        print(f"No PDF download link found for {hansard_to_process.title}")
                else:
                    print(f"No PDF download link available for {hansard_to_process.title}")

        browser.close()
        print("\n--- Scraping Complete ---")
