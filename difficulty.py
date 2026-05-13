#schwierigkeit

def get_speed(difficulty):
    if difficulty == "easy":                #Raster nur bei easy (difficulty == 0) anzeigen
        return 250

    elif difficulty == "normal":
        return 150

    elif difficulty == "hard":
        return 100

    else:
        return 150     #standart