from transformers import AutoModel, AutoTokenizer
import torch

model_name = 'Alibaba-NLP/gte-multilingual-base'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True)

texts = ["Hello world"]
batch_dict = tokenizer(texts, max_length=8192, padding=True, truncation=True, return_tensors='pt')

# TEST WITHOUT POSITION_IDS
try:
    outputs = model(**batch_dict)
    print("Success without position_ids!")
except Exception as e:
    print(f"Failed without position_ids: {e}")

# TEST WITH POSITION_IDS
print("Trying with explicit position_ids...")
try:
    position_ids = torch.arange(batch_dict['input_ids'].shape[1], dtype=torch.long).unsqueeze(0).expand_as(batch_dict['input_ids'])
    batch_dict['position_ids'] = position_ids
    outputs = model(**batch_dict)
    print("Success with position_ids!")
except Exception as e:
    print(f"Failed with position_ids: {e}")