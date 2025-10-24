# 🧭 NLP Environment Setup Summary

## 🎯 Goal
Establish a stable, reproducible Conda-based environment that uses spaCy and ScispaCy, including:
- Biomedical and clinical NLP using **spaCy** + **SciSpaCy**
- Transformer-based modeling using **Hugging Face Transformers**
- Interactive development in **JupyterLab**
- Clean dependency management across compiled and Python-only packages

---

## ⚙️ System Context
- **OS:** macOS  
- **Conda installation:** `/Users/mariakalimeri/opt/anaconda3`  
- **Python version:** 3.10  
- **Shell:** `zsh`

---

## 🧩 Issues Encountered & Solutions

### 1️⃣ spaCy + SciSpaCy version conflicts
**Problem:** `pip`/Conda couldn’t resolve versions; mismatched `thinc`, `numpy`, and `spaCy` builds.  
**Root cause:** `scispacy` requires `spacy >= 3.6,<3.7`, while newer `thinc`/`numpy` wheels break ABI compatibility.  
**Solution:**  
- Pin `spaCy = 3.6.1`, `thinc = 8.1.10`, `numpy = 1.26.4`.  
- Install `scispacy` separately with `--no-deps` to reuse the Conda-installed `spaCy`.

---

### 2️⃣ pip attempting to compile from source
**Problem:** `pip install scispacy` tried to compile `spaCy` / `thinc` using Rust + Cython.  
**Fix:**  

<pre>```
pip install scispacy==0.5.3 --no-deps
```
</pre>

This forces SciSpaCy to link against the existing Conda binaries.

### 3️⃣ Tokenizers build failure

**Problem:**  tokenizers (Rust-based) failed to build when installing Transformers.
**Fix:**
Use pre-compiled Conda-Forge binaries:

<pre>
```
conda install -c conda-forge tokenizers=0.19.1 transformers=4.42.4
```
</pre>

### 4️⃣ “Permission denied” errors writing to /Library/...

**Problem:** pip used macOS system Python 3.13 instead of Conda’s Python.
**Fix:**
Always invoke pip through the environment’s Python:

<pre>
```
python -m pip install scispacy==0.5.3 --no-deps
```
</pre>

Verify with:

<pre>
```
which python
which pip
```
</pre>

Both should point inside /opt/anaconda3/envs/nlp_env/.

### 5️⃣ Conda initialization missing

**Problem:** source ~/miniconda3/etc/profile.d/conda.sh not found.
**Root cause:** Conda installed under /Users/mariakalimeri/opt/anaconda3.
**Fix:**

<pre>
```
source /Users/mariakalimeri/opt/anaconda3/etc/profile.d/conda.sh
```
</pre>

Add to ~/.zshrc for persistence.

### ✅ Final Working Environment

| Package      | Version | Source          |
| ------------ | ------- | --------------- |
| Python       | 3.10    | Conda           |
| spaCy        | 3.6.1   | Conda           |
| thinc        | 8.1.10  | Conda           |
| numpy        | 1.26.4  | Conda           |
| SciSpaCy     | 0.5.3   | pip (--no-deps) |
| transformers | 4.42.4  | Conda           |
| tokenizers   | 0.19.1  | Conda           |
| datasets     | 2.18.0  | Conda           |
| jupyterlab   | 4.0.0   | Conda           |

### ⚙️ Final Environment Creation Steps

All the instructions are listed in the file environment.yml, which we will use to create the conda environment

<pre>
```bash
conda env create -f environment.yml
conda activate nlp_env
python -m pip install scispacy==0.5.3 --no-deps
```
</pre>

The last command ensures the correct version of scispacy is installed

### ➕ Bonus: Add the environment as a kernel in jupyter notebook 

To add the conda environment as a kernel that can be used in jupyter run the following while the environment is activated
<pre>
```bash
python -m ipykernel install --user --name=nlp_env
jupyter lab
```
</pre>

Now, jupyter lab will open in anew tab and the environment can be selected as the active kernel
