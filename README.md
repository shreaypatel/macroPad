This repository contains the relevant documentation for my custom macropad project. I designed this macropad to be slim, portable and minimalist to match my use case needs. I will primarily use it for onshape CAD shortcuts, 
but I am looking to explore setting up a different mode on it for KiCad shortcuts. The macropad connects to a computer via usb c. I began my design process with the wiring of the schematic. Here I opted for a 3x2 keyboard matrix 
to set up the switch connections. This takes up less input connections on the microcontroller while allowing me to customize 6 individual cherry mx switches. Next, I connected the diodes in between the switches to prevent keyboard
ghosting. Lastly, I set up a rotary rotary encoder switch for the zoom function on onshape CAD. 

<img width="1221" height="772" alt="image" src="https://github.com/user-attachments/assets/6c0617dc-1950-4ecb-9920-b5c58a72b2f9" />

With the schematic complete I moved onto routing the connections on the actual pcb. I also 
organized the layout of the pcb at this stage and ensured that all connections were wired up properly. 

With the elctrical side of things completed I moved onto desiging the 3D printed enclosure for the macropad. Here I built a minimalistic case with cutouts for the switches and rotary encoder switch. I also created a cutout for the USB C connection
port. Notably, I decided to forgo using screws to secure the top and bottom parts of the enclosure. Instead I opted for a press fit conneciton with 4 3D printed studs that connect directly to the top part of the case. These slot into a square shaped
hole in the bottom of the case. This makes the prototyping process easier and allows me to qucikly clean the internals of the macropad if need be. I applied a chamfer to the 4 studs to ensure they smoothly slot into the bottom of the case. I also included 
an elevated platform support for the pcb to rest on in the enclosure. 

<img width="1179" height="778" alt="image" src="https://github.com/user-attachments/assets/ac5fe3cb-1657-435f-be76-f5aa5a3617e7" />

<img width="1351" height="792" alt="image" src="https://github.com/user-attachments/assets/b0640d0f-8272-4f4b-bda4-83df09bca765" />


This concludes my design process. Overall, I had a lot of fun making this project and I would say my favourite part was learning how to use KiCad to design PCBs for the first time. Here is the onshape document link: https://cad.onshape.com/documents/c0725aa56d0443495cbb7afd/w/927aa1fb6a4206026ca4e494/e/183a6f23183eff95dca8855f


**BOM:**

* 1 x 3D printed case
* 1 x SEEED XIAO RP2040
* 4 x CHERRY MX keyswitches
* 1 x EC11 rotary encoder
* 6 x 1N4148 diodes

Final Image of CAD and electronics together: 
<img width="805" height="618" alt="image" src="https://github.com/user-attachments/assets/5adfbbfd-ad3b-4215-b216-b3945e598eed" />



