# Meeting Compuyter Vision - 26/06/2025

Implementation of a face recognition system on low-resource devices, such as smartphones. Pros and cons of different approaches, models, and techniques will be discussed.

## Overfitting

Tackled by implementing: 
- Dropout
- Early Stopping
- Learning Rate Scheduler: adjust the learning rate during training based on validation loss

### Data Augmentation

The augmentation step detects the largest face using MTCNN, rotates it to align the eyes horizontally, crops with a margin, resizes to 128 × 128, and outputs an RGB image. Offline augmentations are applied using a deterministic list of three Albumentations pipelines:
- Horizontal flip
- Small rotation
- Colour/brightness jitter
These augmentations are saved for further processing.

### Data leakage (possible)

Noticed that some models perform closer to 100% accuracy when trained and tested on the augmented dataset. This suggests that the model may be memorizing the training data rather than learning generalizable features. 

This overfitting might be caused due to a `data leakage` issue, where the model has access to information about the test set during training. This happens on the augmented dataset, as for every original picture, there are 3 augmented versions, with a total of 4. On the splitting of the dataset this very similar images are split into training and validation sets, leading to a situation where the model can easily memorize the augmented versions of the training data.

Marked as possible because models like VGG16 jump from 25% in orginal dataset to a reasonable 75%. Models like Vgg16 Custom and MobileNetV2 reach almost 100% accuracy on the augmented dataset, which is suspicious.

## Include more Models

### EOA (state-of-the-art)
Research done on the latest state-of-the-art models for face recognition, including:

- Classical Approaches: PCA, LBP (Local Binary Patterns)
- Transfer Learning (CNN Baselines): VGG16, MobileNetV2 
- Embedding-Based (State-of-the-Art): FaceNet, ArcFace (with KNN classifier)

Will be reasoned on the presentation why these models were chosen and how they compare to each other.

### VGG16 Custom (fine-tuned)
A custom VGG16 model was trained on the dataset, with the following modifications:

#### Fine-Tuning Details:

- **Frozen Layers**: The first 10 layers of VGG16 are frozen to retain low-level feature extraction.
- **Unfrozen Layers**: Deeper layers are unfrozen to adapt to the specific dataset.
- **Regularization**:
    - `BatchNormalization`: Stabilizes activations and accelerates convergence.
    - `Dropout(0.4)`: Applied twice to prevent overfitting.
- **Classification Head**:
    - `GlobalAveragePooling2D`: Reduces spatial dimensions.
    - `Dense(256, activation='relu')`: Learns abstract features.
    - `Dense(num_classes, activation='softmax')`: Outputs class probabilities.

#### Training Configuration:

- **Optimizer**: Adam with a learning rate of 1e-4.
- **Callbacks**:
    - `EarlyStopping`: Stops training when validation loss stops improving.
    - `ReduceLROnPlateau`: Reduces learning rate on validation loss plateau.
- **Precision Policy**: Mixed precision enabled for faster computation.

## Evaluation
Table of results comparing different models and their performance on the validation set. 

#### 2 evaluations:

- Classification: `Accuracy, Precission, Recall and F1` over the validation set
- Verification: Comparing faces 1:1 with binary classification (same or different person) using `Equal Error Rate (EER)` and `Area Under the Curve (AUC)` metrics.
(ArcFace is producing 0.5 results, wrongly, because of the libraries limitations, requires a face detector to work properly, not compatible with the current setup on Colab)

## Web Application Demonsstration
Demo recorded on a video, small app with face login implemented with DeepFace, compares uploaded or webcam image with the database of faces (1 per user), if true, logs in the user, otherwise shows an error message.

