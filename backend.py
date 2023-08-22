import sqlite3

try:
    conn = sqlite3.connect("library.db")
except Exception as e:
    print(f"Failed to connect\n{e}")
    exit(0)

mycursor = conn.cursor()


def create_tables():
    admin_info_tbl = """CREATE TABLE `admin_info` (
                    `id` INTEGER PRIMARY KEY,
                    `usrname` varchar(45) NOT NULL,
                    `passwd` varchar(45) NOT NULL,
                    UNIQUE (`usrname`)
                    );"""
    mycursor.execute(admin_info_tbl)

    lib_reg_tbl = """CREATE TABLE `lib_reg` (
                `lib_id` INTEGER PRIMARY KEY AUTOINCREMENT,
                `fname` varchar(45) NOT NULL,
                `lname` varchar(45) NOT NULL,
                `gen` varchar(10) NOT NULL,
                `dob`TIMESTAMPNOT NULL,
                `email` varchar(45) NOT NULL,
                `phno` varchar(45) NOT NULL,
                `lib_address` varchar(145) NOT NULL,
                `lib_user` varchar(45) NOT NULL,
                `lib_pass` varchar(45) NOT NULL,
                `pfp_path` longtext,
                UNIQUE (`lib_user`),
                UNIQUE (`email`)
                );"""
    mycursor.execute(lib_reg_tbl)

    student_reg_tbl = """CREATE TABLE `student_reg` (
                    `sid` INTEGER PRIMARY KEY AUTOINCREMENT,
                    `fname` varchar(45) NOT NULL,
                    `lname` varchar(45) NOT NULL,
                    `gen` varchar(10) NOT NULL,
                    `dob`TIMESTAMPNOT NULL,
                    `father_name` varchar(45) NOT NULL,
                    `email` varchar(45) NOT NULL,
                    `phno` varchar(45) NOT NULL,
                    `address` varchar(45) NOT NULL,
                    `pfp_path` longtext,
                    UNIQUE (`email`)
                    );"""
    mycursor.execute(student_reg_tbl)
    mycursor.execute("insert into student_reg values(100,'a','a','a','2023-01-01','a','a','a','a','a')")
    mycursor.execute("delete from student_reg where sid=100")


    books_tbl = """CREATE TABLE `books` (
                `book_id` INTEGER PRIMARY KEY AUTOINCREMENT,
                `isbn` varchar(45) NOT NULL,
                `title` varchar(45) NOT NULL,
                `author` varchar(45) NOT NULL,
                `publisher` varchar(45) NOT NULL,
                `edition` varchar(45) NOT NULL,
                `avail_copies` INTEGER NOT NULL,
                `issued_copies` INTEGER NOT NULL DEFAULT '0',
                `total_copies` INTEGER NOT NULL,
                UNIQUE (`isbn`)
                );"""
    mycursor.execute(books_tbl)
    mycursor.execute("insert into books values(1000, 'a', 'a', 'a', 'a', 'a', 1, 1, 1)")
    mycursor.execute("delete from books where book_id=1000")

    issued_books_tbl = """CREATE TABLE `issued_books` (
                    `book_id` INTEGER NOT NULL,
                    `sid` INTEGER NOT NULL,
                    `issue_date`TIMESTAMPNOT NULL,
                    `due_date`TIMESTAMPNOT NULL,
                    `copies` INTEGER NOT NULL,
                    PRIMARY KEY (`book_id`,`sid`),
                    CONSTRAINT `issue_book_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`),
                    CONSTRAINT `issue_sid` FOREIGN KEY (`sid`) REFERENCES `student_reg` (`sid`)
                    );"""
    mycursor.execute(issued_books_tbl)
    
    returned_books_tbl = """CREATE TABLE `returned_books` (
                        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                        `book_id` INTEGER NOT NULL,
                        `sid` INTEGER NOT NULL,
                        `issue_date`TIMESTAMPDEFAULT NULL,
                        `due_date`TIMESTAMPDEFAULT NULL,
                        `return_date`TIMESTAMPNOT NULL,
                        `fine` INTEGER DEFAULT NULL
                        );"""
    mycursor.execute(returned_books_tbl)

    fine_rate_tbl = """CREATE TABLE `fine_rate` (
                    `id` INTEGER PRIMARY KEY,
                    `fine` INTEGER NOT NULL
                    );"""
    mycursor.execute(fine_rate_tbl)

    mycursor.execute("insert into admin_info values(1, 'root', '123')")
    mycursor.execute("insert into fine_rate values(1, 5)")

    conn.commit()
