# Стратегия — это поведенческий паттерн,
# выносит набор алгоритмов в собственные классы
# и делает их взаимозаменимыми.

# https://refactoring.guru/ru/design-patterns/strategy/python/example

class StrategyExample:
    def __init__(self, func=None):
        if func:
             self.execute = func

    def execute(self):
        print("Original execution")

def executeReplacement1():
    print("Strategy 1")

def executeReplacement2():
    print("Strategy 2")

if __name__ == "__main__":
    strat0 = StrategyExample()
    strat1 = StrategyExample(executeReplacement1)
    strat2 = StrategyExample(executeReplacement2)

    strat0.execute()
    strat1.execute()
    strat2.execute()
