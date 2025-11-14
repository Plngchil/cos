from dbconnection import get_connection

class db:
    def __init__(self):
        self.connection = get_connection()
#endpointy do wydarzen 
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
            (id_organizatora, id_miejsca, id_rodzaju, nazwa, data, godz_zacz, godz_zak, deleted)
            VALUES (%s, %s, %s, %s, %s, %s, %s, 0)
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
    def delete_wydarzenie(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            update wydarzenia set
                deleted = 1
            where ID = %s
        """
        values = [id]
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
       
        return {
            "status": "ok" if affected_rows > 0 else "not_found",
            "updated_rows": affected_rows
        }
#endpointy do miejsc 
    def get_miejsca(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM miejsca")
        miejsca = cursor.fetchall()
        cursor.close()
        conn.close()
        return miejsca
    def add_miejsce(self, miejsce_data):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            INSERT INTO miejsca 
            (adres, miasto, deleted)
            VALUES (%s, %s, 0)
        """
        values = (
            miejsce_data['adres'],
            miejsce_data['miasto'],
        )
        cursor.execute(sql, values)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"status": "ok", "added_id": last_id}
    def update_miejsce(self,id, miejsce_data):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            UPDATE miejsca
            SET 
                adres = %s,
                miasto = %s
            WHERE ID = %s
        """
        values = (
            miejsce_data['adres'],
            miejsce_data['miasto'],
            id
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
    def delete_miejsce(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            update miejsca set
                deleted = 1
            where ID = %s
        """
        values = [id]
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return {
            "status": "ok" if affected_rows > 0 else "not_found",
            "updated_rows": affected_rows
        }