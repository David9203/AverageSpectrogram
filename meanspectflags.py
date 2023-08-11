import argparse
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count

def calculate_spectrogram(audio_path):
    y, sr = librosa.load(audio_path)
    spectrogram = np.abs(librosa.stft(y))
    return spectrogram

def process_audio_file(audio_path):
    spectrogram = calculate_spectrogram(audio_path)
    return spectrogram

def main(folder_path, output_csv):
    audio_files = [file for file in os.listdir(folder_path) if file.endswith(".wav")]

    if not audio_files:
        print("No WAV files found in the folder.")
        return

    num_processors = cpu_count()
    print(f"Using {num_processors} processors.")

    audio_paths = [os.path.join(folder_path, audio_file) for audio_file in audio_files]

    sr = librosa.get_samplerate(audio_paths[0])

    with Pool(num_processors) as pool:
        spectrograms = pool.map(process_audio_file, audio_paths)

    total_spectrogram = sum(spectrograms)
    average_spectrogram = total_spectrogram / len(audio_files)

    np.savetxt(output_csv, average_spectrogram, delimiter=',')

    plt.figure(figsize=(10, 6))
    librosa.display.specshow(librosa.amplitude_to_db(average_spectrogram, ref=np.max),
                             sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Average Spectrogram')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate average spectrogram of audio files.")
    parser.add_argument("--folder", required=True, help="Path to the folder containing WAV files.")
    parser.add_argument("--output", default="average_spectrogram.csv", help="Output CSV file name.")
    args = parser.parse_args()
    
    main(args.folder, args.output)
