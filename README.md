![image](https://avatars1.githubusercontent.com/u/57671915?s=200&v=4)
# **APSS**
### **Air Pollution Scanning System**
![language](https://img.shields.io/badge/lang-Python-blue?style=flat-square)
![language](https://img.shields.io/badge/lang-bash-green?style=flat-square)
![license](https://img.shields.io/badge/license-GPLv3-yellow?style=flat-square)
![version](https://img.shields.io/badge/version-v1.0.beta1-green?style=flat-square)
![repo size](https://img.shields.io/github/repo-size/apssproject/apss.svg?style=flat-square)

![contributors](https://img.shields.io/github/contributors/apssproject/apss.svg?style=flat-square)
![last commit](https://img.shields.io/github/last-commit/apssproject/apss.svg?style=flat-square)
![commit activity](https://img.shields.io/github/commit-activity/y/apssproject/apss.svg?style=flat-square)

![twitter](https://img.shields.io/twitter/follow/apss?label=Follow&style=social)

## **Description**
The APSS board is a configuration of a microcontroller such as the Arduino Mega2560 configured with a series of sensors for measuring environmental values such as C02, humidity, electromagnetic waves, etc..
The board can also be equipped with a mini liquid crystal display, an SD module to be used in standalone mode storing data inside, and bluetooth/wifi modules for remote communication with a PC.
The APSS framework loaded on the card takes care of interfacing all compatible sensors connected to each other through a common interface compatible with all sensor configurations.

Its website can be found at [a-pss.it](https://a-pss.it).

The board can take measurements in various ways:
### **Free mode**
In this mode we physically move the board for the area we want to measure. The free mode in turn includes two different modes: automatic and manual. In automatic mode the board will make a measurement every few seconds according to the user's input, in manual mode, the board must be equipped with a button that the user must press each time he wants to perform the measurement.

### **Aero mode**
In this mode the board will have to be equipped with a movement support such as a compatible drone, and we will determine which path the board will have to take to measure the affected area. The accuracy of the measurement must also be specified, i.e. every how many seconds the board must take the measurement. The fewer the seconds, the more accurate the measurement will be.

### **User's inputs**
- **Free mode**
  - **Auto**
    - Time of measurement (seconds)
    - Precision of measurement (seconds)
  - **Manual**
    - Time of measurement (seconds)
- **Aero mode**
  - Time of measurement (seconds)
  - Precision of measurement (seconds)
  - Movement path

## **Data transmission modality**
data transmission from the board to the computer can be done using bluetooth/wifi technology (assuming the board is equipped with compatible sensors) or via serial cable, or during or at the end of the measurement. Alternatively, if the board is equipped with an SD module, it can store the measurements inside it to be imported into APSS manager later.
