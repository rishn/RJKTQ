import v
import string
import random
import csv
import sys
import os
import time
from tabulate import tabulate
from getpass import getpass
def collectinfo(path):
    with open(path,"rb") as file:
        infolist=[eval("".join(list(i.decode("utf-8")[0:len(i)-1]))) for i in file.readlines()]
    return infolist
def writeinfo(a,path):
    with open(path,"ab") as file:
        file.write((str([v.user,v.password,v.rank,v.level,v.high,v.matches,v.wins,v.wl,v.achieve,v.xp,v.levelxp,v.avatar])+"\n").encode("utf-8")) if a==1 and v.isadmin=="No" else file.write((str([v.user,v.password,v.padmin])+"\n").encode("utf-8")) if a==1 and v.isadmin=="Yes" else file.write((str([v.user,v.password])+"\n").encode("utf-8")) if a==2 else print("",end="")
        v.profiles,v.admins=collectinfo(r"data\2.dat"),collectinfo(r"data\3.dat")
def loop(query):
    while True:
        reply=input(query).lower()
        a=1 if reply in v.yes else 2 if reply in v.no else print("Invalid")
        if a==1 or a==2:
            return a
def addtexts(path):
    while True:
        with open(path,"a") as file:
            file.write(input("Enter text to be added: ")+"\n")
        a=loop("Would you like to add more texts? (Yes/No): ")
        if a==2:
            return
def cleartexts(path):
    with open(path,"r") as file:
        texts,a=file.readlines(),[]
    while True:
        try:
            num=int(input("Enter serial no. of text to be deleted: "))
            a.append(texts[num-1])
        except (ValueError,IndexError) as e:
            print("Invalid serial no.")
        b=loop("Would you like to clear more texts? (Yes/No): ")
        if b==2:
            break
    for i in range(len(a)):
        texts.remove(a[i])
    with open(path,'w') as file:
        file.writelines(texts)
def clearance():
    for a in range(5):
        with open(r"data\1.dat","rb") as file:
            admin=file.read().decode("utf-8")
        key=getpass("Enter admin clearance key:".center(172))
        print(("*"*len(key)).center(172)+"\n"+"Invalid clearance key".center(172) if key!=admin else ("*"*len(key)).center(172))
        if key==admin:
            return "Clear"
def buffer(path):
    with open(path,"r") as file:
        texts=file.readlines()
    time.sleep(2)
    print("\n"+"<"*172+"\n"*19+random.choice(texts).split("\n")[0].center(172)+" "*81+"Loading" if texts!=[] else "\n"+"<"*172+"\n"*20,end="",flush=True)
    for i in range(3):
        time.sleep(1.5)
        print("."+"\n"*19 if i==2 else "." if i==0 else ".",end="",flush=True)
def checkinput(query):
    while True:
        answer=input(query)
        for i in answer:
            print("Invalid answer\n" if i.isupper() else "",end="")
            if i.isupper():
                break
        else:
            return answer
def createaccount(infolist):  
    for a in range(5):
        v.usercreate,passcreate=input("Enter Username (Max. 35 chars.; only letters, digits or/and underscore):\n"),getpass(prompt="Enter Password (Only letters, digits or/and underscore): ")
        print("*"*len(passcreate))
        passconfirm,c=getpass(prompt="Confirm Password: "),0
        if v.usercreate=="" or len(v.usercreate)>35:
            a=1
        else:
            for a in v.usercreate:
                a=0 if a in v.userchar else 1
                if a==1:
                    break
        if passcreate=="":
            b=1
        else:
            for b in passcreate:
                b=0 if b in v.userchar else 1
                if b==1:
                    break
        for i in infolist:
            if v.usercreate==i[0]:
                c=1
                break
        print("*"*len(passconfirm)+"\nInvalid Username" if a==1 else "*"*len(passconfirm)+"\nUsername already exists" if c==1 else "*"*len(passconfirm))
        print("Invalid Password\n" if b==1 else "Passwords do not match\n" if passconfirm!=passcreate else "")
        if passconfirm==passcreate and b==0 and c==0 and a==0:
            print("Your account has been successfully created.".center(172)+"\n"+f"Welcome {v.usercreate}".center(172),end="")
            print("\n" if v.isadmin=="No" else "(admin)".center(172) if v.isadmin=="Yes" and v.padmin=="No" else "(primary admin)".center(172),end="") 
            v.user,v.password=v.usercreate,passcreate
            writeinfo(2,r"data\2.dat") if v.isadmin=="No" else writeinfo(2,r"data\3.dat")
            break
