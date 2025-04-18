def Odd_Even_Swap(s: str) -> str:
    return ''.join(a + b for a, b in zip(s[1::2], s[0::2])) + (s[-1] if len(s) % 2 else '')

def Reverse(s: str) -> str:
    return s[::-1]

def Reverse_Words(s: str) -> str:
    return ' '.join(s.split()[::-1])

def Half_Swap(s: str) -> str:
    mid = len(s) // 2
    return s[mid:] + s[:mid]

def Bit_Flip(s: str) -> str:
    return ''.join(chr(~ord(c) & 0xFF) for c in s)

def main():
    print(f"""
    Odd_Even_Swap("134567890"): {Odd_Even_Swap("1234567890")}
    Odd_Even_Swap(Odd_Even_Swap("1234567890")): {Odd_Even_Swap(Odd_Even_Swap("1234567890"))}
    Reverse("1234567890"): {Reverse("1234567890")}
    Reverse(Reverse("1234567890")): {Reverse(Reverse("1234567890"))}
    Reverse_Words("1234567890"): {Reverse_Words("1234567890")}
    Reverse_Words(Reverse_Words("1234567890")): {Reverse_Words(Reverse_Words("1234567890"))}
    Half_Swap("1234567890"): {Half_Swap("1234567890")}
    Half_Swap(Half_Swap("1234567890")): {Half_Swap(Half_Swap("1234567890"))}
    Bit_Flip("1234567890"): {Bit_Flip("1234567890")}
    Bit_Flip(Bit_Flip("1234567890")): {Bit_Flip(Bit_Flip("1234567890"))}
    """)

if __name__ == "__main__":
    main()


