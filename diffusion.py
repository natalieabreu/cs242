import torch
from diffusers import StableDiffusionPipeline
from tqdm import tqdm
import sys
import os

model_id = "Nihirc/Prompt2MedImage"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

out_dir = '/n/holystore01/LABS/barak_lab/Everyone/Users/nabreu/cs242/nonfiltered'
captions_dir = '/n/holyscratch01/barak_lab/Users/nabreu/cs242/roco-dataset/data/train/radiology/captions.txt'
exclude_dir = '/n/holyscratch01/barak_lab/Users/nabreu/cs242/roco-dataset/data/train/radiology/chestxraycaptions.txt'
num_images = 10

start = int(sys.argv[1])
end = int(sys.argv[2])
print(start, end)

exclude_count = 0

with open(captions_dir, 'r') as captions_file, open(exclude_dir, 'r') as exclude_file:
    eid = exclude_file.readline().split('\t')[0]
    for i, caption in enumerate(captions_file):
        c = caption.split('\t')
        id = c[0]
        
        if id == eid:
            exclude_count += 1
            continue
        else:
            while eid != '' and eid < id:
                eid = exclude_file.readline().split('\t')[0]
                if id == eid:
                    exclude_count += 1
                    continue

        if int(id.split('_')[-1] ) < start:
            continue

        if int(id.split('_')[-1] ) >= end:
            print(f"Reached {id}, terminating.")
            break

        if os.path.isfile(f'{out_dir}/ROCO_{id}_9.png'):
            print(f'skipping {id}')
            continue
        elif os.path.isfile(f'{out_dir}/ROCO_{id}_0.png'):
            current_count = 0
            for j in range(num_images):
                if os.path.isfile(f'{out_dir}/ROCO_{id}_{j}.png'): 
                    current_count += 1
                else:
                    break
            prompt = c[1]
            # prompt = caption
            images = pipe(prompt, num_images_per_prompt=num_images-current_count).images

            for j in range(current_count, num_images):
                images[j-current_count].save(f'{out_dir}/ROCO_{id}_{j}.png')
        else:

            prompt = c[1]
            # prompt = caption
            images = pipe(prompt, num_images_per_prompt=num_images).images

            for j in range(num_images):
                images[j].save(f'{out_dir}/ROCO_{id}_{j}.png')

print(exclude_count)
# prompt = "Showing the subtrochanteric fracture in the porotic bone."
# prompt = 'Computed tomography revealing right upper-lung pneumonia, the air–fluid level, and septic embolism'

# prompt = 'Pneumothorax evident on the left, with associated collapse x-ray'
# images = pipe(prompt, num_images_per_prompt=5).images

# for i in range(5):
#     images[i].save(f"pneumothorax-xray-{i}.png")

 
# with open("roco-dataset/data/train/radiology/captions.txt", "r") as f:
#     for i in range(3):
#         l = f.readline().split('\t')
#         prompt = l[1]
#         print(prompt)
#         image = pipe(prompt).images[0]  
    
#         image.save(f'{l[0]}.png')
