# NAND2Tetris Course
(Supplemented by notebook for basic notes and ideas)

## Roadmap
Pt. 1: Hardware
    Build HACK computer
        Silicon to low level code

        elementary logic units (NAND2 to DMUX8Way)
        |
        ALU (Half Adders to ALU)
        |
        Registers and Memory (Bit Memory to Program Counter)
        |
        Computer Architecture (Memory > CPU > Computer)
        |
        Low Level Programs
        |
        Assembler
Pt. 2: Software
    Create full SW hierarchy to run Tetris
        Low level code to Tetris
### Unit 0: 
    Abstraction Layers!
    NAND2: y = a' * b'
        a   b   y
        0   0   1 
        0   1   1 
        1   0   1 
        1   1   0 


### Unit 1: 
#### 1.4 Hardware Description Language (HDL)
    /** Comments here **/

    CHIP Xor {
        in a, b;
        out out;
        // =========================== interface ^
        // Must specify input first then output

    /* First breakdown the truth table you want to implement into all the wires that make it up.
        For instance, xXORy = x'y + xy' which means:
            The out is connected to an OR gate with inputs x'y and xy'
            The out_x'y is connected to an AND gate with inputs x' and y
            The out_xy' is connected to an AND gate with inputs x and y'
            The the out_x' is connected to a NOT gate with input x
            The the out_y' is connected to a NOT gate with input y

            Once you get to the primitive wires, stop and work backwards
            Needed wires: notx, noty, xy', x'y

        (we're using a, b, and out instead of x and y...) **/


        PARTS:
            Not (in=a, out=nota);
            Not (in=b, out=notb);

            And (a=nota, b=b, out=notaAndb);
            And (a=a, b=notb, out=aAndNotb);

            Or (a=aAndNotB, b=notaAndb, out=out);

        // =========================== implementation ^
    }


HDL has infinite FANOUT; meaning it can output any number of a wire instantaneously. (No driving requirements!)

Gate implementation convention:
    function(a=first_input, b=second_input, ..., out=final_output)


#### 1.4 & 1.5 Hardware Simulation
To verify the values of internal and external outputs.
Script based simulation:

    load file_to_be_tested.hdl;
    output-file output_of_test.out;
    set a 0, set b 0, eval, output;
    set a 0, set b 1, eval, output;
    set a 1, set b 0, eval, output;
    set a 1, set b 1, eval, output;

Comparing our output file to a predefined goal file makes testing the performance of our chip less overwhelming for chips with a large number of inputs.

Add this section to your test file along with the pre-populated truth table:

        compare-to output-expectations.cmp,

after selecting the output file on the second line (don't separate the lines with a semicolon, just a comma).

#### 1.6 Multi-bit Buses
Think of a group of bits as a single entity called a **bus**.
In HDL, buses are handled by ___________

For instance, a 16-bit adder gets treated like 2 16-bit numbers are going into it instead of 32 individual lines carrying a sigle bit each.
<img title= "Two 16-bit buses going into a full adder" alt="16-bit Buses" src="figures/16-bit bus adder.png">

Skeleton Code:

        /* Add 2 16-bit numbers */
        CHIP Add16{
            IN a[16],
               b[16];
            OUT out[16];
        
            PARTS:
                //...
        }

To add a third input to this adder,

        CHIP Add3Way16{
            IN a[16], b[16], c[16];
            OUT out[16];

            PARTS:
                Add (a=a, b=b, out=out1);
                Add (a=c, b=out1, out=out);
        }

Working with buses:

1. To access the i'th bit, simply a[i]=element
2. To access a sub-range j to k, a[j..k]=sub_section
3. Use the boolean values 'true' or 'false' to set all the values of the bits in a bus to 1 or 0 respectively


#### 1.7 Programmable Gates
Building a MUX:

    /* 2 input MUX */
    CHIP Mux{
        IN a, b, sel;
        OUT out;

        PARTS:
        Not (a=sel, out=sel_bar);
        And (a=sel, b=b, out=selANDb);
        And (a=sel_bar, b=a, out=sel_barANDa);
        Or (a=selANDb, b=sel_barANDa, out=out);
    }


MUXes to build programmable gates:
eg. AndMuxOr

    /*    Act as an and gate when select is 0 and or gate when select is 1 */
    CHIP AndMuxOr {
        IN a, b, sel;
        OUT out;

        PARTS:
        And (a=a, b=b, out=aANDb);
        Or (a=a, b=b, out=aORb);
        Mux (a=aANDb, b=aORb, sel=sel, out=out);
    }

De-Multiplexor
Takes an input and distributes it to N outputs depending on the select

    /* DeMux */
    CHIP DMux {
        IN in, sel;
        OUT a, b;

        PARTS:
        Not (a=sel, out=sel_bar);
        And (a=in, b=sel_bar, out=a);
        And (a=in, b=sel, out=b);
    }


##### Bus operations:
16-bit Variants of elementary gates:

    /* And16 */
    CHIP And16 {
        IN a[16], b[16];
        OUT out[16];

        PARTS:
        And (a=a[0], b=b[0], out=out[0]); 
        And (a=a[1], b=b[1], out=out[1]); 
        And (a=a[2], b=b[2], out=out[2]); 
        And (a=a[3], b=b[3], out=out[3]); 
        And (a=a[4], b=b[4], out=out[4]); 
        And (a=a[5], b=b[5], out=out[5]); 
        And (a=a[6], b=b[6], out=out[6]); 
        And (a=a[7], b=b[7], out=out[7]); 
        And (a=a[8], b=b[8], out=out[8]); 
        And (a=a[9], b=b[9], out=out[9]); 
        And (a=a[10], b=b[10], out=out[10]);
        And (a=a[11], b=b[11], out=out[11]);
        And (a=a[12], b=b[12], out=out[12]);
        And (a=a[13], b=b[13], out=out[13]);
        And (a=a[14], b=b[14], out=out[14]);
        And (a=a[15], b=b[15], out=out[15]);
    }

### Unit 2: 
### Unit 3: 
### Unit 4: 
### Unit 5: 
### Unit 6: 
