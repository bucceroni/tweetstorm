def numberLimit(text, limit):
    file = open(text)
    i = 1
    count_char = 1
    while count_char > 0:
        tweet = file.read(limit)
        count_char = len(tweet) 
        if count_char == limit:
            i = i + 1
        else:
            count_char = 0
            f = i
            file.close()
    return f

def arrayNumber(text, limit, f):
    file = open(text)
    array = []
    i = 1
    count_char = 1
    while count_char > 0:
        tweet = file.read(limit)
        array.append('{}/{}'.format(i,f) + tweet)
        count_char = len(tweet) 
        if count_char == limit:
            i = i + 1
        else:
            count_char = 0
            f = i
            file.close()
    return array
     
def tweetstorm(text, limit, limit_final):
    f = numberLimit(text, limit)
    array = arrayNumber(text, limit, f)
    i = 0
    while len(array[f-2])>limit_final:
        limit = limit - 1
        f = numberLimit(text, limit)
        array = arrayNumber(text, limit, f)
    for tweets in array:
        print (tweets)
        #print (len(tweets)) #test arrayNumber
       
    
def main():
    text = input('Digite o caminho do arquivo, não esqueça da extensão ".txt"\nPara arquivos localizados na mesma pasta do projeto, digite apenas o nome do arquivo + extensão.\nExemplo(digite): tweetstorm.txt \n')
    try:
        limit = 140
        limit_final = 140
        tweetstorm(text, limit, limit_final)
    except IOError:
        print ("Oops!  Arquivo não encontrado.  Tente novamente...")
    
    
    
if __name__ == "__main__":
    main()