from home_work_5 import HangmanGame
    
if __name__ == "__main__":
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