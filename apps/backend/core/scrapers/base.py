from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple


class BaseScraper(ABC):
    """Abstract base class for provider scrapers."""

    @abstractmethod
    def search(self, keyword: str) -> Tuple[List[Dict[str, Any]], str, str]:
        """Return scraped products along with raw CSS and JS when available."""
        raise NotImplementedError

