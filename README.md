## Nama : Nadya Zuhria Amana
## NRP : 5025211058
## Kelas : Kecerdasan Buatan F

### Tugas 1. Finding Shortest menggunakan Algoritma A*
- Fungsi `Astar(graph, start, goal, sld)`: Fungsi ini merupakan implementasi algoritma A* yang mencari jalur terpendek dari titik awal (`start`) ke titik tujuan (`goal`) dalam graf (`graph`) dengan mempertimbangkan estimasi jarak (`sld`) dari setiap node ke goal. Fungsi ini mengembalikan jalur terpendek dan total biaya yang ditemukan.
```
def Astar(graph, start, goal, sld):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()[1]
        
        if current == goal:
            break
        
        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + graph[current][neighbor]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + sld[neighbor]
                frontier.put((priority, neighbor))
                came_from[neighbor] = current
    
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    
    return path, cost_so_far[goal]

```

- Fungsi `PriorityQueue()`: Ini adalah kelas dari modul `queue` yang digunakan untuk mengimplementasikan antrian dengan prioritas. Antrian ini digunakan untuk menyimpan node yang akan dieksplorasi berdasarkan nilai prioritasnya dalam algoritma A*.
```
from queue import PriorityQueue
```

- Fungsi `frontier.put((priority, node))`: Metode ini digunakan untuk menambahkan elemen ke dalam antrian `frontier`. Dalam hal ini, pasangan `(priority, node)` ditambahkan ke antrian dengan prioritas yang ditentukan oleh `priority`.
```
frontier.put((priority, node))
```

- Fungsi `frontier.get()`: Metode ini digunakan untuk mengambil dan menghapus elemen dengan prioritas tertinggi dari antrian `frontier`. Dalam hal ini, elemen tersebut merupakan pasangan `(priority, node)`.
```
current = frontier.get()[1]
```

- Fungsi `came_from[node]`: Ini adalah dictionary yang menyimpan informasi tentang node mana yang telah dikunjungi sebelumnya saat menjelajahi graf. Digunakan untuk melacak jalur yang ditempuh dari start ke goal.
```
came_from[node] = current
```

- Fungsi `cost_so_far[node]`: Ini adalah dictionary yang menyimpan informasi tentang biaya terkecil yang telah ditemukan untuk mencapai setiap node saat menjelajahi graf. Digunakan untuk memperbarui biaya terkecil saat menemukan jalur yang lebih baik.
```
cost_so_far[neighbor] = new_cost
```

- Fungsi `path.append(node)`: Metode ini digunakan untuk menambahkan node ke dalam jalur yang sedang dibangun saat membangun jalur dari goal ke start setelah algoritma A* selesai.
```
path.append(current)
```

- Fungsi `path.reverse()`: Metode ini digunakan untuk membalikkan urutan elemen dalam jalur sehingga menghasilkan jalur terpendek dari start ke goal.
```
path.reverse()
```

- Fungsi `print("Jalur terpendek dari", start, "ke", goal, "adalah:", path)`: Baris ini mencetak jalur terpendek dari start ke goal ke output dengan menggunakan `print()`. Variabel `start`, `goal`, dan `path` adalah argumen yang digunakan untuk membangun pesan yang akan dicetak.
```
print("Jalur terpendek dari", start, "ke", goal, "adalah:", path)
```

- Fungsi `print("Dengan total biaya:", cost)`: Baris ini mencetak total biaya dari jalur terpendek ke output menggunakan `print()`. Variabel `cost` adalah argumen yang digunakan untuk membangun pesan yang akan dicetak.
```
print("Dengan total biaya:", cost)
```
![Ouput_Tugas1_FindingShortestPath](URL_gambar)

### Tugas 2. TSP with Genetic Algorithm
- `import random`: Pernyataan ini mengimpor modul `random` yang digunakan untuk menghasilkan angka acak dalam algoritma genetika.

- Fungsi `fitness(individual, distance_matrix)`: Fungsi ini menghitung fitness (jarak total) dari individu dalam populasi. Setiap individu direpresentasikan sebagai urutan kota yang dikunjungi. Fungsi ini mengiterasi melalui setiap kota dalam urutan individu dan menjumlahkan jarak antara kota tersebut dan kota berikutnya berdasarkan matriks jarak (`distance_matrix`). Fungsi ini mengembalikan total jarak.
```
def fitness(individual, distance_matrix):
    total_distance = 0
    for i in range(len(individual)-1):
        total_distance += distance_matrix[individual[i]][individual[i+1]]
    total_distance += distance_matrix[individual[-1]][individual[0]]
    return total_distance

```

