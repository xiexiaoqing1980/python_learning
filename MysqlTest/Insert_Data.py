import pymysql

def inser_data(num):
    # conn=pymysql.connect(user="mc_admin",password="kingdee",port="3306",db="bos_branch_dev_new_sys",host="192.168.63.96",charset="utf8")
    conn=pymysql.connect(user="root",password="kingdee",port="3306",db="bos_branch_smoke_sys",host="172.17.4.118",charset="utf8")
    
    # cursor=conn.cursor();
    # sql=""
    # for i in range(0,num):
    #     cursor.execute()

    
if __name__ == '__main__':
    inser_data(10)
    
