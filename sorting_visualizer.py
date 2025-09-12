import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = key
        yield arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            yield arr
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

def visualize_sorting(algorithm, N=50, interval=50):
    arr = list(range(1, N + 1))
    random.shuffle(arr)

    # Choose algorithm
    if algorithm == "bubble":
        title = "Bubble Sort"
        generator = bubble_sort(arr.copy())
    elif algorithm == "insertion":
        title = "Insertion Sort"
        generator = insertion_sort(arr.copy())
    elif algorithm == "selection":
        title = "Selection Sort"
        generator = selection_sort(arr.copy())
    else:
        raise ValueError("Unknown algorithm. Choose from 'bubble', 'insertion', 'selection'.")

    fig, ax = plt.subplots()
    ax.set_title(f"{title} Visualization")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(N * 1.1))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Iterations: {iteration[0]}")

    ani = animation.FuncAnimation(
        fig,
        func=update_fig,
        fargs=(bar_rects, iteration),
        frames=generator,
        interval=interval,
        repeat=False,
        blit=False,
    )
    plt.show()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Visualize Sorting Algorithms")
    parser.add_argument(
        "--algorithm",
        choices=["bubble", "insertion", "selection"],
        default="bubble",
        help="Sorting algorithm to visualize",
    )
    parser.add_argument("--size", type=int, default=50, help="Number of elements")
    parser.add_argument("--interval", type=int, default=50, help="Animation interval (ms)")
    args = parser.parse_args()

    visualize_sorting(args.algorithm, N=args.size, interval=args.interval)
