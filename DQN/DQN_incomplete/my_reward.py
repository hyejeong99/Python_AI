#!/usr/bin/env python

from car import car

def reward_in_game(data):
    reward = 0.0
    xycar = car()
    velocity = xycar.get_velocity()
    if velocity < 0:
	reward -= 2.0
    else:
        reward += 1.0

    return float(reward)

def reward_end_game(data):
    reward = 1.0

    return float(reward)
