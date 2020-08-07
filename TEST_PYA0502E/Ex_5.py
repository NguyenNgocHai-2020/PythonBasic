class Person:

    def __init__(self, name, birth, email, address):
        self.Name = name
        self.Birth = birth
        self.Email = email
        self.Address = address

    def Show_info(self):
        print("Tên : ", self.Name)
        print("Năm sinh : ", self.Birth)
        print("Email : ", self.Email)
        print("Địa chỉ ", self.Address)


class Course:

    def __init__(self, name_course, language):
        self.Name_Course = name_course
        self.Language = language

    def Show_Course(self):
        print("Tên khóa học : ", self.Name_Course)
        print("Ngôn ngữ lập trình : ", self.Language)


class Student(Person, Course):

    def __init__(self, id, name, birth, email, address, university, name_course, language):
        Person.__init__(self,name, birth, email, address)
        Course.__init__(self, name_course, language)
        self.ID = id
        self.University = university

    def Show_info(self):
        print("Mã sinh viên ", self.ID)
        Person.Show_info(self)
        print("Trường đại học : ", self.University)
        Course.Show_Course(self)