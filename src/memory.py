MAX_MEMORY_SIZE = 256
MAX_VALUE = 65535
MIN_VALUE = 0
ADDRES_MAX_VALUE = 255
ADDRES_MIN_VALUE = 0


class Memory:
    def __init__(self, instruction_list: list = None, memory=None):

        self.max_memory_size = MAX_MEMORY_SIZE
        self.memory = {} if memory is None else memory
        self.instruction_list = [] if instruction_list is None else instruction_list

    def add_value(self, key, value):

        self.check_max_memory()

        if key in self.memory:
            raise ValueError("such a cell already exists")

        if not (MIN_VALUE <= value <= MAX_VALUE):
            raise ValueError(f"The value: {value} exceeds the limits")

        if not (ADDRES_MIN_VALUE <= key <= ADDRES_MAX_VALUE):
            raise ValueError(f"The addres {key} exceeds the limits")

        self.memory[key] = value

    def store_value(self, key, value):

        if not (ADDRES_MIN_VALUE <= key <= ADDRES_MAX_VALUE):
            raise ValueError(f"The addres {key} exceeds the limits")

        if not (MIN_VALUE <= value <= MAX_VALUE):
            raise ValueError(f"The value: {value} exceeds the limits")

        if key not in self.memory:
            self.check_max_memory()

        self.memory[key] = value

    def address_to_memory(self, key):

        if key not in self.memory:
            raise ValueError("This memory cell does not exist")

        return self.memory[key]

    def check_max_memory(self) -> None:
        if len(self.memory) >= self.max_memory_size:
            raise ValueError("Memory is overfilled")

    def get_value_by_key(self, key):

        if key in self.memory:
            return self.memory[key]
        else:
            raise ValueError("This memory cell does not exist")


class InstructionMemory:
    def __init__(self, instructions=None):

        self.cpu_commands = ["ADD", "LOAD", "SUB", "STORE", "HLT"]
        self.instructions = [] if instructions is None else instructions

    def add_instruction(self, instruction):

        if len(self.instructions) >= MAX_MEMORY_SIZE:
            raise ValueError("Instruction memory is overfilled")

        self.instructions.append(instruction)

    def get_value_by_key(self, key):

        if not (ADDRES_MIN_VALUE <= key <= ADDRES_MAX_VALUE):
            raise ValueError(f"The addres {key} exceeds the limits")

        if key >= len(self.instructions):
            raise ValueError("This instruction does not exist")

        return self.instructions[key]
