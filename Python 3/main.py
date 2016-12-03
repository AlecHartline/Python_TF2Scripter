import os
import time

delay = 600

wordList = []
words = 0
alias = 0

if not os.path.isfile('inp.txt'):
    file = open('inp.txt', 'w')
    file.truncate()
    file.close()
    print('Put your desired bind text in "inp.txt" and restart program')
    time.sleep(5)
    

else:
    name = input('Bind Name (Short - Unique - No Spaces): ')
    start = input('Letter to bind to start: ')
    stop = input('Letter to bind to stop: ')
    if not os.path.isfile('out.txt'):
        bind = open('out.txt', 'w')
        bind.truncate()
    file = open('inp.txt', 'r+')
    bind = open('out.txt', 'r+')
    bind.truncate()
    text = file.read()
    for line in text.split('\n'):
        words = 0
        if line != ' ' and line != '' and line != '  ':
            for word in line.split(' '):
                if word != '-':
                    if len(wordList) <= 10:
                        wordList.append(word)
                    if len(wordList) == 10 or words == len(line.split(' '))-1:
                        bind.write('alias '+name+str(alias)+' "say ')
                        for i in range(len(wordList)):
                            if i < len(wordList)-1:
                                bind.write(wordList[i]+' ')
                            else:
                                bind.write(wordList[i])
                        bind.write('"\n')
                        wordList = []
                        alias += 1
                words += 1
            
    bind.write('\n//Made With TheBindMan Script v2//\n\n')
    binds = 0
    step = 0
    items = 12
    for i in range(alias):
        if step == 0:
            bind.write('bind '+stop+' "alias '+name+'Bind'+str(binds+1)+'"\n')
            bind.write('alias '+name+'Bind'+str(binds)+' "')
        if step < items:
            bind.write(name+str(i))
            if i+1 < alias:
                bind.write('; wait '+str(delay))
            if step < items-1 and i < alias-1:
                bind.write('; ')
            step += 1

        if step == items or i == alias-1:
            binds += 1
            bind.write('"\n\n')
            step = 0

    bind.write('\nbind '+start+' "exec '+name+'Bind; '+name+'Bind0"\n')

    bind.write('\necho '+name+'Bind has been loaded\n')
    bind.write('echo Created with TheBindMan Script v2\n')

    file = open('inp.txt', 'r')
    bind = open('out.txt', 'r')
    file.close()
    bind.close()
    if os.path.isfile(name+'Bind.cfg'):
        os.remove(name+'Bind.cfg')
    os.rename('out.txt', name+'Bind.cfg')


