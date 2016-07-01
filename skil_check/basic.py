
#画面に自分の「学科名」 「学年」 「学籍番号」 を出力して下さい
def print_self_information():
    print("ITスペシャリスト科")
    print("２年")
    print("s15003")


#自分の年齢が、８０歳になるまであと何年かかるか計算して出力して下さい
def print_how_many_vears_to_80():
    age = 19
    print(80 - age)

#与えられたパラメータが「偶数」か「奇数」かを出力して下さい
def print_odd_or_even(target):
    num = 20
    if num % 2 == 1:
        print("奇数")
    else:
        print("偶数")

#randomモジュールを使用して0-50の整数を生成し、２５がでるまで「ほげ」と出力して下さい
def print_hoge():
    from random import randint
    while(True):
        num = randint(0,50)
        if(num == 25):
            print("hoge")
        else:
            print(num)
#100から1000までの偶数のみ表示して下さい

def print_even_from_100_to_1000():




if __name__ == '__main__':

    print_self_information()
    print_how_many_vears_to_80()
    print_odd_or_even(10)
    print_odd_or_even(13)
    print_hoge()
    print_even_from_100_to_1000()