# MusicCategorization

## Steps to run

### 1. Install conda (2022.05)

*   Download script from anaconda archive. <br>

    https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh

*   cd to directory and run script. <br>
    ```sh
    bash Anaconda3-2022.05-Linux-x86_64.sh
    ```
*   Activate Installation. <br>   
    ```sh
    source ~/.bashrc
    ```

### 2. Download GTZAN Dataset

*   Download dataset and move "Data" to <parent_path>. <br>   

    https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification


### 3. Create environment

*   Create env_full with all anaconda packages.** <br>   
    ```sh
    conda create -n env_full anaconda
    ```

*   Activate environment. <br>   
    ```sh
    conda activate env_full
    ```

### 4. Run Jupyter Notebook

*   cd to github repo and activate enviroment. <br>   

    ```sh
    cd MusicCategorization
    ```

*   Open jupyter notebook. <br>   

    ```sh
    jupyter notebook
    ```

### 5. Confirm folder structure

```
MusicCategorization/
├── Data
│   ├── features_30_sec.csv
│   ├── features_3_sec.csv
│   ├── genres_original
│   └── images_original
├── feature_extractor
│   ├── feat_extract_test.py
│   ├── gtzan_test_features.csv
│   └── test_audio
├── notebooks
│   └── MahindraGTZANFinal.ipynb
└── README.md
```

*    Data contains original GTZAN Dataset.
*   feature_extractor contains test_audio folder with random audio clips to extract features from. dataframe is automatically saved in gtzan_test_features.csv.

*   notebooks folder contain jupyter .ipynbs with models trained on GTZAN Data.