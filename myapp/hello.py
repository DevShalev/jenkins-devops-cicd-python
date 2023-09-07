import fire

def hello(name="World"):
  return "Hello %s!" % name

def taxcal(number=1000):
  return "Tax 17%% of %d is: %.2f!" % (number, float(number) * 0.17)

if __name__ == '__main__':
  fire.Fire(hello)


fire.Fire(taxcal)