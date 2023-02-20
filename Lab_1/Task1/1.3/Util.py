def makeEvenNemberList(list):
    out_list = []

    try:
        out_list = [item for item in list if(int(item) % 2 == 0)]
    except(ValueError):
        print("Invalid list")
    
    return out_list
    