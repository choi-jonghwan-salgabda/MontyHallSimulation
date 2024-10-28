# 게임의 규칙 정의 및 플레이어의 선택 관리
# random 함수를 이용합니다

import random

class MontyHallGame:
    def __init__(self):
        self.doors = [0, 0, 0]  # 0: goat, 1: car
        self.winner = None
    def setup_game(self):
        # 자동차를 무작위로 배치
        car_position = random.randint(0, 2)
        self.doors[car_position] = 1  # 자동차 위치
        self.winner = car_position
    def make_choice(self, player_choice):
        # 플레이어의 선택을 받고, 열릴 문을 결정
        remaining_doors = [i for i in range(3) if i != player_choice and i != self.winner]
        revealed_door = random.choice(remaining_doors)
        return revealed_door
