
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = "last_name"
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
        {
             "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
             "id": self._generateId(),
            "first_name": "Jimmmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    jackson_family = FamilyStructure("Jackson")
    def add_member(member):
        new_member = {
            "id": jackson_family._generateId(),
            "first_name": member.get("first_name", ""),
            "last_name": jackson_family.last_name,
            "age": member.get("age", 0),
            "lucky_numbers": member.get("lucky_numbers", [])
         }
        jackson_family._members.append(new_member)

   
    def delete_member(id):
        for i in range(len(jackson_family._members)):
            if jackson_family._members[i]["id"] == id:
                del jackson_family._members[i]
                return True
        return False

   
    def update_member(id,member):
        for i, m in enumerate(jackson_family._members):
            if m["id"]== id:
                member["id"]= id
                member["last_name"]=jackson_family.last_name
                jackson_family._members[i]={
                    "id": member["id"],
                    "first_name": membe.get("first_name",m["first_name"]),
                    "last_name": member.get("last_name",m["last_name"]),
                    "age": member.get("age",m["age"]),
                    "lucky_numbers": member.get("lucky_numbers",m["lucky_numbers"])
                }
                return True
        return False

 
    def get_member(self, id):
        for member in jackson_family._members:
            if member["id"] == id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return jackson_family._members

    