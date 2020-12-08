#!/usr/bin/env python
""" 2020 code advent, day 8 part 2 """

# acc increases/decreases global accumulator, starting at 0
# jmp is jump
# nop is no-op

# one input is corrupted, either a jmp should be a nop or a nop should be a jmp. making this switch, program will finish
# finishing: executing stack_pointer = len(stack)

# what is value of accumulator before a function is executed a second time?

stack = []
params = []
visit_count = []
accumulator = 0
stack_pointer = 0

reset_pointer = 0

inputfile = open("input.txt", "r")
for line in inputfile:
    (command, param) = line.rstrip().split(' ')
    stack.append(command)
    params.append(int(param))
    visit_count.append(0)

while stack_pointer < len(stack):
    print("sp:", stack_pointer, ";ac:", accumulator, ";cmd:", stack[stack_pointer], ";param:", params[stack_pointer])
    if visit_count[stack_pointer]:
        # whoops, we visited. reset, and try a swap!

        if reset_pointer > len(stack):
            print("reset overflow!", reset_pointer)
        
        print("reset try: ", reset_pointer)
        
        # reset the visit count
        for i,e in enumerate(visit_count):
            visit_count[i] = 0
        
        accumulator = 0
        stack_pointer = 0

        # swap back the previous swap (jmp to nop, nop to jmp)
        if reset_pointer > 0:
            if stack[reset_pointer] == 'jmp':
                stack[reset_pointer] = 'nop'
            elif stack[reset_pointer] == 'nop':
                stack[reset_pointer] = 'jmp'
        
        reset_pointer += 1
        while (stack[reset_pointer] == 'acc'):
            if reset_pointer > len(stack):
                print("bailing")
                exit
            reset_pointer += 1
        
        if stack[reset_pointer] == 'jmp':
            stack[reset_pointer] = 'nop'
        elif stack[reset_pointer] == 'nop':
            stack[reset_pointer] = 'jmp'

    else:
        visit_count[stack_pointer] += 1
        if stack[stack_pointer] == 'acc':
            accumulator += params[stack_pointer]
            stack_pointer += 1
        elif stack[stack_pointer] == 'nop':
            stack_pointer += 1
        elif stack[stack_pointer] == 'jmp':
            stack_pointer += params[stack_pointer]
        else:
            print("unknown command:", stack[stack_pointer])
            break

print("successfully exited. accumulated: ", accumulator)
