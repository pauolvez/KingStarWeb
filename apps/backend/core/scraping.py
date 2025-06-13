"""Placeholder scraping utilities for providers like AliExpress."""

from typing import Any, Dict


def search_provider(keyword: str) -> list[Dict[str, Any]]:
    """Simulate scraping provider to retrieve product list."""
    # TODO: implement real scraping
    return [{"name": f"Product {keyword}", "price": 1.0, "asin": "B000TEST"}]
