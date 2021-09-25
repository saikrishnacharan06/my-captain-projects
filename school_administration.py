import csv
def write_csv(info_list):
	with open('student_info.csv','a',newline='') as csv_file:
		writer=csv.writer(csv_file)
		if csv_file()==0:
			writer.writerow(['name','age','contact_no','e-mail'])
		writer.writerow(info_list)
if __name__=='__main__':
	condition=True
	stu_num=1		
condition=True
while condition:
 stu_info=input('enter your information in the format (name,age,contact_n0,e-mail: ').format('split')
 stu_info_list=stu_info.split(' ')
 print('\n entered info list is:\nname: {}\nage: {}\nconract_no: {}\ne-mail: {}'.format(stu_info_list[0],stu_info_list[1],stu_info_list[2],stu_info_list[3]))
 choice_check=input('is the info correct yes/no ')
 if choice_check=='yes':
	 write_info_csv(stu_info_list)
	 ef=input('yes-if you wanna enter info of other student,no-if you dont want to: ')
     if ef=='yes':
	  condition=True
	  student_num=student_num+1
     elif ef=='no':
	  condition=False
 elif choice_check=='no':
	 print('\nplease re-enter the values')
