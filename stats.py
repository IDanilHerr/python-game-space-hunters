class Stats():
    # statistics tracking

    def __init__(self):
    # initializes statistics
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
    # statistics changing during the game
        self.guns_left = 2
        self.score = 0