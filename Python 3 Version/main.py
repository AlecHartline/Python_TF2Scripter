import os

name = input('Bind Name (Short - Unique - No Spaces): ')
delay = 600

start = input('Letter to bind to start: ')
stop = input('Letter to bind to stop: ')

wordList = []
words = 0
alias = 0

if not os.path.isfile(os.getcwd()+'\\out.txt'):
    bind = open('out.txt', 'w')
    bind.truncate()

if not os.path.isfile(os.getcwd()+'\\inp.txt'):
    file = open('inp.txt', 'w')
    file.truncate()
    file.close()
    print('Put your desired bind text in "inp.txt" and restart program')

else:
    file = open('inp.txt', 'r+')
    bind = open('out.txt', 'r+')
    bind.truncate()
    text = file.read()
    for line in text.split('\n'):
        if line != ' ' and line != '' and line != '  ':
            for word in line.split(' '):
                if word != '-':
                    if words <= 10:
                        wordList.append(word)
                        words += 1
                    if words == 10:
                        bind.write('alias '+name+str(alias)+' "say ')
                        for i in wordList:
                            bind.write(i+' ')
                        bind.write('"\n')
                        wordList = []
                        words = 0
                        alias += 1
            bind.write('alias '+name+str(alias)+' "say ')
            if len(wordList) > 0:
                for i in range(len(wordList)):
                    bind.write(wordList[i]+' ')
            bind.write('"\n')
            words = 0
            wordList = []
            alias += 1
            
bind.write('\n//Made With TheBindMan Script v2//\n\n')
binds = 0
temp = 0

bind.write('alias '+name+'Bind'+str(binds)+' "')
for i in range(alias):
    if temp <= 3:
        bind.write(name+str(i)+'; alias '+name+'Cancel "alias '+name+'Bind'+str(binds+1)+' """; wait '+str(delay)+'; ')
        temp += 1
    if temp == 3:
        binds += 1
        bind.write(name+'Bind'+str(binds))
        bind.write('"\n')
        if i < alias-1:
            bind.write('alias '+name+'Bind'+str(binds)+' "')
        temp = 0

bind.write('\nbind '+start+' "exec '+name+'Bind; '+name+'Bind0"\n')
bind.write('bind '+stop+' "'+name+'Cancel"\n\n')

bind.write('echo '+name+'Bind has been loaded\n')
bind.write('echo Created with TheBindMan Script v2\n')

file = open('inp.txt', 'r')
bind = open('out.txt', 'r')
file.close()
bind.close()
if os.path.isfile(name+'Bind.cfg'):
    os.remove(name+'Bind.cfg')
os.rename('out.txt', name+'Bind.cfg')


