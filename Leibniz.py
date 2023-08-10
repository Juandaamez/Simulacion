__author__       = "Juan David Amezquita Nuñez"
__copyright__    = "Copyright 2023, USTA Tunja"
__credits__      = ["JF Mendoza"]
__license__      = "GPL"
__version__      = "1.0.0"
__maintainer__   = "Juan David Amezquita Nuñez"
__email__        = "juan.amezquita@usantoto.edu.co"
__status__       = "In process"

class Leibniz:

    def find_pi(self, count, sign, sum, terms):

        for i in range(terms):
            t = 1/count *sign
            sum += t
            sign *= -1
            count += 2

        pi = sum * 4
        
        print(pi)
    
lei = Leibniz()

terms = int(input("Cuantos numeros desea generar: ")) 
lei.find_pi(count = 1, sign = 1, sum = 0, terms = terms)


