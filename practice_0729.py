## 함수 선언
def hello(world):
    print("Hello", world)

def hello_ret(world):
    ret_value = "Hello," + str(world)
    return ret_value

name = "guppy"
hello(name)
result = hello_ret(name)


## 함수 안의 함수
def func(number):
    def func_in_func(number):
        print(number)
    print("In func")
    func_in_func(number + 1)

func(1)
# func_in_func(3) <- 함수안에 선언된 함수는 함수 밖에서 호출시 오류


## 타입 힌트
def count_lenth(word: str, num: int) -> int:
    return len(word) * num

lenth = count_lenth("guppy", 33)
print(lenth)


## 변수에 함수를 할당할 수 있다.
def add_with_transform(left, right, transform_func):
    tmp_val = transform_func(left) + transform_func(right)
    return transform_func(tmp_val)

def add_plus_1(number):
    return number + 1

ret_val = add_with_transform(2, 3, add_plus_1)

print(ret_val)

## 람다 함수 : 매번 함수를 변수에 할당하기 번거롭다
## 람다는 어디에도 할당하지 않아도 사용이 가능하다.
func_lambda = lambda x: x+1

print("Not using lambda", add_with_transform(1, 2, func_lambda))
print("Using Lambda", add_with_transform(1, 2, lambda x: x+1))
