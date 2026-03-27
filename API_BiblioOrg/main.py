"""Main application entry point."""

from fastapi import FastAPI, HTTPException
from API_BiblioOrg.database.connection import check_database_connection
from API_BiblioOrg.routers.search_router import router as search_router

app = FastAPI()
app.include_router(search_router)


@app.get("/db-check")
def db_check() -> dict:
    # Check if the database connection is working
    is_connected = check_database_connection()

    if not is_connected:
        raise HTTPException(status_code=500, detail="Database connection failed")

    return {
        "status": "ok",
        "database_connection": "successful"
    }

@app.get("/db-search")
def db_search() -> dict:
    to_search = input("Enter the table and value to search (format: table,value): ")