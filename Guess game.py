from random import randint

intro = "Ugani skrit stevilo med 1 in 10"
print intro

def main():
    while True:
        secret = randint(1, 10)
        guess = int(raw_input("Vpisi skrito stevilo: "))


        if guess == secret:
            print "Bravo stevilka je pravilna :)"

        else:
            print "Stevilo ni pravo. Vec srece prihodnjic :("

if __name__ == '__main__':
    main()


