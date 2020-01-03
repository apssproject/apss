# **CORE**
#### **MAIN CORE FUNCTION**
- _runAllSensors()_
- _runWithSensors(**args)_
- _stopAllSensors()_
- _stopSensors(**args)_
- _sensorsList()_

#### **MAIN PROGRAM FUNCTION**
- _commandListener()_
- _hardware_

### **COMMAND LINE COMMAND OPTIONS**
- _--run-all-sensors_ **[--output] [--time]**
  - Where
   - **[--output]** is 'output.apss' in ~/.apss dir by default.
   - **[--time]** is 60000 ms by default.

- _--run-sensors_ **(sensors) [--output] [--time]**
  - Where
   - **(sensors)** must be specified.
   - **[--output]** is 'output.apss' in ~/.apss dir by default.
   - **[--time]** is 60000 ms by default.

- _--load-firmware_ **(board) (port) [--version]**
  - Positional arguments
    - **(board)** Board is the model of the board where you want to load the apss framework (arduino2560, stm32nucleoHJF43, ecc).
    - **(port)** Port is the link to the port where the board is actually connected (/dev/ACM0, /dev/ACM1, ecc).
  - Optional arguments
    - **[--output]** Version by default is _latest_ but you can specify one (--version=1.21.b1).

**Example of activation by command line:**
``` bash
╭─user@user-linux /home/user ‹system›
╰─$ apss --run-all-sensor
[apss] Starting all sensors:
[apss] Sensors founded:
[apss]  - Humidity
[apss]  - Co2
[apss] Confirm? Y/n
[apss] Starting measuring.. [#########......76%]

```
