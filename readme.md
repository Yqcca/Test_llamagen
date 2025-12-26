# Running Instructions

## Environment Setup

1. First, ensure you have Conda installed on your system. If not, please install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution).

2. Create and activate the conda environment using the provided `environment.yml` file:

```bash
conda env create -f environment.yml
conda activate llamagen
```
If you want to install the environment in a specific directory, you can use the following command:
```bash
conda env create -f environment.yml -p /path/to/your/env
```
If you meet several errors, you need try to install the certain package in the environment.yml file.


## Environment Configuration

The `environment.yml` file specifies all required dependencies. Below is an example:

```yaml
name: llamagen
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.8
  - pip
  - pip:
    - torch
    - transformers
    ...
```

## Prerequisite
1. Download the CUB dataset and place it in the directory `Test_llamagen/Datasets`:
```bash
wget https://data.caltech.edu/records/65de6-vp158/files/CUB_200_2011.tgz
tar -xzvf CUB_200_2011.tgz
```

2. Download the **VAE checkpoint** and place it in `Test_llamagen/pretrained_models/vae`:

```bash
wget https://huggingface.co/FoundationVision/LlamaGen/resolve/main/vq_ds16_c2i.pt
```

## Running the Script

1. Make sure the run.sh script has execute permissions:
```bash
chmod +x run.sh
```

2. Execute the script:
```bash
./run.sh
```

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are properly installed
2. Check that your Python version matches the one specified in environment.yml
3. Verify that run.sh has proper execute permissions
4. Check the logs for any error messages

## Additional Notes
- In run.sh, you need to modify the project root path, conda environment path, dataset path, model path, etc.
- The script requires sufficient disk space and memory
- GPU support is recommended for optimal performance
- For detailed logs, check the output directory after running the script