"""Scraper for AliExpress provider."""

from typing import Any, Dict, List, Tuple
import requests
from bs4 import BeautifulSoup

from .base import BaseScraper


class AliExpressScraper(BaseScraper):
    BASE_URL = "https://www.aliexpress.com/wholesale"

    def search(self, keyword: str) -> Tuple[List[Dict[str, Any]], str, str]:
        params = {"SearchText": keyword}
        resp = requests.get(self.BASE_URL, params=params, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")

        products: List[Dict[str, Any]] = []
        for item in soup.select(".manhattan--container"):
            name = item.select_one(".manhattan--titleText")
            if not name:
                continue
            name_text = name.get_text(strip=True)
            price_el = item.select_one(".manhattan--price-sale span")
            price = float(price_el.get_text(strip=True).replace("US $", "")) if price_el else 0
            products.append({"name": name_text, "price": price, "asin": ""})

        styles = "\n".join(tag.get_text() for tag in soup.find_all("style"))
        scripts = "\n".join(tag.get_text() for tag in soup.find_all("script"))

        return products, styles, scripts

