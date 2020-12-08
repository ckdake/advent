#!/usr/bin/env python
""" 2020 code advent, day 8 part 1 """

# acc increases/decreases global accumulator, starting at 0
# jmp is jump
# nop is no-op

# what is value of accumulator before a function is executed a second time?

stack = []
params = []
visit_count = []
accumulator = 0
stack_pointer = 0

inputfile = open("input.txt", "r")
for line in inputfile:
    (command, param) = line.rstrip().split(" ")
    stack.append(command)
    params.append(int(param))
    visit_count.append(0)

while stack_pointer < len(stack):
    print(
        "sp:",
        stack_pointer,
        ";ac:",
        accumulator,
        ";cmd:",
        stack[stack_pointer],
        ";param:",
        params[stack_pointer],
    )
    if visit_count[stack_pointer]:
        print("accumulated: ", accumulator)
        break
    else:
        visit_count[stack_pointer] += 1
        if stack[stack_pointer] == "acc":
            accumulator += params[stack_pointer]
            stack_pointer += 1
        elif stack[stack_pointer] == "nop":
            stack_pointer += 1
        elif stack[stack_pointer] == "jmp":
            stack_pointer += params[stack_pointer]
        else:
            print("unknown command:", stack[stack_pointer])
            break
