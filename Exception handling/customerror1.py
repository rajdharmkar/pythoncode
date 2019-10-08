class Error ( Exception ):
    """Base class for other exceptions"""
    pass


class PrecedingLetterError ( Error ):
    """Raised when the entered alpahbet is smaller than the actual one"""
    pass


class SucceedingLetterError ( Error ):
    """Raised when the entered alpahbet is larger than the actual one"""
    pass


# our main program
# user guesses an alphabet until he/she gets it right

# you need to guess this alphabet
alphabet = 'k'

while True:
    try:
        apb = raw_input ( "Enter an alphabet: " )
        if apb < alphabet:
            raise PrecedingLetterError
        elif apb > alphabet:
            raise SucceedingLetterError
        break
    except PrecedingLetterError:
        print("The entered alphabet is preceding one, try again!")
        print('')
    except SucceedingLetterError:
        print("The entered alphabet is succeeding one, try again!")
        print('')

print("Congratulations! You guessed it correctly.")


