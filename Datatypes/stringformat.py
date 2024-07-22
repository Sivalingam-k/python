student_name =input('Enter Your Name:')
student_id=int(input('Enter your id card Number:'))
# print("student_name :",student_name,"studentid:",student_id)
print('Methods Type:')
print('1.Title')
print(f"student_name :{student_name.title()} \nstudentid:,{student_id}")
print()
print('1.Upper')
print(f"student_name :{student_name.upper()} \nstudentid:,{student_id}")
print()
print('1.Lower')
print(f"student_name :{student_name.lower()} \nstudentid:,{student_id}")
print()

#Format method

print('Student_Name :{} \n Student_id:{}'.format(student_name,student_id))  #output: name=siva id=123
print('Student_Name :{} \n Student_id:{}'.format(student_id,student_name))  #output: name=123 id=siva