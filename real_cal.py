#！/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:QiFeng Zhang
import re
__Author__ = "Faker"

'''计算表达式字符串'''
bracket = re.compile(r"\([^()]+\)")  #查找最内层括号
div     = re.compile(r"(\d+\.?\d*/-\d+\.?\d*)|(\d+\.?\d*/\d+\.?\d*)")  #查找除法运算
mul     = re.compile(r"(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)")  #查找乘法运算
add     = re.compile(r"(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)")  #查找加法运算
sub     = re.compile(r"(-?\d+\.?\d*--\d+\.?\d*)|(-?\d+\.?\d*-\d+\.?\d*)")  #查找减法运算
c_f     = re.compile(r"\(?\+?-?\d+\.?\d*\)?")   #查找括号内是否运算完毕
strip   = re.compile(r"[^(].*[^)]")   #去除括号

def Div(s):
    '''计算除法'''
    exp = re.split(r'/',div.search(s).group())  #将除法表达式拆分成列表
    return s.replace(div.search(s).group(),str(float(exp[0])/float(exp[1])))  #计算并用结果替换列表中表达式
def Mul(s):
    '''计算乘法'''
    exp = re.split(r'\*',mul.search(s).group())  #将乘法表达式拆分成列表
    return s.replace(mul.search(s).group(),str(float(exp[0])*float(exp[1])))  #计算并用结果替换列表中表达式
def Add(s):
    '''计算加法'''
    exp = re.split(r'\+',add.search(s).group())  #将加法表达式拆分成列表
    return s.replace(add.search(s).group(),str(float(exp[0])+float(exp[1])))  #计算并用结果替换列表中表达式
def Sub(s):
    '''计算减法'''
    exp = sub.search(s).group()   #去除减法表达式
    if exp.startswith('-'):  #如果表达式形如：-2.2-1.2；需变换为：-（2.2+1.2）
        exp = exp.replace('-', '+')         #将-号替换为+号；+2.2+1.2
        res = Add(exp).replace('+', '-')    #调用Add运算，将返回值+3.4变为-3.4
    else:
        exp = re.split(r'-',exp)
        res = str(float(exp[0]) - float(exp[1]))
    return s.replace(sub.search(s).group(),res)

def calc(suanshi):
    s = suanshi
  
    s = u''.join([x for x in re.split('\s+',s)])  #去除字符串中的空白字符
    if not s.startswith('('):  #若字符串不是以括号开始的，增加括号
        s = str('(%s)'%s)
    while bracket.search(s):  #若表达式存在括号，将括号内容取出来存变量
        s = s.replace('--','+')  #将表达式中的--替换成+
        s_search  = bracket.search(s).group()   #查找最内层括号，将括号内容取出
        if div.search(s_search): #如果括号内包含除服，则先算除法
            s = s.replace(s_search,Div(s_search))  #替换除法运算
        elif mul.search(s_search):   #判断是否包含乘法运算
            s = s.replace(s_search,Mul(s_search))  #将乘法计算内容替换乘法表达式
        elif sub.search(s_search): #判断是否包含减法运算
            s = s.replace(s_search,Sub(s_search)) #将减法运算结果替换减法运算表达式
        elif add.search(s_search): #判断是否加法运算
            s = s.replace(s_search,Add(s_search))  #将加法运算结构调换加法运算表达式
        elif c_f.search(s_search):  #加减乘除都不含，判断是否有括号
            s = s.replace(s_search,strip.search(s_search).group())  #对最终结果执行去括号操作

        #print('The answer is %.2f'%(float(s)))
    return s