def login(infolist):
    for a in range(5):
        v.userlogin,passlogin,b=input("Enter Username:\n"),getpass(prompt="Enter Password: "),0
        if v.isadmin=="Yes":
            for i in infolist:
                if [v.userlogin,passlogin]!=i and [v.userlogin,passlogin]==i[0:2]:
                    v.padmin=i[2]
        print("*"*len(passlogin)+"\nUsername or Password is incorrect.\n\n" if [v.userlogin,passlogin] not in infolist or v.userlogin=="" else "*"*len(passlogin)+"\n\n"+f"Welcome {v.userlogin}".center(172),end="")
        if [v.userlogin,passlogin] in infolist and v.userlogin!="":
            v.user,v.password=v.userlogin,passlogin
            break
    print("(primary admin)".center(172) if v.padmin=="Yes" and v.user!="" else "(admin)".center(172) if v.isadmin=="Yes" and v.user!="" else "",end="")
def lifeline():
    print(str(v.ask))
    while True:
        reply,b=input("Choose your lifeline (by entering the corresponding number): "),[]
        a=1 if reply=='1' and "1.Expert" in v.ask else 2 if reply=='2' and "2.Friend" in v.ask else 3 if reply=='3' and "3.Magic 8 Ball" in v.ask else print("\nInvalid\n") 
        if a==1:
            v.lifeans,ll=random.choice((",".join(random.choice(v.ans))+","+(",".join(v.answer))).split(",")),1
            v.ask.remove("1.Expert")
            break
        elif a==2:
            v.lifeans,ll=random.choice((",".join(random.choice(v.ans))+","+(",".join(random.choice(v.ans)))+","+(",".join(v.answer))).split(",")),2
            v.ask.remove("2.Friend")
            break
        elif a==3:
            for d in range(len(v.ans)):
                b.extend(v.ans[d])
            v.lifeans,ll=random.choice(b),3
            v.ask.remove("3.Magic 8 Ball")
            break
    print("\nThe answer might be:",v.lifeans,"\n")
    return ll
