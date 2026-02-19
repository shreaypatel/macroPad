This repository contains the relevant documentation for my custom macropad project. I designed this macropad to be slim, portable and minimalist to match my use case needs. I will primarily use it for onshape CAD shortcut, 
but I am looking to explore setting up a different mode on it for KiCad shortcuts. The macropad connects to a computer via usb c. I began my design process with the wiring of the schematic. Here I opted for a 3x2 keyboard matrix 
to set up the switch connections. This takes up less input connections on the microcontroller while allowing me to customize 6 individual cherry mx switches. Next, I connected the diodes in between the switches to prevent keyboard
ghosting. Lastly, I set up a rotary rotary encoder switch for the zoom function on onshape CAD. 

<img width="1221" height="772" alt="image" src="https://github.com/user-attachments/assets/6c0617dc-1950-4ecb-9920-b5c58a72b2f9" />

With the schematic complete I moved onto routing the connections on the actual pcb. I also 
organized the layout of the pcb at this stage and ensured that all connections were wired up properly. 

<img width="518" height="812" alt="image" src="https://github.com/user-attachments/assets/2d3e9a1c-aadf-4603-be55-06a77f5ea1c2" />

<img width="851" height="835" alt="image" src="https://github.com/user-attachments/assets/be26fa7c-f9e2-4c8d-9f92-16f796d67c12" />

With the elctrical side of things completed I moved onto desiging the 3D printed enclosure for the macropad. Here I built a minimalistic case with cutouts for the switches and rotary encoder switch. I also created a cutout for the USB C connection
port. Notably, I decided to forgo using screws to secure the top and bottom parts of the enclosure. Instead I opted for a press fit conneciton with 4 3D printed studs that connect directly to the top part of the case. These slot into a square shaped
hole in the bottom of the case. This makes the prototyping process easier and allows me to qucikly clean the internals of the macropad if need be. I applied a chamfer to the 4 studs to ensure they smoothly slot into the bottom of the case. 

<img width="1208" height="769" alt="image" src="https://github.com/user-attachments/assets/012a66c5-c76f-494a-8cf4-2760b10ca442" />

<img width="1169" height="780" alt="image" src="https://github.com/user-attachments/assets/6934eb34-03ed-4034-9330-56a760c23162" />

This concludes my design process. Overall, I had a lot of fun making this project and I would say my favourite part was learning how to use KiCad to design PCBs for the first time. 
