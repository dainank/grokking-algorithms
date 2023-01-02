voted = {}  # hash

def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

check_voter("tom")
print(voted)
check_voter("ben")
check_voter("ben")
print(voted)