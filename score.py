class Score():
    def __init__(self, cur_board):
        self.board = cur_board
        self.top_score = []
        self.save_score = True
        self.fime_name = "scores.txt"
        self.read_scores()

    def record_name(self, name):
        """Deal with the player name"""
        if name:
            self.name = str(name)
        else:
            self.name = 'Anonymous'

    def read_scores(self):
        """read the record in scores.txt, and save it in a list"""

        f = open(self.fime_name, "r")
        for line in f:
            line = line.split()
            name = ''
            if len(line) != 2:  # not one name + score
                for n in line[:-2]:
                    name += n + ' '
                name += line[-2]
            else:
                # just one name + score
                name = line[0]
            score = line[-1]
            self.top_score.append((name, score))

    def record_winner(self):
        """record winner and if score is highest record top of the rank"""
        if self.save_score:
            if self.top_score:
                if self.board.black_count > int(self.top_score[0][-1]):
                    new_top = (self.name, self.board.black_count)
                    self.top_score.insert(0, new_top)
                else:
                    self.top_score.append((self.name, self.board.black_count))

            # if the player is the first player in scores rank
            else:
                self.top_score.append((self.name, self.board.black_count))

            record = open(self.fime_name, "w")
            for name, score in self.top_score:
                record.write(name + " " + str(score) + "\n")
                print(name, score)
            record.close()
            self.save_score = False
