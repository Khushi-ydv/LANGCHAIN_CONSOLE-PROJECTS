from pydantic import BaseModel , EmailStr
from typing import Optional 
class Student(BaseModel):
    # name : str
    name : str='khushi'
    age :Optional[int]=None
    email : Optional[EmailStr]=None
    
    
new_student : Student={'age':20 , 'email':'abc@gmail.com'}
student=Student(**new_student)

# print(type(student))
print(student)
