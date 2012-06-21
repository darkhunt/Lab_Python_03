question 1.
n=50
print"the first 50 primes:"
prime_count = 0
possible_prime = 2
while prime_count < n:
    divisor_count = 0
    for i in range(1,possible_prime+1):
        if possible_prime % i == 0:
               divisor_count += 1
    if divisor_count == 2:
        print possible_prime,
        prime_count += 1
        if prime_count % 10 == 0:
            print
    possible_prime += 1


#Lab03_2a
for i in range(7):
    for j in range(1,i+1):
        print j,
    print
print   
#Lab03_2b
for i in range(6,0,-1):
    for j in range(1,i+1):
        print j,
    print
    
#Lab03_2c
for i in range(7):
    for k in range(6-i,0,-1):
            print ' ',
    for j in range(i,0,-1):
        print j,
    print
print
    
#Lab03_2d
for i in range(6,0,-1):
    for j in range(1,i+1):
        print j,
    print
    for k in range(7-i):
            print ' ',
            
#Lab03_2e
for i in range(6):
    for j in range(5-i):
            print ' ',
    for k in range(i,0,-1):
        print k,
    for l in range(2,i+1):
        print l,
    print
