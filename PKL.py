import pickle

# Load the object from the .pkl file
with open('C:\\Users\\21276\\OneDrive\\Bureau\\machinelearningprojet\\nlp_model.pkl', 'rb') as f:
    loaded_object = pickle.load(f)

# Now, you can inspect or use the loaded object
print(loaded_object)
