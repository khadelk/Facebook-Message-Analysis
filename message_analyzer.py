import re

class Messages:
    def __init__(self, file):
        self.file = file
        self.yourName = input('Enter your name: ')
        self.otherName = input('Enter the name of the person whose messages you wish to analyze: ')
        
    def getFile(self):
        infile=open(self.file, 'r')
        content=infile.read()  
        table=str.maketrans('''@#$%^&*()_+=-][\{}|;':"/<>`~\n''','''                             ''')
        splitLines=content.split('\n')[6:]
        joinAgain=' '.join(splitLines)
        self.s=joinAgain.translate(table).strip()    
        return self.s 
    
    def cleanup(self):
        newL=[]
        messages = self.getFile() 
        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']
        rx=re.compile(fr"\s+(?=(?:{'|'.join(months)})\b)", re.I)
        r = (rx.split(messages)) 
        for i in r:
            newL.append([i])
        return newL  
    
    def countMessages(self):
        messageList = self.cleanup()
        count = 0
        countYourName = 0
        countOtherName = 0
        for i in messageList:
            count +=1
            for letters in i:
                if self.yourName in letters:
                    countYourName +=1
                if self.otherName in letters:
                    countOtherName +=1
        print(count)
        print(countYourName)
        print(countOtherName)
    
    def splitList(self):
        newl = []
        final = []
        messageList=self.cleanup()
        newDict = {}
        for l in messageList:
            for message in l:
                for words in message.split(' '):
                    if  words== 'AM':
                        newl.append([l[0][0:l[0].index('AM')+2]]), newl.append([l[0][l[0].index('AM')+2:]])
                    if words == 'PM':
                        newl.append([l[0][0:l[0].index('PM')+2]]), newl.append([l[0][l[0].index('PM')+2:]])
        return newl 
    
    def countWords(self):
        lst = self.splitList()
        messages = [lst[i] for i in range(len(lst)-3) if i%2==1]
        myDict = {}
        lenyourName = len(self.yourName.split(' '))
        lenotherName = len(self.otherName.split(' '))
        for l in messages:
            for words in l:
                if self.yourName in words:
                    if self.yourName in myDict:
                        myDict[self.yourName] += len(words.split(' '))-lenyourName
                    else:
                        myDict[self.yourName] = len(words.split(' '))-lenyourName
                if self.otherName in words:
                    if self.otherName in myDict:
                        myDict[self.otherName] += len(words.split(' '))-lenyourName
                    else:
                        myDict[self.otherName] = len(words.split(' '))-lenyourName  
        return myDict
    
    def mostWords(self):
        wordDict = {}
        lst = self.splitList()
        listmessages = [lst[i] for i in range(len(lst)-3) if i%2==1]        
        for msg in listmessages:
            for sent in msg:
                for words in sent.split(' '):
                    if words not in self.yourName and words not in self.otherName:
                        if words.lower() in wordDict:
                            wordDict[words.lower()]+=1
                        else:
                            wordDict[words.lower()]=1
                            
        sorted_values = sorted(wordDict.values()) # Sort the values
        sorted_dict = {}
        
        for i in sorted_values:
            for k in wordDict.keys():
                if wordDict[k] == i:
                    sorted_dict[k] = wordDict[k]
                    break        
        return sorted_dict
                
    
    
