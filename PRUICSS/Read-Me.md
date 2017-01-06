# PRUICSS Architecture

BBB has 2 PRU's , 32 bits 200MHz RISC Processors. They have their own memory allocation but they can use P9 Headers and share memory with Linux Host Device.

PRU0 and PRU1 each with 8Kb of Program Memory (Stores instructions to be executed by PRU's and 8Kb of Data Memory ( Stores data values manipulated by the program instructions)

PRU0 uses Ram0 and PRU1 uses Ram1. Each PRU can access Data Memory of other PRU's
