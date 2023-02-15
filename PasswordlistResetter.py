import json

PATH_USERNAMES = "C:\\Users\\xboxk\\Desktop\\Python\\LoginSystem\\passwordlist.json" #musí se změnit na váš adresář k souboru hesel
users = {"Username": {}, "Password": {}}
with open(PATH_USERNAMES, "w") as f:
    json.dump(users, f)