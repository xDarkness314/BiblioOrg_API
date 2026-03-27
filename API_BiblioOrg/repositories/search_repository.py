from typing import Any, Optional
from psycopg2 import sql
from API_BiblioOrg.database.connection import get_connection

ALLOWED_TABLES = {
    "usuarios": {"id", "usuario", "categoria", "contraseña", "año"},
    "principal": {"id", "codigo", "libro", "autor", "clasificacion", "estante", "fila", "cantidad_total", "stock"},
    "prestamos": {"id", "codigo", "libro", "nombre", "apellidos", "estado", "fecha_salida", "fecha_devolucion"},
    "observaciones": {"id", "usuario", "titulo", "contenido", "fecha"},
    "lista": {"id", "codigo", "libro", "autor", "disponibilidad", "clasificacion", "estante", "fila", "cantidad_total", "stock"},
    "historial": {"id", "codigo", "libro", "nombre", "apellidos", "fecha_salida", "fecha_devolucion_oportuna", "fecha_devolucion", "devolucion_a_tiempo"}
}

def search_records(table: str, value: str) -> Optional[list[dict[str, Any]]]:
    # Check if the table is allowed
    if table not in ALLOWED_TABLES:
        return None

    connection = None

    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            query = sql.SQL(
                "SELECT * FROM {table}::text ILIKE %s"
            ).format(
                table=sql.Identifier(table),
            )

            cursor.execute(query, (f"%{value}%",))
            rows = cursor.fetchall()

            column_names = [desc[0] for desc in cursor.description]

            return [dict(zip(column_names, row)) for row in rows]

    except Exception:
        return None
    finally:
        if connection is not None:
            connection.close()