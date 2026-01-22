# Hangman Game (Pendu)

```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

Welcome to the **Hangman Game**! A classic word puzzle game built with Python and Pygame. Test your vocabulary and save the stickman from his doom!

## 🎮 Features

*   **Graphical Interface**: A clean and responsive UI built with Pygame.
*   **Visual Progression**: Watch the stickman being drawn part by part with every mistake.
*   **Score Tracking**: Keep track of your winning streak during your session.
*   **Word Library**: Contains a built-in list of random words to guess.
*   **User Feedback**: See your tried letters and current input in real-time.

## 🚀 Getting Started

### Prerequisites

*   Python 3.x installed on your machine.
*   `pygame` library.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/moinahalima-abdou/Pendu.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd Pendu
    ```
3.  Install the required dependencies (if you haven't already):
    ```bash
    pip install pygame
    ```

### How to Play

1.  Run the game using the menu script:
    ```bash
    python Modules/menu.py
    ```
2.  Click **"Play"** on the main menu.
3.  Type letters on your keyboard to guess the hidden word.
    *   **Enter**: Confirm your guess (letter or full word).
    *   **Backspace**: Delete your current input.
4.  You have **7 lives**. Each wrong letter removes a life and draws a part of the hangman.
5.  If you guess the word correctly or find all letters, you **WIN** and gain a point!
6.  If the hangman is fully drawn, you **LOSE**.

## 🛠️ Project Structure

*   `Modules/`
    *   `menu.py`: Validates user input and manages the game loop.
    *   `draw_stickman.py`: Handles the drawing logic for the hangman.
    *   `random_word_generator.py`: Picks a random word from the list.
    *   `display_word.py`: Masks the hidden word (e.g., `_ _ a _ _`).
    *   `verify_letter.py`: Checks if a letter exists in the word.

---
*Enjoy the game and good luck!*
