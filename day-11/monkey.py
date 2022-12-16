import logging
global common
common = 1
# logging.basicConfig(level=logging.DEBUG)
# monkeys are playing keepaway with your items
# 
#    Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
#    Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
#    Test shows how the monkey uses your worry level to decide where to throw an item next.
#        If true shows what happens with an item if the Test was true.
#        If false shows what happens with an item if the Test was false.

# on each inspection your worry = worry // 3
# monkeys take turns inspecting 
# monkeys inspect and throw all items on their turn
# monkeys take turns from 1 to n
# when all monkeies have a turn it is called a round
# when a monkey thows an item to another monkey it goes to the end of that monkeys list
# if a monkey is holding no items at the start of the turn their turn ends

    
class monkey():
    def __init__(self, items: list, operation, test, t, f):
        self.items = items
        self.operation = operation
        self.test = test
        self.t = t
        self.f = f
        self.inspection_count = 0
    
    def process_list(self):
        items = []
        global common
        for old in self.items:
            self.inspection_count += 1
            new = eval(self.operation.strip()[6:])
            # logging.debug(f' monkey is inspectin an item with level {old}, worry level is now {new}')
            new = new % common
            # logging.debug(f' divide by 3 worry level is now {new}')
            items.append(new)
        self.items = items
    
    def take_turn(self):
        self.process_list()
        tlist = []
        flist = []
        for i in self.items:
            if i % self.test == 0:
                tlist.append(i)
            else:
                flist.append(i)
        self.items = []
        return {self.t : tlist,
                self.f : flist}
    
    def catch(self, caught: list):
        for i in caught:
            self.items.append(i)
            

def parse(monkey_file):
    monkeys = []
    in_monkey = False
    tmp_monkey = {} 
    for line in monkey_file:
        if line == '\n':
            in_monkey = False
        elif line.strip()[0] == 'M':
            in_monkey = True
        if in_monkey:
            if line.strip()[0] == "S":
                items = line.strip().split(':')[1]
                items = items.split(',')
                items = list(map(int, items))
                tmp_monkey['items'] = items
            elif line.strip()[0] == "O":
                operation = line.strip().split(':')[1]
                tmp_monkey['operation'] = operation
            elif line.strip()[0] == "T":
                tmp_monkey['test'] = int(line.strip().split('by')[1])
            elif line.strip()[0] == "I":
                if line.strip().split()[1][0] == 't':
                    tmp_monkey['t'] = int(line.strip().split('monkey')[1])
                elif line.strip().split()[1][0] == 'f':
                    tmp_monkey['f'] = int(line.strip().split('monkey')[1])
                    in_monkey = False
                    monkeys.append(monkey(tmp_monkey['items'], tmp_monkey['operation'],tmp_monkey['test'], tmp_monkey['t'], tmp_monkey['f']))
    return monkeys            


with open('day-11/input.txt') as monkey_file:
    monkeys = parse(monkey_file)
    for m in monkeys:
        common = common * m.test
    for i in range(10000):
        print(f'round {i}')
        for monkey in monkeys:
            throws = monkey.take_turn()
            for t in throws:
                monkeys[t].catch(throws[t])
    for monkey in monkeys:
        print(monkey.items)
        print(monkey.inspection_count)
    scores = []
    for monkey in monkeys:
        scores.append(monkey.inspection_count)
    scores.sort()
    print(scores)
    print(scores[-2]*scores[-1])
    