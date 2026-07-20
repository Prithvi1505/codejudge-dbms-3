import heapq

class Process:
    def __init__(self, pid, arrival, burst, priority=0):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.remaining = burst
        self.waiting = 0
        self.turnaround = 0

def fcfs(processes):
    processes = sorted(processes, key=lambda p: p.arrival)
    time = 0
    for p in processes:
        if time < p.arrival:
            time = p.arrival
        p.waiting = time - p.arrival
        time += p.burst
        p.turnaround = time - p.arrival
    return processes

def sjf(processes):
    processes = sorted(processes, key=lambda p: p.arrival)
    time = 0
    ready = []
    completed = []
    i = 0
    while len(completed) < len(processes):
        while i < len(processes) and processes[i].arrival <= time:
            heapq.heappush(ready, (processes[i].burst, processes[i].pid, processes[i]))
            i += 1
        if ready:
            _, _, p = heapq.heappop(ready)
            if time < p.arrival:
                time = p.arrival
            p.waiting = time - p.arrival
            time += p.burst
            p.turnaround = time - p.arrival
            completed.append(p)
        else:
            time += 1
    return completed

# Run simulator with sample data
processes = [
    Process(1, 0, 8),
    Process(2, 1, 4),
    Process(3, 2, 9),
    Process(4, 3, 5),
    Process(5, 4, 2)
]

print("FCFS Results:")
fcfs_results = fcfs(processes[:])
for p in fcfs_results:
    print(f"P{p.pid}: Wait={p.waiting}, Turnaround={p.turnaround}")
