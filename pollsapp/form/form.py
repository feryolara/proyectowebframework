<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <style>
        .myDiv {
          border: 5px outset rgb(26, 28, 128);
          background-color: rgb(255, 123, 0);
          text-align: center;
        }
        </style>
</head>
<body>
    <DIV class="myDiv">
    <CENTER> 
    <B><H1>INSTITUTO TECNOLÓGICO DE CHETUMAL</H1>
        ENCUESTA PARA DETERMINACIÓN DEL AMBIENTE DE TRABAJO<B>
    </CENTER>
</DIV>
    <div>
        Instrucciones:
<br>
El propósito de esta encuesta es identificar las áreas de oportunidad que nos permitan determinar y gestionar el ambiente de trabajo colaborando para cumplir con los requerimientos del Servicio Educativo.
Recuerda que las respuestas son opiniones basadas en tu experiencia de trabajo, por lo tanto no hay respuestas correctas o incorrectas.
Por favor, te pedimos que leas cuidadosamente cada una de las preguntas y marques el número que describa mejor tu opinión, con base en la escala siguiente:
<br>
<br>
5: Totalmente de acuerdo
<br>
4: Parcialmente de acuerdo
<br>
3: Indiferencia
<br>
2: Parcialmente en desacuerdo
<br>
1: Totalmente en desacuerdo
<br>
<br>
    </div>
    <FORM action = "/respuesta/" method = post>
        {% csrf_token %}
        <br>
    Escribe el número de trabajador:<INPUT type = text name = nombre size = 30 >
        Tu nip: <INPUT type = password name = clave size = 8 >
    
    <h3>1. Condiciones de trabajo:</h3>
    <PRE>
    1.1 .- Tengo definidas claramente las funciones de mi puesto:
    <INPUT type = radio name = condicion11 value = "5" > 5
    <INPUT type = radio name = condicion11 value ="4" > 4
    <INPUT type = radio name = condicion11 value ="3" > 3
    <INPUT type = radio name = condicion11 value ="2" > 2
    <INPUT type = radio name = condicion11 value ="1" > 1
     </PRE>
     <PRE>
    1.2 .- Es mi departamento, todos y todas tenemos las mismas oportunidades de mejora laboral:
    <INPUT type = radio name = condicion12 value = "5" > 5
    <INPUT type = radio name = condicion12 value ="4" > 4
    <INPUT type = radio name = condicion12 value ="3" > 3
    <INPUT type = radio name = condicion12 value ="2" > 2
    <INPUT type = radio name = condicion12 value ="1" > 1
     </PRE>
    <PRE>
    1.3 .- No me molesta quedarme tiempo adicional en mi trabajo:
    <INPUT type = radio name = condicion13 value = "5" > 5
    <INPUT type = radio name = condicion13 value ="4" > 4
    <INPUT type = radio name = condicion13 value ="3" > 3
    <INPUT type = radio name = condicion13 value ="2" > 2
    <INPUT type = radio name = condicion13 value ="1" > 1
    </PRE>   
    <PRE>
    1.4 .- Estoy capacitado (a) lo suficiente para hacer bien mi trabajo:
    <INPUT type = radio name = condicion14 value = "5" > 5
    <INPUT type = radio name = condicion14 value ="4" > 4
    <INPUT type = radio name = condicion14 value ="3" > 3
    <INPUT type = radio name = condicion14 value ="2" > 2
    <INPUT type = radio name = condicion14 value ="1" > 1
    </PRE>  
    <PRE>
    1.5 .- Las funciones de mi puesto, las desempeño de acuerdo a como se declaran en el Manual de Organización:
    <INPUT type = radio name = condicion15 value = "5" > 5
    <INPUT type = radio name = condicion15 value ="4" > 4
    <INPUT type = radio name = condicion15 value ="3" > 3
    <INPUT type = radio name = condicion15 value ="2" > 2
    <INPUT type = radio name = condicion15 value ="1" > 1
    </PRE>  
    <PRE>
    1.6 .- Desempeño apropiadamente las responsabilidades y actividades de mi puesto:
    <INPUT type = radio name = condicion16 value = "5" > 5
    <INPUT type = radio name = condicion16 value ="4" > 4
    <INPUT type = radio name = condicion16 value ="3" > 3
    <INPUT type = radio name = condicion16 value ="2" > 2
    <INPUT type = radio name = condicion16 value ="1" > 1
    </PRE>  

    <br>
    <h3>2. Cooperación:</h3>
    <PRE>
    2.1 .- Me siento orgulloso (a) de laborar en el instituto:
    <INPUT type = radio name = cooperacion11 value = "5" > 5
    <INPUT type = radio name = cooperacion11 value ="4" > 4
    <INPUT type = radio name = cooperacion11 value ="3" > 3
    <INPUT type = radio name = cooperacion11 value ="2" > 2
    <INPUT type = radio name = cooperacion11 value ="1" > 1
     </PRE>
     <PRE>
    2.2 .- Mis compañeros (as) de trabajo comparten conmigo información que me ayuda a realizar mi trabajo:
    <INPUT type = radio name = cooperacion12 value = "5" > 5
    <INPUT type = radio name = cooperacion12 value ="4" > 4
    <INPUT type = radio name = cooperacion12 value ="3" > 3
    <INPUT type = radio name = cooperacion12 value ="2" > 2
    <INPUT type = radio name = cooperacion12 value ="1" > 1
     </PRE>
    <PRE>
    2.3 .- Mi relación laboral con mis compañeros del departamento es buena:
    <INPUT type = radio name = condicion13 value = "5" > 5
    <INPUT type = radio name = condicion13 value ="4" > 4
    <INPUT type = radio name = condicion13 value ="3" > 3
    <INPUT type = radio name = condicion13 value ="2" > 2
    <INPUT type = radio name = condicion13 value ="1" > 1
    </PRE>   
    <PRE>
    2.4 .- Considero que en mi área de trabajo se fomenta el trabajo en equipo:
    <INPUT type = radio name = cooperacion14 value = "5" > 5
    <INPUT type = radio name = cooperacion14 value ="4" > 4
    <INPUT type = radio name = cooperacion14 value ="3" > 3
    <INPUT type = radio name = cooperacion14 value ="2" > 2
    <INPUT type = radio name = cooperacion14 value ="1" > 1
    </PRE>  
    <PRE>
    2.5 .- Estoy plenamente integrado (a) en mi trabajo:
    <INPUT type = radio name = cooperacion15 value = "5" > 5
    <INPUT type = radio name = cooperacion15 value ="4" > 4
    <INPUT type = radio name = cooperacion15 value ="3" > 3
    <INPUT type = radio name = cooperacion15 value ="2" > 2
    <INPUT type = radio name = cooperacion15 value ="1" > 1
    </PRE>  
    <PRE>
    2.6 .- La comunicación con mis compañeros(as) de trabajo es buena:
    <INPUT type = radio name = cooperacion16 value = "5" > 5
    <INPUT type = radio name = cooperacion16 value ="4" > 4
    <INPUT type = radio name = cooperacion16 value ="3" > 3
    <INPUT type = radio name = cooperacion16 value ="2" > 2
    <INPUT type = radio name = cooperacion16 value ="1" > 1
    </PRE>  
    <PRE>
    2.7 .- En mi departamento existe un ambiente de respeto:
    <INPUT type = radio name = cooperacion17 value = "5" > 5
    <INPUT type = radio name = cooperacion17 value ="4" > 4
    <INPUT type = radio name = cooperacion17 value ="3" > 3
    <INPUT type = radio name = cooperacion17 value ="2" > 2
    <INPUT type = radio name = cooperacion17 value ="1" > 1
    </PRE>  

    <br>
    <h3>3. Supervición:</h3>
    <PRE>
    3.1 .- Mi jefe (a) es respetuoso conmigo:
    <INPUT type = radio name = supervicion11 value = "5" > 5
    <INPUT type = radio name = supervicion11 value ="4" > 4
    <INPUT type = radio name = supervicion11 value ="3" > 3
    <INPUT type = radio name = supervicion11 value ="2" > 2
    <INPUT type = radio name = supervicion11 value ="1" > 1
     </PRE>
     <PRE>
    3.2 .- Mi jefe (a) atiende mis dudas e inquietudes:
    <INPUT type = radio name = supervicion12 value = "5" > 5
    <INPUT type = radio name = supervicion12 value ="4" > 4
    <INPUT type = radio name = supervicion12 value ="3" > 3
    <INPUT type = radio name = supervicion12 value ="2" > 2
    <INPUT type = radio name = supervicion12 value ="1" > 1
     </PRE>
    <PRE>
    3.3 .- Considero que mi jefe fomenta las relaciones humanas con su personal:
    <INPUT type = radio name = supervicion13 value = "5" > 5
    <INPUT type = radio name = supervicion13 value ="4" > 4
    <INPUT type = radio name = supervicion13 value ="3" > 3
    <INPUT type = radio name = supervicion13 value ="2" > 2
    <INPUT type = radio name = supervicion13 value ="1" > 1
    </PRE>   
    <PRE>
    3.4 .- Mi jefe (a) solamente me pide que me quede tiempo adicional cuando es necesario:
    <INPUT type = radio name = supervicion14 value = "5" > 5
    <INPUT type = radio name = supervicion14 value ="4" > 4
    <INPUT type = radio name = supervicion14 value ="3" > 3
    <INPUT type = radio name = supervicion14 value ="2" > 2
    <INPUT type = radio name = supervicion14 value ="1" > 1
    </PRE>  
    <PRE>
    3.5 .- Estoy de acuerdo que mi trabajo sea supervisado:
    <INPUT type = radio name = supervicion15 value = "5" > 5
    <INPUT type = radio name = supervicion15 value ="4" > 4
    <INPUT type = radio name = supervicion15 value ="3" > 3
    <INPUT type = radio name = supervicion15 value ="2" > 2
    <INPUT type = radio name = supervicion15 value ="1" > 1
    </PRE>  
    <PRE>
    3.6 .- Mi jefe (a) me apoya en la solución de problemas que se presentan en mi trabajo:
    <INPUT type = radio name = supervicion16 value = "5" > 5
    <INPUT type = radio name = supervicion16 value ="4" > 4
    <INPUT type = radio name = supervicion16 value ="3" > 3
    <INPUT type = radio name = supervicion16 value ="2" > 2
    <INPUT type = radio name = supervicion16 value ="1" > 1
    </PRE>  
    <PRE>
    3.7 .- Mi jefe esta pendiente de las actividades que desarollo:
    <INPUT type = radio name = supervicion17 value = "5" > 5
    <INPUT type = radio name = supervicion17 value ="4" > 4
    <INPUT type = radio name = supervicion17 value ="3" > 3
    <INPUT type = radio name = supervicion17 value ="2" > 2
    <INPUT type = radio name = supervicion17 value ="1" > 1
    </PRE> 

    <br>
    <h3>4. Condiciones físicas de trabajo:</h3>
    <PRE>
    4.1 .- Cuenta con espacio físico adecuado para la realización de sus actividades:
    <INPUT type = radio name = fisica11 value = "5" > 5
    <INPUT type = radio name = fisica11 value ="4" > 4
    <INPUT type = radio name = fisica11 value ="3" > 3
    <INPUT type = radio name = fisica11 value ="2" > 2
    <INPUT type = radio name = fisica11 value ="1" > 1
     </PRE>
     <PRE>
    4.2 .- Mi trabajo lo realizo en condiciones seguras.:
    <INPUT type = radio name = fisica12 value = "5" > 5
    <INPUT type = radio name = fisica12 value ="4" > 4
    <INPUT type = radio name = fisica12 value ="3" > 3
    <INPUT type = radio name = fisica12 value ="2" > 2
    <INPUT type = radio name = fisica12 value ="1" > 1
     </PRE>
    <PRE>
    4.3 .- Los niveles de ruido son aceptables para la realización de tu actividad:
    <INPUT type = radio name = fisica13 value = "5" > 5
    <INPUT type = radio name = fisica13 value ="4" > 4
    <INPUT type = radio name = fisica13 value ="3" > 3
    <INPUT type = radio name = fisica13 value ="2" > 2
    <INPUT type = radio name = fisica13 value ="1" > 1
    </PRE>   
    <PRE>
    4.4 .- Los niveles de temperatura son aceptables para la realización de tu actividad.:
    <INPUT type = radio name = fisica14 value = "5" > 5
    <INPUT type = radio name = fisica14 value ="4" > 4
    <INPUT type = radio name = fisica14 value ="3" > 3
    <INPUT type = radio name = fisica14 value ="2" > 2
    <INPUT type = radio name = fisica14 value ="1" > 1
    </PRE>  
    <PRE>
    4.5 .- La limpieza y aseo en general son buenos:
    <INPUT type = radio name = fisica15 value = "5" > 5
    <INPUT type = radio name = fisica15 value ="4" > 4
    <INPUT type = radio name = fisica15 value ="3" > 3
    <INPUT type = radio name = fisica15 value ="2" > 2
    <INPUT type = radio name = fisica15 value ="1" > 1
    </PRE>  
    <PRE>
    4.6 .- Los niveles de iluminación son aceptables para la realización de tu actividad.:
    <INPUT type = radio name = fisica16 value = "5" > 5
    <INPUT type = radio name = fisica16 value ="4" > 4
    <INPUT type = radio name = fisica16 value ="3" > 3
    <INPUT type = radio name = fisica16 value ="2" > 2
    <INPUT type = radio name = fisica16 value ="1" > 1
    </PRE>  
    <PRE>
    4.7 .- Cuento con los equipos y herramientas necesarias para ejecutar mi trabajo:
    <INPUT type = radio name = fisica17 value = "5" > 5
    <INPUT type = radio name = fisica17 value ="4" > 4
    <INPUT type = radio name = fisica17 value ="3" > 3
    <INPUT type = radio name = fisica17 value ="2" > 2
    <INPUT type = radio name = fisica17 value ="1" > 1
    </PRE> 

    <br>
    <h3>5. Satisfacción en el trabajo:</h3>
    <PRE>
    5.1 .- Mi trabajo apoya al logro de los objetivos de la Institución:
    <INPUT type = radio name = p41 value = "5" > 5
    <INPUT type = radio name = p41 value ="4" > 4
    <INPUT type = radio name = p41 value ="3" > 3
    <INPUT type = radio name = p41 value ="2" > 2
    <INPUT type = radio name = p41 value ="1" > 1
     </PRE>
     <PRE>
    5.2 .- Soy respetuoso de la normatividad de la Institución:
    <INPUT type = radio name = p42 value = "5" > 5
    <INPUT type = radio name = p42 value ="4" > 4
    <INPUT type = radio name = p42 value ="3" > 3
    <INPUT type = radio name = p42 value ="2" > 2
    <INPUT type = radio name = p42 value ="1" > 1
     </PRE>
    <PRE>
    5.3 .- No me iría del Instituto aunque me ofrecieran un trabajo similar por el mismo sueldo:
    <INPUT type = radio name = p43 value = "5" > 5
    <INPUT type = radio name = p43 value ="4" > 4
    <INPUT type = radio name = p43 value ="3" > 3
    <INPUT type = radio name = p43 value ="2" > 2
    <INPUT type = radio name = p43 value ="1" > 1
    </PRE>   
    <PRE>
    5.4 .- Siempre trato de colaborar en todas las actividades que se realizan en mi área de trabajo:
    <INPUT type = radio name = p44 value = "5" > 5
    <INPUT type = radio name = p44 value ="4" > 4
    <INPUT type = radio name = p44 value ="3" > 3
    <INPUT type = radio name = p44 value ="2" > 2
    <INPUT type = radio name = p44 value ="1" > 1
    </PRE>  
    <PRE>
    5.5 .- En mi área de trabajo no hay discriminación de género:
    <INPUT type = radio name = p45 value = "5" > 5
    <INPUT type = radio name = p45 value ="4" > 4
    <INPUT type = radio name = p45 value ="3" > 3
    <INPUT type = radio name = p45 value ="2" > 2
    <INPUT type = radio name = p45 value ="1" > 1
    </PRE>  
    <PRE>
    5.6 .- Generalmente pongo en práctica mi iniciativa en el trabajo:
    <INPUT type = radio name = p46 value = "5" > 5
    <INPUT type = radio name = p46 value ="4" > 4
    <INPUT type = radio name = p46 value ="3" > 3
    <INPUT type = radio name = p46 value ="2" > 2
    <INPUT type = radio name = p46 value ="1" > 1
    </PRE>  
    <PRE>
    5.7 .- Estoy motivado (a) por el reconocimiento que mi jefe (a) y los (las) directivos dan a mi trabajo:
    <INPUT type = radio name = p47 value = "5" > 5
    <INPUT type = radio name = p47 value ="4" > 4
    <INPUT type = radio name = p47 value ="3" > 3
    <INPUT type = radio name = p47 value ="2" > 2
    <INPUT type = radio name = p47 value ="1" > 1
    </PRE> 

    <br>
    <h3>5. Participación en cuidado ambiental:</h3>
    <PRE>
    6.1 .- Participo en las actividades que se realiza en la Institución para el Cuidado ambiental:
    <INPUT type = radio name = p51 value = "5" > 5
    <INPUT type = radio name = p51 value ="4" > 4
    <INPUT type = radio name = p51 value ="3" > 3
    <INPUT type = radio name = p51 value ="2" > 2
    <INPUT type = radio name = p51 value ="1" > 1
     </PRE>
     <PRE>
    6.2 .- Considero importante la cultura de reciclaje:
    <INPUT type = radio name = p52 value = "5" > 5
    <INPUT type = radio name = p52 value ="4" > 4
    <INPUT type = radio name = p52 value ="3" > 3
    <INPUT type = radio name = p52 value ="2" > 2
    <INPUT type = radio name = p52 value ="1" > 1
     </PRE>
    <PRE>
    6.3 .- Clasifico la basura que se genera en mi área de trabajo:
    <INPUT type = radio name = p53 value = "5" > 5
    <INPUT type = radio name = p53 value ="4" > 4
    <INPUT type = radio name = p53 value ="3" > 3
    <INPUT type = radio name = p53 value ="2" > 2
    <INPUT type = radio name = p53 value ="1" > 1
    </PRE>   
    <PRE>
    6.4 .- Soy respetuoso de las indicaciones del cuidado de ahorro de energía:
    <INPUT type = radio name = p54 value = "5" > 5
    <INPUT type = radio name = p54 value ="4" > 4
    <INPUT type = radio name = p54 value ="3" > 3
    <INPUT type = radio name = p54 value ="2" > 2
    <INPUT type = radio name = p54 value ="1" > 1
    </PRE>  
    <PRE>
    6.5 .- Considero importante realizar campañas de aseo en la Institucion:
    <INPUT type = radio name = p55 value = "5" > 5
    <INPUT type = radio name = p55 value ="4" > 4
    <INPUT type = radio name = p55 value ="3" > 3
    <INPUT type = radio name = p55 value ="2" > 2
    <INPUT type = radio name = p55 value ="1" > 1
    </PRE>  
    <INPUT type = submit value = "Enviar" >
    <INPUT type = reset value = "Borrar" >
    </FORM>
    </body>
</html>