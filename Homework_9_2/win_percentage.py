class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        total_games = self.wins + self.losses
        if total_games == 0:
            return 0.0
        win_percentage = (self.wins / total_games) * 100
        return win_percentage

    # TODO: Define print_standing()
    def print_standing(self):
        print('Team Name: ', self.name)
        print('Wins: ', self.wins)
        print('Losses: ', self.losses)
        print('Win percentage: {:.2f}%'.format(self.get_win_percentage()))


if __name__ == "__main__":
    team = Team()

    user_name = input('Enter the team name: ')
    user_wins = int(input('Enter the number of wins: '))
    user_losses = int(input('Enter the number of losses: '))

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    team.print_standing()
