from datasets import Dataset
from datasets import load_dataset

solid = Dataset.to_pandas(load_dataset('tharindu/SOLID', split='train'))

import json
json_records = []
for index, row in solid.iterrows():
    instruction = "Comments containing any form of non-acceptable language (profanity) or a targeted offence, which can be veiled or direct, are offensive comments. This includes insults, threats, and posts containing profane language or swear words. Comments that do not contain offence or profanity are not offensive. Is this tweet offensive or not?"
    input = row['text'].strip()
    if row['average'] > 0.7 and row['std'] < 0.1:
      output = "This is an offensive Tweet"
    elif row['average'] < 0.3 and row['std'] < 0.1:
      output = "This is not an offensive Tweet"

    # Create a JSON record
    json_record = {
        'instruction': instruction,
        'input': input,
        'output': output
    }

    # Append the JSON record to the list
    json_records.append(json_record)


output_json_file = 'output_solid.json'
with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(json_records, json_file, ensure_ascii=False, indent=2)

print(f"JSON records saved to {output_json_file}")