import flowpyneutron as fl
import logging
import time

logfile = 'example.log'
volume = 20
rate = 15
n_cylce = 2
init_move = 'pull'


# init log file
logging.basicConfig(filename=logfile, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

# declare the pump
pump = fl.Connection('/dev/ttyUSB0', 115200, verbose=False)
time.sleep(1)
# open serial port
pump.openConnection()
logging.info('Start connection')
time.sleep(1)
# set syringe diameter
pump.setDiameter(28.6)

pump.setVolume(volume)
if init_move == 'pull':
    pump.setRate(-1*rate)
elif init_move == 'push':
    pump.setRate(rate)
else:
    raise Exception('wrong init move : push or pull')

for i in range(n_cylce-1):
# set the volume rate and the volume to be dispensed (mL)
# negative volume correspond to pulling and positive volume to pushing
pump.setVolume(10)
pump.setRate(20)

# start the pump
pump.startPump()
logging.info('Start pump at %.4f mL/min' % 10)
status = pump.getPumpStatus()[0]
while status == 'pump status\r1':
    time.sleep(1)
    status = pump.getPumpStatus()[0]
print('First step done')
logging.info('First step done')

 # second step
pump.setVolume(10)
pump.setRate(-20)

# start the pump
pump.startPump()
status = pump.getPumpStatus()[0]
while status == 'pump status\r1':
    time.sleep(1)
    status = pump.getPumpStatus()[0]
print('Last step done')

