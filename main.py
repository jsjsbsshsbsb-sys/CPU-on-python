from src.CPU import CPU
from src.memory import Memory, InstructionMemory


memory = Memory()
cpu_commands = InstructionMemory()

cpu_commands.add_instruction("LOAD R1, 10")
cpu_commands.add_instruction("LOAD R2, 5")
cpu_commands.add_instruction("ADD R1, R2")
cpu_commands.add_instruction("STORE R1, 0")
cpu_commands.add_instruction("HLT")

cpu = CPU(memory, cpu_commands)
cpu.run()

print("Registers:", cpu.registers)
print("Memory:", memory.memory)
