import threading

counter = 0
lock = threading.Lock()
barrier = threading.Barrier(2)

def unsafe_increment():
    global counter
    for _ in range(100000):
        local = counter
        barrier.wait()  # Force collision
        counter = local + 1

# Run unsafe version first (will show wrong result)
t1 = threading.Thread(target=unsafe_increment)
t2 = threading.Thread(target=unsafe_increment)
t1.start(); t2.start(); t1.join(); t2.join()
print("Unsafe final counter:", counter)  # Will be ~100000 instead of 200000

# Fixed version with Lock
counter = 0
def safe_increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

t1 = threading.Thread(target=safe_increment)
t2 = threading.Thread(target=safe_increment)
t1.start(); t2.start(); t1.join(); t2.join()
print("Safe final counter:", counter)  # 200000
