# **Tempuckey BSN Readme File**
Created by Pengnan Fan on 22 Jun, 2020.  
**Last Update** by Pengnan Fan on 22 Jun, 2020

## Introduction
This repository is developed based on [a PyTorch verion of Boundary Sensitive Network](https://github.com/wzmsltw/BSN-boundary-sensitive-network.pytorch). Some of the codes are edited to run BSN on Tempuckey dataset, a hockey video dataset with "faceoff" action labels.

## RUN101: How to run BSN with Tempuckey
***
> Preparation
1. Setup conda environment. Check [here](#1) for path of requirements.txt.
```bash
# setup conda environment.
conda create --name bsn --file requirements.txt

# then activte it
conda activate bsn
```
2. Prepare PCA models for features. Check for paths: [pca](#6), [dir_to_features](#4)
```bash
# move to pca.py
cd $pca

# run PCA script to get the pca model
python pca.py \
       --feature_dir $dir_to_features \
       --save_dir $where_to_save_pca_model \
       --output_dimension 400 \
```
3. Move to the repository.
***
> TEM Inference
1. To run ActivityNet-pretrained TEM with Tempuckey data. Check for paths: [feature_path](#4), [pca_models](#5)
```bash
python main.py --module TEM \ 
               --mode inference \ 
               
               --feature_path $feature_path \
               --customized_data \
               --dyn_image \ # use this flag if you are using dynamic image features
               
               --pca_model $pca_models \
               --pretrained \ 

# Note: The PCA model should be changed according to the feature path
```
5. To run Tempuckey-preatrained TEM with Tempuckey data. Check for paths: [feature_path](#4), [pca_models](#5)
```bash
python main.py --module TEM \ 
               --mode inference \ 
               
               --feature_path $feature_path \
               --customized_data \
               --dyn_image \ # use this flag if you are using dynamic image features
               
               --pca_model $pca_models \
               --actioness_loss_weight 2.0 \ # for example

# Note: The PCA model should be changed according to the feature path
```
***
> TEM Training
6. To train TEM on Tempuckey data on scratch: Check for paths: [feature_path](#4), [pca_models](#5)
```bash
python main.py --module TEM \ 
               --mode train \ 
               
               --feature_path $feature_path \
               --customized_data \
               --dyn_image \ # use this flag if you are using dynamic image features
               
               --pca_model $pca_models \
               --actioness_loss_weight 2.0 \ # for example

# Note: The PCA model should be changed according to the feature path
```
7. To train TEM on tempuckey with ActivityNet-pretrained model: Check for paths: [feature_path](#4), [pca_models](#5)
```bash
# To be updated
```
***
> PGM
8. To run PGM to outputs of TEM:
```bash
python main.py --module PGM
```
***
> PEM Inference
9. To run ActivityNet-pretrained PEM on outputs of PGM:
```bash
python main.py --module PEM \ 
               --mode inference \
```
10. To run Tempuckey-pretrained PEM on outputs of PGM:
```bash
# To be updated
```
***
> PEM Training
11. To train PEM on Tempuckey:
```bash
# To be updated
```
***
> Post Processing
12. To run post processing to outputs of PEM:
```bash
python main.py --module Post_processing
```

## Paths
**Conda Environment Requirement File**
<span id=1>  
rocket.cim.mcgill.ca:/usr/local/data02/pengnanf/BSN-boundary-sensitive-network.pytorch/requirements.txt
</span>

**Video Infomation File**
<span id=2>
rocket.cim.mcgill.ca:/usr/local/data02/zahra/datasets/Tempuckey/labels/tempuckey_video_info_gt_labels_split.csv
</span>

**Video Annotation File**
<span id=3>
rocket.cim.mcgill.ca:/usr/local/data02/zahra/datasets/Tempuckey/labels/tempuckey_ground_truth_annotations_bsn.json
</span>

**Extracted Features of Tempuckey**  
<span id=4>
<u>C3D pretrained on Kinetics with frames of 8</u>
rocket.cim.mcgill.ca:/usr/local/data02/zahra/datasets/Tempuckey/feats/c2plus1d_kinetics8  
<u>Dynamic Image + ResNet with frames of 8</u>  
rocket.cim.mcgill.ca:/usr/local/data02/zahra/datasets/Tempuckey/feats/dyn_image/win_8_resnet_transformed
</span>

**PCA Models**  
<span id=5>
<u>C3D pretrained on Kinetics with frames of 8</u>
rocket.cim.mcgill.ca:/usr/local/data02/zahra/datasets/Tempuckey/tempuckey_pca/c2plus1d_kinetics8_pca_model.m  
<u>C3D pretrained on Kinetics with frames of 32</u>
rocket.cim.mcgill.ca:/usr/local/data02/zahra/datasets/Tempuckey/tempuckey_pca/c2plus1d_kinetics32_pca_model.m  
<u>Dynamic Image + ResNet with frames of 8</u>  
To be updated
</span>

**Path to PCA**  
<span id=6>
rocket.cim.mcgill.ca:/usr/local/data02/zahra/datasets/Tempuckey/scripts/
</span>