# CS242 Team 2 Data Generation Code

The main file is diffusion.py, which is run with
`python diffusion.py start_idx end_idx`, where start_idx and end_idx 
specify where in the list of captions to start and end (to allow parallel runs).
The image dataset itself is located at `/n/holystore01/LABS/barak_lab/Everyone/Users/nabreu/cs242/` with subdirectories `filtered` and `unfiltered`.

The ROCO repo is not included in this repo but is available at 'https://github.com/razorx89/roco-dataset'

Code was run with the following script:

#!/bin/bash
#SBATCH -J generate_data
#SBATCH -o printouts/generate_data_%j.out
#SBATCH -e printouts/generate_data_%j.err
#SBATCH -p kempner
#SBATCH --account=kempner_barak_lab
#SBATCH --constraint="a100"
#SBATCH -t 0-23:00
#SBATCH --gres=gpu:1
#SBATCH --mem=32000

module load python
source activate cs242

export PYTHONPATH="${PYTHONPATH}:/"

python diffusion.py 70000 80000

source deactivate