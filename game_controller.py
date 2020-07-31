class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.black_wins = False
        self.white_wins = False
        self.tie = False

    def update(self):
        """Carries out necessary actions if black or white wins or tie"""
        if self.black_wins:
            fill(0, 128, 254)
            textSize(70)
            text("Black WIN!!!", self.WIDTH/2 - 200, self.HEIGHT/2 + 20)
        if self.white_wins:
            fill(0, 128, 254)
            textSize(70)
            text("White WIN!!!", self.WIDTH/2 - 200, self.HEIGHT/2 + 20)
        if self.tie:
            fill(0, 128, 254)
            textSize(70)
            text("Tie, good game!!", self.WIDTH/2 - 270, self.HEIGHT/2 + 20)
