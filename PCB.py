from typing import List, Tuple

class PCB:
    def __init__(self, PID: int, arrival_time: int, remaining_task: List) -> None:
        self.PID = PID
        self.state = "ready"
        self.arrival_time = arrival_time
        self.CPU_time = 0
        self.IO_time = 0
        self.accumulated_CPU_time = 0
        self.accumulated_IO_time = 0
        self.accumulated_context_switch = 0
        self.remaining_task = remaining_task
        self.current_start_time = 0

        self.accumulated_wait_time = 0

    def __str__(self) -> str:
        print("Wait time: " + str(self.accumulated_wait_time))
        return "PID: {}, arrival_time: {},state: {}, CPU_time: {}, IO_time: {}, accumulated_CPU_time: {}, accumulated_IO_time: {}, remaining_task: {}".format(self.PID, self.arrival_time, self.state, self.CPU_time, self.IO_time, self.accumulated_CPU_time, self.accumulated_IO_time, self.remaining_task)
