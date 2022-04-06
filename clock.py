from typing import List, Tuple

class Clock:
    def __init__(self) -> None:
        self.time = 0

    def tick(self) -> None:
        self.time += 1