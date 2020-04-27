import xlrd
import connection


course_selections_file = xlrd.open_workbook('Data/Course_selections_2019.xlsx', encoding_override='utf-8')
sheet = course_selections_file.sheet_by_index(0)

months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in range(25343,sheet.nrows):
	row = sheet.row_values(i)
	if row[-1]!='':
		proper_date = row[-1]
		day = proper_date[0:2]
		month = proper_date[3:6]
		if month in months:
			month = str(months.index(month)+1)
		proper_date = day+"/"+month+"/"+row[-1][7:9]
	else:
		proper_date = ""	
	proper_id = row[10]
	if row[10]=='':
		proper_id = 0
	if row[6]=='':
		row[6]=0
	print(row[0],row[1],int(float(row[2])),row[3],row[4],row[6],row[7],row[8],proper_id,proper_date)
	c = connection.cursor.execute("insert into course_selections values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(row[0],row[1],int(float(row[2])),int(float(row[3])),row[4],int(row[6]),row[7],row[8],int(float(proper_id)),proper_date))
	
	connection.connection.commit()
