try:
    x=float("abc123")
    print("The conversion is completed")
except IOError:
    print("This code caused an IOError")
except ValueError:
    print("This code caused an ValueError")
except:
    print("An error happened")

