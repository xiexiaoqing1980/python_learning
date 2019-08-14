
dictb={"name":"bob"}

string="hahhah{name}".format(**dictb)

def test(url):

    # for i in range(1,5):
    #     # url='http://www.qiushibaike.com/hot/page/%d'%i    //%这种方式格式化
    #     url="http://www.qiushibaike.com/hot/page/{}".format(i)   # {},：来格式化
        return url

print(list(map(test,["http://www.qiushibaike.com/hot/page/{}".format(i) for i in range(1,5)] )))
# print(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))



