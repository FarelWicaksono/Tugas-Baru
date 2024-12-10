import random

def generate_deck():
    """Buat deck kartu standar tanpa Joker."""
    suits = ['Hati', 'Wajik', 'Sekop', 'Keriting']
    values = list(range(1, 11)) + [10, 10, 10]  # Angka 1-10, dan semua kartu gambar bernilai 10
    deck = [(str(value), suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    """Hitung nilai total kartu dalam tangan."""
    total = 0
    for card, _ in hand:
        total += int(card)
    return total

def draw_card(deck):
    """Ambil kartu dari deck."""
    if len(deck) > 0:
        return deck.pop()
    return None

def print_hand(hand):
    """Tampilkan kartu dalam tangan."""
    return ', '.join([f"{card} {suit}" for card, suit in hand])

def player_turn(player_name, player_hand, deck):
    """Giliran pemain untuk bermain."""
    while True:
        print(f"\nGiliran {player_name}.")
        print("Kartu Anda:", print_hand(player_hand))
        print("Total nilai Anda:", calculate_score(player_hand))
        
        if calculate_score(player_hand) == 41:
            print(f"{player_name} mencapai 41! Permainan selesai.")
            return True, False  # Pemain langsung menang jika mencapai 41
        
        action = input("Apa yang ingin Anda lakukan? (ambil/buang/selesai/berhenti): ").lower()
        if action == 'ambil':
            card = draw_card(deck)
            if card:
                player_hand.append(card)
                print(f"Kartu yang diambil: {card[0]} {card[1]}")
            else:
                print("Deck habis! Tidak ada kartu untuk diambil.")
                break
        elif action == 'buang':
            print("Kartu Anda:", print_hand(player_hand))
            card_to_discard = input("Masukkan nomor kartu yang ingin dibuang (1-{}): ".format(len(player_hand)))
            try:
                card_to_discard = int(card_to_discard) - 1
                if 0 <= card_to_discard < len(player_hand):
                    discarded_card = player_hand.pop(card_to_discard)
                    print(f"Kartu {discarded_card[0]} {discarded_card[1]} dibuang.")
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Input tidak valid.")
        elif action == 'selesai':
            print(f"{player_name} selesai bermain.")
            return False, False  # Pemain selesai tanpa berhenti
        elif action == 'berhenti':
            print(f"{player_name} memutuskan untuk berhenti bermain.")
            return False, True  # Pemain memutuskan untuk berhenti
        else:
            print("Perintah tidak dikenal.")
    return False, False

def main():
    print("Selamat datang di permainan kartu 41 untuk 2 pemain!")
    deck = generate_deck()
    
    # Nama pemain
    player1_name = input("Masukkan nama pemain 1: ")
    player2_name = input("Masukkan nama pemain 2: ")
    
    # Inisialisasi kartu untuk pemain
    player1_hand = [draw_card(deck) for _ in range(4)]
    player2_hand = [draw_card(deck) for _ in range(4)]
    
    player1_stop = False
    player2_stop = False
    
    # Bergantian giliran
    while len(deck) > 0 and not (player1_stop and player2_stop):
        if not player1_stop:
            win, player1_stop = player_turn(player1_name, player1_hand, deck)
            if win:
                print(f"\n{player1_name} menang dengan skor 41!")
                return
        
        if not player2_stop:
            win, player2_stop = player_turn(player2_name, player2_hand, deck)
            if win:
                print(f"\n{player2_name} menang dengan skor 41!")
                return
    
    # Jika kedua pemain berhenti atau deck habis, tentukan pemenang
    print("\nPermainan selesai.")
    print(f"Kartu {player1_name}: {print_hand(player1_hand)} (Total: {calculate_score(player1_hand)})")
    print(f"Kartu {player2_name}: {print_hand(player2_hand)} (Total: {calculate_score(player2_hand)})")
    
    score1 = calculate_score(player1_hand)
    score2 = calculate_score(player2_hand)
    
    # Skor lebih dari 41 dianggap menang
    if score1 > 41:
        score1 = 0
    if score2 > 41:
        score2 = 0
    
    if score1 > score2:
        print(f"Selamat, {player1_name} menang!")
    elif score2 > score1:
        print(f"Selamat, {player2_name} menang!")
    else:
        print("Permainan seri!")

if __name__ == "__main__":
    main()
