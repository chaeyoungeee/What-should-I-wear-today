import gspread

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
gc = gspread.service_account(filename='./discordbot/key.json')

ws = gc.open("user_DB").worksheet('sheets1')

def check_exist(id):
    id_data = ws.col_values(2)
    for i in id_data:
        if hex(id) == i:
            return True
    return False

def sign_up(name, id):
    ws.insert_row([name, hex(id), 0, 0, 0], len(ws.col_values(2))+1)

def hot_level_update(id, hot_level):
    id_data = ws.col_values(2)
    for idx, i in enumerate(id_data):
        if hex(id) == i:
            ws.update_acell(f'C{idx+1}', hot_level)

def info_update(id, avg_temperature, clothes_level):
    id_data = ws.col_values(2)
    for idx, i in enumerate(id_data):
        if hex(id) == i:
            ws.update_acell(f'D{idx+1}', avg_temperature)
            ws.update_acell(f'E{idx+1}', clothes_level)
            return

def user_save_info(id):
    id_data = ws.col_values(2)
    for idx, i in enumerate(id_data):
        if hex(id) == i:
            return float(ws.acell(f'C{idx+1}').value), float(ws.acell(f'D{idx+1}').value), float(ws.acell(f'E{idx+1}').value)
    return 0, None, None