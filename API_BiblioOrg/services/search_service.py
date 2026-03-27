from typing import Any, Optional
from API_BiblioOrg.repositories.search_repository import search_records

def search_value_in_table(table: str, value: str) -> Optional[list[dict[str, Any]]]:
    # Call repository function to search records
    return search_records(table, value)