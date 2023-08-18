from flask import Flask, render_template,request
import sqlite3


#try:
      #conn=sqlite3.connect("database/baseDeDatosCursos.db")
      #cursor=conn.cursor()
      #cursor.execute("""CREATE TABLE ProgrammingCourses(nombre TEXT, Lecciones INTEGER)""")
#except Exception as ex:
#      print(ex)



COURSES =["Python", "Java", "C#","JavaScript","C++","Ruby","Swift","PHP","Kotlin","Go","Rust","TypeScript" ]

app = Flask(__name__)

@app.route ("/",methods=["GET", "POST"])
def index():
        if request.method == "GET":
            return render_template("index.html",cursos=COURSES)
        
        elif request.method == "POST":
                  conn=sqlite3.connect("database/baseDeDatosCursos.db")
                  cursor=conn.cursor()
                  #AHORA AQUI TENGO QUE CONTECTARME CON LA BASE DE DATOS Y MANDAR LA INFORMACION DEL FORMULARIO
                 # cursor.execute("INSERT INTO ProgrammingCourses (nombre, nombreCurso) VALUES (request.form.get("Name"), curso=request.form.get("Curso"))")
                  cursor.execute("INSERT INTO ProgrammingCourses (nombre, nombreCurso) VALUES (?, ?)", (request.form.get("Name"), request.form.get("Curso")))
                  conn.commit()

                  return render_template("registered.html", name= request.form.get("Name").title(),lastName=request.form.get("LastName").title(), curso=request.form.get("Curso"))

#Aquí agregar a la ruta /registered un método get, la idea es hacer un query a la base de datos y presentar el html el resultado de la busqueda. 
@app.route("/registros", methods=["GET", "POST"])
def registros():
    if request.method == "GET":
        conn = sqlite3.connect("database/baseDeDatosCursos.db")
        cursor = conn.cursor()
        query2="SELECT * FROM ProgrammingCourses"
        result2=cursor.execute(query2)
        todosRegistros=result2.fetchall()

        return render_template("registros.html",todosRegistros=todosRegistros)
    
    
    elif request.method == "POST":
        conn = sqlite3.connect("database/baseDeDatosCursos.db")
        cursor = conn.cursor()

        nombre = request.form.get("NombreEnRegistro")
        #apellido = request.form.get("ApellidoEnRegistro")

        query = "SELECT * FROM ProgrammingCourses WHERE LOWER (nombre) = LOWER(?) "
        result=cursor.execute(query, (nombre,))
        result=result.fetchall()
      
        # query2="SELECT * FROM ProgrammingCourses"
        # result2=cursor.execute(query2)
        # todosRegistros=result2.fetchall()


        # Aquí puedes hacer algo con los resultados de la consulta, como fetchall() o fetchone()
        
      
        
        return render_template("registros.html", registros=result)
        #return render_template("registros.html", registros=result,todosRegistros=todosRegistros)
        # Resto de tu código aquí
    app = Flask(__name__)