def play():
    with open(r"data\5.dat","rb") as file:
            q1,a,c,f,g,ll,v.ask,v.ans=[i.decode("utf-8") for i in file.readlines()],0,0,0,0,0,["1.Expert","2.Friend","3.Magic 8 Ball"],collectinfo(r"data\6.dat")
    print(("="*172)+"QUICK PLAY".center(172)+("="*172)+"\n"+"Failed to start match... Not enough questions entered...".center(172)+'Ask admin to add more questions in "Settings"...'.center(172) if len(q1)<20 else ("="*172)+"QUICK PLAY".center(172)+("="*172)+"\n",end="") 
    if len(q1)<20:    
        return
    print("Are you ready?".center(172),end="",flush=True)
    time.sleep(2)
    print("Let's go!".center(172),flush=True)
    time.sleep(2)
    for b in range(20):
        e,h,q2=0,0,random.choice(q1)
        reply=input(f"Question {b+1} :\n{q2}").lower() if a>=3 else input(f'Question {b+1} :\n{q2}(You can use lifelines by entering "lifeline" or leave the match by entering "quit"/"leave"/"exit".)\n').lower()
        print("\n")
        for d in range(len(q1)):
            if q1[d]==q2:
                v.answer=v.ans[d]
                if reply in v.life and reply not in v.answer:
                    print("All lifelines used already.\n" if a>=3 else "Using lifeline...") 
                    a+=1
                    ll=lifeline() if a<4 else ll 
                    h=1 if a<4 else h
                    reply=input(q2).lower()
                    print("\n")
                    if reply!=v.lifeans and a<4:
                        e,f=1,f+1
                        g=1 if ll==3 else 0
                print("Correct\n" if reply in v.answer else "Please wait...\n" if reply in v.quits else "Incorrect\n")    
                c=1 if reply not in v.answer else 0
                q1.remove(q1[d])
                v.ans.remove(v.ans[d])
                break
        if c==1:
            break
    score=str(b*500) if c==1 else str((b+1)*500)
    v.wins=v.wins if c==1 else str(int(v.wins)+1)
    v.matches,v.xp=str(int(v.matches)+1),v.xp+int(score)
    v.wl='0' if int(v.matches)==int(v.wins) else str(int(v.wins)/(int(v.matches)-int(v.wins)))
    print("Your score:",score,"\n")
    print("New high score!\n\n" if int(v.high)<int(score) else "",end="")
    v.high=score if int(v.high)<int(score) else v.high
    print("Level Up!\n\n" if v.xp-v.levelxp>=25000 else "",end="")
    v.levelxp=v.levelxp+25000 if v.xp-v.levelxp>=25000 else v.levelxp
    v.level=str(int(v.level)+1) if v.xp-v.levelxp>=25000 else v.level
    print("YOU LOSE!" if int(score)<10000 else "YOU WIN!")
    achievements(1) if int(score)==10000 else print("",end="")
    achievements(4) if a==0 and int(score)==10000 else (achievements(2),achievements(3)) if a>=3 and f==0 and int(score)==10000 else achievements(2) if 0<=f<a and int(score)==10000 else print("",end="")
    achievements(5) if a>=3 and f==0 and int(score)<10000 else print("",end="")
    achievements(6) if int(v.level)==50 else achievements(7) if int(v.level)==100 else print("",end="")
    achievements(8) if int(v.wins)==25 else achievements(9) if int(v.wins)==50 else print("",end="")
    achievements(10) if b==0 else print("",end="")
    achievements(11) if ll==1 and e==0 and h==1 and int(score)<10000 else achievements(12) if ll==2 and e==0 and h==1 and int(score)<10000 else print("",end="")
    achievements(13) if "3.Magic 8 Ball" not in v.ask and g==0 and ((0<=f<4 and h==0 and e==0 and int(score)<10000) or (f==2 and a==3 and e==1 and int(score)<10000) or (f==1 and a==2 and e==1 and int(score)<10000) or (0<f<a and int(score)==10000)) else print("",end="")
    achievements(14) if f==1 and e==1 and int(score)<10000 else achievements(15) if 1<f<4 and e==1 and a>3 and int(score)<10000 else print("",end="")
    (achievements(14),achievements(15)) if 1<f<4 and a<=3 and e==1 and int(score)<10000 else print("",end="")
    achievements(15) if 0<f<4 and ((e==0 and int(score)<10000) or (f<a and int(score)==10000)) else print("",end="")
    leaderboard(1)