- Fungsi `selection(population, elite_size)`: Fungsi ini melakukan seleksi individu-individu terbaik dari populasi berdasarkan nilai fitness mereka. Populasi diurutkan berdasarkan nilai fitness menggunakan fungsi `fitness()`. Sejumlah individu terbaik (disebut elit) dipertahankan dalam seleksi, sementara individu lainnya dipilih secara acak dari populasi. Fungsi ini mengembalikan populasi yang terpilih.
```
def selection(population, elite_size):
    fitness_scores = [(fitness(individual, distance_matrix), individual) for individual in population]
    fitness_scores.sort()
    elite = [individual for _, individual in fitness_scores[:elite_size]]
    selected = random.sample(population, len(population)-elite_size)
    return elite + selected

```

- Fungsi `crossover(parent1, parent2)`: Fungsi ini melakukan operasi crossover pada dua orang tua (parent) untuk menghasilkan keturunan (child). Sebuah titik pemutusan (crossover point) secara acak dipilih dalam urutan orang tua, dan bagian sebelum titik pemutusan disalin ke keturunan dari orang tua pertama, sementara bagian setelah titik pemutusan diambil dari orang tua kedua. Sisa gen-gen yang belum ada dalam keturunan diambil secara acak dari orang tua kedua. Fungsi ini mengembalikan keturunan.
```
def crossover(parent1, parent2):
    child = [-1] * len(parent1)
    start = random.randint(0, len(parent1)-1)
    end = random.randint(start, len(parent1)-1)
    for i in range(start, end+1):
        child[i] = parent1[i]
    remaining = [gene for gene in parent2 if gene not in child]
    for i in range(len(child)):
        if child[i] == -1:
            child[i] = remaining.pop(0)
    return child

```

- Fungsi `mutation(individual, mutation_rate)`: Fungsi ini menerapkan operasi mutasi pada individu dengan tingkat mutasi (`mutation_rate`) yang diberikan. Setiap gen dalam individu memiliki peluang (`mutation_rate`) untuk ditukar dengan gen lain secara acak dalam individu. Fungsi ini mengembalikan individu yang sudah dimutasi.
```
def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual)-1)
            individual[i], individual[j] = individual[j], individual[i]
    return individual
```

- Fungsi `genetic_algorithm(distance_matrix, population_size, elite_size, mutation_rate, generations)`: Fungsi ini menjalankan algoritma genetika untuk mencari solusi terbaik (jarak terpendek dan rute terbaik) berdasarkan parameter yang diberikan. Pada setiap generasi, fungsi ini melakukan seleksi individu terbaik, menghasilkan keturunan baru melalui crossover dan mutasi, dan memperbarui populasi. Setelah sejumlah generasi, fungsi ini mengembalikan jarak terbaik dan rute terbaik yang ditemukan.
```
def genetic_algorithm(distance_matrix, population_size, elite_size, mutation_rate, generations):
    population = [[i for i in range(len(distance_matrix))] for _ in range(population_size)]
    for generation in range(generations):
        population = selection(population, elite_size)
        children = []
        while len(children) < population_size - elite_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            child = mutation(child, mutation_rate)
            children.append(child)
        population = population[:elite_size] + children
    fitness_scores = [(fitness(individual, distance_matrix), individual) for individual in population]
    fitness_scores.sort()
    return fitness_scores[0][0], fitness_scores[0][1]
```

- Fungsi `best_distance, best_route = genetic_algorithm(distance_matrix, population_size, elite_size, mutation_rate, generations)`: Pernyataan ini menjalankan algoritma genetika dengan menggunakan parameter yang ditentukan sebelumnya. Hasil terbaik (jarak terpendek dan rute terbaik) disimpan dalam variabel `best_distance` dan `best_route`.

- Fungsi `print("Best Distance:", best_distance)`: Pernyataan ini mencetak jarak terbaik yang ditemukan ke output menggunakan `print()`. Variabel `best_distance` adalah argumen yang digunakan untuk membangun string yang dicetak.

