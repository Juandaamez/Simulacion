class Work:

    def __init__(self, id):
        """Work constructor

        Args:
            id (string): Work identifier
        """
        self._id = id
        self._tasks = None 
        self._status = False

    def __str__(self):
        """Machine output

        Returns:
            String: Work data output
        """
        output = f"Work id: {self._id}\n"
        output += f"Tasks: {self._tasks}\n"
        output += f"Status: {self._status}\n"
        return output