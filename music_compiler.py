import random


def findalbum(arg1, arg2):
    # searching for an album using arg1 in a place defined in arg2
    if str(arg1).lower() in str(arg2).lower():
        print(line[0][0], '-', line[0][1])


def findartist(arg1, arg2):
    # searching for artist using arg1 in a place defined in arg2
    if str(arg1).lower() in str(arg2).lower():
        print(line[0][0], '(' + line[0][1] + ')')


with open('music.csv', 'r') as file1:
    music1 = file1.readlines()
    print(music1)
music = []
for line in music1:
    line = tuple(line.split(' | '))
    name = (line[0], line[1])
    information = (int(line[2]), line[3], line[4])
    line = (name, information)
    music.append(line)
    #artist - line[0][0]
    #album - line[0][1]
    #year - line[1][0]
    #genre - line[1][1]
    #length - line[1][2]
print(music)  # developers option
repeatmain = 1
while repeatmain == 1:
    option = input("""\nWelcome in the CoolMusic! Choose the action:
                    1) Add new album
                    2) Find albums by artist
                    3) Find albums by year
                    4) Find musician by album
                    5) Find albums by letter(s)
                    6) Find albums by genre
                    7) Calculate the age of all albums
                    8) Choose a random album by genre
                    9) Show the amount of albums by an artist *
                    10) Find the longest-time album *
                    0) Exit\n""")
    if option == '1':
        artist = input("Add artist's name: ")
        album = input("Add the name of the album: ")

        again = 0
        while again == 0:
            try:
                year = int(input("Enter album's release year: "))
                again = 1
            except BaseException:
                print("Thats not a correct format, try again: ")

        genre = input("Type genre of the album: ")
        length = input("Enter lenght of the album [mm:ss]: ")
        newline = ((artist, album), (year, genre, length))
        music.append(newline)
        print(music)

        with open('music.csv', 'w') as file2:
            for line in music:
                file2.write(line[0][0] +
                            ' | ' +
                            line[0][1] +
                            ' | ' +
                            str(line[1][0]) +
                            ' | ' +
                            line[1][1] +
                            ' | ' +
                            line[1][2])

    elif option == '2':
        artist = input('Enter artist/band name: ')
        for line in music:
            findalbum(artist, line[0][0])
    elif option == '3':
        year = input('Enter year of release: ')
        for line in music:
            findalbum(year, line[1][0])
    elif option == '4':
        album = input('Enter name (or a part) of an album: ')
        for line in music:
            findartist(album, line[0][1])
    elif option == '5':
        letters = input('Enter letter(s): ')
        for line in music:
            findalbum(letters, line[0][1])
    elif option == '6':
        genre = input('Enter genre: ')
        for line in music:
            findalbum(genre, line[1][1])
    elif option == '7':
        age = 0
        for line in music:
            age1 = 2017 - line[1][0]
            age += age1
        print('The sum of albums age is: ' + str(age))
    elif option == '8':
        genre = input('Choose genre of album: ')
        genrealbums = []
        for line in music:
            if genre.lower() in line[1][1].lower():
                genrealbums.append(line)
        randomline = random.choice(genrealbums)
        print(str(randomline[0][1]), '-', str(randomline[1][1]))
    elif option == '9':
        artist = input('Enter artist/band name: ')
        i = 0
        for line in music:
            if artist.lower() == line[0][0].lower():
                i += 1
        if i > 0:
            print('Numer of artists albums in database: ' + str(i))
        else:
            print('There is no such artist in our database')
    elif option == '10':
        longest = 0
        for line in music:
            length = line[1][2].rstrip()
            length = int(length.replace(':', ''))
            if length > longest:
                longest = length
                longestalbum = line[0][1]
        print('Longest album in our database is ' + str(longestalbum))
    elif option == '0':
        repeatmain = 0
    else:
        print('Wrong pick, try again!!')
