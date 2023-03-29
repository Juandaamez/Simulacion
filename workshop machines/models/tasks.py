from models.task import Task


class Tasks():
    """Task collection class.
    """ 

    def __init__(self):
        """
        Task collection default constructor.
        """
        self._tasks = []

    def add(self, machine, task_ids):
        for i in range(len(machine)):
            task = Task(machine[i], task_ids[i])
            self._tasks.append(task)

    def get_task(self, machine):
        """_summary_

        Args:
            machine (_type_): _description_

        Returns:
            _type_: _description_
        """
        for task in self._tasks:
            if task._machine._id == machine._id:
                return task
        return None
        
    def __str__(self):
        output = 'Tasks: \n['
        for task in self._tasks:
            output += ' ' + task.__str__() + ' '
        return output + ']'