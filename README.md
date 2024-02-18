## Setup

The data used were collected at [Intaka Island Reserve](https://intaka.co.za/) in South Africa.

![Location](./README%20img/data-collect-point.jpeg)
The map below shows the locations where the data where collected. The green points indicate the presence of bird while the red one indicate its absence at a given location. The point size indicates how long audio was recorded at a given location.

The dataset can be downloaded [here](https://drive.google.com/file/d/15m8Y1REw0pbPHfnfSH7mAMXToXcuFM6l/view?usp=sharing). To use your own dataset, follow the following structure:

```
Data/
├── Audios/
│   ├── audio_1.wav
│   ├── audio_2.wav
│   ├── ...
│   ├── ...
│   └── audio_n.wav
├── Annotations/
│   ├── audio_1.svl
│   ├── audio_2.svl
│   ├── ...
│   ├── ...
│   └── audio_n.svl
├── DataFiles/
│   ├── TrainingFiles.txt (list of the training files without extension)
│   └── TestingFiles.txt (list of the testing files without extension)
├── Model_Output/
│   └── <leave empty>
├── Pickled_Data/
│   └── <leave empty>
└── Saved_Data/
    └── <leave empty>
```

The code to make some preprocessing on the data can be downloaded [here](https://drive.google.com/file/d/1LgZoFzkT5g-MLb7uZMu0lOBk1unYPmW4/view?usp=sharing). These codes use the data structure above to make the preprocessing. Read through the notebook to better understand how this is done.

## Some results

Some vocalisation event spectrograms are given below

![Spectrogram](./README%20img/bird-spec.png)

After preprocessing by augmenting the data, the spectrograms can look like below.

![Spectrogram after augmentation](./README%20img/bird-spec-aug.png)

The model architecture is:

![Model architecture](./README%20img/cnn-architecture.jpg)

Belove is the figure showing the loss and the accuracy on the training and validation data.

![Spectrogram](./README%20img/metrics.png)

The confusion matrix oon the testing set is given below.

![Spectrogram](./README%20img/confusion-matrix.png)

To know more about this work, read our paper [here](https://drive.google.com/file/d/1CJtfu1QhRZ9dQI_azCa_aZCZBx-CJafc/view?usp=sharing).
