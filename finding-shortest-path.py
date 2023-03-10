from queue import PriorityQueue

# Buat graf node/kota dan edge beserta cost
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 9, 'E': 2},
    'C': {'F': 4},
    'D': {'G': 1},
    'E': {'H': 7},
    'F': {'I': 3},
    'G': {'J': 1},
    'H': {'J': 2},
    'I': {'J': 3},
    'J': {}
}

# Tentukan start dan goal
start = 'A'
goal = 'J'

# Generate SLD setiap node ke goal
sld = {
    'A': 8,
    'B': 4,
    'C': 10,
    'D': 5,
    'E': 7,
    'F': 6,
    'G': 2,
    'H': 2,
    'I': 3,
    'J': 0
}

# Fungsi untuk menjalankan algoritma A*
def Astar(graph, start, goal, sld):
    # Inisialisasi nilai awal
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    # Lakukan loop sampai goal ditemukan
    while not frontier.empty():
        current = frontier.get()[1]
        
        # Jika sudah sampai di goal, selesai
        if current == goal:
            break
        
        # Cari semua node yang terhubung
        for neighbor in graph[current]:
            # Hitung total cost dari start ke node tetangga
            new_cost = cost_so_far[current] + graph[current][neighbor]
            # Jika node belum pernah dikunjungi atau cost ke node tetangga lebih rendah dari cost yang sudah ada
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + sld[neighbor]  # Hitung nilai priority
                frontier.put((priority, neighbor))
                came_from[neighbor] = current
    
    # Bangun path dari start ke goal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    
    return path, cost_so_far[goal]

# Jalankan algoritma A*
path, cost = Astar(graph, start, goal, sld)

# Tampilkan hasil
print("Jalur terpendek dari", start, "ke", goal, "adalah:", path)
print("Dengan total biaya:", cost)
