# EncodeAI

<details>
<summary><b>Working with the Conda Environment</b> (click to expand)</summary>
<br>

## Setting Up the Conda Environment`

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


## Setting up Twitch API 

First to use the code you need to install `irc` using pip. Locate the pip of your conda environment and use the specific pip.

```bash
conda activate myenv
echo $CONDA_PREFIX
[YOUR PREFIX]/bin/pip(3) install irc
```
#### NOTE: 
It may be pip or pip3

1. **Setup TWITCH_CLIENT_ID**
Useful [reference](https://dev.twitch.tv/docs/authentication/register-app/)

After you obtain TWITCH_CLIENT_ID, put it inside the .env file.

```bash
---rest of the file---
TWITCH_CLIENT_ID='YOUR TWITCH CLIENT ID'
---rest of the file---
```

2. **Setup TWITCH_OAUTH_TOKEN**

Connect using [link](https://twitchapps.com/tmi/), this will prompt you to connect oauth with twitch. It will then generate OAUTH token. It will look something like this:

```bash
oauth::YOUR-TOKEN
```

After you obtain the OAUTH token, put it inside the.env file.

```bash
---rest of the file---
TWITCH_OAUTH_TOKEN='YOUR TWITCH OAUTH TOKEN'
---rest of the file---
```

Check your oauth token and also the relevant client id with the following command:

```bash
curl -X GET 'https://id.twitch.tv/oauth2/validate' \
-H 'Authorization: OAuth <replace with your oauth token>'
```

## Setting up EleventLabs API

1. **Install elevenlabs through pip**

There isn't a way to install the elevenlabs package through conda so just intall it into conda with its appropriate pip.

```bash
echo $CONDA_PREFIX
[YOUR PREFIX]/bin/pip(3) install elevenlabs
```

#### NOTE: 
It may be pip or pip3

2. **Add ELEVEN_API_KEY to .env**

```bash
---rest of the file---
ELEVEN_API_KEY='YOUR  ELEVEN LABS API KEY'
---rest of the file---
```

3. **Installing ffmpeg**

(Need to add the actual instructions...)
Follow instructions [here]()

# FOR TESTING

.env   
```bash
OPENAI_API_KEY='OUR OPEN AI API KEY'
ELEVEN_API_KEY='OUR ELEVEN LABS API KEY'
T_CLIENT_ID='h92ugsewcdxsggcjs7t0lee6uiey84'
TWITCH_OAUTH_TOKEN='oauth:xy8beq6ubgunfjbpgvb1e7bfsb7uxu'
TWITCH_BOT_NAME='auroraencodeai'
TWITCH_BOT_PREFIX='!'
TWITCH_CHANNEL = '#auroraencodeai'
```

Our Twitch account details (Will be deleted after hackathon!)

```bash
username: AuroraEncodeAI
password: L"-?J;A6dvNV*-e
```

For app verification dm/ask Martin