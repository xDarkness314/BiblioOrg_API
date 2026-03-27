"""Create and manage database connections."""

from typing import Any, Optional
import psycopg2
from psycopg2.extensions import connection as PgConnection
from API_BiblioOrg.config.settings import settings


def get_connection() -> PgConnection:
    # Create and return a PostgreSQL connection
    return psycopg2.connect(settings.database_url)


def check_database_connection() -> bool:
    # Return True if the database connection works
    connection: Optional[PgConnection] = None

    try:
        connection = get_connection()
        return True
    except Exception:
        return False
    finally:
        if connection is not None:
            connection.close()


def get_database_time() -> Any:
    # Return current database time
    connection: Optional[PgConnection] = None

    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW();")
            row = cursor.fetchone()

        return row[0] if row else None
    except Exception:
        return None
    finally:
        if connection is not None:
            connection.close()