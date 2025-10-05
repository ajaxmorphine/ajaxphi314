# Mapping A-Z berdasarkan digit π dibelakang koma 3,14... (dengan revisi B=591, U=592)
pi_map = {
    'A': '141', 'B': '591', 'C': '653', 'D': '589',
    'E': '793', 'F': '238', 'G': '462', 'H': '643',
    'I': '383', 'J': '279', 'K': '502', 'L': '884',
    'M': '197', 'N': '169', 'O': '399', 'P': '375',
    'Q': '105', 'R': '820', 'S': '974', 'T': '944',
    'U': '592', 'V': '307', 'W': '816', 'X': '406',
    'Y': '286', 'Z': '208'
}

# Reverse mapping untuk dekripsi
reverse_map = {v: k for k, v in pi_map.items()}

def encrypt_text(text):
    """Mengubah teks ke kode angka"""
    result = []
    for char in text:
        if char.upper() in pi_map:      # huruf A-Z
            result.append(pi_map[char.upper()])
        elif char == " ":               # spasi
            result.append("000")
        else:                           # simbol/angka biarkan
            result.append(char)
    return " ".join(result)

def decrypt_text(code):
    """Mengubah kode angka ke teks"""
    result = []
    for token in code.split():
        if token in reverse_map:        # angka ke huruf
            result.append(reverse_map[token])
        elif token == "000":            # spasi
            result.append(" ")
        else:                           # simbol/angka tetap
            result.append(token)
    return "".join(result)

# ====== Main Program dengan menu ======
print("=== Ajax 3,14 Encoder & Decoder ===")
print("Option: 1 = Enkripsi | 2 = Dekripsi | 0 = Keluar")

for i in range(100):  # maksimal 100x iterasi biar gak infinite
    choice = input("\nPilih opsi (1/2/0): ")
    
    if choice == "1":
        teks = input("Masukkan teks: ")
        hasil = encrypt_text(teks)
        print("Hasil enkripsi:", hasil)
    
    elif choice == "2":
        kode = input("Masukkan kode angka: ")
        hasil = decrypt_text(kode)
        print("Hasil dekripsi:", hasil)
    
    elif choice == "0":
        print("Program selesai, bye!")
        break
    
    else:
        print("Opsi tidak valid, coba lagi!")
