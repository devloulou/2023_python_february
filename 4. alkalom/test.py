http_code = "418"
def p():
    for item in range(4):
        match http_code:
            case "200":
                print("OK")
            case "404":
                print("Not Found")
            case "418":
                print("I'm a teapot")
            case _:
                print("Code not found")

def p():
    for item in range(4):
        if http_code == "200":
            print("OK")
        elif http_code == "404":
            print("Not Found")
        elif http_code == "418":
            print("I'm a teapot")
        else:
            print("Code not found")