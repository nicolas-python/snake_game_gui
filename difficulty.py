#schwierigkeit

def get_speed(difficulty):
    if difficulty == "easy":                #Raster nur bei easy (difficulty == 0) anzeigen
        return 150

    elif difficulty == "normal":
        return 115

    elif difficulty == "hard":
        return 80

    else:
        return 115       #standart