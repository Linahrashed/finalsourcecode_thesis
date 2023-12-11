import ktrain

# Path to the saved model
model_path = "models/bert_model"

# Reload the predictor
predictor = ktrain.load_predictor(model_path)

# Now you can use the predictor to make predictions
message = 'I just broke up with my boyfriend'
prediction = predictor.predict(message)
print('Predicted emotion:', prediction)

# If you want to print the probabilities for each class
probabilities = predictor.predict_proba(message)
class_names = predictor.get_classes()

print('Predicted probabilities:')
for class_name, probability in zip(class_names, probabilities):
    print(f"{class_name}: {probability:.2f}")
