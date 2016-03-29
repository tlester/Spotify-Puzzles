import sys

def get_key(e):
    return (-e[0], e[2])

def get_quality(songs):
    for song in songs:
        song[0] = int(song[0]) * int(song[2])
    return songs

def main():
    songs = []

    count = 0
    for line in sys.stdin:
        line = line.rstrip('\n')
        songs.append(line.split(' '))
        songs[count].append(count)
        count += 1

    tracks = songs[0][0]
    fin_count = int(songs[0][1])
    del songs[0]
    songs = get_quality(songs)
    songs.sort(key=get_key)
    for winner in range(0, fin_count):
        print songs[winner][1]





if __name__ == "__main__":
    sys.exit(main())
