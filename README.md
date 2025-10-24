# Clinical Notes Analysis – Named Entity Recognition and Disease Classification
**Author:** Maria Kalimeri  
**Domain:** Application of NLP in Healthcare  
**Date:** October 2025

---

## 1. Introduction
In this project, I will use a dataset containing clinical notes to examine how Natural Language Processing techniques cam be applied to extract diseases, medications, and symptoms, as well as classify patient records into disease categories.  

**Goals:**
- Named Entity Recognition (NER)
- Entity linking with UMLS or SNOMED CT
- Disease classification
- Visualisation of insights

## 2. How to explore this notebook?

The installation of the libraries has been performed in a dedicated conda environment. **If the environment has not been created yet, do it before continuing!**

As explained in the SetUpEnvironment.md file, in order to use scispacy, an older version of spacy, and other libraries, needed to be installed, instead of the most recent versions. As a result, the installation of libraries needs to be done carefully, according to the following steps (also described in SetUpEnvironment.md).

### Conda Environment Creation Steps

<pre>
conda env create -f environment.yml
conda activate nlp_env
python -m pip install scispacy==0.5.3 --no-deps
</pre>

### Bonus: Add the environment as a kernel in jupyter notebook 

To add the conda environment as a kernel that can be used in jupyter run the following while the environment is activated

On the terminal, move into the project folder and type the following

``bash
python -m ipykernel install --user --name=nlp_env
jupyter lab
``

Now, jupyter lab will open in anew tab and the environment can be selected as the active kernel
