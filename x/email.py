import random
import string
from django.core.mail import send_mail


def generate_2FA():
    caracteres = string.ascii_letters + string.digits
    cadena = "".join(random.choices(caracteres, k=6))
    return cadena


def send_email(email_victim):
    code_2fa = generate_2FA()
    send = send_mail(
        "Código 2FA de X",
        "Tu código 2FA es: " + str(code_2fa),
        "x.com",
        [email_victim],
    )

    if send:
        print("Correo enviado con exito, con el código: " + str(code_2fa))
        return code_2fa
    else:
        print("El correo no pudo ser enviado")
        return None
