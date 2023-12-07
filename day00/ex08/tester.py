from tqdm import tqdm

def process_items(items):
    for item in tqdm(items, desc="Processing"):
        # Process item here
        processed_item = item * 2
        yield processed_item

# Using the generator function
my_items = [1, 2, 3, 4, 5]
result_generator = process_items(my_items)

for processed_item in result_generator:
    print(processed_item)
