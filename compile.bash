#sj2842
# this should be run to generate out put from both captioning models simultaneously
#!/bin/bash
cd torch/neuraltalk2
th eval.lua -model /home/shreya94jain/torch/model_id1-501-1448236541.t7  -image_folder /home/shreya94jain/eval -num_images 10 -beam_size 2 > output_cap.txt
cd
cd torch/densecap
th run_model.lua -input_dir /home/shreya94jain/eval
 