def profile():
    if v.isadmin=="Yes":
        print("="*172+"PROFILE".center(172)+"="*172+"\n"+v.user.center(172)+"\n\n\n\n"+"subordinate admin".center(172) if v.padmin=="No" else "="*172+"PROFILE".center(172)+"="*172+"\n"+v.user.center(172)+"\n\n\n\n"+"primary admin".center(172),end="")
        return
    a=''
    for row in v.achieve:
            a=a+row[0]+" : "+row[1]+"\n\t\t"
    print("="*172+"PROFILE".center(172)+"="*172+"\n"+v.user.center(172)+"\nAvatar: "+v.avatar+"\n\nLevel: "+v.level+"\nNo. of matches played: "+v.matches+"\nNo. of wins: "+v.wins+"\nW/L: "+v.wl+"\nHigh score: "+v.high+"\nAchievements: "+a+"\n"+"Rank: "+v.rank)
    if v.achieve!=[]:
        while True:
            reply1=input("\n\nChange Avatar? (Yes/No): ").lower()
            d=1 if reply1 in v.yes else 2 if reply1 in v.no else print("Invalid")
            if d==1:
                print("\n")
                for a in range(len(v.achieve)):
                    print(f"{a+1}. "+v.achieve[a][0]+",",end=" ")
                print(f"{a+2}. Remove avatar, {a+3}. No change\n")
                while True:
                    reply2=input("Choose your avatar (by entering the corresponding number): ")
                    b=1 if (reply2 in string.digits or reply2 in ['10','11','12','13','14','15','16','17']) and len(v.achieve)+2>=int(reply2) else print("Invalid")
                    if b==1:
                        v.avatar=v.achieve[int(reply2)-1][0] if len(v.achieve)>=int(reply2) else "" if len(v.achieve)+1==int(reply2) else v.avatar 
                        break
                print("\nAvatar changed" if (reply2 in string.digits or reply2 in ['10','11','12','13','14','15','16','17']) and len(v.achieve)+1>=int(reply2) else "")
            if d==1 or d==2:
                break
def achievements(b):
    if b==0:
        print(("="*172)+"ACHIEVEMENTS".center(172)+("="*172))
        for row in v.achievement:
            print(row[0]+" : "+row[1])
    elif b>0:
        v.achieve.append(v.achievement[b-1])
        v.achieve=[list(a) for a in list(dict.fromkeys([(*a,) for a in v.achieve]))]
def leaderboard(b):
    with open(r"data\4.csv","r+",newline="") as file:
        if b==0:
            file.seek(0,0)
            lb,heading,d=list(csv.reader(file,delimiter=',')),["Rank","High score","Level","No. of Achievements","Username"],[]
            for a in lb:
                for b in range(len(lb)):
                    for c in range(b):
                        if int(lb[b][0])>int(lb[c][0]) or (int(lb[b][0])==int(lb[c][0]) and int(lb[b][1])>int(lb[c][1])) or (int(lb[b][0])==int(lb[c][0]) and int(lb[b][1])==int(lb[c][1]) and int(lb[b][2])>int(lb[c][2])) or (int(lb[b][0])==int(lb[c][0]) and int(lb[b][1])==int(lb[c][1]) and int(lb[b][2])==int(lb[c][2]) and lb[b][3]<lb[c][3]):
                            lb[b],lb[c]=lb[c],lb[b]
            for b in range(len(lb)):
                for c in range(len(lb)):
                    d.append(lb[c]) if lb[b][3] in lb[c] and (int(lb[b][0])>int(lb[c][0]) or (int(lb[b][0])==int(lb[c][0]) and int(lb[b][1])>int(lb[c][1])) or (int(lb[b][0])==int(lb[c][0]) and int(lb[b][1])==int(lb[c][1]) and int(lb[b][2])>int(lb[c][2]))) else print("",end="")                        
            for e in d:
                lb.remove(e) if e in lb else print("",end="")
            lb=[list(a) for a in list(dict.fromkeys([(*a,) for a in lb]))]
            for a in range(len(lb)):
                lb[a].insert(0,str(a+1))
                v.rank=str(a+1) if v.user in lb[a] else v.rank
            print(("="*172)+"LEADERBOARD".center(172)+("="*172)+"\n"+tabulate(lb,heading,tablefmt="fancy_grid"))     
        elif b==1:
            write=csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            file.seek(0,2)
            write.writerow((v.high,v.level,str(len(v.achieve)),v.user))
