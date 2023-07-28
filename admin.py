admin=['21441######']  #telegram id of specific user
def is_admin(chat_id):
    chat_id=str(chat_id)
    if chat_id in admin:
        return True
    else:return False
