from typing import TypedDict

class person (TypedDict):
    name : str
    age :int
    
new_person : person ={
    'name':'Khushi',
    'age':20
}
print(new_person)