xray = 0
chest = 0
both = 0
pneumonia = 0
all = 0

ids = set()

with open('roco-dataset/data/train/radiology/keywords.txt', 'r') as f:
    for line in f:
        l = line.split('\t')
        id = l[0]
        keywords = l[1:]
        keywords[-1] = keywords[-1].strip('\n')

        if ('xray' in keywords and 'chest' in keywords and 'pneumonia' in keywords):
            all += 1
            if all < 5:
                print(id)
                print(keywords)
        elif ('xray' in keywords and 'chest' in keywords):
            both += 1
            if both < 5:
                print(id)
                print(keywords)
            ids.add(id)

        if ('xray' in keywords):
            xray += 1
        if ('chest' in keywords):
            chest += 1
        if ('pneumonia' in keywords):
            pneumonia +=1
        
    
with open('roco-dataset/data/train/radiology/captions.txt', 'r') as f1, open('roco-dataset/data/train/radiology/chestxraycaptions.txt', 'w') as f2:
    for line in f1:
        l = line.split('\t')
        id = l[0]
        if id in ids:
            caption = l[1]
            f2.write(f'{id}\t{caption}')

            
    

print(xray)
print(chest)
print(both)
print(all)
print(pneumonia)