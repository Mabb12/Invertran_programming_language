def invertran(code: list):
    pc = 0
    memory = [0] * 16
    len_code = len(code)
    while pc < len_code:
        if code[pc] == "invert":
            memory[code[pc + 1]] = 1 - memory[code[pc + 1]]
            pc += 2
        elif code[pc] == "transition":
            if memory[0] == 1: pc = code[pc + 1]
            else: pc += 2
        print(memory)

invertran(["invert", 5, "invert", 0, "transition", 0])