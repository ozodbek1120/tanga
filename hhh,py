import pymysql

class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()
        
    def ConnectDB(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1120"
        )
        self.cursor=self.db.cursor()
    def CreateDB(self):
        self.cursor.execute("create database if not exists staff")
        self.cursor.execute("use staff")
    def CreateTB(self):
        self.cursor.execute("drop table if exists workers")
        self.cursor.execute("""Create table if not exists workers(
                            id int,
                            first_name varchar(50),
                            last_name varchar(50),
                            telefon_nomer varchar(100),
                            ishchi_id varchar(50),
                            maosh int)""")
    def InserTB(self,id,firt_name,last_name,telefon_nomer,ishchi_id,maosh):
        self.cursor.execute(f'''insert into workers values(
                            {id},
                            "{firt_name}",
                            "{last_name}",
                            "{telefon_nomer}",
                            "{ishchi_id}",
                            {maosh})''')
        self.db.commit()
    def FuulName(self):
        self.cursor.execute(f"SELECT CONCAT(first_name, ' ',  last_name) AS full_name  FROM workers")
        natija=self.cursor.fetchall()
        for i in natija:
            print(i)

    def ItProg(self):
        self.cursor.execute(f"SELECT CONCAT('ISM ',first_name, ' Familiya ',  last_name , ' maosh ' , maosh) AS full_name  FROM workers where ishchi_id='IT_PROG'")
        m=self.cursor.fetchall()
        for i in m:
            print(i)

    def maosh(self):
        self.cursor.execute(f"SELECT CONCAT('ishchi_id :', ishchi_id, ' Maosh : ',  maosh) AS full_name  FROM workers where maosh>5000 and maosh<20000")
        natija=self.cursor.fetchall()
        for i in natija:
            print(i)
    
    def maosh(self):
        self.cursor.execute(f"SELECT CONCAT('ISm :', ishchi_id, ' Maosh : ',  maosh) AS full_name  FROM workers name like ''")
        natija=self.cursor.fetchall()
        for i in natija:
            print(i)
    
    def phone(self):
        self.cursor.execute(f"SELECT *   FROM workers where telefon_nomer like '%6983'")
        natija=self.cursor.fetchall()
        for i in natija:
            print(i)
    
    def sum(self):
        self.cursor.execute(f"SELECT *   FROM workers ")
        natija=self.cursor.fetchall()
        sum=0
        for i in natija:
            sum+=i[5]
        print(f"Jami ishchilarning umumiy oyligi : {sum} ")
    
    def maosh(self):
        self.cursor.execute(f"SELECT * FROM workers where ishchi_id='IT_prog' order by maosh desc  ")
        natija=self.cursor.fetchone()
        print(natija)
    
    def Avg(self):
        self.cursor.execute("SELECT AVG(maosh) FROM workers")
        avg_maosh = self.cursor.fetchone()[0]
        
        self.cursor.execute(f"SELECT * FROM workers WHERE maosh > {avg_maosh}")
        natija = self.cursor.fetchall()
    
        print(f"O'rtacha maosh: {avg_maosh}")
        print("O'rtacha maoshdan yuqori maosh oladigan ishchilar:")
        for i in natija:
            print(i)

    def ITmaosh (self):
        self.cursor.execute("select avg(maosh) from workers")
        avg_maosh = self.cursor.fetchone()[0]
        print(avg_maosh)
        self.cursor.execute(f"SELECT * FROM workers where ishchi_id='IT_prog' and maosh>{avg_maosh}   ")
        natija=self.cursor.fetchall()
        for i in natija:
            print(i)

        

kh=MySQL()
kh.InserTB(1,"Steven", "King", "+998941234567", "AD_PRES", 24000)
kh.InserTB(2,"Neena", "Kochnar", "+998941244668", "AD_VP", 17000)
kh.InserTB(3,"Lex", "De Haan", "+998941244669", "AD_VP", 17000)
kh.InserTB(4,"Aleksandr", "Hunold", "+998941244670", "IT_PROG", 11000)
kh.InserTB(5,"Bruce", "Ernest", "+998941244671", "IT_PROG", 8000)
kh.InserTB(6,"David", "Austin", "+998941244871", "IT_PROG", 6800)
kh.InserTB(7,"Valli", "Pataballa", "+998941244975", "IT_PROG", 6880)
kh.InserTB(8,"Diana", "Lorentz", "+998946254976", "IT_PROG", 6200)
kh.InserTB(9,"Nancy", "Greenberg", "+998946255946", "FI_MGR", 12000)
kh.InserTB(10,"Daniel", "Faviet", "+998946755948", "FI_ACCOUNT", 9000)
kh.InserTB(11,"John", "Chen", "+998946756953", "FI_ACCOUNT", 8200)
kh.InserTB(12,"Ismeal", "Sciarra", "+998946856983", "FI_ACCOUNT", 7700)
kh.InserTB(13,"Den", "Raphaely", "+998946886983", "PU_MAN", 11000)
kh.InserTB(14,"Aleksandr", "Kahoo", "+998946888983", "PU_CLERK", 3100)
# kh.FuulName()
# kh.ItProg()
# kh.maosh()
# kh.phone()
# kh.sum()
# kh.maosh()
# kh.ITmaosh()
isClose = True 
while  isClose: 
    print(f"""                ----< Make a choice >----
          1.1-masala:
          2.2-masala: 
          3.3-masala: 
          4.4-masala;
          5.5-masala:
          6.6-masala:
          7.7-masala:
          8.8-masala:
          9.EXIT:
          """
        )
    
    choice=int(input())
    if choice==1:
        kh.FuulName()
    elif choice==2:
        kh.ItProg()
    elif choice==3:
        kh.maosh()
    elif choice==4:
        kh.phone()
    elif choice==5:
        kh.sum()
    elif choice==6:
        kh.maosh()
    elif choice==7:
        kh.Avg()
    elif choice==8:
        kh.ITmaosh()  
    elif choice==9:
        isClose =False
        print("Dastur tugadi : ")  
    else:
        print("Bunday tanlov mavjud emas : ")