1. MontyHallGame 클래스
기능: 게임 설정과 문 선택

설명:

이 클래스는 Monty Hall 게임의 기본 구조를 정의합니다. 게임에는 세 개의 문이 있습니다. 그 중 한 문 뒤에는 자동차(상)와 나머지 두 문 뒤에는 염소(하)가 있습니다.
setup_game 메서드는 자동차가 무작위로 어떤 문 뒤에 있는지를 결정합니다.
make_choice 메서드는 플레이어의 선택을 받고, 플레이어가 선택하지 않은 문 중에서 자동차가 없는 문을 열어 보여줍니다.
구현 방법:

자동차가 위치할 문을 무작위로 정합니다.
플레이어가 선택한 문을 받고, 나머지 문 중에서 자동차가 없는 문을 하나 열어 보여줍니다.



2. MontyHallSimulator 클래스
기능: 시뮬레이션 실행 및 결과 계산

설명:

이 클래스는 여러 번 게임을 진행하여 두 가지 전략(원래 선택 유지, 선택 번복)의 승률을 비교합니다.
simulate 메서드는 반복문을 사용하여 지정된 횟수만큼 게임을 실행합니다. 매 게임마다 플레이어의 선택을 무작위로 결정하고, 결과를 기록합니다.
구현 방법:

정해진 횟수만큼 게임을 반복합니다.
매 게임에서 플레이어가 무작위로 문을 선택하게 합니다.
열릴 문을 결정한 후, 원래 선택을 유지한 경우와 번복한 경우 각각의 승리 여부를 확인하여 기록합니다.




3. ResultsVisualizer 클래스
기능: 시뮬레이션 결과 시각화

설명:

이 클래스는 시뮬레이션에서 얻은 승률을 그래프로 보여줍니다. 승률을 비교할 수 있어, 어떤 전략이 더 효과적인지 쉽게 이해할 수 있습니다.
plot_results 메서드는 두 전략의 승률을 바 차트로 그립니다.
구현 방법:

승률 데이터를 바 차트 형식으로 준비합니다.
각 전략의 승률을 시각적으로 표현하여 비교할 수 있도록 합니다.


