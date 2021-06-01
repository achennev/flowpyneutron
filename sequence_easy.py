from flowpyneutron import Experiment

exp = Experiment('example.log', port='/dev/ttyUSB0', baudrate=115200)

#  mon premier cycle

exp.startCyle('first loop', 1, 15, 2, init_move='pull')

# exp.startCyle('second loop', 5, 15, 2, init_move='pull')