import uuid

from schedule.core.json_reader import json_settings

settings = json_settings()


def get_cleaned_uuid():
    uuid_ = (str(uuid.uuid1()).replace('-', ''))
    return uuid_

def global_send_mail(subject, message, recipient_list):
    """
    Función para enviar correos
    :param subject: Asunto
    :param message: Mensaje
    :param recipient_list: Lista de usuarios
    :return: 1
    """
    send_html_mail(subject=subject, message='', message_html=message,
                   from_email=f"{settings['EMAIL']['DEFAULT_FROM_NAME']} <{settings['EMAIL']['DEFAULT_FROM_EMAIL']}>",
                   recipient_list=recipient_list)
    # send_mail(
    #     subject,
    #     '',
    #     'some@sender.com',
    #     recipient_list,
    #     html_message=message,
    # )
    return 1
