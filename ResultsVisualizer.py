# 시뮬레이션 결과를 시각적으로 표현합니다.

import matplotlib.pyplot as plt

class ResultsVisualizer:
    def __init__(self, stay_rate, switch_rate):
        self.stay_rate = stay_rate # 결정을 안 바꿨을을 때 비율
        self.switch_rate = switch_rate # 결정을 바꿨을 때 비율

        def plot_results(self):
        # label를 만들어서 승률을 백분률로 변환시켜 plt.show()로 표현하는 기능


