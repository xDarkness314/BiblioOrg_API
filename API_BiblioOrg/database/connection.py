"""Create a connection to the database and return the connection object.nd manage database connections."""

from typing import Any, Optional
import psycopg2
from psycopg2.extensions import connection as PgConnection
from API_BiblioOrg.config.settings import settings

def get_connection() -> PgConnection:
    """Create and return a PostgreSQL connection."""
    return psycopg2.connect(settings.database_url)

def check_database_connection() -> bool:
    """Return True if the database connection works."""
    connection: Optional[PgConnection] = None 
    try:
        connection = get_connection()
        return True
    except Exception as e:
        return False
    finally:
        if connection is not None:
            connection.close()
