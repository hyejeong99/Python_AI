#!/usr/bin/env python

def reward_in_game(data):
    reward = 0.0
    action = data[0]
    dp = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    act = dp[action]
    if (act[1] == 1):
        reward -= 2.0
    elif (act[1] == 0):
        reward -= 1.0
    else:
        reward += 1.0

    return float(reward)

def reward_end_game(data):
    reward = 1.0

    return float(reward)
