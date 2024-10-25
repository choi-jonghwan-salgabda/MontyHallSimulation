# 시뮬레이션을 실행하고 두가지 전략에 대한 승률을 계산합니다.

class MontyHallSimulator:
    def __init__(self, iterations):
        self.iterations = iterations  # 시뮬레이션 반복 횟수
        self.win_count_stay = 0  # 원래 선택 유지 시 승리 횟수
        self.win_count_switch = 0  # 선택 번복 시 승리 횟수

    def simulate(self):
        for _ in range(self.iterations):
            game = MontyHallGame()  # 새로운 게임 생성
            game.setup_game()  # 게임 설정
            
            # 원래 선택 유지 전략
            player_choice = random.randint(0, 2)  # 플레이어의 무작위 선택
            revealed_door = game.make_choice(player_choice)  # 열릴 문 선택
            if player_choice == game.winner:  # 승리 여부 확인
                self.win_count_stay += 1

            # 선택 번복 전략
            final_choice = 0  # 최종 선택 문 초기화
            for door in range(3):
                if door != player_choice and door != revealed_door:
                    final_choice = door  # 남은 문 중 최종 선택
                    break
            if final_choice == game.winner:  # 승리 여부 확인
                self.win_count_switch += 1

    def get_results(self):
        stay_win_rate = self.win_count_stay / self.iterations  # 승률 계산
        switch_win_rate = self.win_count_switch / self.iterations  # 승률 계산
        return stay_win_rate, switch_win_rate