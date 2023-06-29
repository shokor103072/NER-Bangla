from bnlp import NER
bn_ner = NER()
model_path = r"C:\Users\HP\Desktop\NER_Bangla\model\ner_model.pkl"
text = "ডিপিডিসির স্পেশাল টাস্কফোর্সের প্রধান মুনীর চৌধুরী জানান "
result = bn_ner.tag(model_path, text)
# Filter the results to only include 'Person' tag
person_tags = [t for t in result if t[1] == 'B-PER' or t[1] == 'E-PER' or t[1] == 'S-PER']

print(person_tags)
print(result)