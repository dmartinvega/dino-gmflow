# DINO + GMFlow: Deep learning optical flow enhanced with deep learning segmentation

This project combines two main submodules: DINO (for segmentation) and GMFlow (for optical flow). 
It also uses a submodule with general computer vision utilities.

## How to run this project
I ran this project using PyCharm as IDE. In Settings > Project structure: every submodule folder was selected as a source (so they were colored to blue)
Unfortunately, we were not able to create a unique conda environment that is able to manage all the submodules. 

Every submodule has its own dependencies and there were conflicts among them when trying to use only one environment. 
We are using conda virtual environments to run the submodules

### DINO submodule
The biggest issue happened with two libraries needed by DINO (mmcv-full==1.5.0 and mmsegmentation==0.27.0).
These libraries are, unfortunately, compiled using cuda version of the driver (nvidia-smi) and the libraries need the version 11.7.
Whereas Arch Linux, which is my current OS, is running cuda 12.4. 
I do not remember if I changed the Arch cuda driver version to 11.7, but I probably tried.
So at the end the only solution I could find was:
- Boot a flash drive with Ubuntu, in version 20.04 because that was the only version that let me install nvidia-smi 11.7.
- Create the conda environment for DINO from that OS.
- I got an error running the project, that was not letting me install the right python version. I got the following message:
"GeForce RTX 3080 with CUDA capability sm_86 is not compatible with the current PyTorch installation", and I found the solution [here](https://github.com/pytorch/pytorch/issues/45028), by the user 9cat
> the following works for me:
> 
> pip3 install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html

I ran this on the terminal because I was not able to add it to the conda environment, although it may exist a way to do it from the yml file.
- Run this submodule only on that OS. The name of the environment is TODO.

### GMFlow (unimatch)
This submodule can be run in Arch Linux.
GMFlow is run under unimatch repository. The reason of this is that GMFlow is 1/3 of unimatch.
unimatch also has depth and stereo capabilities on it, but we are not using them in this project.
The right virtual environment for this project is unimatch_2, which is in the file conda_environment.yml.

main_unimatch.py is the file I am using to run this submodule.
