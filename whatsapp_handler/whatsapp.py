# from ..constants import EMAIL_FROM, EMAIL_TO, EMAIL_PASS
import os
import pywhatkit

WHATSAPP_TO = os.environ.get("WHATSAPP_TO")


class WhatsappService():

    @staticmethod
    def send_whatsapp_message(*, subject=""):
        pywhatkit.sendwhatmsg_instantly(
            phone_no=WHATSAPP_TO,
            message="msg",
            tab_close=True
        )
