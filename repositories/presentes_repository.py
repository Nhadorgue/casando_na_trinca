from database.connection import get_connection

def buscar_presentes_disponiveis():
    query = """
        SELECT
            id,
            produto,
            categoria,
            valor_estimado,
            imagem,
            link_preco,
            exemplos
        FROM presentes
        WHERE COALESCE(assumido, false) = false
        ORDER BY id
    """
    
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


def marcar_como_assumido(presente_id):
    query = "UPDATE presentes SET assumido = true WHERE id = %s"

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (presente_id,))
            conn.commit()
