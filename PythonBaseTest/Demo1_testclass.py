class demo1:
    '''类属性和方法'''
    count=0    #类属性
    @classmethod      #访问类属性或者类方法，可以定义该方法
    def method1(cls):
        print(cls.count)   #访问类属性
        # cls.method2()       只能访问类方法

    def method2(self):       #实例方法：访问实例属性或者实例方法
        print("null")

    """""""


#调用类方法

demo1.method1()