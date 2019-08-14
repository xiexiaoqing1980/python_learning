
import re
#---匹配以s开头，e结尾的字符串
# text ='site sea sue sweet see case sse ssee loses'
# items=re.findall(r'^s\S*?e$',text)    #此处一定要使用空白字符\S,否则会出错

# print(items)

#----- gropu（）学习----
# string="abcde1234qwe111111a22e"
# item=re.match(r"a.*?q.*?e",string)

# print(item.groups())    #  groups()将分组的字符串给截出来,以元祖返回 ,而group（）：abcde1234qwe  获得一个或多个分组截获的字符串,match一匹配成功就停止匹配,group(将两个分组的值显示出来)：('bcde1234', 'w')


#------不以某个字符串结尾或者开头----

#1、不以某个字符串开头：否定向前：^(?!str)或者^[^str]

# string="seclome"
# pattern=re.compile(r"^(?!we).*")
# items=re.findall(pattern,string)
# print(items)

#1、不以某个字符串结尾：否定向前：^(?<str)或者^[^str]
