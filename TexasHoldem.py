# 德州扑克比大小
class TexasHoldem:
    color = ['D', 'S', 'H', 'C']
    number = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    cards_type = {'sanpai':1, 'duizi':2, 'liangdui':3, 'santiao':4, 'shunzi':5, 'tonghua':6, 'hulu':7, 'tiezhi':8, 'tonghuashun':9}
    newblack = ''
    newwhite = ''

    def __init__(self, black, white):
        self.black, self.white = black, white
        self.newblack = self.black.split(' ')
        self.newwhite = self.white.split(' ')

    # 检查输入格式
    def check_input(self):
        if len(self.black.split(' ')) < 5 or len(self.white.split(' ')) < 5:
            return False
        for item in self.black.split(' '):
            if len(item) != 2:
                return False
            if item[0] not in self.number or item[1] not in self.color:
                return False
        for item in self.white.split(' '):
            if len(item) != 2:
                return False
            if item[0] not in self.number or item[1] not in self.color:
                return False
        return True

    # sort
    def smaller(self, cardA, cardB):
        cardA_index = self.number.index(cardA)
        cardB_index = self.number.index(cardB)
        if cardA_index >= cardB_index:
            return False
        else:
            return True

    def card_sort(self):
        for i in range(1, len(self.newblack)):
            key = self.newblack[i]
            j = i-1
            while j >= 0 and self.smaller(self.newblack[j][0], key[0]):
                self.newblack[j+1] = self.newblack[j]
                j -= 1
            self.newblack[j+1] = key

        for i in range(1, len(self.newwhite)):
            key = self.newwhite[i]
            j = i-1
            while j >= 0 and self.smaller(self.newwhite[j][0], key[0]):
                self.newwhite[j+1] = self.newwhite[j]
                j -= 1
            self.newwhite[j+1] = key

        if self.get_diferent_num(self.newblack)<5:
            i = 0
            while i<len(self.newblack):
                repeat_num = 1
                j = i
                while j < 4:
                    if self.newblack[j][0] != self.newblack[j + 1][0]:
                        j += 1
                        continue
                    repeat_num += 1
                    k = j + 1
                    while k < 4:
                        if self.newblack[j][0] == self.newblack[k + 1][0]:
                            k += 1
                            repeat_num += 1
                            continue
                        else:
                            break
                    if repeat_num > 1 and i != j:
                        # self.newblack[j + repeat_num - 1] = self.newblack[i]
                        # self.newblack[i] = self.newblack[j]
                        # i = j + repeat_num - 1
                        for z in range(0, repeat_num):
                            temp = self.newblack[i+z]
                            self.newblack[i+z] = self.newblack[j + z]
                            self.newblack[j + z] = temp
                        i = i + repeat_num
                        break
                    if i==j:
                        i = i + repeat_num
                        break

                if j==4 and repeat_num==1:
                    i += 1

        if self.get_diferent_num(self.newwhite)<5:
            i = 0
            while i<len(self.newwhite):
                repeat_num = 1
                j = i
                while j < 4:
                    if self.newwhite[j][0] != self.newwhite[j + 1][0]:
                        j += 1
                        continue
                    repeat_num += 1
                    k = j + 1
                    while k < 4:
                        if self.newwhite[j][0] == self.newwhite[k + 1][0]:
                            k += 1
                            repeat_num += 1
                            continue
                        else:
                            break
                    if repeat_num > 1 and i != j:
                        for z in range(0, repeat_num):
                            temp = self.newwhite[i + z]
                            self.newwhite[i + z] = self.newwhite[j + z]
                            self.newwhite[j + z] = temp
                        i = i + repeat_num
                        break
                    if i==j:
                        i = i + repeat_num
                        break
                if j==4 and repeat_num==1:
                    i += 1

        if self.get_diferent_num(self.newblack) == 2:
            if not self.if_tiezhi(self.newblack):
                if self.newblack[2][0]!=self.newblack[0][0]:
                    temp = self.newblack[0]
                    self.newblack[0], self.newblack[1] = self.newblack[3], self.newblack[4]
                    self.newblack[3], self.newblack[4] = temp, temp

        if self.get_diferent_num(self.newwhite) == 2:
            if not self.if_tiezhi(self.newwhite):
                if self.newwhite[2][0]!=self.newwhite[0][0]:
                    temp = self.newwhite[0]
                    self.newwhite[0], self.newwhite[1] = self.newwhite[3], self.newwhite[4]
                    self.newwhite[3], self.newwhite[4] = temp, temp

    # 是否同花
    def if_tonghua(self, cards):
        if cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]:
            return True
        else:
            return False

    # 是否是顺子
    def if_shunzi(self, cards):
        index1, index2, index3, index4, index5 = self.number.index(cards[0][0]), self.number.index(
            cards[1][0]), self.number.index(cards[2][0]), self.number.index(cards[3][0]), self.number.index(cards[4][0])
        if (index1 - 1) == index2 and (index1 - 2) == index3 and (index1 - 3) == index4 and (index1 - 4) == index5:
            return True
        else:
            return False

    # 是否是同花顺
    def if_tonghuashun(self, cards):
        if self.if_tonghua(cards) and self.if_shunzi(cards):
            return True
        else:
            return False

    def get_diferent_num(self, cards):
        temp = {cards[0][0]}
        temp.add(cards[1][0])
        temp.add(cards[2][0])
        temp.add(cards[3][0])
        temp.add(cards[4][0])
        return len(temp)

    # 是否是对子
    def if_duizi(self, cards):
        if self.get_diferent_num(cards)==4:
            return True
        return False

    # 是否是两对
    def if_liangdui(self, cards):
        index1, index2, index3, index4, index5 = self.number.index(cards[0][0]), self.number.index(
            cards[1][0]), self.number.index(cards[2][0]), self.number.index(cards[3][0]), self.number.index(cards[4][0])
        if index1==index2 and index3==index4 and index1!=index3:
            return True
        return False

    # 是否是三条
    def if_santiao(self, cards):
        index1, index2, index3, index4, index5 = self.number.index(cards[0][0]), self.number.index(
            cards[1][0]), self.number.index(cards[2][0]), self.number.index(cards[3][0]), self.number.index(cards[4][0])
        if index1==index2==index3 and index1!=index4 and index4!=index5:
            return True
        return False

    # 是否是葫芦
    def if_hulu(self, cards):
        index1, index2, index3, index4, index5 = self.number.index(cards[0][0]), self.number.index(
            cards[1][0]), self.number.index(cards[2][0]), self.number.index(cards[3][0]), self.number.index(cards[4][0])
        if index1==index2==index3 and index1!=index4 and index4==index5:
            return True
        return False

    # 是否是铁支
    def if_tiezhi(self, cards):
        index1, index2, index3, index4, index5 = self.number.index(cards[0][0]), self.number.index(
            cards[1][0]), self.number.index(cards[2][0]), self.number.index(cards[3][0]), self.number.index(cards[4][0])
        if index1 == index2 == index3 == index4:
            return True
        return False

    # judge
    def judge_cards(self):
        self.card_sort()
        black_current_type = self.cards_type['sanpai']
        white_current_type = self.cards_type['sanpai']
        if self.if_tonghuashun(self.newblack):
            black_current_type = self.cards_type['tonghuashun']
        elif self.if_tonghua(self.newblack):
            black_current_type = self.cards_type['tonghua']
        elif self.if_shunzi(self.newblack):
            black_current_type = self.cards_type['shunzi']
        elif self.if_duizi(self.newblack):
            black_current_type = self.cards_type['duizi']
        elif self.if_liangdui(self.newblack):
            black_current_type = self.cards_type['liangdui']
        elif self.if_santiao(self.newblack):
            black_current_type = self.cards_type['santiao']
        elif self.if_hulu(self.newblack):
            black_current_type = self.cards_type['hulu']
        elif self.if_tiezhi(self.newblack):
            black_current_type = self.cards_type['tiezhi']

        if self.if_tonghuashun(self.newwhite):
            white_current_type = self.cards_type['tonghuashun']
        elif self.if_tonghua(self.newwhite):
            white_current_type = self.cards_type['tonghua']
        elif self.if_shunzi(self.newwhite):
            white_current_type = self.cards_type['shunzi']
        elif self.if_duizi(self.newwhite):
            white_current_type = self.cards_type['duizi']
        elif self.if_liangdui(self.newwhite):
            white_current_type = self.cards_type['liangdui']
        elif self.if_santiao(self.newwhite):
            white_current_type = self.cards_type['santiao']
        elif self.if_hulu(self.newwhite):
            white_current_type = self.cards_type['hulu']
        elif self.if_tiezhi(self.newwhite):
            white_current_type = self.cards_type['tiezhi']

        if black_current_type > white_current_type:
            return "Black wins"
        if black_current_type < white_current_type:
            return "White wins"
        for i in range(0, 5):
            if self.number.index(self.newblack[i][0])>self.number.index(self.newwhite[i][0]):
                return "Black wins"
            if self.number.index(self.newblack[i][0])<self.number.index(self.newwhite[i][0]):
                return "White wins"
        return "Tie"

if __name__ == "__main__":
    while 1:
        black = input("输入：Black:")
        white = input("White:")
        test = TexasHoldem(black, white)
        if not test.check_input():
            print("输入格式错误，请重新输入！")
            del test
            continue
        print("输出：", test.judge_cards())
