# generator/password_generator.py
import secrets
import string

def password_generator(length=12, symbols=True):
    """
    Generate a secure random password.
    
    Args:
        length (int): Length of the password (default 12)
        symbols (bool): Include symbols if True (default True)
        
    Returns:
        str: Randomly generated password
    """
    # Perusmerkistö: isot ja pienet kirjaimet + numerot
    chars = string.ascii_letters + string.digits
    if symbols:
        chars += "!@#$%^&*()-_=+"
    
    # Käytetään secrets.choice turvalliseen satunnaisuuteen
    return ''.join(secrets.choice(chars) for _ in range(length))
