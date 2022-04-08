
from PCB import PCB

class FCFS:
    def __init__(self):
        self.queue = []

    def append(self, pcb: PCB):
        self.queue.append(pcb)

    def pop(self) -> PCB:
        return self.queue.pop(0)
    
    def len(self) -> int:
        return len(self.queue)
    
    def update_wait(self):
        for pcb in self.queue:
            pcb.accumulated_wait_time += 1

class SPN:
    def __init__(self):
        self.queue = []

    def append(self, pcb: PCB):
        self.queue.append(pcb)

    def pop(self) -> PCB:
        # find the shortest process
        shortest = self.queue[0]
        for pcb in self.queue:
            if pcb.remaining_task[0] < shortest.remaining_task[0]:
                shortest = pcb
        return self.queue.pop(self.queue.index(shortest))
    
    def len(self) -> int:
        return len(self.queue)

    def update_wait(self):
        for pcb in self.queue:
            pcb.accumulated_wait_time += 1

class FinishedQueue:
    def __init__(self):
        self.queue = []

    def append(self, pcb: PCB, clock):
        pcb.finish_time = clock.time
        self.queue.append(pcb)

    def pop(self) -> PCB:
        return self.queue.pop(0)
    
    def len(self) -> int:
        return len(self.queue)

    def get_queue(self):
        return self.queue
