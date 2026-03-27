from fastapi import APIRouter, HTTPException, Query
from API_BiblioOrg.services.search_service import search_value_in_table

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
def search(
    table: str = Query(..., description="Table name"),
    value: str = Query(..., description="Value to search")
):
    # Search for records in a table by column and value
    result = search_value_in_table(table, value)

    if result is None:
        raise HTTPException(status_code=500, detail="Search failed")

    return {
        "status": "ok",
        "count": len(result),
        "data": result
    }