"""Simple wrapper around Amazon SP-API.
This is a placeholder implementation to be extended.
"""

from typing import Any, Dict


def search_product_by_asin(asin: str) -> Dict[str, Any]:
    """Retrieve product data from Amazon SP-API.

    This function should use the official Amazon Selling Partner API.
    Currently returns mocked data for development.
    """
    # TODO: integrate with Amazon SP-API
    return {
        "asin": asin,
        "price": 0.0,
        "rank": 0,
    }
