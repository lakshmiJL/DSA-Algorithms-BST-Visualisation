import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Graph Representation for City Navigation
class CityMap:
    def __init__(self):
        self.graph = {}
    
    def add_road(self, start, end, distance):
        if start not in self.graph:
            self.graph[start] = []
        if end not in self.graph:
            self.graph[end] = []
        self.graph[start].append((end, distance))
        self.graph[end].append((start, distance))
    
    def bfs_shortest_path(self, start, end):
        queue = [(start, [start])]
        visited = set()
        
        while queue:
            current_node, path = queue.pop(0)
            if current_node == end:
                return path, len(path) - 1
            
            if current_node not in visited:
                visited.add(current_node)
                for neighbor, _ in self.graph.get(current_node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        
        return None, float('inf')
    
    def visualize(self):
        G = nx.Graph()
        for node in self.graph:
            for neighbor, weight in self.graph[node]:
                G.add_edge(node, neighbor, weight=weight)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

# GUI Implementation
class SmartCityApp:
    def __init__(self, root):
        self.city = CityMap()
        self.root = root
        self.root.title("Smart City Navigation")
        
        tk.Label(root, text="Start Location:").grid(row=0, column=0)
        self.start_entry = tk.Entry(root)
        self.start_entry.grid(row=0, column=1)
        
        tk.Label(root, text="End Location:").grid(row=1, column=0)
        self.end_entry = tk.Entry(root)
        self.end_entry.grid(row=1, column=1)
        
        tk.Label(root, text="Distance:").grid(row=2, column=0)
        self.distance_entry = tk.Entry(root)
        self.distance_entry.grid(row=2, column=1)
        
        tk.Button(root, text="Add Road", command=self.add_road).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Find Shortest Path", command=self.find_path).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Visualize City", command=self.city.visualize).grid(row=5, column=0, columnspan=2)
    
    def add_road(self):
        start = self.start_entry.get()
        end = self.end_entry.get()
        distance = int(self.distance_entry.get())
        self.city.add_road(start, end, distance)
        messagebox.showinfo("Success", f"Road added between {start} and {end} with distance {distance}")
    
    def find_path(self):
        start = self.start_entry.get()
        end = self.end_entry.get()
        path, distance = self.city.bfs_shortest_path(start, end)
        if path:
            messagebox.showinfo("Shortest Path", f"Path: {' -> '.join(path)}\nDistance: {distance}")
        else:
            messagebox.showerror("Error", "No path found")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartCityApp(root)
    root.mainloop()
