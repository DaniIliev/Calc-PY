import math
import tkinter as tk

sum = ''
memory = 0
number = ''

def addNumber(value):
  global number
  global sum
  number += str(value)
  sum += str(value)
  textResult.config(text=sum)  


def addOperator(operator):
    print(operator)
    global number
    global sum 
    global memory
    textMemory.config(text='Memory: {}'.format(memory))
    
    if(operator == "+"):
        sum = sum + "+"
    elif(operator == "-"):
        sum = sum  + "-"
    elif(operator == "×"):
        sum = sum + "*"
    elif(operator == "÷"):
        sum = sum + "/"
    elif(operator == "%"):
        length = len(str(number))
        sum = sum[:-int(length)]
        print(type(number))
        sum = sum + str(float(number) / 100)
    elif(operator == "√"):
        length = len(str(number))
        sum = sum[:-int(length)]
        sum = sum + str(math.sqrt(float(number)))
    elif(operator == "yˣ"):
        sum += "**"
    elif(operator == '('):
        sum = sum + "("
    elif(operator == ')'):
        sum = sum  + ")"
    elif(operator == ","):
        sum = sum + "."
    elif(operator == "MC"):
        memory = 0
        textMemory.config(text='Memory: {}'.format(memory))
    elif(operator == "MR"):
        print("The number in memory is", memory)
    elif(operator == "MS"):
        sum = str(eval(sum))
        print('save memory', sum)
        memory = float(sum)
        textMemory.config(text='Memory: {}'.format(memory))
        number = ''
    elif(operator == "M+"):
        sum = str(eval(sum))
        memory += float(sum)
        textMemory.config(text='Memory: {}'.format(memory))
    elif(operator == "M-"):
        sum = str(eval(sum))
        memory -= float(sum)
        textMemory.config(text='Memory: {}'.format(memory))
    elif(operator == "C"):
        print('reset')
        sum = ''
        print(sum)
    elif(operator == "CE"):
        sum = sum[:-1]
        print(sum)
    elif(operator == "="):
        result = eval(sum)
        textResult.config(text=result)  
        sum = str(result)
    else:
        print("Invalid operator!")
    number = ''
    textResult.config(text=sum)  
    


def calculator():  
    global sum 
    memory = 0
    isSpecial = False
    isMemoUse = False
    isTrue = True
    
    while(isTrue): 
        if((isMemoUse == False) and (isSpecial == False)):
            try:
                float(number)
            except:
                print("Error")
                continue
        else:
            number = ''
            isMemoUse = False
            isSpecial = False
  
root = tk.Tk()
root.title('Calculator App')
root.geometry("500x350")

textResult = tk.Label(root,text="", font=('Arial', 30)  ,borderwidth=2,relief="groove", width=20)
textResult.grid(columnspan=7)

textMemory = tk.Label(root,text="Memory: 0", font=('Arial', 16) , width=20)
textMemory.grid(columnspan=5)

CE_button = tk.Button(root, text='CE', command=lambda:addOperator('CE'), width=5,height=2)
CE_button.grid(row=2, column=2)

C_button = tk.Button(root, text="C", command=lambda:addOperator('C'), width=5,height=2)
C_button.grid(row=2, column=1)

exponention_Button = tk.Button(root, text="yˣ", width=5, command=lambda:addOperator("yˣ"), height=2)
exponention_Button.grid(row=2, column=5)


prozent_Button = tk.Button(root, text='％', command=lambda:addOperator('%'), width=5, height=2)
prozent_Button.grid(row=2, column=3)

sqrt_Button = tk.Button(root,text="√", command=lambda:addOperator('√'),width=5, height=2)
sqrt_Button.grid(row=2, column=4)

mc_button = tk.Button(root, text="MC", command=lambda:addOperator('MC'), width=5, height=2)
mc_button.grid(row=3, column=1)

mr_button = tk.Button(root,text="MR", command=lambda:addOperator('MR'), width=5, height=2)
mr_button.grid(row=3, column=2)

ms_button = tk.Button(root, text="MS", command=lambda:addOperator('MS'), width=5,height=2)
ms_button.grid(row=3, column=3)

m_add_button = tk.Button(root, text="M+", command=lambda:addOperator('M+'), width=5,height=2)
m_add_button.grid(row=3, column=4)

m_subst_button = tk.Button(root, text="M-", command=lambda:addOperator('M-'),width=5,height=2)
m_subst_button.grid(row=3, column=5)


button1 = tk.Button(root, text="1", command=lambda:addNumber(1), width=5,height=2)
button1.grid(row=4, column=1)

button2 = tk.Button(root, text="2", command=lambda:addNumber(2), width=5,height=2)
button2.grid(row=4, column=2)


button3 = tk.Button(root, text="3", command=lambda:addNumber(3), width=5,height=2)
button3.grid(row=4, column=3)

addition = tk.Button(root, text="+",  command=lambda:addOperator('+'), width=5,height=2)
addition.grid(row=5, column=4)


substraction = tk.Button(root, text="-",  command=lambda:addOperator('-'), width=5,height=2)
substraction.grid(row=5, column=5)

multiplication = tk.Button(root, text="×",  command=lambda:addOperator('×'), width=5,height=2)
multiplication.grid(row=6, column=4)

division = tk.Button(root, text="÷", command=lambda:addOperator('÷'), width=5,height=2)
division.grid(row=6, column=5)

buttonBracketRight = tk.Button(root, text="(", command=lambda:addOperator('('), width=5,height=2)
buttonBracketRight.grid(row=4, column=4)

buttonBracketLeft = tk.Button(root, text=")", command=lambda:addOperator(')'), width=5,height=2)
buttonBracketLeft.grid(row=4, column=5)

result = tk.Button(root, text="=", width=14, command=lambda:addOperator('='),height=2)
result.grid(row=7, column=4, columnspan=5,)


button4 = tk.Button(root, text="4", command=lambda:addNumber(4), width=5,height=2)
button4.grid(row=5, column=1)


button5 = tk.Button(root, text="5", command=lambda:addNumber(5), width=5,height=2)
button5.grid(row=5, column=2)


button6 = tk.Button(root, text="6", command=lambda:addNumber(6),width=5,height=2)
button6.grid(row=5, column=3)


button7 = tk.Button(root, text="7", command=lambda:addNumber(7), width=5,height=2)
button7.grid(row=6, column=1)


button8 = tk.Button(root, text="8", command=lambda:addNumber(8), width=5,height=2)
button8.grid(row=6, column=2)


button9 = tk.Button(root, text="9", command=lambda:addNumber(9), width=5,height=2)
button9.grid(row=6, column=3)

button0 = tk.Button(root, text="0", command=lambda:addNumber(0), width=15,height=2)
button0.grid(row=7, column=1, columnspan=2)

buttonComa = tk.Button(root, text=",", command=lambda:addOperator(","), width=5,height=2)
buttonComa.grid(row=7, column=3)

root.mainloop()