def settings():
    print(("="*172)+"SETTINGS".center(172)+("="*172))
    options="1. Add questions and answers   2. View stored game data   3. Clear stored game data   4. Change admin clearance key   5. Edit admin data   6. Edit buffer texts   7. Exit".center(172) if v.padmin=="Yes" else "1. Add questions and answers           2. View stored game data           3. Clear stored game data           4. Edit buffer texts           5. Exit".center(172)
    while True:
        reply1=input("\nWhat would you like to do?\n"+options+"(Enter the corresponding number.) ")
        a=1 if reply1=="1" else 2 if reply1=="2" else 3 if reply1=="3" else 4 if reply1=="4" and v.padmin=="Yes" else 5 if reply1=="5" and v.padmin=="Yes" else 6 if (reply1=="6" and v.padmin=="Yes") or (reply1=="4" and v.padmin=="No") else 7 if (reply1=="7" and v.padmin=="Yes") or (reply1=="5" and v.padmin=="No") else print("Invalid")
        if a==1:
            while True:
                q,ans=input("\n\nEnter question to be added: "),[]
                ans.append(checkinput("Enter the correct answer to the question (in lowercase only): "))
                while True:
                    reply2=input("Would you like to add more answers?(Yes/No): ").lower()
                    b=1 if reply2 in v.yes else 2 if reply2 in v.no else print("Invalid")
                    if b==1:
                        ans.append(checkinput("Enter the correct answer to the question (in lowercase only): "))
                    if b==2:
                        break
                with open(r"data\5.dat","ab") as file:
                    file.write((q+"\n").encode("utf-8"))
                with open(r"data\6.dat","ab") as file:
                    file.write((str(ans)+"\n").encode("utf-8"))
                c=loop("Would you like to enter more questions? (Yes/No): ")
                if c==2:
                    break
            print("Questions and answers successfully added...")  
        elif a==2:
            with open(r"data\4.csv",'r') as file1:
                with open(r"data\5.dat",'rb') as file2:
                    heading1,heading2,heading3,heading4,b,c,d,e,f,g=["User","Rank","Lvl","HS","Plays","Wins","W/L","Titles","XP","BreakXP","Avatar"],["HS","Lvl","No. of Achievements","User"],["Sl no.","Question"],["Sl no.","Set of answers"],[i.decode("utf-8") for i in file2.readlines()],collectinfo(r"data\6.dat"),list(csv.reader(file1,delimiter=',')),[],[],[]
            for i in range(len(b)):
                e.append([str(i+1),b[i]])
                f.append([str(i+1),",".join(c[i])])
            for row in v.profiles:
                h=list(row)
                if len(h)!=2 and h[8]!="":
                    for i in range(len(h[8])):
                        for j in range(len(v.achievement)):
                            if h[8][i]==v.achievement[j]:
                                h[8][i]=str(j+1)
                                break
                    h[8]=",".join(h[8])
                h.remove(h[1])
                g.append(h)
            print("\n\nPrinting player accounts data...\n\n"+tabulate(g,heading1,tablefmt="psql")+"\n\n\nPrinting leaderboard data...\n\n"+tabulate(d,heading2,tablefmt="psql")+"\n\n\nPrinting questions and answers...\n\nQuestions\n"+tabulate(e,heading3,tablefmt="psql")+"\n\n"+"Corresponding answers\n"+tabulate(f,heading4,tablefmt="psql")+"\n")
        elif a==3:
            for c in range(5):
                j,h=['accounts','leaderboard','questions and answers'],0
                reply2=input(f'\n\nWhat would you like to clear?\n1. {j[0]}, 2. {j[1]}, 3. {j[2]}\n(Enter the corresponding number or keep pressing "Enter" to not clear anything.) ')
                b=1 if reply2=='1' else 2 if reply2=='2' else 3 if reply2=='3' else print("Invalid",end="")
                if b==1 or b==2 or b==3:
                    print(f"\nClearing {j[b-1]} data...\n")
                if b==1:
                    reply3=input("Do you want to clear (1.all accounts) or (2. selected accounts)? (Enter the corresponding number.) ")
                    e=1 if reply3=="1" else 2 if reply3=="2" else print("Invalid",end="")
                    if e==1:
                        v.profiles,h=[],1
                    elif e==2:
                        while True:
                            f,reply4,g=len(v.profiles),input("Enter account whose data is to be deleted:\n"),[]
                            for i in v.profiles:
                                g.append(i) if reply4==i[0] else print("",end="")
                            for i in g:
                                h=1
                                v.profiles.remove(i)
                            print("Invalid account\n" if len(v.profiles)==f else "",end="")
                            d=loop("Would you like to clear more accounts? (Yes/No): ")
                            if d==2:
                                break
                    if reply3 in ['1','2']:
                        with open(r"data\2.dat","wb") as file:
                            file.writelines([(str(i)+"\n").decode("utf-8") for i in v.profiles])
                elif b==2:
                    with open(r"data\4.csv",'w',newline=''):
                        h=1
                elif b==3:
                    reply3=input("Do you want to clear (1.all questions and answers) or (2. selected questions and answers)? (Enter corresponding number.) ")
                    e=1 if reply3=="1" else 2 if reply3=="2" else print("Invalid")
                    if e==1:
                        q,ans,h=[],[],1
                    elif e==2:
                        with open(r"data\5.dat","rb") as file:
                            q,ans,f,g=file.readlines(),collectinfo(r"data\6.dat"),[],[]
                        while True:
                            try:
                                num=int(input("Enter serial no. of question and set of answers to be deleted: "))
                                f.append(q[num-1])
                                g.append(ans[num-1]) 
                            except (ValueError,IndexError) as e:
                                print("Invalid serial no.")
                            d=loop("Would you like to clear more questions and answers? (Yes/No): ")
                            if d==2:
                                break
                        for i in range(len(f)):
                            h=1
                            q.remove(f[i])
                            ans.remove(g[i])
                    if reply3 in ['1','2']:
                        with open(r"data\5.dat",'wb') as file:
                            file.writelines(q)
                        with open(r"data\6.dat",'wb') as file:        
                            file.writelines([(str(i)+"\n").decode("utf-8") for i in ans])
                print(f"Cleared required {j[int(reply2)-1]} data...\n" if h==1 else "\n" if c==4 else "",end="")
                if reply2 in ['1','2','3']:
                    break
        elif a==4:
            with open(r"data\1.dat","rb") as file:
                admin==file.read().decode("utf-8")
            key=getpass("\n\n"+"Enter new admin clearance key:".center(172))
            print(("*"*len(key)).center(172))
            if key==admin:
                newkey=getpass("Enter new admin clearance key:".center(172))
                print(("*"*len(newkey)).center(172))
                confirm=getpass("Confirm new admin clearance key:".center(172))
                print(("*"*len(confirm)).center(172))
                if newkey not in [admin,""] and confirm==newkey:
                    with open(r"data\1.dat",'wb') as file:
                        file.write(newkey.encode("utf-8"))
                    print("Clearance key successfully updated...".center(172))
                else:
                    print("Invalid key".center(172))
            else:
                print("Invalid key".center(172))
        elif a==5:
            heading,d=["User","Primary Admin"],[]
            for i in v.admins:
                c=list(i)
                c.remove(c[1])
                d.append(c)
            print("\n\nPrinting admin accounts data...\n\n"+tabulate(d,heading,tablefmt="psql")+"\n")
            while True:
                reply2=input("Do you want to delete subordinate admin account info? (Yes/No): ")
                b=1 if reply2 in v.yes else 2 if reply2 in v.no else print("Invalid")
                if b==1:
                    while True:
                        c,reply3,e=len(v.admins),input("Enter account whose data is to be deleted:\n"),[]
                        for i in range(len(v.admins)):
                            e.append(v.admins[i]) if reply3==v.admins[i][0] and ((len(v.admins[i])==2 and v.admins[i+1][2]=="No") or (len(v.admins[i])==3 and v.admins[i][2]=="No")) else print("",end="")
                        for i in e:
                            v.admins.remove(i)
                        print("Invalid account\n" if len(v.admins)==c else "",end="")
                        d=loop("Would you like to clear more accounts? (Yes/No): ")
                        if d==2:
                            break
                    with open(r"data\6.dat","wb") as file:
                        file.writelines([(str(i)+"\n").decode("utf-8") for i in v.admins])
                if b in [1,2]:
                    break
        elif a==6:
            with open(r"data\7.txt","r") as file1:
                with open(r"data\8.txt","r") as file2:
                    heading1,heading2,actions,hints=["Sl no.","Actions"],["Sl no.","Hints"],file1.readlines(),file2.readlines()
            actions,hints=[[actions.index(i)+1,i] for i in actions],[[hints.index(i)+1,i] for i in hints]
            print("\n\nPrinting actions displayed at the start of the game...\n\n"+tabulate(actions,heading1,tablefmt="psql")+'\n\nPrinting hints displayed at the "Main Menu"...\n\n'+tabulate(hints,heading2,tablefmt="psql")+"\n")
            for i in range(5):
                reply2=input('How would you like to edit buffer texts?\n1. Add actions  2. Add hints  3. Delete actions  4. Delete hints  (Enter the corresponding number or keep pressing "Enter" to not make any changes.) ')
                addtexts(r"data\7.txt") if reply2=="1" else addtexts(r"data\8.txt") if reply2=="2" else cleartexts(r"data\7.txt") if reply2=="3" else cleartexts(r"data\8.txt") if reply2=="4" else print("Invalid\n")
                if reply2 in ['1','2','3','4']:
                    break
        elif a==7:
            return
