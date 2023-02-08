def create_cast_list(filename):
    cast_list = []
    delimitador = ', '
    with open(filename) as f:
        for line in f:
            line_splitted = line.split(delimitador)
            cast_list.append(line_splitted[0])
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)