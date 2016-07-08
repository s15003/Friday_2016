#与えられた２つのパラメータの合計を２倍したものが６０を超えているかどうか
def check_sum_2times_over_60(par1, par2):
    if (par1+par2)*2 >= 60:
        print("こえてます")
    else:
        print("こえてないっす")


#与えられた金額に消費税率８％を含めた値が５０００を超えているかどうか
def tax_include(cost):
    if (cost * 1.08) > 5000:
        print("超えてるんだよなぁ")
    else:
        print("超えてません")


#与えら  れたスコアを８０位上なら'A'、６０位上８０未満なら'B'、４５以上６０未満ならC
#４５未満は'F'と返す
def judge_rank(score):
    if score >= 80:
        print("A")
    elif score >= 60:
        print("B")
    elif score >= 45:
        print("C")
    else:
        print("F")

#与えられた数値の階乗を返す。ただし再帰は使用禁止
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


#与えられた数値の２の階乗を返す。再帰使用禁止。　便利な演算子利用禁止。


if __name__ == '__main__':
    check_sum_2times_over_60(10, 12)
    tax_include(4800)
    judge_rank(49)
    factorial(5)