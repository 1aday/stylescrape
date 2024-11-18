from firecrawl import FirecrawlApp
from time import sleep
import os

class SEHKellyScraper:
    def __init__(self, api_key: str):
        self.app = FirecrawlApp(api_key=api_key)
        self.base_url = "https://www.styleforum.net/threads/s-e-h-kelly.277070"
        self.output_dir = "seh_kelly_thread"
        
    def scrape_thread(self):
        """Scrape all pages of the S.E.H Kelly thread and save as markdown."""
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        # Scrape each page
        for page in range(1, 415):  # Goes from page 1 to 414
            print(f"Scraping page {page}...")
            
            # Construct URL for current page
            if page == 1:
                url = self.base_url
            else:
                url = f"{self.base_url}/page-{page}"
            
            try:
                # Scrape the page using markdown format
                result = self.app.scrape_url(
                    url,
                    params={
                        'formats': ['markdown'],
                        'onlyMainContent': True,
                        'waitFor': 2000
                    }
                )
                
                # Save the page content as markdown
                file_path = os.path.join(self.output_dir, f'page_{page:03d}.md')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(result['markdown'])
                
                print(f"Successfully saved page {page}")
                
            except Exception as e:
                print(f"Error scraping page {page}: {str(e)}")
            
            # Sleep between requests to be nice to the server
            sleep(2)

def main():
    # Replace with your Firecrawl API key
    API_KEY = "API KEY HERE"
    
    scraper = SEHKellyScraper(API_KEY)
    scraper.scrape_thread()
    
    print("Scraping complete! Files saved in 'seh_kelly_thread' directory")

if __name__ == "__main__":
    main()