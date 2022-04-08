
from typing import List, Tuple
from PCB import PCB
from clock import Clock
from CPU import CPU
from custom_queue import FCFS, SPN

CPU_count = 1

# List of process ready to be dispatched, dispatch based on the arrival time
dispatch_queue:List[PCB] = []

# Ready queue
ready_queue:List[PCB] = []

# FCFS queue, first come first serve
FCFS_queue = FCFS()

# Event queue, storing all process finish waiting for IO
event_queue = SPN()

# IO queue, storing all process waiting for IO
IO_queue:List[PCB] = []

finished_queue:List[PCB] = []

# function to read data from file
def read_data(filename: str) -> List[PCB]:
    with open(filename, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split(",") for line in lines]
        lines = [[int(i) for i in line] for line in lines]
        lines = [PCB(line[0], line[1], line[2:]) for line in lines]
        return lines

def is_cpu_idle(CPU_list: List[CPU]) -> bool:
    for cpu in CPU_list:
        if cpu.state == "busy":
            return False
    return True

# read data from file and add to dispatch queue
dispatch_queue = read_data("data/data_long.csv")
process_count = len(dispatch_queue)

# create clock
clock = Clock()

# create CPU
main_CPU = []
for i in range(CPU_count):
    main_CPU.append(CPU())

while clock.time < 150 or len(ready_queue) > 0 or len(IO_queue) > 0 or event_queue.len() > 0 or not is_cpu_idle(main_CPU):
    # tick
    clock.tick()


    # dispatch process
    to_delete = []
    for i in range(len(dispatch_queue)):
        if dispatch_queue[i].arrival_time == clock.time:
            ready_queue.append(dispatch_queue[i])
            to_delete.append(i)

    # for i in range(len(dispatch_queue)):
    #     if dispatch_queue[i].arrival_time == clock.time:
    #         ready_queue.pop(i)


    # CPU process from fcfs queue
    for i in range(CPU_count):
        if main_CPU[i].state == "idle":
            if FCFS_queue.len() > 0:
                main_CPU[i].state = "busy"
                # main_CPU[i].current_process = ready_queue.pop(0)
                main_CPU[i].current_process = FCFS_queue.pop()
                main_CPU[i].start_time = clock.time
            else:
                continue
        else:
            if main_CPU[i].current_process.remaining_task[0] == 0:
                main_CPU[i].state = "idle"
                main_CPU[i].current_process.CPU_time = clock.time - main_CPU[i].start_time
                main_CPU[i].current_process.accumulated_CPU_time += main_CPU[i].current_process.CPU_time
                
                # remove the current task 
                main_CPU[i].current_process.remaining_task.pop(0)

                # check if process is waiting for IO
                if len(main_CPU[i].current_process.remaining_task) > 0:
                    main_CPU[i].current_process.state = "waiting"
                    main_CPU[i].current_process.accumulated_context_switch += 1
                    main_CPU[i].current_process.current_start_time = clock.time
                    IO_queue.append(main_CPU[i].current_process)
                    main_CPU[i].current_process = None
                else:
                    main_CPU[i].current_process.state = "finished"
                    finished_queue.append(main_CPU[i].current_process)
                    main_CPU[i].current_process = None
            else:
                main_CPU[i].current_process.remaining_task[0] -= 1

    # IO process
    IO_remove = []
    for i in range(len(IO_queue)):
        if IO_queue[i].remaining_task[0] == 0: # io is finished
            IO_queue[i].IO_time = clock.time - IO_queue[i].current_start_time
            IO_queue[i].accumulated_IO_time += IO_queue[i].IO_time

            # remove the current task
            IO_queue[i].remaining_task.pop(0)

            # mark process to be remove from IO
            IO_remove.append(i)

            # check if process need to be executed again
            if len(IO_queue[i].remaining_task) > 0:
                IO_queue[i].state = "waiting"
                IO_queue[i].accumulated_context_switch += 1
                event_queue.append(IO_queue[i])
            else:
                IO_queue[i].state = "finished"
                finished_queue.append(IO_queue[i])

        else:
            IO_queue[i].remaining_task[0] -= 1

    # remove finished process from IO queue
    IO_remove.reverse()
    for i in IO_remove:
        IO_queue.pop(i)


    # move 1 element from the event queue to the fcfs queue
    FCFS_queue.append(event_queue.pop())



print("a")


