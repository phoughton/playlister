import itertools

# Your music library contains N songs and your friend wants to listen to L songs during your road trip (repeats are allowed). Make a playlist so that every song is played at least once, and a song can only be played again only if K other songs have been played. Return the number of possible playlists.

# Examples: 
# $ numPlaylists(N = 3, L = 3, K = 1)
# $ 6 // [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]


def num_play_lists(N, L, K):
    combos = []
    songs = list(range(1,N+1))
    for pos in range(L):
        # print(combos)
        if pos == 0:    
            for song in songs:
                combos.append([song])
        else:
            new_combos = []

            for pl in combos:
                for song in songs:
                    playlist = pl.copy()
                    playlist.append(song)

                    new_combos.append(playlist)
            combos = new_combos

    # Filter out lists with missing songs
    #
    all_song_combos = combos.copy()
    for song in songs:
        new_combos = []
        for playlist in all_song_combos:
            if song in playlist:
                new_combos.append(playlist)
        all_song_combos = new_combos    
 

    # Filter out lists where repeats are too soon
    #
    ok_repeat_combos = []
    for playlist in all_song_combos:
        bad_repeat = False
        for index in range(len(playlist)):
            start = max(0, index-K)
            if playlist[index] in playlist[start:index]:
                bad_repeat = True
        if not bad_repeat:
            ok_repeat_combos.append(playlist)
                
    print
    print(len(ok_repeat_combos))
    for playlist in ok_repeat_combos:
        print(playlist)


num_play_lists(N=3, L=4, K=1)
#num_play_lists(N=3, L=4, K=1)

