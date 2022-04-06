from typing import List, Tuple

class CPU:
    def __init__(self) -> None:
        self.state = "idle"
        self.current_process = None
        self.start_time = 0
        self.accumulated_busy_time = 0
        self.accumulated_idle_time = 0

    def update_stat(self):
        if self.state == "idle":
            self.accumulated_idle_time += 1
        else:
            self.accumulated_busy_time += 1