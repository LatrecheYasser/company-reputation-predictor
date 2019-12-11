import json
import os

to_replace = {"À" : "A","Á" : "A","Â" : "A","Ã": "A","Ä": "A",
    "Å": "A",
    "Æ": "AE",
    "Ç": "C",
    "È": "E",
    "É": "E",
    "Ê": "E",
    "Ë": "E",
    "Ì": "I",
    "Í": "I",
    "Î": "I",
    "Ï": "I",
    "Ñ": "N",
    "Ò": "O",
    "Ó": "O",
    "Ô": "O",
    "Õ": "O",
    "Ö": "O",
    "Ø": "O",
    "Ù": "U",
    "Ú": "U",
    "Û": "U",
    "Ü": "U",
    "Ý": "Y",
    "à": "a",
    "á": "a",
    "â": "a",
    "ã": "a",
    "ä": "a",
    "å": "a",
    "æ": "ae",
    "è": "e",
    "é": "e",
    "ç": "c",
    "ê": "e",
    "ë": "e",
    "ì": "i",
    "í": "i",
    "î": "i",
    "ï": "i",
    "ð": "o",
    "ñ": "n",
    "ò": "o",
    "ó": "o",
    "ô": "o",
    "õ": "o",
    "ö": "o",
    "ø": "o",
    "ù": "u",
    "ú": "u",
    "û": "u",
    "ü": "u",
    "ý": "y",
    "ÿ": "y",
    "’":"'"}



files = os.listdir()

files.remove('process.py')

for y in files:
    if y[0] != '_':
        print(y)

    with open(y) as f:
        file = json.load(f)

        

    to_remove = list()
    for i in range(len(file['list'])):

        if len(file['list'][i]['text']) < 15:
            to_remove.append(i)
        else:
            try:
                file['list'][i].pop('description')
            except:
                pass
            for f in ['text','title']:
                for k in to_replace.keys():
                    y = y.replace(k,to_replace[k])
                    file['list'][i][f] = file['list'][i][f].replace(k,to_replace[k])
        
    file['list'][i]['tags'] = [y[:-5]]
        
    j = 0
    for i in to_remove:
        file['list'].pop(i-j)
        j += 1
            
    with open('_'+y, 'w') as fp:
        fp.write(
        '{ \"list\" : [ \n' +
        ',\n'.join(json.dumps(i) for i in file['list']) +
        ']\n } ')
