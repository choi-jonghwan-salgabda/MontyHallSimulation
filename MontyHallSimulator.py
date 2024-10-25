# 시뮬레이션을 실행하고 두가지 전략에 대한 승률을 계산합니다.

class MontyHallSimulator:
    def __init__(self, iterations):
        self.iterations = iterations # 시뮬레이션 반복 횟수
        self.win_count_stay = 0 # 원래 선택 유지 시 승리 횟수
        self.win_count_switch = 0 # 선택 번복 시 승리 횟수

    def simulate(self):
        # MontyHallGame() Class 객체화 
        game = MontyHallGame() # 새로운 게임 시작
        game.setup_game() # 게임 설정(자동차를 무작위로 배치하는 함수)


        # 선택을 유지했을 때

        # 선택을 번복했을 때


    def get_results(self):
        # 승률을 계산합니다

