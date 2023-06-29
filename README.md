# Installation
## PIP installer
`pip install bnlp_toolkit`
## or Upgrade

`pip install -U bnlp_toolkit`
- Python: 3.6, 3.7, 3.8, 3.9
- OS: Linux, Windows, Mac

# Bangali NER
## Train NER Tag Model `train.py`
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
- `ner_model.pkl` 
- [Saved Model after Training - drive_link](https://drive.google.com/file/d/142uUmhN74gKVKZ68fDcYQZjjN0Ygz7Mr/view?usp=drive_link)
## Find NER Tag Using Trained Model `test.py`

```
from bnlp import NER
bn_ner = NER()
model_path = "./path/ner_model.pkl"
text = "ডিপিডিসির স্পেশাল টাস্কফোর্সের প্রধান মুনীর চৌধুরী জানান "
result = bn_ner.tag(model_path, text)
print(result)
[('ডিপিডিসির', 'O'), ('স্পেশাল', 'O'), ('টাস্কফোর্সের', 'O'), ('প্রধান', 'O'), ('মুনীর', 'B-PER'), ('চৌধুরী', 'E-PER'), ('জানান', 'O')]

# Filter the results to only include 'Person' tag
person_tags = [t for t in result if t[1] == 'B-PER' or t[1] == 'E-PER' or t[1] == 'S-PER']
print(person_tags)
[('মুনীর', 'B-PER'), ('চৌধুরী', 'E-PER')]

```
# References
- [BNLP_TOOLKIT](https://github.com/sagorbrur/bnlp/tree/master)
- [NER DATA](https://github.com/MISabic/NER-Bangla-Dataset/tree/master)
