import math 

action = 0
while action != "Q":
    print("~~~~Select a formula to check its equation and variables.~~~~")
    print(" ")
    print("[1] Mechanical Energy")
    print("[2] Uniform Accelerated Motion")
    print("[Q] to quit.")
    print(" ")
    action = input("Type your chosen action: ")
    print(" ")
    
    if action == "1":
        print("~~~~You chose the formula for Mechanical Energy~~~~")
        print(" ")
        print("Mechanical Energy = (Mass * Gravity * Height) + (0.5 * Mass * Velocity^2)")
        print(" ")
        print("[1] Total Mechanical Energy (J)")
        print("[2] Mass (Kg)")
        print("[3] Height (m)")
        print("[4] Velocity (m/s)")
        print("[B] Go back to formula selection.")
        print(" ")
        var1 = input("Choose an unknown variable: ")
        print(" ")
        
        if var1 == "1":
            m = float(input("Give the value of mass (kg): "))
            h = float(input("Give the value of height (m): "))
            v = float(input("Give the value of velocity (m/s): "))
            print(" ")
            me = ((m * 9.8 * h) + (0.5 * m * (v ** 2)))
            print("The total Mechanical Energy is", me, "Joules")
            print(" ")
            
        elif var1 == "2":
            me = float(input("Give the value of the Total Mechanical Energy (J): "))
            h = float(input("Give the value of height (m): "))
            v = float(input("Give the value of velocity (m/s): "))
            print(" ")
            m = ((2 * me) / ((2 * 9.8 * h) + (v ** 2)))
            print("The mass is", m, "Kg")
            print(" ")

        elif var1 == "3":
            me = float(input("Give the value of the Total Mechanical Energy (J): "))
            m = float(input("Give the value of mass (kg): "))
            v = float(input("Give the value of velocity (m/s): "))
            print(" ")
            h = ((me / (m * 9.8)) - ((v ** 2) / (2 * 9.8))) 
            print("The height is", h, "m")
            print(" ")

        elif var1 == "4":
            me = float(input("Give the value of the Total Mechanical Energy (J): "))
            m = float(input("Give the value of mass (kg): "))
            h = float(input("Give the value of height (m): "))
            print(" ")
            v = (math.sqrt((2 * m * (me - (9.8 * h * m)))) / m) 
            print("The velocity is", v, "m/s")
            print(" ")
            
    elif action == "2":
        print("~~~~You chose the formula for Uniform Accelerated Motion~~~~")
        print(" ")
        print("Change in distance = (Initial Velocity * Time) + (0.5 * Acceleration * Time^2)")
        print(" ")
        print("[1] Change in distance (x)")
        print("[2] Initial Velocity (m/s)")
        print("[3] Time (s)")
        print("[4] Acceleration (m/s^2)")
        print("[B] Go back to formula selection.")
        print(" ")
        var2 = input("Choose an unknown variable: ")
        print(" ")

        if var2 == "1":
            vi = float(input("Give the value of the initial velocity (m/s): "))
            t = float(input("Give the value of time (s): "))
            a = float(input("Give the value of acceleration (m/s^2): "))
            print(" ")
            x = ((vi * t) + (0.5 * a * (t ** 2)))
            print("The change in distance is", x, "m")
            print(" ")
            
        elif var2 == "2":
            x = float(input("Give the value of the change in distance (m): "))
            t = float(input("Give the value of time (s): "))
            a = float(input("Give the value of acceleration (m/s^2): "))
            print(" ")
            vi = ((x / t) - ((t * a) / 2))
            print("The initial velocity is", vi, "m/s")
            print(" ")

        elif var2 == "3":
            x = float(input("Give the value of the change in distance (m): "))
            vi = float(input("Give the value of its initial velocity (m/s): "))
            a = float(input("Give the value of acceleration (m/s^2): "))
            print(" ")
            t = ((1 * - 1) * ((vi - math.sqrt((vi ** 2) + (2 * a * x))) / a))
            print("The time is", t, "s")
            print(" ")

        elif var2 == "4":
            x = float(input("Give the value of the change in distance (m): "))
            vi = float(input("Give the value of its initial velocity (m/s): "))
            t = float(input("Give the value of time (s): "))
            print(" ")
            a = (((2 * x) / (t ** 2)) - ((2 * vi) / t))
            print("The acceleration is", a, "m/s^2")
            print(" ")
            
    any = input("Press any key to continue...")
    print(" ")        

    
