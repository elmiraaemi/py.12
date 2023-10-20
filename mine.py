from Media import Media
from Film import Film
from Clip import Clip
from Serise import Serise
from Documentary import Documentary
import pyfiglet

MEDIA=[]
file=open("python\T12\date.txt","r")
for line in file:
    res=line.split(",")
    if len(res)==10:
        if res[0]=="film":
            my_obj=Film(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7])
        elif res[0]=="series":
            my_obj=Serise(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8])
        elif res[0]=="documentary":
            my_obj=Documentary(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7])
        else:
            my_obj=Clip(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[9])
        MEDIA.append(my_obj)
file.close()

def write_to_database():
    d = open("python\T12\date.txt", "w")
    for m in MEDIA:
        if m.type=="film" or m.type=="documentary":
            d.write(str(m.type)+","+str(m.name)+","+str(m.director)+","+str(m.imdb)+","+str(m.url)+","+str(m.duration)+ "," + str(m.casts) + "," + str(m.productionyear) + ",1,---"+"\n")
        elif m.type=="series":
            d.write(str(m.type)+","+str(m.name)+","+str(m.director)+","+str(m.imdb)+","+str(m.url)+","+str(m.duration)+ "," + str(m.casts) + "," + str(m.productionyear) + "," + str(m.episodnumber) + ",---"+"\n")
        else:
            d.write(str(m.type)+","+str(m.name)+","+str(m.director)+","+str(m.imdb)+","+str(m.url)+","+str(m.duration)+ "," + str(m.casts) + "," + str(m.productionyear) + ",1," + str(m.genre)+"\n")
    d.close()

def loading():
    result = pyfiglet.figlet_format('your movies', font = 'roman')
    print(result)

def menu():
    print('1 for add movie')
    print('2 for edit movie')
    print('3 for delete movie')
    print('4 for search movie')
    print('5 for show list movies')
    print('6 for super search')
    print('7 for download the movie')
    print('8 for exit')

def add():
    type=input("type : ")
    name=input("name : ")
    director=input("director : ")
    imdb=input("IMDB : ")
    url=input("url : ")
    duration=input("duration : ")
    casts=input("casts (separate with |): ")
    year=input("year: ")
    if type=="film":
        new_film=Film(type,name,director,imdb,url,duration,casts,year)
        MEDIA.append(new_film)
    elif type=="documentary":
        new_documentary=Documentary(type,name,director,imdb,url,duration,casts,year)
        MEDIA.append(new_documentary)
    elif type=="series":
        episod_number=input("Enter number of episodes of series: ")
        new_series=Serise(type,name,director,imdb,url,duration,casts,year,episod_number)
        MEDIA.append(new_series)
    else:
        genre=input("Enter genre of clip:")
        new_clip=Clip(type,name,director,imdb,url,duration,casts,year,genre)
        MEDIA.append(new_clip)

def edit():
    name=input("name of media ? : ")
    
    for i in range(len(MEDIA)):
        if MEDIA[i].name==name:    
            print('1 for name')
            print('2 for IMDB')
            print('3 for casts')
            print('4 for year')
            print('5 for duration')
            print('6 for url')
            print('7 for exit')
            e = int(input())
            if e == 1:
                MEDIA[i].name=input(' type rename media : ')
                print('Done')
            elif e == 2:
                MEDIA[i].IMDB=float(input(' type reIMDB media : '))
                print('Done')
            elif e == 3:
                MEDIA[i].casts=input(' type recasts media : ')
                print('Done')
            elif e == 4:
                MEDIA[i].year=int(input(' type reyear media : '))
                print('Done')
            elif e == 5:
                MEDIA[i].duration=int(input(' type reduration media : '))
                print('Done')
            elif e == 6:
                MEDIA[i].url=input(' type reurl media : ')
                print('Done')
            elif e == 7:
                break  
        else:
            print('Does not exist')

def remove():
    name=input('name of movie ? : ')
    for media in MEDIA:
        if media.name==name:
            MEDIA.remove(media)
            print('Done')
            break
    else:
        print("Not found!")

def search():
    s=input("name or type of movie ? : ")
    for media in MEDIA:
        if media.name==s or media.type==s:
            print(media[media])            
            break
    else:
        print("Does not exist")

def advanced_search():
    a=int(input("minimum minute: "))
    b=int(input("maximum minute: "))
    n=0
    for media in MEDIA:
        if a<= int(media.duration) <=b:
            media.showinfo()
            n+=1
    if n==0:
        print("Does not exist")

def show():
    print("name \t   director \t    IMDB \t duration \t\t casts  \t\t year ")
    print()
    for media in MEDIA:
        print(media.name, "\t", media.director,"\t",media.imdb,"\t", media.duration,"\t", media.casts ,"\t\t",media.year)
        print()

loading()
while True:
    menu()
    a=int(input())
    if   a<2:
        add()
    elif a==2:
        edit()
    elif a==3:
        remove()
    elif a==4:
        search()
    elif a==5:
        show()
    elif a==6:
        advanced_search()
    elif a==7:
        name=input("\n name of movie ? : ")
        for m in MEDIA:
            if m.name==name:
                m.download()
    elif a==8:
        exit() 