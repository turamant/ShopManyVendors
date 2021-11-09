class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


class Fibbonachi:

    def __iter__(self):
        self.cur_val = 0
        self.next_val = 1
        return self

    def __next__(self):
        tmp = self.next_val
        self.next_val += self.cur_val
        self.cur_val = tmp
        return tmp


f = Fibbonachi()
print(f)
for i in Fibbonachi():
    print(i)
    if i > 100:
        break
