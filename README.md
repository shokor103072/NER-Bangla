# Installation
## PIP installer
`pip install bnlp_toolkit`
## or Upgrade

`pip install -U bnlp_toolkit`
- Python: 3.6, 3.7, 3.8, 3.9
- OS: Linux, Windows, Mac

# Bangali NER
## Train NER Tag Model
- run `python train.py`
```
import json
from bnlp import NER

# Load JSON data 
with open('Bangla-NER-Splitted-Dataset.json', 'r') as f:
    data = json.load(f)

# Convert the data into the required format
def transform_data(data):
    transformed_data = []
    for item in data:
        sentence_data = list(zip(item['sentence'], item['bioes_tags']))
        transformed_data.append(sentence_data)
    return transformed_data

train_data = transform_data(data['train'])
test_data = transform_data(data['test'])

# Initialize the NER model and train
bn_ner = NER()
model_name = "ner_model.pkl"
bn_ner.train(model_name, train_data, test_data)

```
The provided Python script trains a Named Entity Recognition (NER) model using the BNLP toolkit on a JSON dataset which is downloaded [from this repository](https://github.com/MISabic/NER-Bangla-Dataset/tree/master). Post-processing the data, the model training begins and subsequently saves the trained model as 'ner_model.pkl' [model drive_link](https://drive.google.com/file/d/142uUmhN74gKVKZ68fDcYQZjjN0Ygz7Mr/view?usp=drive_link).

During execution, the script displays progress, with 64155 and 3564 representing training and testing instances respectively. Post-training, the script evaluates the model's performance, achieving around 0.9 in both accuracy and F1 Score (micro), and finally confirms that the model is successfully saved.
```
64155
3564
Training Started........
It will take time according to your dataset size...
Training Finished!
Evaluating with Test Data...
Accuracy is: 
0.8999959281729712
F1 Score(micro) is: 
0.8999959281729712
Model Saved!
```

This script will generate a Named Entity Recognition (NER) model, aptly titled 
- `ner_model.pkl` ([Saved Model after training - drive_link](https://drive.google.com/file/d/142uUmhN74gKVKZ68fDcYQZjjN0Ygz7Mr/view?usp=drive_link))
## Find NER Tag Using Trained Model 
if you want to use already trained model please download pretrain model from [google drive](https://drive.google.com/file/d/142uUmhN74gKVKZ68fDcYQZjjN0Ygz7Mr/view?usp=drive_link) (29.8MB) and set the model path in `test.py` file
- run `python test.py`

```
from bnlp import NER

def collect_entities(tagged_text):
    entities = []
    current_entity = []
    for word, tag in tagged_text:
        if tag == 'O':
            if current_entity:
                entities.append(' '.join(current_entity))
                current_entity = []
        elif tag in ['B-PER', 'I-PER', 'E-PER', 'S-PER']:
            current_entity.append(word)
    if current_entity:
        entities.append(' '.join(current_entity))
    return entities

# Load trained model
bn_ner = NER()
model_path = "/content/ner_model.pkl"

# List of texts for Named Entity Recognition
text_list = [
    "আব্দুর রহিম নামের কাস্টমারকে একশ টাকা বাকি দিলাম",
    "১০০ টাকা জমা দিয়েছেন কবির",
    "ডিপিডিসির স্পেশাল টাস্কফোর্সের প্রধান মুনীর চৌধুরী জানান",
    "অগ্রণী ব্যাংকের জ্যেষ্ঠ কর্মকর্তা পদে নিয়োগ পরীক্ষার প্রশ্নপত্র ফাঁসের অভিযোগ উঠেছে।",
    "সে আজকে ঢাকা যাবে",
]

# Perform Named Entity Recognition for each text and extract entities tagged as 'Person'
for text in text_list:
    tagged_text = bn_ner.tag(model_path, text)
    person_entities = collect_entities(tagged_text)
    print(person_entities)



Output :
['আব্দুর রহিম', 'কাস্টমারকে']
['কবির']
['মুনীর চৌধুরী']
['কর্মকর্তা']
[]

```
# References
- [BNLP_TOOLKIT](https://github.com/sagorbrur/bnlp/tree/master)
- [NER DATA](https://github.com/MISabic/NER-Bangla-Dataset/tree/master)