def quitgame(b):
    print(("="*172)+"QUIT".center(172)+("="*172) if b==0 else "<"*172+"="*172+"QUIT".center(172)+("="*172))
    while True:
        reply1=input("Do you really want to quit the game? (Yes/No): ").lower()
        v.x=0 if b==0 and reply1 in v.yes else sys.exit() if b==1 and reply1 in v.yes else print("") if b==1 and reply1 in v.no else print("",end="") if b==0 and reply1 in v.no else print("Invalid")
        if reply1 in v.no or (b==0 and reply1 in v.yes):
            return
if os.path.isdir("data")==False:
    os.mkdir("data")
with open(r"data\1.dat","a+b") as f1,open(r"data\2.dat","ab") as f2,open(r"data\3.dat","ab") as f3,open(r"data\4.csv","a",newline='') as f4,open(r"data\5.dat","ab") as f5,open(r"data\6.dat","ab") as f6,open(r"data\7.txt","a") as f7,open(r"data\8.txt","a") as f8:
    print("\n"*15+"+"*172+"/"*86+"\\"*86+"="*172+">"*172+"RJK'S".center(172)+"TRIVIA QUEST™".center(172)+"<"*172+"="*172+"\\"*86+"/"*86+"+"*172,flush=True)
    f1.seek(0,0)
    reply,admin,v.profiles,v.admins=getpass(prompt="\n"*3+'Press "Enter" to start'.center(172)+"\n"*9),f1.read().decode("utf-8"),collectinfo(r"data\2.dat"),collectinfo(r"data\3.dat")
