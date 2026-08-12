import numpy as np

def step_function(z_):
    if z_ >= 0:
        return 1
    return 0

print(step_function(-1.8))
print(step_function(-100000))
print(step_function(0.0))
print(step_function(2.1))
print(step_function(9999))

def AND_(x1, x2):
    w1, w2 = 0.5, 0.5               # 가중치 (weight)
    b = -0.7                        # 편향 (bias)
    z = w1 * x1 + w2 * x2 + b       # 가중합과 편향 연산
    y = step_function(z)            # 활성화 함수 적용 (step function)
    return y                        # 최종 출력 반환

# AND 게이트 예시 실행 결과 확인
print(f"AND(0,0) :  {AND_(0, 0)}")  # 출력: 0
print(f"AND(1,0) :  {AND_(1, 0)}")  # 출력: 0
print(f"AND(0,1) :  {AND_(0, 1)}")  # 출력: 0
print(f"AND(1,1) :  {AND_(1, 1)}")  # 출력: 1

def AND(x1, x2):
    x = np.array([x1, x2])          # 입력(input)을 NumPy 배열로 정의
    w = np.array([0.5, 0.5])        # 가중치(weight)를 NumPy 배열로 정의
    b = -0.7                        # 편향(bias)
    z = np.sum(x * w) + b           # 가중합과 편향 연산
    y = step_function(z)            # 활성화 함수 적용 (step function)
    return y                        # 최종 출력 반환

# AND 게이트 예시 실행 결과 확인
print(f"AND(0,0) :  {AND(0, 0)}")   # 출력: 0
print(f"AND(1,0) :  {AND(1, 0)}")   # 출력: 0
print(f"AND(0,1) :  {AND(0, 1)}")   # 출력: 0
print(f"AND(1,1) :  {AND(1, 1)}")   # 출력: 1

# TODO: OR 게이트 구현

def OR(x1, x2):
    x = np.array([x1, x2])          # 입력(input)을 NumPy 배열로 정의
    w = np.array([-0.5, -0.5])        # 가중치(weight)를 NumPy 배열로 정의
    b = -0.7                        # 편향(bias)
    z = np.sum(x * w) + b           # 가중합과 편향 연산
    y = step_function(z)            # 활성화 함수 적용 (step function)
    return y                        # 최종 출력 반환

print(f"OR(0,0) :  {OR(0, 0)}")  # 출력: 0
print(f"OR(1,0) :  {OR(1, 0)}")  # 출력: 1
print(f"OR(0,1) :  {OR(0, 1)}")  # 출력: 1
print(f"OR(1,1) :  {OR(1, 1)}")  # 출력: 1