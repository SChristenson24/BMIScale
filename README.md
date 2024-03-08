# How to Run:
### BMI Scale Python CLI Application

## 1. Downloading Application
There are a couple of ways to download this application:
### Using GitHub Desktop
- Make sure to have GitHub Desktop and Visual Studio Code installed on your machine
- Navigate to the green "<> Code" dropdown menu within this repository.
- Click "Open with GitHub Desktop", which will take you to GitHub Desktop
- Set the local path to where you want the application
- Then click "Open with Visual Studio Code'

### Using Git Commands
- Navigate to your terminal
- Navigate to where you wish to clone the repository to
  ```
  cd /your/file/path/to/code/here
  ```
- Once you are in the file location you'd like the to clone to, use this command
  ```
  git clone https://github.com/SChristenson24/BMIScale.git)https://github.com/SChristenson24/BMIScale.git
  ```

## 2. Running the application
### Python Installation
Within the two files, you will have one that contains the calcBMI() function, __bmi.py__, and one that contains the tests, __test_bmi.py__. To run these files, **you must have python installed**.

To check if you have Python installed, run the version command:
```
python --version
```
or
```
python3 --version
```
If you do no get an output with the python version, you will need to install python and pip.

### Files
If you would like to only use the scale, run __bmi.py__ using the command (in your choice of editor terminal):

```
python bmi.py
```
or
```
python3 bmi.py
```

If you would like to use the scale along with the tests, run __test_bmi.py__ using the command:

```
python3 -m unittest test_bmi.py
```

### Execution
Both of the files take in the same inputs. First you will be prompted to input your height. The first input should be your height in feet, then after your height in inches (not total inches, refer to the example below).
After your height, you will input your weight in pounds. These are the only inputs you will need to provide. Now, the output will depend on what files you run. If you run __bmi.py__, you will get an output showing the 
BMI and what category you fall into. If you run __test_bmi.py__, you will also get your BMI and category, but also the results of the tests. 

### Example Input & Output
Let's say I am 5 foot 2 inches and weight 120 pounds

__bmi.py__

Input:
```
Please provide your height in feet (Ex. if 5' 3'', input 5)
5
Please provide your height in inches (Ex. if 5' 3'', input 3)
2

Please provide your weight in lbs: 
120
```

Output:
```
BMI: 21.9

Normal weight
```

__test_bmi.py__

Input:
```
Please provide your height in feet (Ex. if 5' 3'', input 5)
5
Please provide your height in inches (Ex. if 5' 3'', input 3)
2

Please provide your weight in lbs: 
120
```

Output:
```
BMI: 21.9

Normal weight

..
BMI: 18.514150494967655
.
BMI: 24.998009107129324
.
BMI: 30.01714062317013
.
BMI: 25.01753880174427
.
BMI: 29.997610928555186
.
BMI: 18.49462080035271
.
----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```
