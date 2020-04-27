from tkinter import *
from functools import partial
import connection

a = Tk()
a.geometry("400x400")
a.title("DB final project")

def task1():
	global task1query
	new = Tk()
	new.geometry("600x600")
	lab1 = Label(new,text="Find most popular courses for semester (You should pass a number of semester and year, and output list of courses with teachers )").grid(row=0,column=0)
	year = StringVar()
	semester = StringVar()
	yearEntry = Entry(new, textvariable=year).grid(row=1, column=0)
	semestrEntry = Entry(new, textvariable=semester).grid(row=2, column=0)
	task1query = partial(task1query, year, semester)
	searchButton = Button(new, text="Find", command=task1query).grid(row=4, column=0)  
	


def task1query(year,semester):
	new2 = Tk()
	new2.geometry("800x400")
	new2.title("Query result")
	c = connection.cursor.execute("select emp_id, count(subject_code) from course_sections where subject_year=2015  group by subject_code, emp_id order by count(subject_code) desc").fetchall()
	for i in range(len(c)):
		l = Label(new2,text=c[i]).grid(row=i,column=0)
	

def task2():
	global task2query
	new = Tk()
	new.geometry("600x600")
	lab1 = Label(new,text="Find most popular teacher in section for semester (You should pass a number of semester and year and code of subject, and output teacher practice and lecture").grid(row=0,column=0)
	year = StringVar()
	semester = StringVar()
	yearEntry = Entry(new, textvariable=year).grid(row=1, column=0)
	semestrEntry = Entry(new, textvariable=semester).grid(row=2, column=0)
	task2query = partial(task2query, year, semester)
	searchButton = Button(new, text="Find", command=task2query).grid(row=4, column=0)  
	


def task2query(year,semester):
	new2 = Tk()
	new2.geometry("800x400")
	new2.title("Query result")
	c = connection.cursor.execute("select practice_teacher,count(practice_teacher) from course_selections where practice_teacher!=0 and subject_year=2016 and subject_term=1  group by practice_teacher order by count(practice_teacher) desc").fetchall()
	for i in range(len(c)):
		l = Label(new2,text=c[i]).grid(row=i,column=0)
	



def task3():
	global task3query
	new = Tk()
	new.geometry("600x600")
	lab1 = Label(new,text="Calculate GPA of student for the semester and total").grid(row=0,column=0)
	year = StringVar()
	semester = StringVar()
	yearEntry = Entry(new, textvariable=year).grid(row=1, column=0)
	semestrEntry = Entry(new, textvariable=semester).grid(row=2, column=0)
	task3query = partial(task3query, year, semester)
	searchButton = Button(new, text="Find", command=task3query).grid(row=4, column=0)  
	


def task3query(year,semester):
	new2 = Tk()
	new2.geometry("800x400")
	new2.title("Query result")
	c = connection.cursor.execute("select student_id,total_mark, subject_code  from course_selections group by subject_code,student_id,total_mark").fetchall()
	for i in range(len(c)):
		l = Label(new2,text=c[i]).grid(row=i,column=0)
	


def task4():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")

def task5():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")

def task6():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")

def task7():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")

def task8():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")

def task9():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")

def task10():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")

def task11():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")

def task12():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")

def task13():
	new = Tk()
	new.geometry("600x600")
	
	print("here we go")


lbl1 = Label(a,text="Task 1 ->").grid(row=0,column=0)
task1 = partial(task1)
b = Button(a,text="TASK ONE",command=task1).grid(row=0,column=1)

lbl2 = Label(a,text="Task 2 ->").grid(row=1,column=0)
task2 = partial(task2)
b2= Button(a,text="TASK TWO",command=task2).grid(row=1,column=1)

lbl3 = Label(a,text="Task 3 ->").grid(row=2,column=0)
task3 = partial(task3)
b3 = Button(a,text="TASK THREE",command=task3).grid(row=2,column=1)

lbl4 = Label(a,text="Task 4 ->").grid(row=3,column=0)
task4 = partial(task4)
b4 = Button(a,text="TASK FOUR",command=task4).grid(row=3,column=1)

lbl5 = Label(a,text="Task 5 ->").grid(row=4,column=0)
task5 = partial(task5)
b5 = Button(a,text="TASK FIVE",command=task5).grid(row=4,column=1)

lbl6 = Label(a,text="Task 6 ->").grid(row=5,column=0)
task6 = partial(task6)
b6 = Button(a,text="TASK SIX",command=task6).grid(row=5,column=1)

lbl7 = Label(a,text="Task 7 ->").grid(row=6,column=0)
task7 = partial(task7)
b7 = Button(a,text="TASK SEVEN",command=task7).grid(row=6,column=1)

lbl8 = Label(a,text="Task 8->").grid(row=7,column=0)
task8 = partial(task8)
b8 = Button(a,text="TASK EIGHT",command=task8).grid(row=7,column=1)

lbl9 = Label(a,text="Task 9 ->").grid(row=8,column=0)
task9 = partial(task9)
b9 = Button(a,text="TASK NINE",command=task9).grid(row=8,column=1)

lbl10 = Label(a,text="Task 10 ->").grid(row=9,column=0)
task10 = partial(task10)
b10 = Button(a,text="TASK TEN",command=task10).grid(row=9,column=1)

lbl11 = Label(a,text="Task 11").grid(row=10,column=0)
task11 = partial(task11)
b11 = Button(a,text="TASK ELEVEN",command=task11).grid(row=10,column=1)

lbl12 = Label(a,text="Task 12 ->").grid(row=11,column=0)
task12 = partial(task12)
b12 = Button(a,text="TASK TWELVE",command=task12).grid(row=11,column=1)

lbl13 = Label(a,text="Task 13 ->").grid(row=12,column=0)
task13 = partial(task13)
b13 = Button(a,text="TASK THIRTEEN",command=task13).grid(row=12,column=1)

a.mainloop()


