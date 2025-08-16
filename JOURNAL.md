---
title: "KyraDock"
author: "Karan"
description: "A Powerful developer friendly AI Assistant device."
created_at: "2025-06-24"
---

## TOTAL TIME SPEND: 38h (remake whole once)

### May 17 — Time Spent: 3 hours

* Finalized the project idea and name: **KyraDock**, an AI-powered smart assistant dock.
* Conducted initial research on features, necessary components, and design.

---

### May 18–19 — Time Spent: 7 hours

* Designed some 3D concept models to explore potential ideas.
* Started sourcing required components such as speaker, amplifier, switches, and fan on QuartzComponents.

![3D Models](https://github.com/user-attachments/assets/4179ab3e-0551-4a9b-bc2f-37856004a8f7)
![3D Models](https://github.com/user-attachments/assets/b0dd2926-5d44-4129-b6a5-9759a9f25bd8)

---

### May 20 — Time Spent: 50 mins

* Shifted component sourcing from QuartzComponents to RoboCraze due to payment gateway issues.
---

### June 10 — Time Spent: 5 hours

* Finalized the overall enclosure design and internal component layout.
* Decided not to include holes for the speaker, switch, microphone, and exhaust fan in the CAD model, opting to manually drill them later using a dremel for more flexible placement.
* Defined placement for key components:

  * [3W x2 Speakers](https://amzn.in/d/aNKvVoh) positioned near the sides of body for sound output.
  * 5V mini cooling fan mounted at the rear side for air exhaust.

![Speaker](https://github.com/user-attachments/assets/3459c4a1-1c78-4695-b217-35222d38b8ac)
![Fan](https://github.com/user-attachments/assets/9974a4f0-4c5b-4b7a-bdc3-378670575318)

* Created an initial circuit diagram mapping connections between Raspberry Pi, amplifier, fan, and other component.

![image](https://github.com/user-attachments/assets/59f5c9cf-bad2-4793-bb12-8bf726c4bd31)

---

### June 12 — Time Spent: 5 hours

* Rebuilt the KyraDock enclosure to correct dimension mismatches and improve fit for components.
* Adjusted Raspberry Pi and screen alignment to reduce extra space and made it more compact.

**Back Lid Completed** — Time Spent: 20 mins

* Created and fitted the back lid to enclose the assembly. Designed it to be detachable for future hardware modifications.

![New Body](https://github.com/user-attachments/assets/83ff21b3-52e1-4513-a089-1ce18d0dc96b)
![Lid](https://github.com/user-attachments/assets/2926423b-727c-4b78-94ee-d5ad6e72d3dd)
![Lid](https://github.com/user-attachments/assets/8a4dd21d-41cd-4d0d-a5ef-8451f106243b)

---

### June 14 — Time Spent: 1 hours

* Added additional components and finalized BOM.
* Enhanced circuit diagram.
![image](https://github.com/user-attachments/assets/21da881f-2749-48f7-a418-758b413d5d6e)

### June 17 — Time Spent: 2 hours
* Started work on Kyra assistant code, added basic wakeup word and ai question.

## July 29 - Time Spend: 3 hours
* optimized BOM, on same cost added more components for more features, including, ai vision, multi-purpose speaker setup with bluetooth support.
<img width="1041" height="639" alt="image" src="https://github.com/user-attachments/assets/3e28d53c-0ea2-4b94-b2da-526b12a2dc15" />

--------------

### 9 August to 12 August (Rebuild): - Time Spend: 10 hours
- so we are rebuilding kyradock to make it cheaper and more better.
- new circuit diagram:
<img width="1920" height="649" alt="image" src="https://github.com/user-attachments/assets/d06023be-d1bf-47dd-87e8-66050846d644" />

- made base and added support for screen screws:
<img width="305" height="189" alt="Fusion360_tDFOAnu2nW" src="https://github.com/user-attachments/assets/476667b9-1361-4bae-b769-5f399d9e29b7" />
<img width="298" height="194" alt="Fusion360_njSS57gOE0" src="https://github.com/user-attachments/assets/4a431c0e-0912-405b-8b2d-ff66d4f73ada" />

- covered top and then polished it:
<img width="317" height="244" alt="Fusion360_SVdMAvunx4" src="https://github.com/user-attachments/assets/d1102613-197e-4b5d-827a-8041b36e026b" />
<img width="351" height="289" alt="Fusion360_Q7eIrj5fWu" src="https://github.com/user-attachments/assets/e1294746-638c-46b9-a0ca-3b6268586f9a" />

- marked top touch buttons:
<img width="364" height="307" alt="Fusion360_XOlHWsg9Ct" src="https://github.com/user-attachments/assets/8274dc9c-8b73-4076-a470-cdb3cc7b60f4" />

- added svgs for the touch buttons i want:
<img width="960" height="362" alt="Fusion360_6O28NqHHGk" src="https://github.com/user-attachments/assets/b8a861db-2e38-4d20-b71e-cc229af899e4" />

- im going to add: mute, volume, listen, mode, and a custom button for running some scripts or other workflows directly using the button.

- here is finished look of touch buttons:

<img width="960" height="362" alt="Fusion360_O7QakM8WVM" src="https://github.com/user-attachments/assets/da17bdcc-f6bf-4728-81ac-6e2c8bd7869f" />

- i also made good space for touch sensor modules:
<img width="960" height="362" alt="Fusion360_TD9yMNOVYU" src="https://github.com/user-attachments/assets/f56caf55-cc58-497b-8104-96ff671be38d" />
<img width="960" height="362" alt="Fusion360_N6gNqwxqz8" src="https://github.com/user-attachments/assets/dc6f97d6-ff59-4f3d-ae34-9a03977d3c42" />

- added small holes for mic modules:
<img width="960" height="362" alt="Fusion360_uL5N4Xp2NJ" src="https://github.com/user-attachments/assets/6abdbb66-a446-40fb-b0fe-484d2816187f" />
<img width="960" height="362" alt="Fusion360_VfHuKgqBMj" src="https://github.com/user-attachments/assets/379f848e-5664-4cf7-8297-d718ff6cd09a" />

- added back panel and we are keeping out speakers on back side cuz no area left ;p
<img width="960" height="362" alt="Fusion360_RaRNyqPHrP" src="https://github.com/user-attachments/assets/2dd9036f-d2d5-4bb0-b3c9-f69a232332ed" />

- made holes for speakers output sounds:
<img width="960" height="362" alt="Fusion360_aKAHWZLGNK" src="https://github.com/user-attachments/assets/1d8dfac1-e173-466c-b2e1-26cf9adc5a86" />
<img width="344" height="241" alt="Fusion360_KAzgBLdl6N" src="https://github.com/user-attachments/assets/5d3dc272-2f68-4d3a-9e8f-a4f1f350a00c" />

- did some final things and made the whole case more better and polished:
<img width="550" height="368" alt="Fusion360_j2AfIr8uOp" src="https://github.com/user-attachments/assets/6a1ca8a8-5751-4b21-ae69-7cfda1b1b3c3" />
<img width="680" height="373" alt="Fusion360_ZqpiBTJud0" src="https://github.com/user-attachments/assets/9c83329f-d4df-4644-a8ff-ba1e1525721d" />

- added space for usb c port at back for power up whole system:
<img width="292" height="217" alt="Fusion360_ZSKbNiHr91" src="https://github.com/user-attachments/assets/a83c2e30-a9bd-4647-a8f5-5d93a99970f2" />

- here is final kyradock renders:
<img width="418" height="353" alt="Fusion360_MifFIdHvIN" src="https://github.com/user-attachments/assets/5c4b60b9-5e1b-4385-aefd-c41bb934bffb" />
<img width="585" height="207" alt="Fusion360_hUhD3b9yuh" src="https://github.com/user-attachments/assets/46e42b3d-7193-48d7-b671-cf1ff34ad771" />

- filled inward gaps in buttons from back side:
<img width="447" height="302" alt="Fusion360_bUSNLFSlyg" src="https://github.com/user-attachments/assets/6eb88b31-da3c-4d0d-9d19-29de780d168a" />

- made 4 stands under body for support and uplift:
<img width="435" height="248" alt="Fusion360_PaMIYmxLgk" src="https://github.com/user-attachments/assets/d008658b-c617-44ff-94d2-ce913f0814f5" />
<img width="447" height="295" alt="Fusion360_A1MIwRGyqA" src="https://github.com/user-attachments/assets/88694d65-f5a4-49a1-a3c1-54b7945e822d" />

- made holes for brass insert, for 3mm bolts
<img width="438" height="303" alt="Fusion360_Qj37kUzKEC" src="https://github.com/user-attachments/assets/9443a6c3-6107-45d4-9805-5f6b798bf8d9" />
<img width="394" height="292" alt="Fusion360_pHonHFjULk" src="https://github.com/user-attachments/assets/f97189d1-69ff-493f-85a4-8e415b39266a" />


- updated BOM and README.
