try:
    import tkinter
except ImportError:     # python 2
    import Tkinter as tkinter

from calculator_functions import global_clear, local_clear, add, subtract, multiply, divide, equals, number_insert

from functools import partial

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry("240x320")
mainWindow["padx"] = 36
mainWindow["pady"] = 72
mainWindow.resizable(False, False)

# Columns
for column in range(4):
    mainWindow.columnconfigure(column, weight=1)

# Rows
for row in range(6):
    mainWindow.rowconfigure(row, weight=1)

# Result entry
resultFrame = tkinter.LabelFrame(mainWindow, text="Result")
resultFrame.grid(row=0, column=0, columnspan=4, rowspan=1)

result = tkinter.Entry(resultFrame)
result.grid(row=0, column=0)

# Keys
keyFrame = tkinter.Frame(mainWindow)
keyFrame.grid(row=1, column=0, columnspan=4, rowspan=5)

keyPad = [[('C', 1, "global_clear"), ('CE', 1, "local_clear"), ],
          [('7', 1, ""), ('8', 1, ""), ('9', 1, ""), ('+', 1, "add"), ],
          [('4', 1, ""), ('5', 1, ""), ('6', 1, ""), ('-', 1, "subtract"), ],
          [('1', 1, ""), ('2', 1, ""), ('3', 1, ""), ('*', 1, "multiply"), ],
          [('0', 1, ""), ('=', 2, "equals"), ('/', 1, "divide"), ],
          ]  # key values, spans, *operations

first_term = final_result = 0
operation = ""
rowCounter = 0
for keyRow in keyPad:
    columnCounter = 0
    for key in keyRow:
        # Binding commands to buttons
        action = None
        if key[2] != "":
            if key[2] == "global_clear":
                action = partial(global_clear, result)
            if key[2] == "local_clear":
                action = partial(local_clear, result)
            if key[2] == "add":
                action = partial(add, result)
            if key[2] == "subtract":
                action = partial(subtract, result)
            if key[2] == "multiply":
                action = partial(multiply, result)
            if key[2] == "divide":
                action = partial(divide, result)
            if key[2] == "equals":
                action = partial(equals, result)
        else:
            action = partial(number_insert, result, key[0])
        keyButton = tkinter.Button(keyFrame, text=key[0], command=action)

        keyButton.grid(row=rowCounter, column=columnCounter, sticky="nsew", columnspan=key[1])
        columnCounter += key[1]     # incrementing by column span
    rowCounter += 1

mainWindow.mainloop()
