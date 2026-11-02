#!/usr/bin/env python3
"""
DMorse - Morse Code Utility (Python)
A simple command-line tool for encoding and decoding Morse code.
"""

import sys

# --- morse maps ---
morse_map = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z','-----':'0','.----':'1','..---':'2',
    '...--':'3','....-':'4','.....':'5','-....':'6','--...':'7',
    '---..':'8','----.':'9',
    '.-.-.-':'.','--..--':',','..--..':'?','-.-.--':'!','-..-.':'/',
    '.--.-.':'@','.-.-.':'+','-...-':'=','---...':':','.-..-.':'"',
    '.-...':'&','...-..-':'$','-.--.':'(','-.--.-':')'
}
text_to_morse = {v: k for k, v in morse_map.items()}

# --- banner ---
BANNER = r"""
 ██████╗ ███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗
 ██╔══██╗████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝
 ██║  ██║██╔████╔██║██║   ██║██████╔╝███████╗█████╗  
 ██║  ██║██║╚██╔╝██║██║   ██║██╔══██╗╚════██║██╔══╝  
 ██████╔╝██║ ╚═╝ ██║╚██████╔╝██║  ██║███████║███████╗
 ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                                  
        DMorse — Morse Code Utility
            v1.0  •  by Muhammad Junaid Akhtar
 """

def show_banner():
    print(BANNER)
    print("Usage: run the script and choose an option. Supports letters, numbers, and common punctuation.")
    print("- Use '/' as a word separator when encoding or decoding.\n")

# --- core functions ---
def decode_morse(morse_code):
    decoded = ""
    unknown = False
    for token in morse_code.split():
        if token == "/":
            decoded += " "
        elif token in morse_map:
            decoded += morse_map[token]
        else:
            decoded += "?"
            unknown = True
    return decoded, unknown


def encode_text(text):
    parts = []
    unknown_chars = []
    for ch in text.upper():
        if ch == " ":
            parts.append("/")
        elif ch in text_to_morse:
            parts.append(text_to_morse[ch])
        else:
            parts.append("<?>")
            unknown_chars.append(ch)
    return " ".join(parts), unknown_chars


def menu_loop():
    while True:
        print("╔═[ DMorse ]══════════════════════════════════╗")
        print("║ 1) Decode Morse Code                         ║")
        print("║ 2) Decode & Save to Text File                ║")
        print("║ 3) Encode Text to Morse Code                 ║")
        print("║ 4) Exit                                      ║")
        print("╚══════════════════════════════════════════════╝")
        choice = input("Select option: ").strip()

        if choice == '4':
            print("\nExiting DMorse ⚡")
            break

        if choice == '1' or choice == '2':
            morse = input("\nEnter Morse code (use / for spaces):\n").strip()
            decoded, warn = decode_morse(morse)
            print("\nDecoded text:", decoded)
            if warn:
                print("⚠ Warning: Some codes were not recognized and are shown as '?'.")
            if choice == '2':
                fn = "decoded_output.txt"
                with open(fn, "w", encoding="utf-8") as f:
                    f.write(decoded)
                print(f"💾 Saved to {fn}")

        elif choice == '3':
            text = input("\nEnter text to encode:\n").strip()
            encoded, bad = encode_text(text)
            print("\nMorse code:", encoded)
            if bad:
                uniq = sorted(set(bad))
                print("⚠ Unsupported characters:", ", ".join(uniq))
                print("These were replaced with `<?>`.")
        else:
            print("Invalid option. Please try again.")

# --- main ---
def main():
    show_banner()
    try:
        menu_loop()
    except (KeyboardInterrupt, EOFError):
        print("\n\nInterrupted. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
