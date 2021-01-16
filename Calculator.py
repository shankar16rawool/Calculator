from tkinter import *
from PIL import ImageTk, Image
import math

class Calculator:
    def __init__(self, root):
        self.root=root
        self.root.title('Calculator')
        self.root.resizable(False, False)
        self.width=str(int(root.winfo_screenwidth()/4.8))
        self.height=str(int(root.winfo_screenheight()/1.728))

        self.pos_x=str(int(root.winfo_screenwidth()/2-float(self.width)/2))
        self.pos_y=str(int(root.winfo_screenheight()/2-float(self.height)/2))
        
        self.root.geometry(self.width+'x'+self.height+'+'+self.pos_x+'+'+self.pos_y)

        self.img_icon=Image.open('icon.ico').resize((50,50), Image.ANTIALIAS)
        self.img_icon=ImageTk.PhotoImage(self.img_icon)
        self.root.iconphoto(False, self.img_icon)
        

        self.font_lbl_1=('Times New Roman', int(root.winfo_screenwidth()/102.4))
        self.font_lbl_2=('Times New Roman', int(root.winfo_screenwidth()/59.07))
        self.font_btn=('Times New Roman', int(root.winfo_screenwidth()/102.4))

        self.char_str=''
        self.len_char_str=0
        self.operators=['+', '-', '*', '/', '%']

        self.pack_frames()
        self.pack_elements()

    def create_frames(self):    
        self.frm_lbl_row_1=Frame(root)
        self.frm_btn_row_1=Frame(root)
        self.frm_btn_row_2=Frame(root)
        self.frm_btn_row_3=Frame(root)
        self.frm_btn_row_4=Frame(root)
        self.frm_btn_row_5=Frame(root)
        self.frm_btn_row_6=Frame(root)
        self.frm_btn_row_7=Frame(root)

    def pack_frames(self):
        self.create_frames()
        
        self.frm_lbl_row_1.pack(expand=True, fill='both')
        self.frm_btn_row_1.pack(expand=True, fill='both')
        self.frm_btn_row_2.pack(expand=True, fill='both')
        self.frm_btn_row_3.pack(expand=True, fill='both')
        self.frm_btn_row_4.pack(expand=True, fill='both')
        self.frm_btn_row_5.pack(expand=True, fill='both')
        self.frm_btn_row_6.pack(expand=True, fill='both')
        self.frm_btn_row_7.pack(expand=True, fill='both')
    
    def create_elements(self):
        self.lbl_1=Label(self.frm_lbl_row_1, bg='#ffffff', font=self.font_lbl_1, anchor=E, height=1)
        self.lbl_2=Label(self.frm_lbl_row_1, bg='#ffffff', font=self.font_lbl_2, anchor=SE, height=1)
        
        self.btn_pc=Button(self.frm_btn_row_1, text=' % ', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=lambda:self.enter_char('%'))
        self.btn_del=Button(self.frm_btn_row_1, text='DEL', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=self.delete_command)
        self.btn_c=Button(self.frm_btn_row_1, text=' C ', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=self.delete_all_command)
        self.btn_back=Button(self.frm_btn_row_1, text=' < ', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=self.backspace_command)

        self.btn_abs=Button(self.frm_btn_row_2, text='|x|', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=self.absolute)
        self.btn_right=Button(self.frm_btn_row_2, text='(', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=lambda:self.enter_char('('))
        self.btn_left=Button(self.frm_btn_row_2, text=')', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=lambda:self.enter_char(')'))
        self.btn_fact=Button(self.frm_btn_row_2, text='x!', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=self.factorial)

        self.btn_rec=Button(self.frm_btn_row_3, text='1/x', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=self.reciprocal)
        self.btn_sqr=Button(self.frm_btn_row_3, text='x²', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=self.square)
        self.btn_sqrt=Button(self.frm_btn_row_3, text='√x', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=self.sqrt)
        self.btn_div=Button(self.frm_btn_row_3, text='÷', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=lambda:self.enter_char('/'))

        self.btn_7=Button(self.frm_btn_row_4, text='7', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('7'))
        self.btn_8=Button(self.frm_btn_row_4, text='8', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('8'))
        self.btn_9=Button(self.frm_btn_row_4, text='9', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('9'))
        self.btn_mul=Button(self.frm_btn_row_4, text='×', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=lambda:self.enter_char('*'))

        self.btn_4=Button(self.frm_btn_row_5, text='4', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('4'))
        self.btn_5=Button(self.frm_btn_row_5, text='5', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('5'))
        self.btn_6=Button(self.frm_btn_row_5, text='6', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('6'))
        self.btn_sub=Button(self.frm_btn_row_5, text='-', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=lambda:self.enter_char('-'))

        self.btn_1=Button(self.frm_btn_row_6, text='1', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('1'))
        self.btn_2=Button(self.frm_btn_row_6, text='2', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('2'))
        self.btn_3=Button(self.frm_btn_row_6, text='3', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('3'))
        self.btn_add=Button(self.frm_btn_row_6, text='+', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=lambda:self.enter_char('+'))

        self.btn_pm=Button(self.frm_btn_row_7, text='+/-', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=self.change_sign)
        self.btn_0=Button(self.frm_btn_row_7, text='0', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('0'))
        self.btn_dot=Button(self.frm_btn_row_7, text='.', font=self.font_btn, width=2, relief=GROOVE, bg='#ffffff', command=lambda:self.enter_char('.'))
        self.btn_equal=Button(self.frm_btn_row_7, text='=', font=self.font_btn, width=2, relief=GROOVE, bg='#f7f7f7', command=self.calculate)

        self.hover_btns(self.btn_pc, '#e0e0e0', '#f7f7f7')
        self.hover_btns(self.btn_del, '#e0e0e0', '#f7f7f7')
        self.hover_btns(self.btn_c, '#e0e0e0', '#f7f7f7')
        self.hover_btns(self.btn_back, '#e0e0e0', '#f7f7f7')

        self.hover_btns(self.btn_abs, '#e0e0e0', '#f7f7f7')
        self.hover_btns(self.btn_right, '#e0e0e0', '#f7f7f7')
        self.hover_btns(self.btn_left, '#e0e0e0', '#f7f7f7')
        self.hover_btns(self.btn_fact, '#e0e0e0', '#f7f7f7')

        self.hover_btns(self.btn_rec, '#e0e0e0', '#f7f7f7')
        self.hover_btns(self.btn_sqrt, '#e0e0e0', '#f7f7f7')
        self.hover_btns(self.btn_sqr, '#e0e0e0', '#f7f7f7')
        self.hover_btns(self.btn_div, '#e0e0e0', '#f7f7f7')

        self.hover_btns(self.btn_7, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_8, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_9, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_mul, '#e0e0e0', '#f7f7f7')

        self.hover_btns(self.btn_4, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_5, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_6, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_sub, '#e0e0e0', '#f7f7f7')

        self.hover_btns(self.btn_1, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_2, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_3, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_add, '#e0e0e0', '#f7f7f7')

        self.hover_btns(self.btn_pm, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_0, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_dot, '#e0e0e0', '#ffffff')
        self.hover_btns(self.btn_equal, '#e0e0e0', '#f7f7f7')
        
    def hover_btns(self, btn_name, ent_col, leave_col):        
        btn_name.bind('<Enter>', lambda x:btn_name.configure(bg=ent_col))
        btn_name.bind('<Leave>', lambda x:btn_name.configure(bg=leave_col))

    def pack_elements(self):
        self.create_elements()
        
        self.lbl_1.pack(expand=True, fill='both')
        self.lbl_2.pack(expand=True, fill='both')
        
        self.btn_pc.pack(side=LEFT, expand=True, fill='both')
        
        self.btn_del.pack(side=LEFT, expand=True, fill='both')
        self.btn_c.pack(side=LEFT, expand=True, fill='both')
        self.btn_back.pack(side=LEFT, expand=True, fill='both')

        self.btn_abs.pack(side=LEFT, expand=True, fill='both')
        self.btn_right.pack(side=LEFT, expand=True, fill='both')
        self.btn_left.pack(side=LEFT, expand=True, fill='both')
        self.btn_fact.pack(side=LEFT, expand=True, fill='both')

        self.btn_rec.pack(side=LEFT, expand=True, fill='both')
        self.btn_sqr.pack(side=LEFT, expand=True, fill='both')
        self.btn_sqrt.pack(side=LEFT, expand=True, fill='both')
        self.btn_div.pack(side=LEFT, expand=True, fill='both')

        self.btn_7.pack(side=LEFT, expand=True, fill='both')
        self.btn_8.pack(side=LEFT, expand=True, fill='both')
        self.btn_9.pack(side=LEFT, expand=True, fill='both')
        self.btn_mul.pack(side=LEFT, expand=True, fill='both')

        self.btn_4.pack(side=LEFT, expand=True, fill='both')
        self.btn_5.pack(side=LEFT, expand=True, fill='both')
        self.btn_6.pack(side=LEFT, expand=True, fill='both')
        self.btn_sub.pack(side=LEFT, expand=True, fill='both')

        self.btn_1.pack(side=LEFT, expand=True, fill='both')
        self.btn_2.pack(side=LEFT, expand=True, fill='both')
        self.btn_3.pack(side=LEFT, expand=True, fill='both')
        self.btn_add.pack(side=LEFT, expand=True, fill='both')

        self.btn_pm.pack(side=LEFT, expand=True, fill='both')
        self.btn_0.pack(side=LEFT, expand=True, fill='both')
        self.btn_dot.pack(side=LEFT, expand=True, fill='both')
        self.btn_equal.pack(side=LEFT, expand=True, fill='both')

    def enter_char(self, char):
        if len(self.char_str)==0 and char in self.operators:
            pass
        elif char==')' and self.char_str.count('(')==self.char_str.count(')'):
            pass
        else:
            self.char_str+=char
            if len(self.char_str)>2:
                if self.char_str[-1] in self.operators and self.char_str[-2] in self.operators:
                    self.char_str=self.char_str[:len(self.char_str)-1]
        self.lbl_2.configure(text=self.char_str)

    def calculate(self):
        try:
            if '%' in self.char_str:
                num1=float(self.char_str.split('%')[0])
                num2=float(self.char_str.split('%')[1])
                self.result=str((num1/100)*num2)
                
            else:
                self.result=str(round(eval(self.char_str),15))
            if self.result.count('.')>0 and self.result.endswith('0'):
                self.result=str(int(float(self.result)))
                    
            self.lbl_2.configure(text=self.result)
            self.lbl_1.configure(text=self.char_str)
            self.char_str=self.result

        except SyntaxError:
            self.lbl_2.configure(text='Invalid expression')
            self.char_str=''
        except ZeroDivisionError:
            self.lbl_2.configure(text='Can not divide by zero')
            self.char_str=''

    def change_sign(self):
        if len(self.char_str)!=0:
            if self.char_str!='0':
                if self.char_str[0]!='-':
                    self.char_str='-'+self.char_str
                else:
                    self.char_str=self.char_str[1:]
        self.lbl_2.configure(text=self.char_str)

    def backspace_command(self):
        self.char_str=self.char_str[:len(self.char_str)-1]
        self.lbl_2.configure(text=self.char_str)

    def delete_command(self):
        self.char_str=''
        self.lbl_2.configure(text=self.char_str)

    def delete_all_command(self):
        self.char_str=''
        self.lbl_1.configure(text=self.char_str)
        self.lbl_2.configure(text=self.char_str)

    def square(self):
        if len(self.char_str)>0:
            try:
                self.num=str(round(float(self.char_str)**2,15))
                if self.num.count('.')>0 and self.num.endswith('0'):
                        self.num=str(int(float(self.num)))
    
                self.lbl_1.configure(text=self.char_str+'²')
                self.lbl_2.configure(text=self.num)

            except (ValueError, TypeError):
                self.lbl_2.configure(text='Invalid Input')
                
            self.char_str=self.num

    def sqrt(self):
        try:
            if len(self.char_str)>0:
                self.num=str(round(float(self.char_str)**0.5,15))
                if self.num.count('.')>0 and self.num.endswith('0'):
                        self.num=str(int(float(self.num)))
        
                self.lbl_1.configure(text='√'+self.char_str)
                self.lbl_2.configure(text=self.num)
                
        except (ValueError, TypeError):
            self.lbl_2.configure(text='Invalid Input')

        self.char_str=self.num

    def reciprocal(self):
        try:
            if len(self.char_str)>0:
                self.num=str(round(1/float(self.char_str),15))
                if self.num.count('.')>0 and self.num.endswith('0'):
                        self.num=str(int(float(self.num)))
        
                self.lbl_1.configure(text='1/'+self.char_str)
                self.lbl_2.configure(text=self.num)
                
        except (ValueError, TypeError):
            self.lbl_2.configure(text='Invalid Input')
        except ZeroDivisionError:
            self.lbl_2.configure(text='Can not divide by zero')

        self.char_str=self.num

    def absolute(self):
        try:
            if len(self.char_str)>0:
                self.num=str(round(abs(float(self.char_str)),15))
                if self.num.count('.')>0 and self.num.endswith('0'):
                    self.num=str(int(float(self.num)))
        
                self.lbl_1.configure(text='|'+self.char_str+'|')
                self.lbl_2.configure(text=self.num)

        except (ValueError, TypeError):
            self.lbl_2.configure(text='Invalid Input')

        self.char_str=self.num

    def factorial(self):
        try:
            if len(self.char_str)>0:
                self.num=str(math.factorial(float(self.char_str)))
                if self.num.count('.')>0 and self.num.endswith('0'):
                        self.num=str(int(float(self.num)))
        
                self.lbl_1.configure(text=self.char_str+'!')
                self.lbl_2.configure(text=self.num)
                
        except (ValueError, TypeError):
            self.lbl_2.configure(text='Invalid Input')

        self.char_str=self.num

    def percent(self):
        pass
    
root=Tk()
calculator=Calculator(root)
root.mainloop()
