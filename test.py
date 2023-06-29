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
model_path = "./ner_model.pkl"

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