buffer(r"data\7.txt")
if admin=="":
    v.padmin,v.isadmin="Yes","Yes"
    while True:
        with open(r"data\3.dat","wb") as file:
            print(">"*172)
        newkey,v.admins=getpass(prompt="Enter new admin clearance key:".center(172)),[]
        print(("*"*len(newkey)).center(172))
        confirm=getpass(prompt="Confirm new admin clearance key:".center(172))
        print(("*"*len(confirm)).center(172)+"\n"+"Admin clearance key successfully updated...".center(172) if newkey==confirm and newkey!="" else ("*"*len(confirm)).center(172)+"\n"+"Invalid key".center(172)+"\n")
        if newkey==confirm and newkey!="": 
            with open(r"data\1.dat","wb") as file:
                file.write(newkey.encode("utf-8"))
            while True:
                print("<"*172+"="*172+"LOG IN".center(172)+"="*172+"\nCreate account.\n")
                if clearance()=="Clear":
                    createaccount(v.admins)
                if v.user!="":
                    break
            break
else:         
    while True:
        print(">"*172+"="*172+"LOG IN".center(172)+"="*172+"\n" if v.y==1 else "",end="")
        reply1,v.padmin,v.y=input("\n1. Player or 2. Admin ? (Enter the correspondng no.): "),"No",0
        v.isadmin="No" if reply1=="1" else "Yes" if reply1=="2" else v.isadmin
        print("Invalid\n" if reply1 not in ['1','2'] else "",end="")
        if reply1 in ['1','2']:
            reply2=input("Don't have an account? (Yes/No): ").lower()
            print("\n" if reply2 in v.yn else "\nInvalid")
            if reply2 in v.yn:
                v.y=1
                print("Create account.\n" if reply2 in v.no else "Sign In.\n")
                if v.isadmin=="No" or clearance()=="Clear":
                    createaccount(v.profiles) if reply2 in v.no and reply1=="1" else createaccount(v.admins) if reply2 in v.no and reply1=="2" else login(v.profiles) if reply2 in v.yes and reply1=="1" else login(v.admins)  
                quitgame(1) if v.user=="" else print("",end="")
                if v.user!="":
                    break
