def traffic_signal(color):
    if color == 'RED':
        print("The colour is red, please STOP")
    elif color == 'YELLOW':
        print("The colour is yellow, please SLOW DOWN")
    elif color == 'GREEN':
        print("The colour is green, PLEASE GO")
    else:
        print("COLOUR INVALID...not a traffic signal color ")


traffic_signal('RED')
traffic_signal('GREEN')
traffic_signal('YELLOW')
traffic_signal('BLUE')
