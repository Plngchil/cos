from dbconnection import get_connection

class db:
    def __init__(self):
        self.connection = get_connection()

    def get_wydarzenia(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM wydarzenia")
        wydarzenia = cursor.fetchall()
        cursor.close()
        conn.close()
        return wydarzenia

    def add_wydarzenie(self, wydarzenie_data):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            INSERT INTO wydarzenia 
            (id_organizatora, id_miejsca, id_rodzaju, nazwa, data, godz_zacz, godz_zak)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            wydarzenie_data['id_organizatora'],
            wydarzenie_data['id_miejsca'],
            wydarzenie_data['id_rodzaju'],
            wydarzenie_data['nazwa'],
            wydarzenie_data['data'],
            wydarzenie_data['godz_zacz'],
            wydarzenie_data['godz_zak']
        )

        cursor.execute(sql, values)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"status": "ok", "added_id": last_id}
    
    def update_wydarzenie(self, wydarzenie_data):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            UPDATE wydarzenia
            SET 
                id_organizatora = %s,
                id_miejsca = %s,
                id_rodzaju = %s,
                nazwa = %s,
                data = %s,
                godz_zacz = %s,
                godz_zak = %s
            WHERE ID = %s
        """

        values = (
            wydarzenie_data['id_organizatora'],
            wydarzenie_data['id_miejsca'],
            wydarzenie_data['id_rodzaju'],
            wydarzenie_data['nazwa'],
            wydarzenie_data['data'],
            wydarzenie_data['godz_zacz'],
            wydarzenie_data['godz_zak'],
            wydarzenie_data['ID']
        )

        cursor.execute(sql, values)
        conn.commit()

        affected_rows = cursor.rowcount

        cursor.close()
        conn.close()

        return {
            "status": "ok" if affected_rows > 0 else "not_found",
            "updated_rows": affected_rows
        }
    def delete_wydarzenie(self, data_wydarzenia):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            update 
        """