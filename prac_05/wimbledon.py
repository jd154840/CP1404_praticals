"""
Estimated Time: 30 min
Actual Time: 40 min
"""
FILENAME = 'wimbledon.csv'


def main():
    data = get_wimbledon_data()
    winners = get_winners(data)
    max_length_winner = max({len(winner) for winner in winners.keys()})
    for player in winners:
        print(f"{player:{max_length_winner}} -  {winners[player]}")
    countries = get_countries(data)
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def get_winners(data):
    winners = {}
    for tournament in data:
        winner = tournament[2]
        if winner in winners:
            winners[winner] += 1
        else:
            winners[winner] = 1
    return winners


def get_countries(data):
    countries = set()
    for tournament in data:
        country = tournament[1]
        countries.add(country)
    return countries


def get_wimbledon_data():
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        useful_data = in_file.readlines()[1:]
        for line in useful_data:
            line = line.strip()
            parts = line.split(',')
            parts[0] = int(parts[0])
            data.append(parts)
        in_file.close()
    return data


main()
