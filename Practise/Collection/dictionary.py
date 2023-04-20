# dictionary- a changable , unordered collection of unique key value :pair
# fast becoz they use hashing allow us to access a value quickly

capitals = {'India': 'Newdelhi',
            'Finland': 'Helsinki',
            'Poland': 'Warsaw'}
print(capitals['India'])
# print(capitals['Germany']) if key doesn't exist , error will occur

capitals.update({'India': 'Bharat'})
capitals.pop('Poland')  # remove the key value pair
# capitals.clear() # clear the dictionary

print(capitals.get('Germany'))  # safer method is get instead of directly asking for key
print(capitals.keys())
print(capitals.values())
print(capitals.items())  # it will print all the key value pairs

for key, value in capitals.items():
    print(key, value)
