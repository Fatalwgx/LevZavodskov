# Simple TicTacToe game

---

It was made as a part of Jetbrains' Python Beginner course. I took this course in order to reinforce my Python fundamentals knowledge and familiarize its concepts and best practices

### How to play

The game features a 3 by 3 grid, initially blank. It takes input from player in form of 2 numerical strings divided by whitespace as dimentional coordinates.
First turn goes to player 'X', the next to player 'O'. The game will stop once one of the conditions is reached:
1. Either of players has won, outputs who won the game
2. Neither of the players was able to win and the game is declared as a draw

For example:
- "1 1" would leave players mark at first row, first square.

Game state:

| X _ _ |

| _ _ _ |

| _ _ _ |


- "2 3" would leave player's mark at second row, third square.

Game state:

| X _ _ |

| _ _ O |

| _ _ _ |

