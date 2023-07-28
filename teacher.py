teacher=['242234#####'] # teacher id of specific teacher

def is_teacher(chat_id):
    chat_id=str(chat_id)
    if chat_id in teacher:
        return True
    else: return False
