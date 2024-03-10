import heapq

def minimum_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # перетворюємо список в купу
    total_cost = 0

    while len(cables) > 1:
        # об'єднуємо два найкоротших кабелі
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        combined_length = shortest1 + shortest2
        total_cost += combined_length
        
        # додаємо новостворений кабель до купи
        heapq.heappush(cables, combined_length)
    
    return total_cost

# Приклад використання
cables = [2, 13, 4, 15]
min_cost = minimum_cost_to_connect_cables(cables)
print("Мінімальні витрати на з'єднання кабелів:", min_cost)
