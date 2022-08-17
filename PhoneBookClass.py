class Entry:
  def __init__(self, name, phonenumber, next=None): 
    self.name = name
    self.phonenumber = phonenumber
    self.next = next

class PhoneBook:
  def __init__(self):  
    self.head = None


  def insert(self, name, phonenumber):
    newEntry = Entry(name, phonenumber)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newEntry
    else: 
      self.head = newEntry

  def inserthead(self, name, phonenumber):
    newEntry = Entry(name, phonenumber)
    newEntry.next = self.head
    self.head = newEntry

  def delete(self, name):
    pointer1 = self.head
    if self.head is None:
      return
    elif pointer1.name == name:
      self.head = pointer1.next
      return
    else:
        while pointer1 != None:
          if pointer1.name == name:
            pointer2.next = pointer1.next
            pointer1.next = None
            break
          else:
            pointer2 = pointer1
            pointer1 = pointer1.next

  def searchbyname(self, name):
    p1 = self.head
    while p1 is not None:
        if p1.name == name:
          return p1.phonenumber
        p1 = p1.next

  def searchbynumber(self, number):
    p1 = self.head
    while p1 is not None:
      if p1.phonenumber == number:
        return p1.name
      p1 = p1.next

  def sort(self):
    if self.head is not None and self.head.next is not None:
      p1 = self.head
      p2 = p1.next
      p3 = self.head
      size = 1
      while p3.next is not None:
        p3 = p3.next
        size = size + 1
      p3 = Entry("dummy", 0)
      while size > 1:
        while p1.next is not None:
          if p1.name > p2.name:
            p3.name = p1.name
            p3.phonenumber = p1.phonenumber
            p1.name = p2.name
            p1.phonenumber = p2.phonenumber
            p2.name = p3.name
            p2.phonenumber = p3.phonenumber
          p1 = p2
          p2 = p2.next
        p1 = self.head
        p2 = p1.next
        size = size - 1

  def updatename(self, oldname, newname):
    p1 = self.head
    size = 1
    while p1.next is not None:
      p1 = p1.next
      size = size + 1  
    p1 = self.head
    while size != 0:
      if p1.name == oldname:
        p1.name = newname
        size = 0
      else:
        size = size - 1
        p1 = p1.next

def updatephonenumber(self, oldname, newnumber):
    p1 = self.head
    size = 1
    while p1.next is not None:
      p1 = p1.next
      size = size + 1  
    p1 = self.head
    while size != 0:
      if p1.name == oldname:
        p1.phonenumber = newnumber
        size = 0
      else:
        size = size - 1
        p1 = p1.next

def reverse(self):
  if self.head is not None and self.head.next is not None:
    p1 = self.head
    p2 = p1.next
    p3 = p2.next
    p1.next = None
    while p2.next is not None:
      p2.next = p1
      p1 = p2
      p2 = p3
      p3 = p3.next
    p2.next = p1
    self.head = p2

  def print(self):
    current = self.head
    while(current):
      print(current.name)
      print(current.phonenumber)
      current = current.next