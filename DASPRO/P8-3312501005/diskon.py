def get_diskon(member):
    match member:
        case "silver":
            return 25 / 100
        case "gold":
            return 50 / 100
        case "platinum":
            return 75 / 100
