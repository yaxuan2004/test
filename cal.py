import tkinter
import easygui,re
from real_cal import *
class mycal():
    def __init__(self,tk):
        self.tk=tk
        self.set_tk()

    def set_tk(self):
        tk.title('小小计算器')
        
        self.input_label=tkinter.Label(tk,text='请您输入算式：')    
        self.input_label.grid(row=0,column=0)
        # self.input_label.pack(side=tkinter.LEFT)
        self.input_entry=tkinter.Entry(tk,bd=5,width=25)
        self.input_entry.focus()
        self.input_entry.grid(row=0,column=5)
        # self.input_entry.pack()
        self.output_label=tkinter.Label(tk,text='结果：')
        self.output_label.grid(row=1,column=0)
        # self.input_entry.pack(side=tkinter.LEFT)
        self.output_entry=tkinter.Entry(tk,bd=1,width=25)
        self.output_entry.grid(row=1,column=5)
        # self.output_entry.pack()
        self.cal_button=tkinter.Button(tk,text='计算',command=self.cal)
        self.cal_button.grid(row=5,column=0)
        # self.cal_button.pack()
    #encoding=utf-8

    def is_number(self,s):#判断结果是否为数字
        
        if s[0]=="-":
                s=s[1:]
        
        for i in s:
            if i not in ".0123456789":
                flag=False
                break
            else:
                flag=True
                        
        return flag

    def cal(self):
        res=self.input_entry.get().strip()
        self.output_entry.delete(0,tkinter.END)
        try:
            r=calc(res)
            if not self.is_number(str(r)):
                easygui.msgbox('算式输入不正确:%s'%str(r),'异常')
                return ''
            else:
                self.output_entry.insert(0,str(r))
                return r
        except Exception as e:
            easygui.msgbox(e,'异常')
            return None
    '''
    def check(self):
        res=self.input_entry.get()
        if res==None:
            return False
        
        if (re.search('^\d',res) or re.search('^(',res))  and (re.search(')$',res) or re.search('\d$',res)):
            return True
        else:
            return False
    '''

if __name__=='__main__':
    tk=tkinter.Tk()
    cal=mycal(tk)
    tk.geometry("300x200+400+300")
    tk.mainloop()
