python train.py --dataroot ~/datasets/celeba_crop/img_align_celeba/ --name face_glass_mouth --model cycle_gan --dataset_mode unaligned_fromlist --img_list_A img_list_wearglass_mouthclosed.txt --img_list_B img_list_noglass_mouthopen.txt --no_dropout --gpu_ids 0,1 --batchSize 4 --lambda_identity 0