#schwierigkeit

def get_speed(difficulty):
    if difficulty == "easy":                #Raster nur bei easy (difficulty == 0) anzeigen
        return 200

    elif difficulty == "normal":
        return 125

    elif difficulty == "hard":
        return 100

    else:
        return 125       #standart