from .memory import Memory, InstructionMemory


class CPU:
    def __init__(self, memory: Memory, cpu_commands: InstructionMemory ,running: bool = False):
        
        self.memory = memory
        self.running = running
        self.cpu_commands = cpu_commands
        self.instructions = self.memory.instruction_list
        self.pc = 0
        self.registers = {
            "R1": 0,
            "R2": 0,
            "R3": 0,
            "R4": 0
        }

    def Decode_command(self, command):
        
        if command in self.cpu_commands:
            if command == "ADD":
                ...
            elif command == "LOAD":
                ...
            elif command == "SUB":
                ...
            elif command == "STORE":
                ...
            elif command == "HLT":
                ...
        
        return
    
    def fetch_instruction(self):
        
        self. instruction = self.memory.get_value_by_key(self.pc)
        return self.instruction
        
    def command_done(self) -> None:
        
        self.pc += 1