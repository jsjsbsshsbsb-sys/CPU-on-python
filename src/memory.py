
MAX_MEMORY_SIZE = 256
MAX_VALUE = 65534
MIN_VALUE = 0
ADDRES_MAX_VALUE = 255
ADDRES_MIN_VALUE = 0

class Memory:
    def __init__(self, instruction_list: list, memory = {}):
        
        self.max_memory_size = MAX_MEMORY_SIZE
        self.memory = memory
        self.instruction_list = instruction_list
        
    
    def add_value(self, key, value):
        
        self.check_max_memory()
        
        
        if key in self.memory:
            raise ValueError("such a cell already exists")
        
        if not (MIN_VALUE <= value <= MAX_VALUE):
            raise ValueError(f"The value: {value} exceeds the limits")
        
        if not (ADDRES_MIN_VALUE <= key <= ADDRES_MAX_VALUE):
            raise ValueError(f"The addres {key} exceeds the limits")
        
        self.memory[key] = value
        print(self.memory)
        
    
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
    def __init__(self):
        
        self.cpu_commands = ["ADD", "LOAD", "SUB", "STORE", "HLT"]
