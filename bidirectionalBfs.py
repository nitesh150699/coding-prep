from collections import deque, defaultdict

def find_best_meeting_restaurant_bidirectional(grid, friends, restaurants, blockers):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Distance tracking and reachable count for restaurants
    friends_distances = defaultdict(lambda: float('inf'))
    restaurants_distances = defaultdict(lambda: float('inf'))
    restaurant_reach_count = defaultdict(int)  # Tracks how many friends reach each restaurant
    
    # Initialize BFS queues
    friends_queue = deque([(friend[0], friend[1], 0) for friend in friends])
    restaurants_queue = deque([(restaurant[0], restaurant[1], 0) for restaurant in restaurants])
    
    # Initialize friends distances
    for friend in friends:
        friends_distances[(friend[0], friend[1])] = 0
    
    # Initialize restaurant distances
    for restaurant in restaurants:
        restaurants_distances[(restaurant[0], restaurant[1])] = 0

    # Minimum distance tracking
    min_distance = float('inf')
    best_restaurant = None
    
    # Perform bidirectional BFS
    while friends_queue or restaurants_queue:
        # Process BFS from friends
        if friends_queue:
            x, y, dist = friends_queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 'B':
                    if friends_distances[(nx, ny)] > dist + 1:
                        friends_distances[(nx, ny)] = dist + 1
                        friends_queue.append((nx, ny, dist + 1))
                    
                    # If this cell is a restaurant, update reach count
                    if grid[nx][ny] == 'R':
                        restaurant_reach_count[(nx, ny)] += 1

        # Process BFS from restaurants
        if restaurants_queue:
            x, y, dist = restaurants_queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 'B':
                    if restaurants_distances[(nx, ny)] > dist + 1:
                        restaurants_distances[(nx, ny)] = dist + 1
                        restaurants_queue.append((nx, ny, dist + 1))
                    
                    # If this cell has been reached by all friends, calculate distance
                    if (nx, ny) in restaurant_reach_count and restaurant_reach_count[(nx, ny)] == len(friends):
                        total_dist = friends_distances[(nx, ny)] + restaurants_distances[(nx, ny)]
                        if total_dist < min_distance:
                            min_distance = total_dist
                            best_restaurant = (nx, ny)

    # Return the best restaurant and the minimum total distance
    return best_restaurant, min_distance if best_restaurant else (None, -1)

# Example Usage
grid = [
    ['.', 'F', '.', 'R', 'B'],
    ['.', '.', 'B', '.', '.'],
    ['R', 'B', 'F', '.', 'R'],
    ['F', '.', 'B', '.', '.'],
    ['.', '.', '.', 'F', '.']
]

friends = [(0, 1), (2, 2), (3, 0)]  # Friends' positions
restaurants = [(0, 3), (2, 0), (2, 4)]  # Restaurants' positions
blockers = [(0, 4), (1, 2), (2, 1)]  # Blockers' positions

best_restaurant, min_distance = find_best_meeting_restaurant_bidirectional(grid, friends, restaurants, blockers)

if best_restaurant:
    print(f"The best restaurant is at {best_restaurant} with a minimum total distance of {min_distance}.")
else:
    print("No valid restaurant found.")
