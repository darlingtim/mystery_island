def playerNameValidation(name):
    error = []
    if not name:
            error.append("name cannot be empty")
    if len(name) < 2 :
        error.append( "username must be 2 or more characters")
    if len(name) > 15:
        error.append( "username cannot be greater than 15 characters")
    if " " in name:
        error.append( "space is not allowed in username")

    if len(error) >= 1:
         return error
    else:
         return "valid"

    