from time import sleep

from models.machines import Machines
from models.works import Works

#Juan David Amezquita Nuñez

class Simulator:
    def __init__(self):
        self._machines = None
        self._works = None
        self._clock = 0

    def initialize(self, machine_ids, work_ids, task_ids):
        self._machines = Machines()
        self._machines.add(machine_ids)

        self._works = Works()
        self._works.add(work_ids)

        self._works.add_tasks(self._machines._machines, task_ids)

    def update_clock(self):
        self._clock += 1
        sleep(1)
        print(f"Clock: {self._clock}")

    def simulation_end(self):
        for work in self._works._works:
            if not work._status:
                return False
        return True
    
    def is_processing(self, work):
        for machine in self._machines._machines:
            if not machine._available:
                if machine._current_work._id == work._id:
                   return True
        return False
    
    def choose_work(self, machine):
        for work in self._works._works:
            if not work._status and not self.is_processing(work): 
               task = work._tasks.get_task(machine)
               if task is not None:
                   return work, task
        return None, None
    
    def assign_works(self):
        for machine in self._machines._machines:
            if machine._available:
                work, task = self.choose_work(machine)
                machine.process(work, task)
                print(f"The work {work._id}, task {task._task_time} was assigned to machine {machine._id}. ")

    def show_status(self):
        print(self._machines)

    def update_count_downs(self):
        for machine in self._machines._machines:
            #Deseaba saber como hacer para que cuando el contador llegue a 0
            #status, available y completed se conviertieran en true para asi
            #poder nuevamente encontrar un nuevo trabajo para la maquina que se vaya desocupando.
            if machine._count_down == 0:
            #    for work in self._works._works:
            #        work._status = True
            #    for machine in self._machines._machines:
            #        machine._available = True

                for task in self._task._task:
                    if machine._id == task._machine._id:
                        task._completed = True
                        machine._available = True
            
            if not machine._available:
                machine._count_down -= 1
                for task in machine._current_work._tasks._tasks:
                    task._count_down -= 1

    def run(self):
        while not self.simulation_end():
            self.assign_works()
            #self.update_events()
            self.update_clock()
            self.show_status()
            self.update_count_downs()
            
