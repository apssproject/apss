# **APSS board core documentation**

The APSS board is a configuration of a microcontroller such as the Arduino Mega2560 configured with a series of sensors for measuring environmental values such as C02, humidity, electromagnetic waves, etc..
The board can also be equipped with a mini liquid crystal display, an SD module to be used in standalone mode storing data inside, and bluetooth/wifi modules for remote communication with a PC.
The APSS framework loaded on the card takes care of interfacing all compatible sensors connected to each other through a common interface compatible with all sensor configurations.

The framework for the apss board consists of a common interface for various types of sensors and modules, to be used to make measurements.
Before loading the framework on the board, the user must manually enter in a configuration file which modules he wants to use and in which pins they are connected.
