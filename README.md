# Clinical Notes Analysis – Named Entity Recognition and Disease Classification

**Author:** Maria Kalimeri  
**Domain:** Application of NLP in Healthcare  
**Date:** October 2025

---

## 1. Introduction

In this project, I use a dataset containing clinical notes (transcriptions) to explore how Natural Language Processing (NLP) techniques can be applied to extract medical concepts from free text and use them to predict medical specialty.

**Goals**

- Named Entity Recognition (NER) to identify medications and medical conditions in free text
- Entity linking with UMLS to standardise extracted medical concepts
- Medical specialty classification
- Visualisation of insights

The main focus of this project was to explore how unstructured medical text can be transformed into structured features that can be used with conventional machine learning models. Rather than aiming primarily for the highest possible classification performance, I focused on building an end-to-end pipeline that takes raw clinical text, extracts and standardises medical concepts, transforms them into numerical features, and uses those features to make a prediction.

## 2. Methods

At a high level, the steps I took to process the free text and extract data to classify each transcript into medical specialties are the following

- Processed the data with spaCy and ScispaCy to detect entities (chemicals and diseases), no finetuning was performed
- I used sciSpacy's entity linker, to standardise each entity into UMLS CUIs [1]
- CUI2vec embeddings were used to project CUIs into a vector space [2]
- Used these feature vectors to train and compare several conventional machine learning classifiers, with model selection based on cross-validation and hyperparameter tuning.

## 3. Results

### Entity recogniion

No fine-tuning was performed for the entity recognition task, and no labelled ground truth was available for this dataset. Consequently, I did not calculate quantitative performance metrics for entity recognition. Manual inspection showed both successful entity extraction and examples of missed or imperfectly classified entities. A small number of transcriptions contained no detected entities.

### Entity linking

Entity linking was applied to map extracted medical concepts to UMLS CUIs. In the absence of labelled ground truth, I performed qualitative spot checks of the mappings, including checking whether different expressions referring to the same medical concept were mapped consistently.

### Embeddings

Approximately 85% of the detected CUIs had corresponding embeddings available in CUI2Vec. The CUIs associated with each transcription were mapped to their available embeddings, and the embeddings were averaged to produce a single feature vector for each record. Records for which no usable embeddings were available were removed from the classification dataset.

### Classification

After removing medical specialties with too few samples for meaningful model training and evaluation, the classification dataset contained 4,310 transcriptions across 19 medical specialties.

A DummyClassifier was used to establish a naive baseline. Several conventional machine learning models were then compared using stratified cross-validation and macro F1-score, including Logistic Regression, Linear SVM, XGBoost, Random Forest and AdaBoost. The strongest-performing models were subsequently evaluated using hyperparameter tuning.

Logistic Regression produced the best overall performance. Hyperparameter tuning resulted in only a small improvement over the default model, suggesting that classifier choice and tuning were not the main limitations on performance.

## 4. Conclusion/Future Work

This project demonstrates an end-to-end approach for transforming unstructured clinical text into structured features that can be used with conventional machine learning models. Medical entities were extracted from clinical transcriptions, standardised using UMLS CUIs, and represented numerically using CUI2Vec embeddings before being used for medical specialty classification.

While the classification models performed better than the naive baseline, overall performance remained modest and hyperparameter tuning produced only small improvements. This suggests that the representation of the clinical notes, rather than classifier selection alone, is an important limitation. Averaging CUI2Vec embeddings provides a compact representation of the medical concepts present in each transcription, but discards much of the contextual information contained in the original text.

Future work could therefore focus on improving the input representation rather than further classifier tuning. Possible directions include combining concept-level CUI information with contextual embeddings from biomedical language models such as BioClinicalBERT or PubMedBERT, exploring more informative methods for aggregating entity embeddings, and filtering low-confidence entity extractions.

## 5. Project structure and execution order

The project is split into two main stages:

1. `text_processing/Healthcare_Text_Processing.ipynb`
   - loads the raw `mtsamples.csv` dataset
   - performs text preprocessing
   - extracts disease/chemical entities using SciSpaCy
   - links detected entities to UMLS CUIs
   - saves `data/processed/CUI_medicalSpecialties.parquet`

2. `analysis/Modelling.ipynb`
   - loads the processed CUI dataset
   - retrieves CUI2Vec embeddings
   - aggregates embeddings at transcription level
   - prepares the classification dataset
   - trains and evaluates conventional machine-learning classifiers

Two separate conda environments are used because the SciSpaCy pipeline requires older spaCy-compatible dependencies, while the modelling stage uses a more recent analysis environment.

## 6. Running the project

### Data setup

Download the Medical Transcriptions dataset from Kaggle

`https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions`

and place the CSV file at:

`data/raw/mtsamples.csv`

The raw dataset is not included in this repository.

The installation of the libraries has been performed in dedicated conda environments. **If the environments have not been created yet, do it before continuing!**

### Conda Environment Creation Steps

As explained in the Set_Up_NLP_Environment.md file, in order to use scispacy, an older version of spacy, and other libraries, needed to be installed, instead of the most recent versions. As a result, the installation of libraries needs to be done carefully, according to the following steps (also described in Set_Up_NLP_Environment.md).

Having the restriction of old spaCy version meant that older versions of other libraries also needed to be installed. To not be restricted by this in the analysis part of the project, I used two different environments: one for text processing (entity recognition and linking) and one for analysis (embeddings and classification).

#### NLP environment

On the terminal, move into the project folder and type the following

<pre>
conda env create -f envs/environment_nlp.yml
conda activate nlp_env
python -m pip install scispacy==0.5.3 --no-deps
</pre>

#### Analysis environment

On the terminal, move into the project folder and type the following

<pre>
conda env create -f envs/environment_analysis.yml
conda activate analysis_env
</pre>

### Bonus: Add the environment as a kernel in jupyter notebook

To add the conda environment as a kernel that can be used in jupyter run the following while the environment is activated

<pre>
python -m ipykernel install --user --name=nlp_env
python -m ipykernel install --user --name=analysis_env

jupyter lab
</pre>

Now, jupyter lab will open in anew tab and the environment can be selected as the active kernel

## References

[1] Bodenreider O. (2004). The Unified Medical Language System (UMLS): integrating biomedical terminology. Nucleic acids research, 32(Database issue), D267–D270. https://doi.org/10.1093/nar/gkh061
[2] https://pmc.ncbi.nlm.nih.gov/articles/PMC6922053/