try:
    mycursor.execute("select * from admin_info")
except Exception as e:
    create_tables()


def populate_tables():
    populate_books = """INSERT INTO `books` VALUES (1001,'1375649302846','ML using Python','Aman','Aman Publications','5th',10,0,10),(1002,'9780131872486','Thinking in Java','Bruce Eckel','Pearson','4th',5,0,5),(1003,'9780008471286','The Lord of the Rings','J.R.R. Tolkien','HarperCollins','Single Volume Illustrated',5,0,5),(1004,'9781593279288','Python Crash Course','Eric Matthes','No Starch Press','2nd',20,0,20),(1005,'9781838987572','Node.js Web Development','David Herron','Packt Publishing','5th',50,0,50),(1006,'9788175993259',"Gulliver\'s Travels",'Jonathan Swift','Fingerprint! Publishing','NA',30,0,30),(1007,'9780008118044','Hobbit','J.R.R. Tolkien','HarperCollins','Film tie-in edition',24,1,25),(1008,'9781401237554','Fables Vol. 1','Bill Willingham','DC Comics','2012',39,1,40),(1009,'9781684158638','Power Rangers Vol. 5','Ryan Parrot','Boom! Studios','NA',80,0,80),(1010,'9788131708088','Neural Networks','James A. Freeman','Pearson Education','1',20,0,20),(1011,'9780137470358','Learning Deep Learning','Magnus Ekman','Pearson Education','NA',79,1,80),(1012,'9781582407111','Invincible Vol. 1','Robert Kirkman','Image Comics','NA',9,1,10),(1013,'9788177091878','Concepts of Physics V. 1','H.C. Verma','Bharati Bhavan','1st',75,0,75),(1014,'9780321584106','Eloquent Ruby','Russ Olsen','Addison-Wesley','1',80,0,80);"""
    mycursor.execute(populate_books)
    populate_librarians = """INSERT INTO `lib_reg` VALUES (1,'John','Wick','M','1992-10-18','john@gmail.com','7018631283','NYC','john','john123', NULL);"""
    mycursor.execute(populate_librarians)
    populate_students = """INSERT INTO `student_reg` VALUES (101,'Peter','Parker','M','2000-04-01','Richard Parker','peterbparker@gmail.com','9837623762','NYC',''),(102,'Amit','Kumar','M','2004-07-22','Ram Singh','amitk227@gmail.com','7029748784','Mandi, H.P.',NULL),(103,'Rahul','Kumar','M','2000-09-28','Goverdhan Singh','rahul28mandi@gmail.com','8848593640','Mandi, H.P.',NULL),(104,'Ruhi','Singh','F','2005-12-10','Prem Singh','ruhi2006@gmail.com','7028373863','Rishikesh, Uttarakhand',NULL),(105,'Neha','Thakur','F','2006-08-04','Lalman Sharma','neha123@gmail.com','9870654321','Shimla, H.P.',NULL),(106,'Monika','Sharma','F','2006-06-26','Raj Kumar','monaa123@gmail.com','8234509873','Kullu, H.P.',NULL),(107,'Mukesh','Kumar','M','2005-01-26','Sanjay Kumar','mk2005@gmail.com','8274897813','Mandi, H.P.',NULL),(108,'Ajay','Kumar','M','2004-10-06','Vijay Kumar','ajay2004@gmail.com','9837847873','Agra, U.P.',NULL);"""
    mycursor.execute(populate_students)
    conn.commit()

# populate_tables()



def add_librarian(fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass, pfp_path):
    if pfp_path==None:
        query = "insert into lib_reg(fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass) values(?,?,?,?,?,?,?,?,?)"
        mycursor.execute(query, (fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass))
    else:
        query = "insert into lib_reg(fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass, pfp_path) values(?,?,?,?,?,?,?,?,?,?)"
        mycursor.execute(query, (fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass, pfp_path))
    conn.commit()

def search_librarian(libID):
    mycursor.execute(f"select lib_id, fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass from lib_reg where lib_id={libID}")
    return mycursor.fetchone()

def edit_librarian(libID, fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass, pfp_path):
    if pfp_path!=None:
        query = "update lib_reg set fname=?, lname=?, gen=?, dob=?, email=?, phno=?, lib_address=?, lib_user=?, lib_pass=?, pfp_path=? where lib_id=?"
        mycursor.execute(query, (fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass, pfp_path, libID))
    else:
        query = "update lib_reg set fname=?, lname=?, gen=?, dob=?, email=?, phno=?, lib_address=?, lib_user=?, lib_pass=?, pfp_path=NULL where lib_id=?"
        mycursor.execute(query, (fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass, libID))
    conn.commit()

