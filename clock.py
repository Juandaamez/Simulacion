import time

class Simulator:

    def __init__(self, timeout, delay):
        """_summary_

        Args:
            timeout (_type_): _description_
            delay (_type_): _description_
        """
        _clock   = 60
        _timeout = timeout
        _delay   = delay


while simulation_clock <= simulation_timeout:
    print(f"Clock:{simulation_clock} secs.")
    simulation_clock += 1
    time.sleep(simulation_delay)