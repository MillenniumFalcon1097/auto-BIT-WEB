# Python Script for BIT-Web Auto Connection
<br><br>
[![wakatime](https://wakatime.com/badge/github/MillenniumFalcon1097/auto_BIT_WEB.svg)](https://wakatime.com/badge/github/MillenniumFalcon1097/auto_BIT_WEB)  
This is a python-implemented script for automatically connecting to BIT-Web. If you find this repo helpful, please click **star** for me.
BIT-Web refers to the CN of Beijing Institute of Technology named "BIT-Web"

**Note**: The current script only works in Ubuntu. Another version for Windows is under construction.  

## Prerequisites
- Ubuntu LTS with native FireFox Browser installed
- Python 3.x


## Getting Started
### Installation

- Clone this repo:
```bash
git clone https://github.com/MillenniumFalcon1097/auto_BIT_WEB.git
cd auto_BIT_WEB
```
- Install [Geckodriver](https://github.com/mozilla/geckodriver/releases):  
   - Geckodriver is used to drive the browser and simulate mouse action. (I assume you already have Firefox installed on your system.)
  - After extraction, move the file to `/usr/bin`.
  - Then ` sudo gedit /etc/profile`, add the following line to the end of the file:
  `export PATH="$PATH: /opt/firefox:/usr/bin"`
- Install Selenium:
  - **(Recommend)** For pip users, please type the command `sudo pip install selenium`.
  - For Conda users, you can create a new Conda environment and then install via `conda install selenium`.

### Config your own data  
By opening `config.ini` you can manage your own setting.
  - `STU_ID` refers to your student ID, eg: 1122334455.
  - `PASSWD` refers to your account password, eg: passcode123.
  - `INTERVAL` in seconds, which stands for the interval between times you want the script to execute. 
  - `PROJ_DIR` the project folder where you put in.
  - `PYTHON_DIR` the python interpreter path you want to execute the script (if you have multiple python interperters, be careful to choose the proper one.)
  - `LOG` the log file path.

### We Need Automatic !
- Just run the script below in bash (or in your conda env)
```bash
python main.py
```
- You can monitor script execution via log file.
