import os
import fnmatch

rootDir = raw_input('Starting directory: ')
allfiles = []

for dirName, subdirlist, filelist in os.walk(rootDir):
    for filename in filelist:
        fullpath = os.path.join(dirName,filename)
        allfiles.append(fullpath)

pattern_string = raw_input('Pattern String: ')
input_file_list = fnmatch.filter(allfiles, pattern_string)

print 'found %d files that match the pattern \"%s\".' % (len(input_file_list), pattern_string)

for n in input_file_list:
    print n

codec = raw_input('ffmpeg vcodec argument: ')

for f in input_file_list:
    os.system('ffmpeg -i \"%s\" -vcodec %s  \"%s.mpg\"' % (f, codec, f))