- Fungsi `print("Best Route:", best_route)`: Pernyataan ini mencetak rute terbaik yang ditemukan ke output menggunakan `print()`. Variabel `best_route` adalah argumen yang digunakan untuk membangun string yang dicetak.

![Ouput_Tugas2_TSPwithGA](URL_gambar)

### Tugas 3. MAP Coloring CSP
-  `import copy`: Mengimpor modul `copy` yang digunakan untuk membuat salinan objek.

- `Graph definition` : Mendefinisikan graf dengan variabel `variables` yang merupakan daftar semua node, `domains` yang merupakan daftar domain warna untuk setiap node, dan `neighbors` yang berisi tetangga-tetangga setiap node.

- Fungsi `constraint` memeriksa apakah tetangga-tetangga suatu node memiliki warna yang berbeda. Fungsi ini melakukan iterasi pada tetangga-tetangga dari variabel `var`. Jika ada tetangga yang sudah ada di dalam `assignment` dan memiliki nilai yang sama dengan `value`, fungsi mengembalikan `False`, menunjukkan bahwa konstrain tidak terpenuhi. Jika tidak ada tetangga yang melanggar konstrain, fungsi mengembalikan `True`.
```
# Constraint function to check if neighboring nodes have different colors
def constraint(var, value, assignment):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True
```

- Fungsi `backtrack` menerapkan algoritma backtracking untuk menyelesaikan masalah pemberian warna pada graf. Fungsi ini menggunakan rekursi untuk mencoba semua kemungkinan pemberian warna pada setiap variabel. Pada setiap langkah, fungsi memeriksa apakah panjang `assignment` sudah sama dengan panjang `variables`. Jika sudah, fungsi mengembalikan `assignment` karena itu adalah solusi yang lengkap. Jika belum, fungsi memilih variabel yang belum diberi nilai menggunakan fungsi `select_unassigned_variable`. Fungsi kemudian mencoba semua nilai dalam domain variabel tersebut dengan menggunakan fungsi `order_domain_values`. Fungsi `constraint` digunakan untuk memeriksa konstrain dan jika konstrain terpenuhi, nilai dimasukkan ke dalam `assignment` dan rekursi dilakukan untuk memproses variabel selanjutnya. Jika tidak ada solusi yang ditemukan, fungsi mengembalikan `None`.
```
# Backtracking algorithm
def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment)
    for value in order_domain_values(var, assignment):
        if constraint(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[var]
    return None
```

- Fungsi `select_unassigned_variable` merupakan fungsi bantu yang digunakan untuk memilih variabel yang belum diberi nilai dari `assignment`. Fungsi ini melakukan iterasi pada variabel-variabel dalam `variables` dan mengembalikan variabel pertama yang belum ada dalam `assignment`.
```
# Helper function to select an unassigned variable
def select_unassigned_variable(assignment):
    for variable in variables:
        if variable not in assignment:
            return variable
```

- Fungsi `order_domain_values` merupakan fungsi bantu yang digunakan untuk mengurutkan nilai domain variabel `var`. Fungsi ini mengembalikan daftar nilai domain dari `domains[var]`.
```
# Helper function to order the domain values
def order_domain_values(var, assignment):
    return domains[var]
```

- Fungsi `check_solution` merupakan fungsi bantu yang digunakan untuk memeriksa apakah solusi yang ditemukan valid. Fungsi ini melakukan iterasi pada setiap variabel dalam `solution` dan memeriksa apakah tetangga-tetangganya memiliki nilai yang sama. Jika ada tetangga yang memiliki nilai yang sama, fungsi mengembalikan `False`, menunjukkan bahwa solusi tidak valid. Jika tidak ada pelanggaran, fungsi mengembalikan `True`.
```
# Helper function to check if the solution is valid
def check_solution(solution):
    for variable in solution:
        for neighbor in neighbors[variable]:
            if neighbor in solution and solution[variable] == solution[neighbor]:
                return False
    return True
```
- `Main function` : Pada bagian utama program, fungsi `backtrack` dipanggil dengan `assignment` awal yang kosong (`{}`). Hasil dari fungsi tersebut disimpan dalam `solution`. Jika tidak ada solusi yang ditemukan (solusi adalah None), pesan "No solution found" dicetak. Jika ada solusi yang ditemukan, solusi dicetak.

![Ouput_Tugas3_MapColoringTSP](URL_gambar)
