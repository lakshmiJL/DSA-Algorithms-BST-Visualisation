import matplotlib.pyplot as plt
import numpy as np
import time
import random

# Function to update the plot
def update_plot(arr, rects, text_labels, ax):
    for rect, val, text in zip(rects, arr, text_labels):
        rect.set_height(val)
        text.set_position((rect.get_x() + rect.get_width()/2, val + 1))
        text.set_text(str(val))  # Update text above bars
    plt.pause(0.2)

# Bubble Sort Algorithm (with visualization)
def bubble_sort_visual(arr, rects, text_labels, ax):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap values
                update_plot(arr, rects, text_labels, ax)
    return arr

# Insertion Sort Algorithm (with visualization)
def insertion_sort_visual(arr, rects, text_labels, ax):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            update_plot(arr, rects, text_labels, ax)
        arr[j + 1] = key
        update_plot(arr, rects, text_labels, ax)
    return arr

# Merge Sort Algorithm (with visualization)
def merge_sort_visual(arr, l, r, rects, text_labels, ax):
    if l < r:
        mid = (l + r) // 2
        merge_sort_visual(arr, l, mid, rects, text_labels, ax)
        merge_sort_visual(arr, mid + 1, r, rects, text_labels, ax)
        merge(arr, l, mid, r, rects, text_labels, ax)

# Merge two halves with visualization
def merge(arr, l, mid, r, rects, text_labels, ax):
    left = arr[l:mid+1]
    right = arr[mid+1:r+1]
    
    i = j = 0
    k = l
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        update_plot(arr, rects, text_labels, ax)
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        update_plot(arr, rects, text_labels, ax)
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        update_plot(arr, rects, text_labels, ax)
run = True
# Main function to create visualization
def visualize_sorting():
    global run
    arr = [random.randint(1, 50) for _ in range(10)]  # Generate random numbers
    fig, ax = plt.subplots()
    
    # Create initial bars
    rects = ax.bar(range(len(arr)), arr, color='skyblue')

    # Create text labels above bars
    text_labels = [ax.text(rect.get_x() + rect.get_width()/2, rect.get_height() + 1, 
                           str(int(rect.get_height())), ha='center', va='bottom', fontsize=12) for rect in rects]
    
    ax.set_ylim(0, max(arr) + 10)  # Adjust Y-axis
    ax.set_title("Sorting Algorithm Visualization")

    plt.ion()  # Interactive mode ON
    plt.show()
    
    print("Choose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Quit")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        bubble_sort_visual(arr, rects, text_labels, ax)
    elif choice == 2:
        insertion_sort_visual(arr, rects, text_labels, ax)
    elif choice == 3:
        merge_sort_visual(arr, 0, len(arr)-1, rects, text_labels, ax)
    elif choice == 4:
        run = False
        
    else:
        print("Invalid choice!")

    plt.ioff()  # Turn off interactive mode
    plt.show()

# Run the sorting visualizer
while run == True:
    visualize_sorting()
