import psycopg2

conn = psycopg2.connect(
    dbname="название_бд",
    user="пользователь",
    password="пароль",
    host="localhost",  # или IP адрес сервера
    port="5432"         # стандартный порт PostgreSQL
)

# Курсор для выполнения запросов
cur = conn.cursor()

# Пример запроса
cur.execute("SELECT * FROM material_type;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Завершение
cur.close()
conn.close()


# query = """
# SELECT
#     p.name AS product_name,
#     pt.name AS product_type,
#     mt.name AS material,
#     w.name AS workshop_name,
#     pw.production_time_hours
# FROM product p
# JOIN product_type pt ON p.product_type_id = pt.id
# JOIN material_type mt ON p.material_type_id = mt.id
# JOIN product_workshop pw ON pw.product_id = p.id
# JOIN workshop w ON pw.workshop_id = w.id
# ORDER BY p.name;
# """
#
# cur.execute(query)
# rows = cur.fetchall()