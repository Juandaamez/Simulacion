class Task:

    def __init__(self, machine, task_time):
        """Default constructor

        Args:
            id (string): Work identifier
            task(list): Task List.
        """
        self._machine = machine
        self._task_time = task_time
        self._count_down = task_time
        self._completed = False

    def __str__(self):
        """Machine output

        Returns:
            String: Work data output
        """
        output = f"Machine: {self._machine._id} "
        output += f" Task Time: {self._task_time} "
        output += f" Count Down: {self._count_down} "
        output += f" Completed: {self._completed} "
        return output
        
