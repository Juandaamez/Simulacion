class Machine:

    def __init__(self, id):
        """Machine constructor

        Args:
            id (string): machine identifier
        """
        self._id = id
        self._available = True
        self._current_work = None
        self._count_down = 0

    def process(self, work, task):
        self._available = False
        self._current_work = work
        self._count_down = task._count_down

    def __str__(self):
        """Machine output

        Returns:
            String: Machine data output
        """
        output = f"Machine: [id: {self._id}, "
        output += f" Available: {self._available}, "
        output += f" Current work: {self._current_work._id}, "
        output += f" Count down: {self._current_work}]"
        return output