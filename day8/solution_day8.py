with open('input.txt', 'r') as f:
    instructions = f.readlines()

visited_instructions = []

keep_going = True
line = 0
accumulator = 0
while keep_going:
    if line in visited_instructions:
        keep_going = False
        break
    else:
        instruction = instructions[line]
        if instruction.startswith('nop'):
            visited_instructions.append(line)
            line+=1
        elif instruction.startswith('acc'):
            acc = int(instruction[4:])
            accumulator += acc
            visited_instructions.append(line)
            line+=1
        elif instruction.startswith('jmp'):
            jump = int(instruction[4:])
            visited_instructions.append(line)
            line += jump
        else:
            raise (ValueError, 'We dont know this instruction')

print('Accumulator=%d'%accumulator)