def delete_librarian(libID):
    mycursor.execute(f"delete from lib_reg where lib_id={libID}")
    conn.commit()

def admin_info(usrname):
    mycursor.execute(f"select usrname, passwd from admin_info where usrname='{usrname}'")
    return mycursor.fetchone()

def librarian_info(usrname):
    mycursor.execute(f"select lib_id, fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass from lib_reg where lib_user='{usrname}'")
    return mycursor.fetchone()

def add_student(fname, lname, gen, dob, fathername, email, phno, address, pfp_path):
    if pfp_path==None:
        query = "insert into student_reg(fname, lname, gen, dob, father_name, email, phno, address) values(?,?,?,?,?,?,?,?)"
        mycursor.execute(query, (fname, lname, gen, dob, fathername, email, phno, address))
    else:
        query = "insert into student_reg(fname, lname, gen, dob, father_name, email, phno, address, pfp_path) values(?,?,?,?,?,?,?,?,?)"
        mycursor.execute(query, (fname, lname, gen, dob, fathername, email, phno, address, pfp_path))
    conn.commit()

def search_student(sid):
    mycursor.execute(f"select sid, fname, lname, gen, dob, father_name, email, phno, address from student_reg where sid={sid}")
    return mycursor.fetchone()

def delete_student(sid):
    mycursor.execute(f"delete from student_reg where sid={sid}")
    conn.commit()

def edit_student(sid, fname, lname, gen, dob, fathername, email, phno, address, pfp_path):
    if pfp_path!=None:
        query = "update student_reg set fname=?, lname=?, gen=?, dob=?, father_name=?, email=?, phno=?, address=?, pfp_path=? where sid=?"
        mycursor.execute(query, (fname, lname, gen, dob, fathername, email, phno, address, pfp_path, sid))
    else:
        query = "update student_reg set fname=?, lname=?, gen=?, dob=?, father_name=?, email=?, phno=?, address=?, pfp_path=NULL where sid=?"
        mycursor.execute(query, (fname, lname, gen, dob, fathername, email, phno, address, sid))
    conn.commit()

def add_new_book(isbn, book_title, author, publisher, edition, total_copies):
    query = "insert into books(isbn, title, author, publisher, edition, avail_copies, total_copies) values(?, ?, ?, ?, ?, ?, ?)"
    mycursor.execute(query, (isbn, book_title, author, publisher, edition, total_copies, total_copies))
    conn.commit()

def add_book_copies(bookID, copies):
    mycursor.execute(f"update books set avail_copies=avail_copies+{copies}, total_copies=total_copies+{copies} where book_id={bookID}")
    conn.commit()

def search_book(bookID):
    mycursor.execute(f"select isbn, title, author, publisher, edition, total_copies from books where book_id={bookID}")
    return mycursor.fetchone()

def search_book_for_copies(bookID):
    mycursor.execute(f"select isbn, title, author, publisher, edition, avail_copies from books where book_id={bookID}")
    return mycursor.fetchone()

def delete_new_book(bookID):
    mycursor.execute(f"delete from books where book_id={bookID}")
    conn.commit()

def delete_book_copies(bookID, copies):
    mycursor.execute(f"update books set avail_copies=avail_copies-{copies}, total_copies=total_copies-{copies} where book_id={bookID}")
    conn.commit()

def edit_book(bookID, isbn, book_title, author, publisher, edition):
    query = "update books set isbn=?, title=?, author=?, publisher=?, edition=? where book_id=?"
    mycursor.execute(query, (isbn, book_title, author, publisher, edition, bookID))
    conn.commit()

def search_book_issue(bookID):
    mycursor.execute(f"select isbn, title, author, publisher, edition, avail_copies from books where book_id={bookID}")
    return mycursor.fetchone()

def search_student_issue(sid):
    mycursor.execute(f"select fname, lname, email, phno from student_reg where sid={sid}")
    return mycursor.fetchone()

def issue_book(bookID, sid, issue_date, due_date):
    mycursor.execute(f"insert into issued_books(book_id, sid, issue_date, due_date, copies) values({bookID}, {sid}, '{issue_date}', '{due_date}', 1)")
    mycursor.execute(f"update books set avail_copies=avail_copies-1, issued_copies=issued_copies+1 where book_id={bookID}")

    conn.commit()

