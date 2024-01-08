## SPERO
## Introduction
This is the repository of the Support for Pandemic and Epidemic Robot (SPERO), which was created by Petra Christian University in reaction to the COVID-19 Pandemic. SPERO is an autonomous robot designed to deliver food and medicine to COVID-19 patients in hospitals and disinfect rooms in hospitals, offices, and warehouses using UV-C technology. The robot operates on Raspberry Pi 4, employing the Robot Operating System (ROS) framework and utilizing MQTT protocols for the sensor's data transmission. Additionally, it features a user-friendly interface for seamless operation.

It's important to note that this repository solely emphasizes the room disinfection functionality as it was separately developed by a different team.

News Article (Indoensian): https://news.detik.com/berita-jawa-timur/d-5070279/robot-spero-uk-petra-siap-bantu-nakes-rs-royal-tangani-pasien-covid-19 <br>
Demo Video (Indoensian): https://www.youtube.com/watch?app=desktop&v=6mw96LuuPDw

## Key Highlight
### Robot Structure:
- Designed with modularity in mind, the UV-C serves as an independent module separate from the mobile robot, enabling the potential for diverse robot functionalities.
- Dimensions: 50 cm length, 50 cm width, 175 cm height with 5 cm ground clearance.
- Estimated weight: 25 kg. 
- Body structure comprises a 4mm thick iron frame beneath the robot and a 2mm thick iron body.

### Robot Control System:
- Utilizes Raspberry Pi 4 as the microcontroller, programmed with ROS Noetic and Python.
- Implements multithreading for continuous sensor readings during operation.
- Distance and motion sensors are connected to Wemos D1 Mini ESP8266 for wireless communication with Raspberry Pi 4 using the MQTT protocol (IoT).
- Equipped with proximity sensors to prevent collisions during the disinfection process and motion sensors to detect human presence, ensuring the safety of individuals around UV-C radiation.

### Remote Control and Monitoring System:
- Operator's Raspberry Pi 400 features a user interface for video monitoring and robot control.
- Involves a camera processed by Raspberry Pi Zero W in the robot, transmitting video wirelessly to Raspberry Pi 400 via LAN.
- Facilitates manual control through a joystick in the event of robot issues or obstacles.
- Joystick inputs are transmitted via the local area network to Raspberry Pi 4 for immediate control, minimizing delays.

### Electrical Power System:
- The robot is powered by a 12V 35Ah battery.
- The MAX471 module monitors battery voltage, and Raspberry Pi 4 sends notifications to the operator if the battery drops below normal.
- An inverter converts 12V DC from the battery to 220V AC for powering UV-C lamps.
- The battery can sustain full operational conditions for 1 hour and disinfect an area of 172 square meters in the process.


## Robot Components
### Mobile Robot component: <br>
1 Raspberry Pi 4 <br> 
4 Motors (Planetary Gearbox, 24V, 60W) <br>
4 Omni-directional Wheels <br>
4 Motor Drivers BTS7960 H Bridge 43A <br>
1 PWM 16 Channel PCA9685 <br>
1 Magnetic Navigation Sensor TCB MGS-16FP <br>
8 Distance Sensors VL53L0X <br>
6 Infrared Motion Sensors HC-SR501 <br> 
9 Wemos D1 Mini ESP8266 <br>
1 Battery (12v 35Ah) <br>
1 Voltage and Current Sensor MAX471 <br>
1 Power supply 12V 30A (to charge the battery) <br>
1 Inverter 1000W <br>
6 UV-C Lamps <br>
1 Relay <br>
1 Raspberry Pi Zero W <br> 
1 Camera OmniVision OV5647 <br>
1 Router Prolink PRN2001 <br>
Custom-designed PCBs <br>

### Remote Control and Monitoring component: <br>
1 Raspberry Pi 400 <br>
1 monitor
1 Joystick <br>

## Robot Design
### Initial Design 
<p align="center">
  <img src="/figures/robot_base.png" style="width:200px;"/>
  <img src="/figures/UVC_module.png" style="width:200px;"/>
  <img src="/figures/full_robot.png" style="width:200px;"/>

### Final Product 
<p align="center">
  <img src="/figures/final_robot.jpg" style="height:400px;"/>
  <img src="/figures/robot_and_me.jpg" style="height:400px;"/>
</p>
<p align="center">
  <img src="/figures/internal.jpg" style="width:250px;"/>
</p>
