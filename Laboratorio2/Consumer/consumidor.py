import pika
import json

def mensaje_rec(channel):   
    def callback(ch, method, properties, body):
        recData = True
        mensaje = json.loads(body.decode('utf-8'))
        print("-------------------------------------------")
        print(f'Id: {mensaje["id"]}\nFecha: {mensaje["fecha"]}\nHora: {mensaje["hora"]}\nValor: {mensaje["datos"]}{mensaje["tipod"]}')
    channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


def __main__(): 
    print("########## INICIO CONSUMER ############\n")
    print("PARA COMENZAR INGRESE LOS SIGUENTES DATOS: \n")
    while True:
        try:
            ip = input("1.Ingrese la direccion IP: ")         #Se solicita direccion IP del servicio RabbitMQ
            usuario = input("2. Ingrese el usuario del servicio RabbitMQ: ")            #El user ingresa el usuario para el servicio de RabbitMQ
            contra = input("3. Ingrese la contraseña del usuario de RabbitMQ: ")        #El user ingresa la contraseña del usuario de RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters(ip, 5672, '/',     #Se establece conexion con el servidor 
            pika.PlainCredentials(usuario, contra)))           #Se autorizan los credenciales
            channel = connection.channel()                     #Se establece la conexion con el canal
            break
        except:
            print("Error en la conexion, ingrese los datos nuevamente...")    #Se crea el mensaje que se le mostrara al user de un error si los datos no concuerdan con los establecidos
    queue = input("Ingrese el exchange: ")              #
    mensaje_rec(channel)
__main__()