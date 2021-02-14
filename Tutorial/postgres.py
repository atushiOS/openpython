import pyodbc


def ExecuteSQLBySQLServer(sql):
    con = pyodbc.connect(r'DRIVER={SQL Server};SERVER=rain-vm2.yamamoto.nitech.ac.jp\SQLExpress;DATABASE=osm_road_db;UID=postgres;PWD=usadasql;')
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

ExecuteSQLBySQLServer("select * from osm_car_2po_4pgr")
