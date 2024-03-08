# EncodeAI

<details>
<summary><b>Working with the Conda Environment</b> (click to expand)</summary>
<br>

## Setting Up the Conda Environment

This project uses a conda environment to manage dependencies. To set up the environment on your local machine, follow these steps:

1. **Install Miniconda or Anaconda**:

   If you haven't already, install Miniconda or Anaconda on your machine. Visit [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual) for installation instructions.

2. **Create the Environment**:

   Navigate to the project directory and run the following command to create a conda environment from the `environment.yml` file:

```bash
conda env --name myenv create -f environment.yml
```

3. **Activate the Environment**:

    Once the environment is created, you can activate it using:

```bash
conda activate myenv
```

Replace `myenv` with the name of the environment specified in the `environment.yml` file.

## Working with the Conda Environment

### Installing Additional Packages

If you need to install additional packages, make sure to activate the environment and use:

```bash
conda install package-name
```

Or, if the package is only available via pip (still check installation guide for the specific package):

```bash
pip install package-name
```

There may be other ways to install a package for example using `conda-forge`  ( `conda install package -c conda-forge` ) so always look for instructions online.

### Updating the Environment

If you've added new packages or made other changes to the environment that you want to share with the team, you can update the `environment.yml` file by running:

```bash
conda env export --from-history > environment.yml
```

**Note:** The yml file contains `prefix` field which relates to the path of the environment **locally**, conda however, doesn't care and besides manually deleting the line there doens't seem to be a way to avoid creating that line when exporting.

**Note:** Use the `--from-history` flag to only include packages you've explicitly installed, avoiding platform-specific packages in the environment file.

### Sharing Changes

After updating the `environment.yml` file, commit and push the changes to the GitHub repository so the team members can update their environments by running:

```bash
conda env update --file environment.yml --prune
```

The `--prune` option removes any dependencies that are no longer needed from the environment.

### Adding conda environment to JupyterLab

To make your conda environment visible to JupyterLab you need to add your environment by creating a kernel spec:

```bash
python -m ipykernel install --user --name YourEnvironmentName --display-name "Display Name"
```

### Running JupyterLab

1. Intall JupyterLab:

```bash
pip3 install jupyter
```

2. Navigate to the notebooks directory:

```bash
cd notebooks
```

3. Run JupyterLab

```bash
jupyter lab
```

</details>

### Running the program

1. **Create Conda environment**

```bash
cd src
conda env create --name myenv -f environment.yml
```

#### NOTE: 

Change myenv for the name you want.

2. Create .env

Create .env and change the placeholders for your keys/tokens

```bash
AUTH_TOKEN_STABILITY_AI='Your Stability AI token'
```