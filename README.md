# Phishing X

Un clon de **X** (Twitter).

# ⚠️ ADVERTENCIA

Este proyecto fue desarrollado **exclusivamente con fines educacionales** como parte de un curso de seguridad informática. **No debe ser utilizado en ningún otro contexto ni con intenciones maliciosas.**

**Aviso Legal:**

Este código **no debe ser utilizado fuera del entorno educacional ni aplicado a sistemas en producción, redes, o dispositivos ajenos sin autorización.**
**El autor no se hace responsable por el uso indebido de este código.** Cualquier intento de utilizar este proyecto para propósitos distintos a los estipulados en este repositorio es **bajo su propia responsabilidad.**

Este proyecto tiene como **único objetivo enseñar y concientizar sobre las técnicas de ciberseguridad y los riesgos asociados.** Asegúrate de cumplir con todas las leyes y regulaciones aplicables en tu jurisdicción.

# Requisitos:

- Python 3
- Virtualenv (pip install virtualenv)
- Dependencias de requeriments.txt
- Cuenta de mailtrap (https://mailtrap.io/)

# Instalación:

Crear un entorno virtual de python:

```bash
$ python -m venv venv
```

Activar el entorno virtual:

```bash
$ .\venv\Scripts\activate
```

Instalar las dependencias del archivo requirements.txt:

```bash
$ pip install -r requirements.txt
```

# Configuración:

Entrar a el archivo settings.py para configurar el servidor de mailtrap y poder enviar correos. A continuación un diagrama de las rutas del proyecto para encontrar el archivo:

```bash
/phishingX
│
├── phishingX/
│   └── settings.py # <--- MODIFICAR ESTE
├── x/
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

Dentro del archivo settings.py modificar las ultimas lineas que hacen referencia a mailtrap con los datos de nuestra cuenta:

```python
# MAILTRAP
EMAIL_HOST = "sandbox.smtp.mailtrap.io"
EMAIL_HOST_USER = "**************"
EMAIL_HOST_PASSWORD = "**************"
EMAIL_PORT = "2525"
```

# Ejecución:

Para ejecutar el servidor web usar el comando:

```bash
$ python manage.py runserver
```

**Nota:** Las credenciales del usuario se guardan en el archivo db.sqlite3 en la tabla x_victim.

```

                                  *(%@@@@@*#@@@,..
                       ,/#@@@@@@@@@@@@@@@@@@@@@..
                .*#@@@@@@@@@@@@@@@@@@@@@@@@@@@..
                 *#@@@@@@@@@@@@@@.*##@@@@@@@@..
                 *#@@@@.#        *##@@@@@@@@..
                 *#@@,..*@&     *##@@@@@@@@..
                        .#@@@@@@@@@@@@@@@@...
                      .#      **@@@@@@@@@...
                       .@@@@@@%#@@@@@@@@...
                          .%@@@@@@@@@@@...
                           *##@@@@@@@@.,.
  *#@@..                 *#@@@@@@@@@@*..
    *#&@@@@..       *#@@@@@@@@@@@@@@&..
      *#@@@@@@@*#@@@@@@@@@@@@@@@@@@@..
        *#@@@@@@@@@@@@@@@@@@&,.
          *#@@@@@@@@..                   Hecho por Julio NG
```