if v.isadmin=="No":
    for j in range(len(v.profiles)):
        if [v.user,v.password]==v.profiles[j][0:2] and [v.user,v.password]!=v.profiles[j] and v.user==v.userlogin:  
            v.rank,v.level,v.high,v.matches,v.wins,v.wl,v.achieve,v.xp,v.levelxp,v.avatar=v.profiles[j][2],v.profiles[j][3],v.profiles[j][4],v.profiles[j][5],v.profiles[j][6],v.profiles[j][7],v.profiles[j][8],v.profiles[j][9],v.profiles[j][10],v.profiles[j][11]
        elif v.user==v.usercreate or (v.user==v.userlogin and [v.user,v.password]!=v.profiles[j][0:2] and [v.user,v.password]==v.profiles[j-1]):
            v.rank,v.level,v.high,v.matches,v.wins,v.wl,v.achieve,v.xp,v.levelxp,v.avatar="","1","0","0","0","0",[],0,0,""
            print(">"*172,end="")
            (profile(),leaderboard(1))
            break
while True:
    buffer(r"data\8.txt")
    print(">"*172+"="*172+"RJKTQ®".center(172)+"MAIN MENU".center(172)+"="*172,end="",flush=True)
    reply=input("1.Play             2.Profile             3.Achievements             4.Leaderboard             5.Credits             6.Help             7.Quit".center(172)+"\nWhere would you like to go next?\n(Enter the corresponding number.) ") if v.isadmin=="No" else input("1.Profile                  2. Settings                  3.Credits                  4.Help                  5.Quit".center(172)+"\nWhere would you like to go next?\n(Enter the corresponding number.) ")
    buffer(r"data\8.txt")
    print(">"*172,end="")
    play() if reply=="1" and v.isadmin=="No" else profile() if (reply=="1" and v.isadmin=="Yes") or (reply=="2" and v.isadmin=="No") else achievements(0) if reply=="3" and v.isadmin=="No" else leaderboard(0) if reply=="4" and v.isadmin=="No" else print(v.gamecredits,end="") if (reply=="5" and v.isadmin=="No") or (reply=="3" and v.isadmin=="Yes") else print(v.patch) if (reply=="6" and v.isadmin=="No") or (reply=="4" and v.isadmin=="Yes") else quitgame(0) if (reply=="7" and v.isadmin=="No") or (reply=="5" and v.isadmin=="Yes") else settings() if reply=="2" and v.isadmin=="Yes" else print("\nInvalid")
    if v.x==0:
        break   
writeinfo(1,r"data\2.dat") if v.isadmin=="No" else writeinfo(1,r"data\3.dat") 
