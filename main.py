import dbcon
import sys
import os
import datetime


def create_user():
    try:
        n = raw_input("Enter name : ")
        p = raw_input("Enter password : ")
        dbcon.User.create(username=n, password=p)
        print "User creation success!!!"
        raw_input()
    except:
        return False


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


def create_log(cur_user):
    try:
        t = raw_input("Enter Log type : ")
        c = raw_input("Enter Log content : ")
        r = input("Enter rating [1 to 5]")
        dbcon.Log.create(time=datetime.datetime.now(), log_type=t, log_content=c, rating=r, log_user=cur_user)
        print "Log added to Database"
    except:
        return False


def check_log(cur_user):
    try:
        check = dbcon.Log.select().count()
        if check != 0:
            print("Logs by "+cur_user)
            result = dbcon.Log.select().where(dbcon.Log.log_user == cur_user).order_by(dbcon.Log.time)
            i=1
            for name in result:
                print str(i)+"-------Time : "+str(name.time) + " Log type: " + name.log_type
                print "Rating: "+name.rating*u"\u2605"+(5-name.rating)* u"\u2606"
                print "message: "+name.log_content+"\n"
                i=i+1
        else:
            print "No log found. . . create a log"
    except:
        print sys.exc_info()[0]
        return False
def search_log(cur_user,term):
    try:
        result = dbcon.Log.select().where(dbcon.Log.log_user ==cur_user and dbcon.Log.log_type == term).order_by(dbcon.Log.time)
        i=1
        for name in result:
            print str(i)+"-------Time : "+str(name.time) + " Log type: " + name.log_type
            print "Rating: "+name.rating*u"\u2605"+(5-name.rating)* u"\u2606"
            print "message: "+name.log_content+"\n"
            i=i+1
    except Exception, e:
        print e

def action(cur_user):
    i = True
    while i:
        os.system('clear')
        chck = input("action menu : \n1.create a new log\n2.check logs\n3.Search logs\n4.logout")
        if chck == 1:
            os.system('clear')
            print "creating new log...."
            create_log(cur_user)
        elif chck == 2:
            os.system('clear')
            print "checking logs...."
            check_log(cur_user)
            raw_input()
        elif chck == 3:
            os.system('clear')
            term = raw_input('enter Search type: ')
            search_log(cur_user,term) 
            raw_input()
        else:
            os.system('clear')
            print "logging out system...bye " + cur_user
            i = False


def main(name=None):
    try:
        print '''Welcome to the plog - personal blogging assistant'''
        ch = raw_input("Login(y|n) : ")
        if ch == 'y':
            cur_user = check_login()
            action(cur_user)
        else:
            if create_user() == False:
                print "user creation failed"
                sys.exit(0)
            cur_user = check_login()
            action(cur_user)
    except:
        print sys.exc_info()[0]
        print "logging out system...bye "
        sys.exit(0)


if __name__ == '__main__':
    main()
