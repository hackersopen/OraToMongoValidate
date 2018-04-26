import cx_Oracle

con = cx_Oracle.connect('sysroot/26-Apr-2k18@demo-hackathon-db.cwdpnc8wdowf.us-east-2.rds.amazonaws.com/ORCL')
print(con.version)