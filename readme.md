# Python Script for BIT-Web Auto Connection
<br><br>
This is a python-implemented script for auto connecting to BIT-Web. If you find it helpful, please click **star** for me.
BIT-Web refers to the CN of Beijing Institute of Technology named "BIT-Web"

**Note**: The current script only works in Ubuntu. Another version for Windows is under construction.  

## Prerequisites
- Ubuntu LTS with native FireFox installed
- Python 3.x


## Getting Started
### Installation

- Clone this repo:
```bash
git clone https://github.com/MillenniumFalcon1097/auto_BIT_WEB.git
cd pytorch-CycleGAN-and-pix2pix
```
- Install [Geckodriver](https://github.com/mozilla/geckodriver/releases) | which is used to drive the browser and simulate mouse action. (I assume you already have Firefox installed on your system.)
- Install Selenium:
  - **(Recommend)** For pip users, please type the command `sudo pip install selenium`.
  - For Conda users, you can create a new Conda environment and then install via `conda install selenium`.

### Config your own data  
By opening `config.ini` you can manage your own setting.
  - `STU_ID` refers to your student ID.
  - `PASSWD` refers to your account password.
  - `INTERVAL` in seconds, which stands for the interval between times you want the script to execute. 
  - `PROJ_DIR` the project folder where you put in.
  - `PYTHON_DIR` the python interpreter path you want to execute the script (if you have multiple python interperters, be careful to choose the proper one.)
  - `LOG` the log file path.

### We Need Automatic !
- Just run the script below in bash
```bash
python main.py
```
- You can monitor script execution via log file.
