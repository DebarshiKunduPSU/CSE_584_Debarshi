from datasets import load_dataset
import re
import pandas as pd

# Load the IMDB dataset instead of WikiText
dataset = load_dataset("imdb")


def truncate_sentences(text, num_words=5):
    # Split the text into sentences based on punctuation
    sentences = re.split(r'(?<=[.!?]) +', text)
    truncated_texts = []

    # Process each sentence, truncating to the specified number of words
    for sentence in sentences:
        # Take the first 'num_words' words
        words = sentence.split()[:num_words]
        truncated_text = ' '.join(words)  # Join them back into a string

        if truncated_text:  # Only add non-empty strings
            truncated_texts.append(truncated_text)

    return truncated_texts


truncated_dataset = []

# Go through the first 1000 text samples in the dataset and truncate them
for text in dataset['train']['text'][:1000]:
    truncated_dataset.extend(truncate_sentences(text))

# Convert the truncated texts into a DataFrame
df = pd.DataFrame(truncated_dataset, columns=["truncated_text"])

# Save the DataFrame to a CSV file named xi.csv
df.to_csv("truncated.csv", index=False)
