from database.DB_connect import DBConnect
from model.arco import Arco
from model.order import Order


class DAO():
    @staticmethod
    def getAllStores():
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor(dictionary=True)

        query = """select s.store_id 
                    from stores s"""

        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row["store_id"])
        cnx.close()
        return result

    @staticmethod
    def getAllNodes(store_id):
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor(dictionary=True)

        query = """select *
                    from orders o 
                    where o.store_id = %s"""

        cursor.execute(query, (store_id,))

        result = []
        for row in cursor:
            result.append(Order(**row))
        cnx.close()
        return result

    @staticmethod
    def getAllEdges(store_id, max_giorni, idMap):
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor(dictionary=True)

        query = """select t.ordine1, t.ordine2, i1.numItems + i2.numItems as peso
                    from (select o1.order_id as ordine1, o2.order_id as ordine2
                    from orders o1, orders o2
                    where o1.store_id = %s and o2.store_id = %s and o1.order_id > o2.order_id and o1.order_date <> o2.order_date and datediff(o1.order_date, o2.order_date) < %s) t,
                    (select *, sum(oi.quantity) as numItems 
                    from order_items oi 
                    group by oi.order_id ) i1, (select *, sum(oi.quantity) as numItems
                    from order_items oi 
                    group by oi.order_id ) i2
                    where t.ordine1 = i1.order_id and t.ordine2 = i2.order_id """

        cursor.execute(query, (store_id, store_id, max_giorni,))

        result = []
        for row in cursor:
            result.append(Arco(idMap[row["ordine1"]], idMap[row["ordine2"]], row["peso"]))
        cnx.close()
        return result
