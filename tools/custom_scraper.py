# Crawl4AI scrapper logic. 
import asyncio
from crawl4ai import AsyncWebCrawler

class UniversityScraper:
    async def scrape_university(self,url: str) -> str:
        """
        Pure async function to be called inside a LngGraph node.
        """
        async with AsyncWebCrawler(verbose=True) as crawler:
            result=await crawler.arun(url=url,bypass_cache=True)
            if result.success:
                return result.markdown
            return f"Error: {result.error_message}"