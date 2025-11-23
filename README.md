---------------------------------------------------------------AUDITORIA DE SISTEMAS----------------------------------------------------
-------------------------------------------Hecho por: Julian Castillo, David Cruz y Santiago Torres---------------------------------------

Más que un README, es una compilación de evidencias para probar que mi proyecto backend en FastAPI

Bien, comenzamos con los post de cada colección por medio de Swagger:

<img width="1852" height="796" alt="image" src="https://github.com/user-attachments/assets/527638a6-47ee-4c6f-89df-fe45cc6d8b2d" />

Aquí se añade la información y luego le damos execute y mostramos MongoDB:

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/8d62ac78-e9ae-42da-b292-b76fdf993f0d" />

Se ve la plataforma de Mongo con dos usuarios en su debida coleccion, Pancho (prueba) y Julian, el que acabamos de implementar.
Ahora lo modificaremos y eliminaremos a Pancho:

Put/update
<img width="1919" height="916" alt="image" src="https://github.com/user-attachments/assets/4728c506-f348-41d2-ae25-ae79e9245a47" />

<img width="1919" height="811" alt="image" src="https://github.com/user-attachments/assets/d478258f-7617-4422-bd88-a682aa2461f8" />

Delete:
<img width="1919" height="933" alt="image" src="https://github.com/user-attachments/assets/e8834246-61e2-4ac9-ba8c-94284776f935" />

<img width="1919" height="886" alt="image" src="https://github.com/user-attachments/assets/c04d18c9-914e-4696-bd79-ee4b4799173a" />

Pancho ya no se encuentra en la base de datos, qué pasa si pone algo que no sea "student", "tutor" o "admin" en el campo de rol?
<img width="1919" height="882" alt="image" src="https://github.com/user-attachments/assets/64700f6a-576f-433c-b064-5007c597aa48" />

Esto pasa, devuelve un error 422 para información "improcesable"

Todo lo demás puede ser intuido por esto mismo, ya que las otras collecciones funcionan de manera similar o incluso identica, así que dejaré imagenes de los diferentes procesos:
Tutor Availability:
<img width="1919" height="817" alt="image" src="https://github.com/user-attachments/assets/d8190db9-d9ad-4c97-b159-05a78cfe3494" />


<img width="1919" height="709" alt="image" src="https://github.com/user-attachments/assets/982c03e5-e886-4192-b711-4d2f5a3a7891" />

Classes:
<img width="1919" height="993" alt="image" src="https://github.com/user-attachments/assets/3ab12a55-607f-4b3c-b179-ed802e462764" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/adea1bbe-37d7-4ef3-aba1-6baf314bb48d" />

