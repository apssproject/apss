# **COMMAND LINE INTERFACE**
#### **Usage:**
``` bash
apss <option> [--help] [--version] [--license]
```

#### **Where [option] include:**
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
    - **(board)** Is the model of the board where you want to load the apss framework (arduino2560, stm32nucleoHJF43, ecc).
    - **(port)** Is the link to the port where the board is actually connected (/dev/ACM0, /dev/ACM1, ecc).
  - Optional arguments
    - **[--version]** By default is _latest_ but you can specify one (--version=1.21.b1).

- _--list-outputs_ **[--filter] [--output]**
  - Optional arguments
    - **[--filter]** You can specify a filter to your search such as the date, the dimension of the measuring etc. A complete list of the option is following:
      - date=dd/mm/yy
      - dimension=30mq/20mb
      - sensors=co2,dht
      **Example of syntax**
      ``` bash
      ╭─user@user-linux /home/user ‹system›
      ╰─$ apss --list-outputs --filter=03/01/2020,Co2          
      ```          
    - **[--output]** By default is _none_ but you can specify a file's path of 'console' for cli output.

#### **Example of activation by command line:**
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
