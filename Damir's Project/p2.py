import xlrd
import connection


course_schedule_file = xlrd.open_workbook('Data/Course_sections.xlsx', encoding_override='utf-8')
sheet = course_schedule_file.sheet_by_index(0)


months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	
for i in range(1,sheet.nrows):
	row = sheet.row_values(i)
	if row[-2]!='':
			proper_date = row[-2]
			day = proper_date[0:2]
			month = proper_date[3:6]
			if month in months:
				month = str(months.index(month)+1)
			proper_date = day+"/"+month+"/"+row[-2][7:-2]
	else:
			proper_date = ''
	
	#print(row)
	#print(row[0],row[1],int(row[2]),int(row[3]),row[4],row[5],int(row[6]),row[7],row[8],row[9],int(row[10]),proper_date,row[12])
	try:
		c = connection.cursor.execute("insert into course_sections values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(row[0],row[1],int(row[2]),int(row[3]),row[4],row[5],int(row[6]),row[7],row[8],row[9],int(row[10]),proper_date,row[12]))
		connection.connection.commit()
	except:
		print("row missed",i)