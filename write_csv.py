import csv
import os
import pandas as pd
captions_dir = '/n/holyscratch01/barak_lab/Users/nabreu/cs242/roco-dataset/data/train/radiology/captions.txt'
filtered_dir = '/n/holystore01/LABS/barak_lab/Everyone/Users/nabreu/cs242/filtered'
out_dir = '/n/holystore01/LABS/barak_lab/Everyone/Users/nabreu/cs242/nonfiltered'

# with open('included_data_2.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ',
#                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     with open(captions_dir, 'r') as captions_file:
#         for i, line in enumerate(captions_file):
#             c = line.split('\t')
#             id = c[0]
#             caption = c[1].strip()

#             # if (int(id.split('_')[-1]) > 20846):
#             #     break
#             if os.path.isfile(f'{filtered_dir}/{id}_9.png') and os.path.isfile(f'{out_dir}/ROCO_{id}_9.png'):
#                 writer.writerow([id, caption, 1])
#                 print(f'{id} duplicated')
#             elif os.path.isfile(f'{out_dir}/ROCO_{id}_9.png'):
#                 writer.writerow([id, caption, 0])
#             elif os.path.isfile(f'{filtered_dir}/{id}_9.png'):
#                 writer.writerow([id, caption, 1])
#             elif os.path.isfile(f'{out_dir}/ROCO_{id}_0.png') or os.path.isfile(f'{filtered_dir}/{id}_0.png'):
#                 print(f'{id} incomplete')

# filtered_count = 0
# with open('included_data_2.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for i, row in enumerate(spamreader):
#         filtered_count += int(row[-1])
#         if i < 5:
#             print(', '.join(row))

# print(filtered_count)


df = pd.read_csv("included_data_2.csv", sep='|', on_bad_lines='warn')
print(df.head())

for index, row in df.iterrows():
    if index > 5:
        break
    print(row[0], row[1], row[2])