def search_book_std_return(bookID, sid):
    mycursor.execute(f"select book_id, sid, issue_date, due_date, copies from issued_books where book_id={bookID} and sid={sid}")
    rows = mycursor.fetchone()
    if rows!=None:
        return 0
    return None

def search_dates(bookID, sid):
    mycursor.execute(f"select issue_date, due_date from issued_books where book_id={bookID} and sid={sid}")
    return mycursor.fetchone()

def return_book(bookID, sid, issue_date, due_date, return_date, fine):
    mycursor.execute(f"insert into returned_books(book_id, sid, issue_date, due_date, return_date, fine) values({bookID}, {sid}, '{issue_date}', '{due_date}', '{return_date}', {fine})")
    mycursor.execute(f"update books set avail_copies=avail_copies+1, issued_copies=issued_copies-1 where book_id={bookID}")
    mycursor.execute(f"delete from issued_books where book_id={bookID} and sid={sid}")

    conn.commit()


def search_book_full(bookID):
    mycursor.execute(f"select isbn, title, author, publisher, edition, total_copies from books where book_id={bookID}")
    bookRow = mycursor.fetchone()
    if bookRow!=None:
        mycursor.execute(f"select avail_copies from books where book_id={bookID}")
        avail_copies = mycursor.fetchone()

        issued_copies = int(bookRow[-1]) - int(avail_copies[0])
        issued_copies = (issued_copies,)

        row = bookRow+issued_copies+avail_copies
        return row
    return None

def show_librarians():
    mycursor.execute(f"select lib_id, fname, lname, gen, dob, email, phno, lib_address, lib_user, lib_pass from lib_reg")
    return mycursor.fetchall()

def show_students():
    mycursor.execute(f"select sid, fname, lname, gen, dob, father_name, email, phno, address from student_reg")
    return mycursor.fetchall()

def show_books():
    mycursor.execute(f"select book_id, isbn, title, author, publisher, edition, avail_copies, issued_copies, total_copies from books")
    return mycursor.fetchall()

def show_issued_books():
    mycursor.execute(f"select book_id, sid, issue_date, due_date from issued_books")
    return mycursor.fetchall()

def show_returned_books():
    mycursor.execute(f"select book_id, sid, issue_date, due_date, return_date, fine from returned_books")
    return mycursor.fetchall()

def get_librarian_pfp(libID):
    mycursor.execute(f"select pfp_path from lib_reg where lib_id={libID}")
    return mycursor.fetchone()

def get_student_pfp(sid):
    mycursor.execute(f"select pfp_path from student_reg where sid={sid}")
    return mycursor.fetchone()

def change_admin_info(username, new_username, new_password):
    query = "update admin_info set usrname=?, passwd=? where usrname=?"
    mycursor.execute(query, (new_username, new_password, username))
    conn.commit()

def get_recent_sid():
    mycursor.execute(f"select sid from student_reg order by sid")
    sid = mycursor.fetchall()[-1][0]
    return sid

def get_recent_libid():
    mycursor.execute(f"select lib_id from lib_reg order by lib_id")
    libid = mycursor.fetchall()[-1][0]
    return libid

def get_recent_bookid():
    mycursor.execute(f"select book_id from books order by book_id")
    bookid = mycursor.fetchall()[-1][0]
    return bookid

def get_issued_copies(bookID):
    mycursor.execute(f"select issued_copies from books where book_id={bookID}")
    return mycursor.fetchone()

def get_total_copies(bookID):
    mycursor.execute(f"select total_copies from books where book_id={bookID}")
    return mycursor.fetchone()

def get_fine_val():
    mycursor.execute(f"select fine from fine_rate where id=1")
    return mycursor.fetchone()

def edit_fine(new_fine):
    mycursor.execute(f"update fine_rate set fine={new_fine} where id=1")
    conn.commit()

def show_avail_books():
    mycursor.execute(f"select book_id, isbn, title, author, publisher, edition, avail_copies, issued_copies, total_copies from books order by issued_copies asc")
    return mycursor.fetchall()

def get_books_by_query(query):
    mycursor.execute(f"select book_id, isbn, title, author, publisher, edition, avail_copies, issued_copies, total_copies from books where title like '%{query}%' or author like '%{query}%' or publisher like '%{query}%' order by issued_copies asc")
    return mycursor.fetchall()

def clear_returned_books():
    mycursor.execute(f"truncate returned_books")
    return conn.commit()