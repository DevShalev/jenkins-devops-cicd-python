import fire

def hello(name="World"):
  return "Hello %s!" % name

def taxcal(number=1000):
  return "tax of 1000 is: %s!" % float(number)*0.17

if __name__ == '__main__':
  fire.Fire(hello)


fire.Fire(taxcal)