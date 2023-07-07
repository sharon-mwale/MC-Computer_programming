import random

def main():
    play_game()

class HangmanGame:
    def __init__(self):
        self.word_list = ["apple", "banana", "cherry", "durain", "elderberry", "fig", "grapefruit"]
        self.word = ""
        self.guessed_letters = []
        self.attempts = 6

    def start_game(self):
        self.word = random.choice(self.word_list)
        self.guessed_letters = []
        self.attempts = 6        

    def guess_letter(self, letter):
        if len(letter) != 1:
            return "Please enter a single letter."

        if letter in self.guessed_letters:
            return "You have already guessed that letter. Try again."

        if letter not in self.word:
            self.attempts -= 1
            return "Incorrect guess. You have {} attempts left.".format(self.attempts)
        else:
            self .guessed_letters.append(letter)

        word_progress = ""
        for char in self.word:
            if char in self.guessed_letters:
                word_progress += char + ""
        else:
            word_progress += "_"

        if "_" not in word_progress:
            return"Congratulation! you have guessed the word correctly."
        else:
            return word_progress
        
def play_game():
    while True:
        game = HangmanGame()
        game.start_game()
        print("\nNew game! Guess the word:")
        print(game.guess_letter(""))
        while game.attempts > 0:
            letter = input("Enter a letter: ")
            result = game.guess_letter(letter)
            print(result)
            if "Congratulations" in result or "You ran out of attempts" in result:
                break

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
                
if __name__== "__main__":
    main()