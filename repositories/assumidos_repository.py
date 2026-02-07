from database.connection import get_connection

def inserir_assumido(presente_id, nome_convidado):
    query = """
        INSERT INTO presentes_assumidos
        (presente_id, nome_convidado)
        VALUES (%s, %s)
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (presente_id, nome_convidado))
            conn.commit()
