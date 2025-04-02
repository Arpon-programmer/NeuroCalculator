# NeuroCalculator

NeuroCalculator is a simple neural network model designed to perform basic addition operations. It takes two numbers as input and predicts their sum.

## Features

- Great accuracy on a very small dataset.
- Accepts two single-digit numbers as input.
- Trains a neural network to predict the sum of the inputs.
- Demonstrates the use of deep learning for basic arithmetic tasks.

## Requirements

- Python 3.x
- TensorFlow or PyTorch (depending on your preferred framework)
- NumPy
- Matplotlib (optional, for visualization)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Arpon-programmer/NeuroCalculator.git
    cd NeuroCalculator
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Train the model:
    ```bash
    python train.py
    ```

2. Test the model:
    ```bash
    python test.py
    ```

3. Use the model for predictions:
    ```bash
    python predict.py --num1 <number1> --num2 <number2>
    ```

## Example

```bash
python predict.py --num1 3 --num2 5
# Output: The predicted sum is 8.
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
