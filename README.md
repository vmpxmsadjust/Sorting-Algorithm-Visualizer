# Sorting Algorithm Visualizer

This Python script visualizes common sorting algorithms in real-time using Matplotlib animations.  
You can easily compare how different algorithms sort a shuffled array step-by-step.

## Features

- **Bubble Sort**, **Insertion Sort**, and **Selection Sort** visualizations
- Customizable array size and animation speed
- Interactive Matplotlib bar animation

## Requirements

- Python 3.7+
- `matplotlib`

Install dependencies with:
```bash
pip install matplotlib
```

## Usage

Run the script from the terminal:

```bash
python sorting_visualizer.py --algorithm bubble
```

### Options

- `--algorithm`  Sorting algorithm to use (`bubble`, `insertion`, or `selection`). Default is `bubble`.
- `--size`       Number of elements in the array. Default is `50`.
- `--interval`   Animation interval in milliseconds. Default is `50`.

**Examples:**
```bash
python sorting_visualizer.py --algorithm insertion --size 100
python sorting_visualizer.py --algorithm selection --interval 25
```

## How it Works

The script uses Python generators to yield the array state at each sorting step. Matplotlib animates these steps as a bar chart, letting you watch the sorting process in real time.

## Adding More Algorithms

To add a new algorithm, define a generator function (like `bubble_sort`) that yields the array after each swap or key operation. Then, add it to the `visualize_sorting` function.

## License

MIT License
