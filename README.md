This repository contains the relevant documentation for my custom macropad project. I designed this macropad to be slim, portable and minimalist to match my use case needs. I will primarily use it for onshape CAD shortcuts, 
but I am looking to explore setting up a different mode on it for KiCad shortcuts. The macropad connects to a computer via usb c. I began my design process with the wiring of the schematic. Here I opted for a 3x2 keyboard matrix 
to set up the switch connections. This takes up less input connections on the microcontroller while allowing me to customize 6 individual cherry mx switches. Next, I connected the diodes in between the switches to prevent keyboard
ghosting. Lastly, I set up a rotary rotary encoder switch for the zoom function on onshape CAD. This is the ****CAD onshape source file https://cad.onshape.com/documents/c0725aa56d0443495cbb7afd/w/927aa1fb6a4206026ca4e494/e/183a6f23183eff95dca8855f ****

<img width="1221" height="772" alt="image" src="https://github.com/user-attachments/assets/6c0617dc-1950-4ecb-9920-b5c58a72b2f9" />

With the schematic complete I moved onto routing the connections on the actual pcb. I also 
organized the layout of the pcb at this stage and ensured that all connections were wired up properly. 

<img width="485" height="854" alt="image" src="https://github.com/user-attachments/assets/5d9a9af9-c062-457c-ad8f-066960590c64" />

<img width="582" height="926" alt="image" src="https://github.com/user-attachments/assets/106eb868-745d-41f3-bc89-f40febc59621" />


With the elctrical side of things completed I moved onto desiging the 3D printed enclosure for the macropad. Here I built a minimalistic case with cutouts for the switches and rotary encoder switch. I also created a cutout for the USB C connection
port. Notably, I decided to forgo using screws to secure the top and bottom parts of the enclosure. Instead I opted for a press fit conneciton with 4 3D printed studs that connect directly to the top part of the case. These slot into a square shaped
hole in the bottom of the case. This makes the prototyping process easier and allows me to qucikly clean the internals of the macropad if need be. I applied a chamfer to the 4 studs to ensure they smoothly slot into the bottom of the case. I also included 
an elevated platform support for the pcb to rest on in the enclosure. Superglue can also be used to more securely attach the pins into their respective holes. 

<img width="961" height="713" alt="image" src="https://github.com/user-attachments/assets/fcf53d8f-c5ea-4422-b951-dd61d7028995" />

<img width="779" height="759" alt="image" src="https://github.com/user-attachments/assets/41bbfcbc-2dc1-4e9d-af2d-26f684eab307" />


This concludes my design process. Overall, I had a lot of fun making this project and I would say my favourite part was learning how to use KiCad to design PCBs for the first time. 


**BOM:**

* 1 x 3D printed case
* 1 x SEEED XIAO RP2040
* 4 x CHERRY MX keyswitches
* 1 x EC11 rotary encoder
* 6 x 1N4148 diodes

Final Image of CAD and electronics together: 
<img width="1020" height="720" alt="image" src="https://github.com/user-attachments/assets/d50def15-8522-4cf8-9b10-86c30bb4e499" />




