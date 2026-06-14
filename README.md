# Korea Investment Open API Mock Trading Auto Trading System

## 1. Project Overview

This project is a simple automatic trading system based on the Korea Investment Securities Open API project structure.
For safety, the current version runs in **simulation mode**, and it is designed to be extended to the official **mock trading / 모의투자** environment.

이 프로젝트는 한국투자증권 Open API 구조를 참고하여 만든 자동매매 시스템입니다. 실제 투자 위험을 피하기 위해 현재 버전은 simulation mode로 실행되며, 이후 공식 모의투자 환경과 연결할 수 있도록 구성했습니다.

## 2. Main Features

- Stock price inquiry structure
- Moving average trading strategy
- BUY / SELL / HOLD signal generation
- Simulated order execution
- Trading log saving
- Safe configuration with `.env.example`

## 3. Trading Strategy

This project uses a simple moving average strategy.

| Condition | Signal |
|---|---|
| Current price > Moving average | BUY |
| Current price < Moving average | SELL |
| Current price = Moving average | HOLD |

한국어 설명:

현재 가격이 이동평균보다 높으면 상승 추세로 판단하여 BUY 신호를 생성합니다. 현재 가격이 이동평균보다 낮으면 하락 추세로 판단하여 SELL 신호를 생성합니다. 두 값이 같으면 HOLD 신호를 생성합니다.

## 4. System Flow

```text
1. Load configuration
2. Get recent stock prices
3. Calculate moving average
4. Generate trading signal
5. Execute simulation order
6. Save trading log
```

한국어:

```text
1. 설정값 불러오기
2. 최근 주가 데이터 조회
3. 이동평균 계산
4. 매매 신호 생성
5. 시뮬레이션 주문 실행
6. 거래 로그 저장
```

## 5. Project Structure

```text
hanto-auto-trading-system/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── main.py
├── config.py
├── market_api.py
├── order_api.py
├── strategy.py
├── trader.py
└── logs/
    └── sample_log.txt
```

| File | Role |
|---|---|
| `main.py` | Program entry point |
| `config.py` | Loads settings from `.env` |
| `market_api.py` | Gets stock price data |
| `strategy.py` | Implements moving average strategy |
| `order_api.py` | Executes simulated orders |
| `trader.py` | Controls the whole trading flow |
| `logs/` | Saves trading results |

## 6. How to Run

### Step 1. Install packages

```bash
pip install -r requirements.txt
```

### Step 2. Create `.env`

Copy `.env.example` and rename it to `.env`.

```text
MODE=simulation
STOCK_CODE=005930
QUANTITY=1
MA_WINDOW=5
```

### Step 3. Run the program

```bash
python main.py
```

If `python` does not work on Windows, use:

```bash
py main.py
```

## 7. Example Output

```text
[CONFIG] mode=simulation, stock_code=005930, quantity=1
[PRICE] current_price=73500, moving_average=72500.0
[SIGNAL] BUY
[ORDER] [2026-06-18 14:30:21] Simulation order completed: BUY 1 shares of 005930 at 73500 KRW
```

## 8. Security Notice

Real API keys, app secrets, account numbers, and passwords are not included in this repository.

실제 API Key, App Secret, 계좌번호, 비밀번호는 GitHub에 업로드하지 않습니다.

## 9. Reference and My Contribution

This project refers to the official Korea Investment Securities Open API sample project structure for understanding authentication, price inquiry, and order request flow.

공식 샘플 코드는 인증 방식과 API 요청 구조를 이해하기 위해 참고했습니다. 제가 직접 구현한 부분은 다음과 같습니다.

- Moving average strategy
- BUY / SELL / HOLD signal generation
- Automatic trading flow controller
- Simulation order execution
- Trading log saving
- README explanation
