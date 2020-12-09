import numpy as np
import copy


def run_sequence(instructions):
    terminated=False
    keep_going = True
    line = 0
    accumulator = 0
    max_jump = -1
    visited_instructions = []
    while keep_going:
        if line in visited_instructions:
            # print('still looping')
            keep_going = False
            break
        elif line>=len(instructions):
            print('Terminated!!!')
            keep_ging = False
            terminated = True
            break
        else:
            instruction = instructions[line]
            if instruction.startswith('nop'):
                jmp = int(instruction[4:])
                visited_instructions.append(line)
                # print('line: %d, potential jump point: %d'%(line, line+jmp))
                max_jump = max(max_jump, line+jmp)                  
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

    print('we finished, with line=%d'%line)
    return accumulator, terminated

with open('input.txt', 'r') as f:
    orig_instructions = f.readlines()

instructions = copy.copy(orig_instructions)
    
mod_line=0
tried_line = -1
for i, line in enumerate(instructions):
    if line.startswith('nop') and tried_line<i:
        new_line = 'jmp' + line[3:]
        instructions[i] = new_line
        tried_line = i
        a, t = run_sequence(instructions)
        if t:
            print(a, new_line, orig_instructions[i])
            break
        else:
            instructions[i]=orig_instructions[i]
            continue
    elif line.startswith('jmp') and tried_line<i:
        new_line = 'nop' + line[3:]
        instructions[i] = new_line
        tried_line = i
        a, t = run_sequence(instructions)
        if t:
            print(a, new_line, orig_instructions[i])
            break
        else:
            instructions[i]=orig_instructions[i]
            continue
    elif line.startswith('acc'):
        continue
    else:
        raise ValueError

