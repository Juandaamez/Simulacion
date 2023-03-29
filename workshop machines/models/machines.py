from models.machine import Machine


class Machines:
    def __init__(self):
        self._machines = list()

    def add(self, machines):
        for id in machines:
            machine = Machine(id)
            self._machines.append(machine)

    def __str__(self):
        output = "[Machines: \n["
        for machine in self._machines:
            output += machine.__str__() + ' '
        return output + ']'