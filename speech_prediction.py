import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write

# Load speech signal
fs, speech_signal = read('original_speech.wav')

# Normalize the speech signal. This ensures that the speech signal has consistent amplitude scaling for accurate prediction and avoids distortion when processing.
speech_signal = speech_signal / np.max(np.abs(speech_signal))

# Define experimental values
p1 = 0.825
p2 = 0.562

# Calculate a and b
a = (p2 - p1**2) / (1 - p1**2)
b = (p1 * (1 - p2)) / (1 - p1**2)

# Find the point where the speech signal exceeds a threshold to crop empty samples or else prediction would be inaccurate
threshold = 0.01
start_index = np.argmax(np.abs(speech_signal) > threshold)

# Crop the signal from the start_index onwards. Now this would be used for prediction
cropped_speech_signal = speech_signal[start_index:]

# Initialize a prediction array
predicted_signal = np.zeros_like(cropped_speech_signal)

# First two samples are not be predicted (we assume them as is)
predicted_signal[0] = cropped_speech_signal[0]
predicted_signal[1] = cropped_speech_signal[1]

# Implement the second-order prediction. Using X_n = a * X_(n-2) + b * X_(n-1) where a and b are calculated above.
for n in range(2, len(cropped_speech_signal)):
    predicted_signal[n] = a * cropped_speech_signal[n-2] + b * cropped_speech_signal[n-1]

# Plot the original (cropped) and predicted signals
plt.figure(figsize=(10, 6))
plt.plot(np.arange(len(cropped_speech_signal)), cropped_speech_signal, label='Original Signal', color='blue', alpha=0.5)
plt.plot(np.arange(len(cropped_speech_signal)), predicted_signal, label='Predicted Signal', color='red', linestyle='--')
plt.title('Second Order Speech Prediction')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.savefig('prediction_plot.png')
plt.close()

# Save the predicted speech and the original (cropped) speech (Convert to 16-bit PCM format)
predicted_signal = np.int16(predicted_signal * 32767)
write('predicted_speech.wav', fs, predicted_signal)
cropped_signal = np.int16(cropped_speech_signal * 32767)
write('original_speech_cropped.wav', fs, cropped_signal)

# Calculate the Mean Squared Error (MSE) between the original (cropped) and predicted signals
mse = np.mean((cropped_speech_signal - predicted_signal) ** 2)
print(f'MSE between original and predicted speech: {mse}')