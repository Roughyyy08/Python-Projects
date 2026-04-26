import random

class RockPaperScissors():
    Choices = ["rock", "paper", "scissors"]
    Winner_Map = {
        ("paper", "rock") : "Paper Covers Rock",
        ("rock", "scissors") : "Rock Crushes Scissors",
        ("scissors", "paper") : "Scissors Cuts Paper",
    }

    def __init__(self):
        self.rounds_played = 0
        self.players_score = 0
        self.computers_score = 0
        self.ties = 0

    def computer_choice(self):
        return random.choice(self.Choices)
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "tie"
        elif (player, computer) in self.Winner_Map:
            return "player"
        else:
            return "computer"
        
    def show_score(self):
            print(f"\nScores:\nYou: {self.players_score} | Computer: {self.computers_score} | Ties: {self.ties}")
            print("-" * 45)
    
    def play_round(self):
        print(f"\nRound {self.rounds_played + 1}")
        print("Choose: rock, paper scissors (or quit to exit)")

        player = input("Enter your choice: ").strip().lower()

        if player == "quit":
            return False
        
        if player not in self.Choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            return True
        
        computer = self.computer_choice()
        print(f"Computer chose: {computer}")

        result = self.determine_winner(player, computer)
        self.rounds_played += 1

        if result == "tie":
            self.ties += 1
            print("It's a Tie")

        elif result == "player":
            self.players_score += 1
            reason = self.Winner_Map.get((player, computer))
            print(f"You Win! {reason}")
            
        else:
            self.computers_score += 1
            reason = self.Winner_Map.get((computer, player))
            print(f"Computer Wins! {reason}")
            
        self.show_score()
        return True

    def final_result(self):
        print("\n" + "=" * 35)
        print("GAME OVER")

        print(f"Rounds played: {self.rounds_played}")
        print(f"Your total wins: {self.players_score}")
        print(f"Computer total wins: {self.computers_score}")
        print(f"Ties: {self.ties}")

        if self.players_score > self.computers_score:
            print("Overall winner: YOU! 🎉")
        elif self.computers_score > self.players_score:
            print("Overall winner: Computer 🤖")
        else:
            print("Overall result: It's a draw!")

        print("\n" + "=" * 35)

    def start(self):
        print("=" * 35)
        print("   ROCK PAPER SCISSORS")
        print("=" * 35)

        while True:
            keep_playing = self.play_round()
            if not keep_playing:
                break

        self.final_result()



game = RockPaperScissors()
game.start()