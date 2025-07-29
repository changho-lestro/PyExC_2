import sys
sys.path.append("./lab07")

from PyQt6.QtWidgets import QApplication, QDialog, QInputDialog, QMessageBox
import random

from frmGuess import Ui_frmGuess

times_guessed = 0
num_to_guess = random.randrange(1,101)

class Mainwindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmGuess()
        self.ui.setupUi(self)
        self.ui.timesGuessedLabel.setText(str(times_guessed))
        # Connect Guess button to guess_click function
        self.ui.guess_button.clicked.connect(self.guess_click)
        self.show()

    def guess_click(self):
        global num_to_guess
        global times_guessed

        guess, okPressed = QInputDialog.getInt(self, "Enter Guess", "Guess 1-100", value=1,min=1,max=100,step=1)

        if okPressed:
            times_guessed = times_guessed + 1
            self.ui.timesGuessedLabel.setText(str(times_guessed))

            if guess == num_to_guess: # Case of Correct Guess
                QMessageBox.question(self, "Congratulations!", "You guessed the right number! \n You used "+ str(times_guessed)+ "guesses. \n The number was " + str(num_to_guess) + "."
                                     , QMessageBox.StandardButton.Ok)

                # Reset the game
                num_to_guess = random.randrange(1,101)
                # Reset times_guessed
                times_guessed = 0
                # Show the updated times_guessed
                self.ui.timesGuessedLabel.setText(str(times_guessed))

            elif guess < num_to_guess:  # Less than the answer
                QMessageBox.question(self, "Low!", "Your guess is too low." , QMessageBox.StandardButton.Ok)

            elif guess > num_to_guess:  # Larger than the answer
                QMessageBox.question(self, "High!", "Your guess is too high." , QMessageBox.StandardButton.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Mainwindow()
    sys.exit(app.exec())



