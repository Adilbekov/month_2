import random

class HangmanGame:
    def __init__(self, words):
        self.words = words
        self.word_to_guess = ""
        self.guesses_remaining = 7
        self.guesses = []
    
    def select_random_word(self):
        self.word_to_guess = random.choice(self.words)
    
    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        return display
    
    def make_guess(self, letter):
        if letter in self.guesses:
            return "You already guessed that letter."
        self.guesses.append(letter)
        if letter not in self.word_to_guess:
            self.guesses_remaining -= 1
        if self.check_win():
            return "Congratulations! You guessed the word: " + self.word_to_guess
        elif self.check_loss():
            return "You lost. The word was: " + self.word_to_guess
        return self.display_word()
    
    def check_win(self):
        return set(self.word_to_guess).issubset(self.guesses)
    
    def check_loss(self):
        return self.guesses_remaining == 0

def main():
    words = ["python", "java", "javascript", "ruby", "csharp", "php"]
    game = HangmanGame(words)
    game.select_random_word()
    print("Welcome to Hangman!")
    
    while not game.check_win() and not game.check_loss():
        print("Word to guess: ", game.display_word())
        print("Guesses remaining: ", game.guesses_remaining)
        guess = input("Enter a letter: ").lower()
        result = game.make_guess(guess)
        print(result)
    
if __name__ == "__main__":
    main()