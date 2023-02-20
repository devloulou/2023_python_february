"""
Exception handling - kivételkezelés

try:
    próbáld lefuttatni a kódót
except:
    ha hibára fut a kód, akkor mi történjen
finally:
    ha véged ért a try és except ág, akkor mi történjen - finally mindig le fog futni

"""

a = 1
b = 0


try:
    sol = a / b
except Exception as e:
    print("Ez most az Exception ág")
    try:
        print("alma")
    except:
        ...

except ZeroDivisionError as error:
    print(error)
finally:
    print("Ez mindig lefut")


a = 2
b = 3
try:
    if a < b:
        raise Exception("Baj az, hogy a 2 kisebb mint a 3")
except Exception as e:
    print(e)