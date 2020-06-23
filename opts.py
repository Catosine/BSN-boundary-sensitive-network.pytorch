"""
@edited_by pengnan.fan@mail.mcgill.ca
@last_update 22 Jun, 2020

Change Log:

[22 Jun, 2020]
Add following flags:
    --pretrained
        This is used to suggest using ActivityNet-pretrained BSN weights for training/inferencing
    
    --pca_model
        This is used to show the path to certain pca models
    
    --customized_data
        This is a flag used to indicate a non-ActivityNet data is feeding into BSN
    
    --dyn_image
        This is a flag used to indicate a dynamic image extracted Tempuckey data is feeding into BSN
    
    --reshape_size
        This is used to linear interpolate non-ActivityNet data for TEM.

    --actioness_loss_weight
        This is used to change the actioness weight of TEM loss.
    
"""

import argparse


def parse_opt():
    parser = argparse.ArgumentParser()
    # Overall settings
    parser.add_argument(
        '--module',
        type=str,
        default='TEM')
    parser.add_argument(
        '--mode',
        type=str,
        default='train')
    parser.add_argument(
        '--checkpoint_path',
        type=str,
        default='./tempuckey_checkpoint')
        
    # Overall Dataset settings
    parser.add_argument(
        '--video_info',
        type=str,
        #default="./data/activitynet_annotations/video_info_new.csv"
        #default="./data/tempuckey_annotations/new_tempuckey_info_split.csv"
        default="/usr/local/data02/zahra/datasets/Tempuckey/labels/tempuckey_video_info_gt_labels_split.csv"
        )
    parser.add_argument(
        '--video_anno',
        type=str,
        #default="./data/activitynet_annotations/anet_anno_action.json"
        #default="./data/tempuckey_annotations/video_labels.json"
        #default="/usr/local/data02/zahra/datasets/Tempuckey/labels/tempuckey_ground_truth_annotations_pf_updated.json"
        default="/usr/local/data02/zahra/datasets/Tempuckey/labels/tempuckey_ground_truth_annotations_bsn.json"
        )
    parser.add_argument(
        '--pca_model',
        type=str,
        #default="/usr/local/data02/zahra/datasets/Tempuckey/tempuckey_pca/c2plus1d_kinetics8_pca_model.m"
        default="/usr/local/data02/zahra/datasets/Tempuckey/tempuckey_pca/dyn_image_win_8_resnet_transformed_pca_model.m"
    )
    parser.add_argument(
        '--customized_data',
        action='store_true'
    )
    parser.add_argument(
        '--dyn_image',
        action='store_true'
    )
    parser.add_argument(
        '--pretrained',
        action='store_true'
    )
    
    # TEM Dataset settings
    parser.add_argument(
        '--temporal_scale',
        type=int,
        #default=100,
        default=512
        )
    parser.add_argument(
        '--boundary_ratio',
        type=float,
        default=0.1)
    parser.add_argument(
        '--feature_path',
        type=str,
        #default="./data/activitynet_feature_cuhk/"
        default="/usr/local/data02/zahra/datasets/Tempuckey/feats/dyn_image/win_8_resnet_transformed/"
        )
    parser.add_argument(
        '--reshape_size',
        type=int,
        #default=512
        default=512
    )

    
    # PEM Dataset settings
    parser.add_argument(
        '--pem_top_K',
        type=int,
        default=500)
    parser.add_argument(
        '--pem_top_K_inference',
        type=int,
        default=1000)

    # TEM model settings
    parser.add_argument(
        '--tem_feat_dim',
        type=int,
        default=400)
    parser.add_argument(
        '--tem_hidden_dim',
        type=int,
        default=512)


    # PEM model settings
    parser.add_argument(
        '--pem_feat_dim',
        type=int,
        default=32)
    parser.add_argument(
        '--pem_hidden_dim',
        type=int,
        default=256)
    
    # TEM Training settings
    parser.add_argument(
        '--tem_training_lr',
        type=float,
        default=0.001)
    parser.add_argument(
        '--tem_weight_decay',
        type=float,
        default=0.0001)
    parser.add_argument(
        '--tem_epoch',
        type=int,
        default=20)
    parser.add_argument(
        '--tem_step_size',
        type=int,
        default=7)
    parser.add_argument(
        '--tem_step_gamma',
        type=float,
        default=0.1)
    parser.add_argument(
        '--tem_batch_size',
        type=int,
        default=16)
    parser.add_argument(
        '--tem_match_thres',
        type=float,
        default=0.5)
    parser.add_argument(
        '--actioness_loss_weight',
        type=float,
        default=2.0)

    # PEM Training settings
    parser.add_argument(
        '--pem_training_lr',
        type=float,
        default=0.01)
    parser.add_argument(
        '--pem_weight_decay',
        type=float,
        default=0.00001)
    parser.add_argument(
        '--pem_epoch',
        type=int,
        default=20)
    parser.add_argument(
        '--pem_step_size',
        type=int,
        default=10)
    parser.add_argument(
        '--pem_step_gamma',
        type=float,
        default=0.1)
    parser.add_argument(
        '--pem_batch_size',
        type=int,
        default=16)
    parser.add_argument(
        '--pem_u_ratio_m',
        type=float,
        default=1)
    parser.add_argument(
        '--pem_u_ratio_l',
        type=float,
        default=2)
    parser.add_argument(
        '--pem_high_iou_thres',
        type=float,
        default=0.6)
    parser.add_argument(
        '--pem_low_iou_thres',
        type=float,
        default=0.2)

    # PEM inference settings
    parser.add_argument(
        '--pem_inference_subset',
        type=str,
        default="valid")

    # PGM settings
    parser.add_argument(
        '--pgm_threshold',
        type=float,
        default=0.5)
    parser.add_argument(
        '--pgm_thread',
        type=int,
        default=8)	
    parser.add_argument(
        '--num_sample_start',
        type=int,
        default=8)
    parser.add_argument(
        '--num_sample_end',
        type=int,
        default=8)
    parser.add_argument(
        '--num_sample_action',
        type=int,
        default=16) # num_sample_start + end + action should equal to pem_feat_dim
    parser.add_argument(
        '--num_sample_interpld',
        type=int,
        default=3)
    parser.add_argument(
        '--bsp_boundary_ratio',
        type=float,
        default=0.2)

    # Post processing
    parser.add_argument(
        '--post_process_top_K',
        type=int,
        default=100)
    parser.add_argument(
        '--post_process_thread',
        type=int,
        default=8)
    parser.add_argument(
        '--soft_nms_alpha',
        type=float,
        default=0.75)
    parser.add_argument(
        '--soft_nms_low_thres',
        type=float,
        default=0.65)
    parser.add_argument(
        '--soft_nms_high_thres',
        type=float,
        default=0.9)
    parser.add_argument(
        '--result_file',
        type=str,
        default="./output/dyn_image/result_proposal.json")
    parser.add_argument(
        '--save_fig_path',
        type=str,
        default="./output/evaluation_result.jpg")

    args = parser.parse_args()

    return args
