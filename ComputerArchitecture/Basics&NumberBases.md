## Challenge One:

# Q1: How long does it take the number of transistors on a CPU to double? What is the common name for this rule of thumb?

Two years, although the cost of computers is halved. This is referred to as Moore's Law

# Q2: Why are registers necessary? Why not just use RAM?

Registers allow for quick access from the CPU because they are held within it (whereas RAM is connected to CPU via a memory bus -> takes longer to access). They hold the instructions that the CPU is currently processing whereas RAM holds the instructions & data that the CPU requires themselves. 

# Q3: Why is cache useful?

Cache is useful to allow for easy access to instructions and data from the CPU that have already previously been accessed along with instuctions and data the cache thinks the CPU may try to access in future. Eg when the CPU makes a call to address 2 in RAM for the first time, once it is retreived the cache will store it for easy retrieval the next time it is required, which will prevent the CPU from having to make another trip to RAM. It may also grab and store the contents of address 3, 4, and 5 on the assumption that the CPU may soon require them.

# Q4: What is a CPU word?

The CPU word is the size of the data with the which the CPU can interact with eg perform mathematical operations on in the ALU

# Q5: What is the system bus and how wide is it?

The system bus is  a collection of wires on the motherboard that allows for the transfer of data from the CPU to RAM and peripherals.
It is as wide as the the CPU word eg a 64-bit CPU has a 64-bit wide data bus.

# Q6: Describe the pins that are on a CPU chip

The pins on a CPU chip allow for an electrical connection between the CPU and the outside world. They are a formation of wires on the chip that fit into a socket on the motherboard/backplane that the CPU is attached to (these can be LGA, BGA OR PGA sockets).

# Q7: What is a CPU instruction?

A CPU instruction is a command that the CPU can fetch from RAM, interpret (decode) and execute some sort of action. It can take the form of a byte or a squence of bytes in memory and can be used to perform some sort of operation eg adding/multiplying two numbers in the ALU