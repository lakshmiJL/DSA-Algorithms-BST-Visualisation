import tkinter as tk
from tkinter import messagebox

class Event:
    def __init__(self, date, name, description):
        self.date = date
        self.name = name
        self.description = description
        self.left = None
        self.right = None

class EventBST:
    def __init__(self):
        self.root = None

    def insert(self, date, name, description):
        def _insert(node, date, name, description):
            if node is None:
                return Event(date, name, description)
            if date < node.date:
                node.left = _insert(node.left, date, name, description)
            else:
                node.right = _insert(node.right, date, name, description)
            return node
        
        self.root = _insert(self.root, date, name, description)

    def search(self, date):
        def _search(node, date):
            if node is None:
                return None
            if node.date == date:
                return node
            elif date < node.date:
                return _search(node.left, date)
            else:
                return _search(node.right, date)
        
        return _search(self.root, date)

    def delete(self, date):
        def _delete(node, date):
            if node is None:
                return node
            if date < node.date:
                node.left = _delete(node.left, date)
            elif date > node.date:
                node.right = _delete(node.right, date)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self._min_value_node(node.right)
                node.date, node.name, node.description = temp.date, temp.name, temp.description
                node.right = _delete(node.right, temp.date)
            return node
        
        self.root = _delete(self.root, date)

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        events = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                events.append(f"Date: {node.date}, Name: {node.name}, Description: {node.description}")
                _inorder(node.right)
        _inorder(self.root)
        return events

class EventApp:
    def __init__(self, root):
        self.tree = EventBST()
        self.root = root
        self.root.title("Event Management System")
        
        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Event Name:").grid(row=1, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1)
        
        tk.Label(root, text="Description:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(root)
        self.desc_entry.grid(row=2, column=1)
        
        tk.Button(root, text="Add Event", command=self.add_event).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Search Event", command=self.search_event).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Delete Event", command=self.delete_event).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="Show All Events", command=self.show_events).grid(row=6, column=0, columnspan=2)
        
        self.events_listbox = tk.Listbox(root, width=50, height=10)
        self.events_listbox.grid(row=7, column=0, columnspan=2)
    
    def add_event(self):
        date = self.date_entry.get()
        name = self.name_entry.get()
        desc = self.desc_entry.get()
        if date and name and desc:
            self.tree.insert(date, name, desc)
            messagebox.showinfo("Success", f"Event '{name}' added on {date}!")
        else:
            messagebox.showerror("Error", "All fields are required!")
    
    def search_event(self):
        date = self.date_entry.get()
        event = self.tree.search(date)
        if event:
            messagebox.showinfo("Event Found", f"{event.name} on {event.date}\n{event.description}")
        else:
            messagebox.showerror("Error", "No event found on this date!")
    
    def delete_event(self):
        date = self.date_entry.get()
        self.tree.delete(date)
        messagebox.showinfo("Success", f"Event on {date} deleted!")
    
    def show_events(self):
        self.events_listbox.delete(0, tk.END)
        events = self.tree.inorder_traversal()
        for event in events:
            self.events_listbox.insert(tk.END, event)

if __name__ == "__main__":
    root = tk.Tk()
    app = EventApp(root)
    root.mainloop()
