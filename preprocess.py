import pandas as pd

df = pd.read_csv("/content/flickr30k_images/results.csv", delimiter="|")
print(df.columns)

df.columns = ['image', 'caption_number', 'caption']
print(df[df.isnull().any(axis=1)])

df.loc[19999, 'caption_number'] = "4"
df.loc[19999, 'caption'] = "A dog runs across the grass ."

ids = [id_ for id_ in range(len(df) // 5) for _ in range(5)]
df['id'] = ids
df.to_csv("captions.csv", index=False)

image_path = "/flickr30k_images/flickr30k_images"
captions_path = "/"

print(df.head())

