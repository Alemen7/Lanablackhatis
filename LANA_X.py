
import os,sys,hashlib
os.system('clear') # if you Use windows put "CLS"
print '''
    +---------------------------------+
    | [+] Black HAT islamic      [+]  |
    | [+]      Ahmed kaissar     [+]  |
    | [+]      Database_HK       [+]  |
    | [+]      ALYEMENI          [+]  |
    +---------------------------------+
    
    1  > > > base64\t\t 
    2  > > > MD5\t\t  
    3  > > > SHA-1\t\t
    4  > > > SHA-224\t\t
    5  > > > SHA-256\t\t
    6  > > > SHA-384\t\t
    7  > > > SHA-512\t\t
    8  > > > base16\t\t
    9  > > > base32\t\t 
    99 > > > exit
'''

select = raw_input('Select : ')
if select == '1' : 
        import base64
        print '''
        1 > > > Encrypt
        2 > > > Decrypt
        '''
        select = raw_input('Select : ')
        if select == '1' : 
            encrypt = raw_input('Enter anything for Encryption : ')
            en = base64.b64encode(encrypt)
            print 'Your Encryption : ' + en
        elif select == '2' :
            decrypt = raw_input('Enter anything for Decryption : ')
            de = base64.b64decode(decrypt)
            print 'Your Decryption : ' + de
elif select == '2' :
    in_user = raw_input("Enter anything for Encryption : ")
    md5 = hashlib.md5(in_user).hexdigest()
    print 'Your Decryption : ' + md5
elif select == '3' :
    in_user = raw_input("Enter anything for Encryption : ")
    sha1 = hashlib.sha1(in_user).hexdigest()
    print 'Your Decryption : ' + sha1
elif select == '4' :
    in_user = raw_input("Enter anything for Encryption : ")
    sha224 = hashlib.sha224(in_user).hexdigest()
    print 'Your Decryption : ' + sha224

elif select == '5' : 
    in_user = raw_input("Enter anything for Encryption : ")
    sha256 = hashlib.sha256(in_user).hexdigest()
    print 'Your Decryption : ' + sha256
elif select == '6' : 
    in_user = raw_input("Enter anything for Encryption : ")
    sha384 = hashlib.sha384(in_user).hexdigest()
    print 'Your Decryption : ' + sha384
elif select == '7' : 
    in_user = raw_input("Enter anything for Encryption : ")

    sha512 = hashlib.sha512(in_user).hexdigest()
    print 'Your Decryption : ' + sha512
elif select == '8' :
    import base64
    print '''
    1 > > > Encrypt
    2 > > > Decrypt
    '''
    select = raw_input('Select : ')
    if select == '1' : 
        encrypt = raw_input('Enter anything for Encryption : ')
        en = base64.b16encode(encrypt)
        print 'Your Encryption : ' + en
    elif select == '2' :
        decrypt = raw_input('Enter anything for Decryption : ')
        de = base64.b16decode(decrypt)
        print 'Your Decryption : ' + de
elif select == '9' :
    import base64
    print '''
    1 > > > Encrypt
    2 > > > Decrypt
    '''
    
    select = raw_input('Select : ')
    if select == '1' : 
        encrypt = raw_input('Enter anything for Encryption : ')
        en = base64.b32encode(encrypt)
        print 'Your Encryption : ' + en
    elif select == '2' :
        decrypt = raw_input('Enter anything for Decryption : ')
        de = base64.b32decode(decrypt)
        print 'Your Decryption : ' + de
elif select == '99' : 
    print " [+] ok Exit [+]"
    sys.exit()
else : 
    print "Error In Input !! \n\nPlease Try Again >>> ." 
