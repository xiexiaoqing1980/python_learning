
def insert_data(num):
    filepath="D:\\insert_data.sql"
    with open(filepath,"w+") as f:    # 清空文件内容后追加
        for i in range(0,num):
            fid=580852489465628672+i
            before_insert="DELETE FROM `t_ut_boslist_batch_proces` where FId = '{}';\n".format(fid)
            insert_sql="INSERT INTO `t_ut_boslist_batch_proces` VALUES ({}, '{}', 'A', 13466739, 13466739, 0, NULL, '2019-3-13 10:10:13', '2019-3-13 10:10:09');\n".format(fid,i)
            f.write(before_insert+insert_sql)


if __name__ == '__main__':
    
    insert_data(50000)


