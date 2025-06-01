import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'].index(rank) + 2
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)
    
    def play_card(self):
        return self.cards.pop(0) if self.cards else None
    
    def has_cards(self):
        return len(self.cards) > 0

class WarGame:
    def __init__(self):
        self.player = Player("You")
        self.bot = Player("Bot")
        self.round_num = 0
    
    def setup(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        deck = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(deck)
        
        for i, card in enumerate(deck):
            if i % 2 == 0:
                self.player.add_cards(card)
            else:
                self.bot.add_cards(card)
        
        print(f"Game ready! You have {len(self.player.cards)} cards, Bot has {len(self.bot.cards)} cards")
    
    def play_round(self):
        self.round_num += 1
        
        player_card = self.player.play_card()
        bot_card = self.bot.play_card()
        
        if not player_card or not bot_card:
            return False
        
        cards_played = [player_card, bot_card]
        
        print(f"\nRound {self.round_num}:")
        print(f"You play: {player_card}")
        print(f"Bot plays: {bot_card}")
        
        while player_card.value == bot_card.value:
            print("WAR!")
            
            war_cards = []
            for _ in range(2):
                p_card = self.player.play_card()
                b_card = self.bot.play_card()
                if not p_card or not b_card:
                    return False
                war_cards.extend([p_card, b_card])
            
            cards_played.extend(war_cards)
            player_card = war_cards[-2]
            bot_card = war_cards[-1]
            
            print(f"War cards - You: {player_card}, Bot: {bot_card}")
        
        if player_card.value > bot_card.value:
            winner = self.player
            print("You win this round!")
        else:
            winner = self.bot
            print("Bot wins this round!")
        
        random.shuffle(cards_played)
        winner.add_cards(cards_played)
        
        print(f"Your cards: {len(self.player.cards)}, Bot cards: {len(self.bot.cards)}")
        return True
    
    def play(self):
        self.setup()
        
        while self.player.has_cards() and self.bot.has_cards() and self.round_num < 50:
            input("\nPress Enter to play next round...")
            if not self.play_round():
                break
        
        print("\n" + "="*40)
        if len(self.player.cards) > len(self.bot.cards):
            print("🎉 YOU WIN THE GAME!")
        elif len(self.bot.cards) > len(self.player.cards):
            print("🤖 BOT WINS THE GAME!")
        else:
            print("🤝 IT'S A TIE!")
        
        print(f"Final score - You: {len(self.player.cards)}, Bot: {len(self.bot.cards)}")

if __name__ == "__main__":
    game = WarGame()
    game.play()