import pandas as pd


def load_data(filepath: str):
    data = pd.read_csv(filepath)

    cards = []

    for i, row in data.iterrows():
        item = {
            "Front": row["Character"] + " - " + row["Pinyin"],
            "Back": row["Definition"],
        }

        cards.append(item)

    pairs = []

    for i in range(len(cards)):
        if not i + 1 > len(cards) - 1:
            pairs.append((cards[i], cards[i + 1]))
        else:
            pairs.append((cards[i],))
        i += 1

    return pairs
