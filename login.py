import dbcon


def create_user():
    try:
        n = raw_input("Enter name : ")
        p = raw_input("Enter password : ")
        dbcon.User.create(username=n, password=p)
        print "User creation success!!!"
        raw_input()
    except:
        return False

def check_login():
    lname = raw_input("login id : ")
    pword = raw_input("password : ")
    if check_user(lname, pword):
        print "Welcome " + lname
        return lname
    else:
        chck = raw_input("sorry . .wanna try signup? (y|n)")
        if chck == 'y':
        	create_user()
        else:
            sys.exit(0)

def check_user(lname, password):
    try:
        n = dbcon.User.get(dbcon.User.username == lname)
        p = dbcon.User.get(dbcon.User.username == lname).password
        if p == password:
            print "login success"
            return True
        else:
            print("wrong password")
            return False
    except:
        return False

def change_password(lname):
	try:
		chnge = dbcon.User()
		new_pass = raw_input("Please enter the new password")
		conf_pass = raw_input("Confirm password ")
		if new_pass == conf_pass:
			query=chnge.update(dbcon.User.password==new_pass).where(username = lname)
			query.execute()
			print lname
			print dbcon.User.password
			return True
		else:
			print "sorry please enter confirm password correctly"
	except:
		print "change_password failed"
