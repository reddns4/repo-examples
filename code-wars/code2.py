# Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
# Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
# Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")

def song_decoder(song):
    res = ''
    for i in song.split('WUB'):
        if str(i) != '':
            res += i + ' '
    return res.rstrip()

print('"' + song_decoder("AWUBBWUBC") + '"', "WUB should be replaced by 1 space")
print('"' + song_decoder("AWUBWUBWUBBWUBWUBWUBC") + '"', "multiples WUB should be replaced by only 1 space")
print('"' + song_decoder("WUBAWUBBWUBCWUB") + '"', "A B C","heading or trailing spaces should be removed")