# Assembler written in Python 3 for NAND2Tetris project 6
import os.path
import sys
import typing
import mmap


dest_lkp: typing.Dict[str, str] = {
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

jmp_lkp: typing.Dict[str, str] = {
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

cmp_lkp: typing.Dict[str, str] = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0100011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1100011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101",
}

predefined_lkp: typing.Dict[str, str] = {
    "R0": "0",
    "R1": "1",
    "R2": "2",
    "R3": "3",
    "R4": "4",
    "R5": "5",
    "R6": "6",
    "R7": "7",
    "R8": "8",
    "R9": "9",
    "R10": "10",
    "R11": "11",
    "R12": "12",
    "R13": "13",
    "R14": "14",
    "R15": "15",
    "SCREEN": "16384",
    "KBD": "24576",
    "SP": "0",
    "LCL": "1",
    "ARG": "2",
    "THIS": "3",
    "THAT": "4",
}


def sanitize_line(line: str) -> typing.List[str]:
    """
    Take a line and output a list with no white space.
    Input: line string
    Output: List of tokens
    """

    if line != "b''":
        new_line = line[2:-5]  # remove the b' and line part of the string
        tokens = new_line.split()
        return tokens
    else:
        return [""]


def is_instr(line: typing.List[str]) -> bool:
    if len(line) == 0:
        return False
    elif line[0] == "//":
        return False
    else:
        return True


def a_to_opcode(
    line: typing.List[str], variables: typing.List[str]
) -> typing.Tuple[str, typing.List[str]]:
    value = line[0][1:]
    if value.isnumeric():
        opcode = f"{int(value):016b}"
    else:
        # check for value in variables
        if value in variables:
            opcode = f"{(16 + variables.index(value)):016b}"
        else:
            # check for value in pre-defined symbols
            if value in predefined_lkp.keys():
                opcode = f"{int(predefined_lkp[value]):016b}"
            else:
                variables.append(value)
                opcode = f"{(16 + variables.index(value)):016b}"
    return opcode, variables


def c_to_opcode(line: typing.List[str]) -> str:
    opcode = "111"
    mnemonic = "".join(line)
    tmp = mnemonic.replace(";", "=")
    tmp = tmp.split("=")
    print(tmp)
    if "=" in mnemonic:
        dest = dest_lkp[tmp[0]]
        tmp.pop(0)
    if ";" in mnemonic:
        jmp = jmp_lkp[tmp[-1]]
    else:
        jmp = "000"

    opcode += dest
    opcode += cmp_lkp[tmp[0]]
    opcode += jmp
    return opcode


def main(file: str) -> None:
    label_lkp: typing.Dict[str, str] = {}
    instr: typing.List[typing.List[str]] = []
    opcodes: typing.List[str] = []
    variables: typing.List[str] = []

    with open(file, "r") as f:
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
            while True:
                line = sanitize_line(str(mm.readline()))
                if line == [""]:
                    break
                if is_instr(line):
                    if line[0][0] == "@":
                        opcode, variables = a_to_opcode(line, variables)
                    else:
                        opcode = c_to_opcode(line)
                    opcodes.append(opcode)
        print(*opcodes, sep="\n")
    return None


if __name__ == "__main__":
    # check file exists
    # if not sys.argv[1]:
    #     filepath = "add/Add.asm"
    # else:
    #    filepath = sys.argv[1]
    filepath = "add/add_test.asm"

    if not os.path.exists(filepath):
        print("File not found!")
        sys.exit(0)
    else:
        sys.exit(main(filepath))
