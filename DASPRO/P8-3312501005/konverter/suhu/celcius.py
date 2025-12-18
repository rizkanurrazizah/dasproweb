def celcius(suhu, unit):
    if unit == "f":
        return (5/9) * (suhu - 32)
    elif unit == "r":
        return (5/4) * suhu
    elif unit == "k":
        return suhu - 273
    else:
        return 0
