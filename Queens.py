import pandas as pd

def read_tracker():
    # Read the CSV file
    Tracker_df = pd.read_csv('C:/Users/wwo20/Documents/Games Leaderboard/GamesLeaderboard/QueensLeaderboard.csv')

    # Convert the 'time' column to seconds for easier comparison
    Tracker_df['time_in_seconds'] = Tracker_df['Time'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))

    # Rank players for each day based on their time (ascending order)
    Tracker_df['rank'] = Tracker_df.groupby('Date')['time_in_seconds'].rank(method='min')

    # Assign points based on rank (1st = 3 points, 2nd = 2 points, 3rd = 1 point)
    def assign_points(rank):
        if rank == 1:
            return 3
        elif rank == 2:
            return 2
        elif rank == 3:
            return 1
        else:
            return 0

    Tracker_df['points'] = Tracker_df['rank'].apply(assign_points)

    # Calculate cumulative points for each player
    cumulative_scores = Tracker_df.groupby('Player').agg(
        total_points=('points', 'sum')
    ).reset_index()

    # Sort players by total points in descending order
    leaderboard = cumulative_scores.sort_values(by='total_points', ascending=False)

    return leaderboard