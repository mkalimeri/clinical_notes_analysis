# Clinical Notes Analysis – Named Entity Recognition and Disease Classification
**Author:** Maria Kalimeri  
**Domain:** Application of NLP in Healthcare  
**Date:** October 2025

---

## 1. Introduction
In this project, I use a dataset containing clinical notes (transcripts) to examine how Natural Language Processing techniques cam be applied to extract diseases, medications, and symptoms, as well as predict the medical specialty based on symptoms.  

**Goals:**
- Named Entity Recognition (NER) to identify medications and medical conditions in free text
- Entity linking with UMLS
- Medical specialty perdiction
- Visualisation of insights

My main focus in this project was to explore how free medical text can be processed and produce tabular data that can be used with conventional machine learning models (e.g. linear regression, bagging/boosting methods). My focus was not on achieving the highest performance on the classification task.

## 2. Methods

At a high level, the steps I took to process the free text and extract data to classify each transcript into medical specalties are the following

- Processed the data with spaCy and ScispaCy to detect entities (chemicals and diseases), no finetuning was performed
- I used sciSpacy's entity linker, to standardise each entity into UMLS CUIs [1]
- CUI2vec embeddings were used to project CUIs into a vector space [2]
- The embeddings were passed as input into classifiers, the best classifier was chosen by means of cross validation and hyperparameter tuning

## 3. Results

### Entity recogniion
No finetuning was performed for the entity recognition task, and there was no ground truth available. Consequently, I did not calculate success metrics on the entity recognition task. There was a small amount of text with no entities.

### Entity linking
Entity linking was succesfully applies. Again, no ground truth was available.

### Embeddings
85% of the CUIs dtected had corresponding embeddings available in CUI2vec. 

### Classification
**Todo**

## 4. How to explore this notebook?

The installation of the libraries has been performed in dedicated conda environments. **If the environments have not been created yet, do it before continuing!**

As explained in the Set_Up_NLP_Environment.md file, in order to use scispacy, an older version of spacy, and other libraries, needed to be installed, instead of the most recent versions. As a result, the installation of libraries needs to be done carefully, according to the following steps (also described in Set_Up_NLP_Environment.md).

Having the restriction of old spaCy version meant that older versions of other libraries also needed to be installed. To not be restricted by this in the analysis part of the project, I used two different environments: one for text processing (entity recognistion and linking) and one for analysis (embeddings and classification).

### Conda Environment Creation Steps

#### NPL environment
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
