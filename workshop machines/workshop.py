from controllers.simulator import Simulator

#Juan David Amezquita Nuñez

if __name__ == "__main__":
    machine_list = ['A', 'B']
    work_list    = ['W1', 'W2', 'W3', 'W4', 'W5']
    task_list    = {
        'W1': [30,50],
        'W2': [ 0,40],
        'W3': [20,70],
        'W4': [30, 0],
        'W5': [50,20]
    }

    simulator = Simulator()
    simulator.initialize(machine_list, work_list, task_list)
    simulator.run()