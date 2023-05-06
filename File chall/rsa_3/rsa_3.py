class RSA:
    def __init__(self):
        self.n = 5835849141972415516562164777590600916570589166422039289302554835569696192150270851430968308687162649229377439380800096910180769127775637271780244052117395146078164421458617959724532644257601836154656137717505688047274291687336103924232013283899029988317854887436379713530001406810062108106729288439424569051388212049886935571366642883502049123
        self.flag = 'ISPCTF{....}'
    
    def encrypt(self):
        self.cipher = [pow(ord(c),1,self.n).to_bytes(length=5, byteorder='big') for c in self.flag] 
        with open('cipher','wb') as f:
            for cipher in self.cipher:
                f.write(cipher)  
                f.write('\n'.encode()) 
    def decrypt(self):
        with open('cipher','rb') as f:
            self.cipher = f.read().splitlines()
            
if __name__ == '__main__':
    rsa = RSA()
    rsa.encrypt()
    