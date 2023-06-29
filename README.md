# Installation
## PIP installer
`pip install bnlp_toolkit`
## or Upgrade

`pip install -U bnlp_toolkit`
- Python: 3.6, 3.7, 3.8, 3.9
- OS: Linux, Windows, Mac

# Bangali NER
## Train NER Tag Model
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
The block of Python code provided above is a script for training a Named Entity Recognition (NER) model using the BNLP toolkit. The script loads a dataset in JSON format which is downloaded [from this repository](https://github.com/MISabic/NER-Bangla-Dataset/tree/master), processes the data into a suitable format for training, initializes a new NER model, and trains it using the prepared data. The model, once trained, is saved as ner_model.pkl.

Upon execution, this script displays the progress of the training process. The numbers 64155 and 3564 likely represent the number of training and testing instances respectively. The script will then indicate that the training has started and will take some time depending on the size of the dataset.

Once the training process is complete, the script evaluates the model's performance using the test data, and provides two metrics: accuracy and F1 Score (micro). Finally, it indicates that the model has been saved successfully.
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
- `ner_model.pkl`
## Find NER Tag Using Trained Model

```
from bnlp import NER
bn_ner = NER()
model_path = "model/ner_model.pkl"
text = "ডিপিডিসির স্পেশাল টাস্কফোর্সের প্রধান মুনীর চৌধুরী জানান "
result = bn_ner.tag(model_path, text)
# Filter the results to only include 'Person' tag
person_tags = [t for t in result if t[1] == 'B-PER' or t[1] == 'E-PER' or t[1] == 'S-PER']

print(person_tags)
[('মুনীর', 'B-PER'), ('চৌধুরী', 'E-PER')]
print(result)
[('ডিপিডিসির', 'O'), ('স্পেশাল', 'O'), ('টাস্কফোর্সের', 'O'), ('প্রধান', 'O'), ('মুনীর', 'B-PER'), ('চৌধুরী', 'E-PER'), ('জানান', 'O')]
```
