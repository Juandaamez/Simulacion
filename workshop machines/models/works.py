from models.tasks import Tasks
from models.work import Work

class Works():
    """Work class.
    """ 

    def __init__(self):
        """
        Work collection default constructor.
        """
        self._works = list()

    def add(self, works_ids):
        for id in works_ids:
            work = Work(id)
            self._works.append(work)

    def add_tasks(self, machines, task_ids):
        for work in self._works:
            tasks = Tasks()
            tasks.add(machines, task_ids[work._id])
            work._tasks = tasks

    def __str__(self):
        """Report of the works class.

        Returns:
            string: The class report.
        """
        output = 'Works: ['
        for work in self._works:
            output += ' ' + work.__str__() + ' '
        return output + ']'