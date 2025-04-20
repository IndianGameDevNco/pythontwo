from random import choice, randint
from typing import Callable, List
alphabet: str = 'abcdefghijklmnopqrstuvwxyz'

def Odd_Even_Swap(s: str) -> str:
    return ''.join(a + b for a, b in zip(s[1::2], s[0::2])) + (s[-1] if len(s) % 2 else '')

def Reverse(s: str) -> str:
    return s[::-1]

def Reverse_Words(s: str) -> str:
    return ' '.join(i[::-1] for i in s.split())

def Half_Swap(s: str) -> str:
    if len(s) % 2 != 0:
        s += s[-1]
    mid = len(s) // 2
    return s[mid:] + s[:mid]

millitary_algorithms: List[tuple[str, Callable[[str], str], Callable[[str], str]]] = [
    ("Odd_Even_Swap", Odd_Even_Swap, Odd_Even_Swap),
    ("Reverse", Reverse, Reverse),
    ("Reverse_Words", Reverse_Words, Reverse_Words),
    ("Half_Swap", Half_Swap, Half_Swap), 
    ]

def Bit_Flip(s: str) -> str:
    return ''.join(chr(~ord(c) & 0xFF) for c in s)

def Black_Hole_Cipher(s: str) -> str:
    return ''.join(
        Caeser_Cipher(i, alphabet.index(i)) if i in alphabet else i
        for i in s.lower()
    )

def Caeser_Cipher(s: str, k: int = 3) -> str:
    return ''.join(
        alphabet[(alphabet.index(i) + k) % len(alphabet)] if i in alphabet else i
        for i in s.lower()
    )

def Decode_Caeser_Cipher(s: str, k: int = 3) -> str:
    return Caeser_Cipher(s.lower(), -k)

def Encode_Millitary_Message(s: str, header: str) -> str:
    algo_index = randint(0, len(millitary_algorithms) - 1)
    key = randint(1, 25)
    _, encode_func, _ = millitary_algorithms[algo_index]

    encoded = encode_func(f"{header}::{s}")
    ciphered = Caeser_Cipher(encoded, key)

    metadata = f"{algo_index}{key:02}" 
    return metadata + ciphered


def Decode_Millitary_Message(s: str, header: str) -> str:
    try:
        algo_index = int(s[0])
        key = int(s[1:3])
        ciphered = s[3:]

        _, _, decode_func = millitary_algorithms[algo_index]
        decoded = decode_func(Decode_Caeser_Cipher(ciphered, key))
        if decoded.startswith(f"{header}::"):
            return decoded.split("::", 1)[1]
        
    except Exception as e:
        return f"Error: {e}"

    return "404 - Header not found"


def main():
    print(f"""
    Odd_Even_Swap("1234567890"): {Odd_Even_Swap("1234567890")}
    Odd_Even_Swap(Odd_Even_Swap("1234567890")): {Odd_Even_Swap(Odd_Even_Swap("1234567890"))}
    Reverse("1234567890"): {Reverse("1234567890")}
    Reverse(Reverse("1234567890")): {Reverse(Reverse("1234567890"))}
    Reverse_Words("1234567890"): {Reverse_Words("1234567890")}
    Reverse_Words(Reverse_Words("1234567890")): {Reverse_Words(Reverse_Words("1234567890"))}
    Half_Swap("1234567890"): {Half_Swap("1234567890")}
    Half_Swap(Half_Swap("1234567890")): {Half_Swap(Half_Swap("1234567890"))}
    Bit_Flip("1234567890"): {Bit_Flip("1234567890")}
    Bit_Flip(Bit_Flip("1234567890")): {Bit_Flip(Bit_Flip("1234567890"))}
    Caeser_Cipher("1234567890"): {Caeser_Cipher("1234567890")}
    Black_Hole_Cipher("Hi1234567890"): {Black_Hole_Cipher("Hi1234567890")}
    Decode_Caeser_Cipher(Caeser_Cipher("Hi1234567890")): {Decode_Caeser_Cipher(Caeser_Cipher("Hi1234567890"))}
    """)

if __name__ == "__main__":
    main()


