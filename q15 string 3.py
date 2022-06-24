chars =['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
chars[13] = 'n'
shifted_chars[13] = 'p'
chars[0] = 'a'
shifted_chars[0] = 'c'  
print(chars)
print(shifted_chars)
