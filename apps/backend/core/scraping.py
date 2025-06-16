"""Utility functions to run provider scrapers."""

from typing import Any, Dict, List, Tuple

from .scrapers.aliexpress import AliExpressScraper

SCRAPERS = {
    "aliexpress": AliExpressScraper(),
}


def search_provider(provider: str, keyword: str) -> Tuple[List[Dict[str, Any]], str, str]:
    """Search products using the scraper associated with the provider."""
    scraper = SCRAPERS.get(provider)
    if not scraper:
        raise ValueError(f"Provider {provider} not supported")
    return scraper.search(keyword)

