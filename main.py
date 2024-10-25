import random
import matplotlib.pyplot as plt

# 이전에 정의한 클래스들 (MontyHallGame, MontyHallSimulator, ResultsVisualizer, Documentation) 추가

def main():
    # 시뮬레이션 반복 횟수 설정
    iterations = 10000  # 예: 10,000회

    # 1. MontyHallSimulator 객체 생성
    simulator = MontyHallSimulator(iterations)

    # 2. 시뮬레이션 실행
    simulator.simulate()

    # 3. 승률 계산
    stay_rate, switch_rate = simulator.get_results()

    # 4. 결과 시각화
    visualizer = ResultsVisualizer(stay_rate, switch_rate)
    visualizer.plot_results()

    # 5. 문서화
    documentation = Documentation("Monty_Hall_Results")
    documentation.add_content(f"원래 선택 유지 시 승률: {stay_rate * 100:.2f}%")
    documentation.add_content(f"선택 번복 시 승률: {switch_rate * 100:.2f}%")
    documentation.generate_document()

# 프로그램 시작점
if __name__ == "__main__":
    main()

