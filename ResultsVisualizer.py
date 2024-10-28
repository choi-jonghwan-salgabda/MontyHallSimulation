# 시뮬레이션 결과를 시각적으로 표현합니다.
import matplotlib.pyplot as plt

class ResultsVisualizer:
    def __init__(self, stay_rate, switch_rate):
        self.stay_rate = stay_rate
        self.switch_rate = switch_rate

    def plot_results(self):
        labels = ['원래 선택 유지', '선택 번복']
        rates = [self.stay_rate * 100, self.switch_rate * 100]

        plt.bar(labels, rates, color=['blue', 'orange'])
        plt.ylabel('승률 (%)')
        plt.title('Monty Hall 문제 승률 비교')
        plt.ylim(0, 100)
        plt.show()
