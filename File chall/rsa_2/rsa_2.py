n = 882564595536224140639625987659416029426239230804614613279163
e = 65537
def rsa(mess):
    return pow(mess, e, n)
mess = 'ISPCTF{....}'
cipher = [rsa(ord(c)) for c in mess]
with open('cipher.txt', 'w') as f:
    f.write('\n'.join([str(x) for x in cipher]))