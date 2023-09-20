// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(CHECK)
	@8192
	D=A
	@i
	M=D

	@KBD
	D=M
	@LOOP_BLK
	D; JNE

(LOOP_WHT)
	@i
	D=M
	@CHECK
	D; JEQ

	@i
	M=M-1
	@SCREEN
	D=A
	@i
	A=D+M // Point to RAM[i + SCREEN]
	M=0
	@LOOP_WHT
	0; JMP

(LOOP_BLK)
	@i
	D=M
	@CHECK
	D; JEQ

	@i
	M=M-1
	@SCREEN
	D=A
	@i
	A=D+M // Point to RAM[i + SCREEN]
	M=-1
	@LOOP_BLK
	0; JMP
