# llSPS-INT-846-Smart-Agriculture-system-based-on-IoT
## Smart Agriculture system based on IoT

This system allows the user (Farmer) to analyse the data collected from the sensors on his/her farm and access the data from anywhere in the world using IBM Cloud services and also get Real-time weather data of the fram location. The motors can be controlled directly from the web UI thus allowing the farmer to take care of the farm from anywhere at anytime provided an internet connection. 

## Dashboard
The collected data is simulated from [IBM IoT Senor](https://watson-iot-sensor-simulator.mybluemix.net/) and the weather data is collected from [OpenWeather's Api](http://api.openweathermap.org/data/2.5/weather?q=Mumbai&units=metric&appid=577a1cbdcb2a11d51cc74f5f5962791a). The UI of the Dashboard is shown below:

![](https://github.com/SmartPracticeschool/llSPS-INT-846-Smart-Agriculture-system-based-on-IoT/blob/master/Images/Dashboard(tab1).PNG)

## Controls
The water-motor can be controlled through the following UI:
![](https://github.com/SmartPracticeschool/llSPS-INT-846-Smart-Agriculture-system-based-on-IoT/blob/master/Images/Controls(tab2).PNG)

## Node-Red Program Flow
The .json file can be accessed [here](https://github.com/SmartPracticeschool/llSPS-INT-846-Smart-Agriculture-system-based-on-IoT/blob/master/NodeRed_ProjectFlow.json).
The flow is as shown:
![](https://github.com/SmartPracticeschool/llSPS-INT-846-Smart-Agriculture-system-based-on-IoT/blob/master/Images/Flow.PNG)

## Python IDE
The commands through the NodeRed Dashboard are sent to the cloud and are read by a Python script running locally to read the command and then take appropriate actions via actuators. The python code for the same is available [here](https://github.com/SmartPracticeschool/llSPS-INT-846-Smart-Agriculture-system-based-on-IoT/blob/master/IBMWatson_Code_for%20_Data_Reception.py). The command read by the IDE is shown below:
![](https://github.com/SmartPracticeschool/llSPS-INT-846-Smart-Agriculture-system-based-on-IoT/blob/master/Images/PythonIDE.jpg)

