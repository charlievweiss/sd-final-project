def = board_math(rider_weight, riding_style_value):
    import MATH

    ## INPUT VALUES:
    # rider_weight = rider weight in lbs
    # riding_style_value = discrete value that represent the desired stiffness of the board 0, 1, or 2
    deformation_matrix = [.013, .026, .040] #deformation remapping in inches in the center of the board

    ## FANCY MATH STUFF:
    ## constants:
    E_f = 72 * 10**9 #youngs modulous of one layer of 6oz fiberglass
    w = deformation_matrix(riding_style_value) #remaps descrite input to mm value of flex also known as the mid span deflection
    v = 0.33 #poisons ratio - this is kinda just a close enought value
    L =  .685 #total lenghth of the desk (specimin) m
    b = .190 #width of the deck/ specimin m
    P = rider_weight * 4.44822 #centrally applied load in Newtons converts lbs to newtons
    a = .443 #span of the deck in m
    c = .013 #core shear thickness m
    fiber_thickness = .0015 #thickness of one layer of fiberglass in m

    for layers in [1,2,3,4]:
        ## variables:
        #layers = number of layers of fiberglass
        #E_c = #youngs modulous of the core - a changing value based on the geometry
        h = c + (fiberthickness * layers) #thickness of the deck/specimin including fiberglass ***this might actually be better suited as a variable

        # S = (P / ((h + c) * b)) #core shear stress
        # F = ((P * a) / (2 * f * (h + c))) * b #average facing stress
        D = (E_f * (h**3 - c**3) * b) / (12 * (1. - v**2)) #flexural stiffness
        N = 1 / (4 * ((w / (P * a) - (a**2 / (48 * D))))) #shear stiffness - utilizing the deflection equation
        G = ((N * 4 * c) / ((h + c)**2 * b))/1000 #core shear modulous
        side_length = 1.04466 - 0.0000795962 * G + 0.000000000131406 * G**2 #side length of the hexagon
        if side_length <=.75 and side_length >= .2:
            break
        else:
            side_length = none

    ## OUTPUTS:
    percent_coverage = .25 #setting this as a constant for now until find a better way to impliment
    area_of_hex = (3 * math.sqrt(3) / 2) * side_length**2
    large_side_length = math.sqrt((side_length**2) / (1 - percent_coverage))
    web_thickness = (large_side_length - side_length) / 2 #the thickness of the webs between hex cut outs
    fiberglass_layers = layers #bidirectional 6oz fiberglass

    small_circle = side_length * math.sqrt(3) #inscribed circle of a hex
    big_circle = large_side_length * math.sqrt(3) #inscribed circle for large hex

    Outputs = small_circle, big_circle

    return Outputs
