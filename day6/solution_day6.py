
with open('input.txt', 'r') as f:
    lines = f.readlines()

pos_questions = []

questions = set(())
all_questions = []

for line in lines:
    if len(line)>1:
        line = line.strip()
        questions = questions.union(set(line))
    else:
        #print(line)
        #print(questions)
        pos_questions.append(len(questions))
        all_questions.append(questions)
        questions = set(())
all_questions.append(questions)
pos_questions.append(len(questions))

print('First result: ', sum(pos_questions))


pos_questions = []
all_questions = []
in_block = False
for line in lines:
    #print(line)
    #print(questions)
    if in_block and len(line)>1:
        line = line.strip()
        questions.intersection_update(set(line))
    elif len(line)>1 and not in_block:
        line = line.strip()
        questions = set(line)
        in_block=True
    else:
        #print(line)
        #print(questions)
        pos_questions.append(len(questions))
        all_questions.append(questions)
        in_block = False
        
all_questions.append(questions)
pos_questions.append(len(questions))

print('Second solution: ', sum(pos_questions))

