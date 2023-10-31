try:
    transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]


    stats = {}

    for user_id, transaction_type in transactions:
        if user_id not in stats:
            stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}
        stats[user_id][transaction_type] += 1

    for user_id, user_stats in stats.items():
        transaction_counts = user_stats[1], user_stats[2], user_stats[3]
        mft = max(range(1, 4), key=lambda k: user_stats[k])
        lft = min(range(1, 4), key=lambda k: user_stats[k])

        user_stats['mft'] = mft
        user_stats['lft'] = lft

    print(stats)
except ValueError as e:
        print("Invalid input. Please enter a word.")