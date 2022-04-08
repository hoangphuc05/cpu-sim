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
        self.finish_time = 0

    def __str__(self) -> str:
        return "PID: {}, throughput time: {}, wait time: {}, context switching count: {}".format(self.PID, self.finish_time - self.arrival_time, self.accumulated_wait_time, self.accumulated_context_switch)
    
    def print(self) -> None:
        print("PID: {}, throughput time: {}, wait time: {}, context switching count: {}".format(self.PID, self.finish_time - self.arrival_time, self.accumulated_wait_time, self.accumulated_context_switch))

    def out_csv_line(self) -> str:
        return "{},{},{},{},{},{}".format(self.PID, self.finish_time - self.arrival_time, self.accumulated_wait_time, self.accumulated_context_switch, self.accumulated_CPU_time, self.accumulated_IO_time)