# Speech Prediction using Second-Order AR Model

This project demonstrates the use of a second-order Auto-Regressive (AR) model to predict speech signals based on a given sequence of speech samples. The model is based on the equation:

`x_n = a * x_(n-2) + b * x_(n-1)`

where:
- `x_n` is the predicted speech sample at time step `n`,
- `x_(n-1)` and `x_(n-2)` are the two previous speech samples,
- `a` and `b` are model coefficients computed from experimental values `p1` and `p2`.

The project reads a speech file (e.g., WAV or converted OPUS file), applies the second-order prediction model, and compares the original and predicted signals by calculating the Mean Squared Error (MSE).

> Refer to [this .txt](explanation.txt) for a detailed explanation.

## Authors
- [Sanidhya Kumar](https://github.com/notsanidhyak/)
- [Varun Vilvadrinath](https://github.com/varunvilva/)
- 
## Requirements

- Python 3.x
- `numpy`
- `scipy`
- `matplotlib`
- `sounddevice`

You can install the required dependencies with:

```bash
pip install numpy scipy matplotlib sounddevice
```

## How to Use

1. **Prepare your speech file**:
   - Make sure your speech file is in the `.wav` format. If you have a different format (e.g., OPUS), you will need to convert it to WAV using online converters.
   
2. **Run the script**:
   - Place the script in the same directory as the `.wav` file or update the script to point to the correct path.
   
    ```bash
    python speech_prediction.py
    ```

3. **Output**:
   - The script will:
     - Normalize and crop the speech signal.
     - Apply the second-order AR prediction model.
     - Save the predicted signal as `predicted_speech.wav`.
     - Save a plot comparing the original and predicted signals as `prediction_plot.png`.
     - Print the Mean Squared Error (MSE) between the original and predicted signals in the terminal.

4. **Files Created**:
   - `prediction_plot.png`: A plot showing the comparison between the original and predicted signals.
   - `predicted_speech.wav`: The predicted speech signal saved as a `.wav` file.
   - `original_speech_cropped.wav`: The cropped version of the original speech signal saved as a `.wav` file.

<br>

---
