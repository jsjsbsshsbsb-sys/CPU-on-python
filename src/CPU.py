from .memory import Memory, InstructionMemory


class CPU:
    def __init__(self, memory: Memory, cpu_commands: InstructionMemory, running: bool = False):

        self.memory = memory
        self.running = running
        self.cpu_commands = cpu_commands
        self.instructions = self.cpu_commands.instructions
        self.pc = 0
        self.registers = {
            "R1": 0,
            "R2": 0,
            "R3": 0,
            "R4": 0
        }

    def Decode_command(self, command, obj1=None, obj2=None):

        if command not in self.cpu_commands.cpu_commands:
            raise ValueError(f"Unknown command: {command}")

        if command == "ADD":

            if obj1 not in self.registers or obj2 not in self.registers:
                raise ValueError("ADD needs two registers")

            res = self.registers[obj1] + self.registers[obj2]
            self.registers[obj1] = res

        elif command == "LOAD":

            if obj1 not in self.registers:
                raise ValueError(f"Unknown register: {obj1}")

            self.registers[obj1] = int(obj2)

        elif command == "SUB":

            if obj1 not in self.registers or obj2 not in self.registers:
                raise ValueError("SUB needs two registers")

            res = self.registers[obj1] - self.registers[obj2]
            self.registers[obj1] = res

        elif command == "STORE":

            if obj1 not in self.registers:
                raise ValueError(f"Unknown register: {obj1}")

            self.memory.store_value(int(obj2), self.registers[obj1])

        elif command == "HLT":

            self.running = False

        return

    def fetch_instruction(self):

        self.instruction = self.cpu_commands.get_value_by_key(self.pc)
        return self.instruction

    def command_done(self) -> None:

        self.pc += 1

    def run(self):

        self.running = True

        while self.running:

            try:
                instruction = self.fetch_instruction()
            except ValueError:
                self.running = False
                break

            instruction = instruction.replace(",", " ").split()

            if not instruction:
                self.command_done()
                continue

            command = instruction[0].upper()
            obj1 = instruction[1] if len(instruction) > 1 else None
            obj2 = instruction[2] if len(instruction) > 2 else None

            self.Decode_command(command, obj1, obj2)

            if self.running:
                self.command_done()

        return
