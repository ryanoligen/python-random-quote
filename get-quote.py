import random


def primary():
  # print("Keep it logically awesome.")

  # f = open("quotes.txt", "a")
  # f.write(" Hello Python")
  # f.close()

  f = open('quotes.txt')
  for i in f.readlines():
    i = i.strip('\n')
    print(i)

  # last = 13
  # rnd = random.randint(0, last)
  # print(quotes[rnd])

if __name__== "__main__":   
  primary()
