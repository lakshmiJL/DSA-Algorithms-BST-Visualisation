import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None
        self.graph = nx.DiGraph()

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
        self.update_graph()
    
    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)
    
    def inorder_traversal(self, root):
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right) if root else []
    
    def update_graph(self):
        self.graph.clear()
        self._build_graph(self.root)
    
    def _build_graph(self, root):
        if root:
            if root.left:
                self.graph.add_edge(root.val, root.left.val)
                self._build_graph(root.left)
            if root.right:
                self.graph.add_edge(root.val, root.right.val)
                self._build_graph(root.right)
    
    def draw_tree(self):
        plt.figure(figsize=(6, 4))
        
        pos = self.hierarchy_pos(self.graph, self.root.val)  # Custom layout function
        nx.draw(self.graph, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, edge_color="gray")
        
        plt.show()

    def hierarchy_pos(self, G, root, width=1.0, vert_gap=0.2, xcenter=0.5, pos=None, level=0, parent=None):
        """Creates a hierarchical layout for the BST visualization"""
        if pos is None:
            pos = {root: (xcenter, 1 - level * vert_gap)}
        else:
            pos[root] = (xcenter, 1 - level * vert_gap)
        
        children = list(G.successors(root))
        if len(children) > 0:
            dx = width / 2
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = self.hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, xcenter=nextx, pos=pos, level=level+1, parent=root)
        return pos

class BSTVisualizer:
    def __init__(self, root):
        self.tree = BST()
        self.root = root
        self.root.title("Binary Search Tree Visualizer")

        self.label = tk.Label(root, text="Enter a number:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.insert_button = tk.Button(root, text="Insert", command=self.insert)
        self.insert_button.pack()
        
        self.traverse_button = tk.Button(root, text="Inorder Traversal", command=self.show_traversal)
        self.traverse_button.pack()
        
        self.visualize_button = tk.Button(root, text="Visualize", command=self.visualize_tree)
        self.visualize_button.pack()
    
    def insert(self):
        try:
            key = int(self.entry.get())
            self.tree.insert(key)
            messagebox.showinfo("Success", f"Inserted {key} into BST")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    
    def show_traversal(self):
        traversal = self.tree.inorder_traversal(self.tree.root)
        messagebox.showinfo("Inorder Traversal", f"{traversal}")
    
    def visualize_tree(self):
        self.tree.draw_tree()

if __name__ == "__main__":
    root = tk.Tk()
    app = BSTVisualizer(root)
    root.mainloop()
