import sys
import ibmiotf.device

organization = "1k2xrj"
deviceType = "Data"
deviceId = "1234"
authMethod = "token"
authToken = "123456789"

def commandHandler(cmd):
    print("Command received: %s" % cmd.data)

    for key in cmd.data.keys():
        if key == 'motor':
            if cmd.data['motor'] == 'ON':
                print("MOTOR is turned ON")

            elif cmd.data['motor'] == 'OFF':
                print("MOTOR is turned OFF")

try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod,
                     "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

deviceCli.connect()

while True:
    deviceCli.commandCallback = commandHandler
