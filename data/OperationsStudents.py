import psycopg2

db_name = 'frs_db'
user = "postgres"
password = "123"
host = "localhost"
port = "5432"


# conn = psycopg2.connect(database=db_name, user=user, password=password, host=host
#                         , port=port)
#
# cur = conn.cursor()

# class OperationsStudents:
#     def create_student(self, name, surname, middle_name, group):
#         conn = psycopg2.connect(database=db_name, user=user, password=password, host=host, port=port)
#         cur = conn.cursor()
#         try:
#             assert surname is not None
#             assert name is not None
#             assert middle_name is not None
#             assert group is not None
#             columns = ['name', 'surname', 'middle_name', 'group']
#             line_operators = ','.join(['%s' for _ in columns])
#             values = [name, surname, middle_name, group]
#             cur.execute(f'INSERT INTO student VALUES({line_operators})', values)
#             conn.commit()
#             conn.close()
#             return True
#         except:
#             return False

#     def get_all(self):
#         conn = psycopg2.connect(database=db_name, user=user, password=password, host=host, port=port)
#         cur = conn.cursor()
#         cur.execute('''SELECT surname, name, middle_name FROM student''')
#         data = cur.fetchall()
#         print(data)
#         formatted_data = [' '.join(item) for item in data]

#         cur.close()
#         conn.close()
#         return formatted_data
