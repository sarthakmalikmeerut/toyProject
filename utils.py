import pickle
import numpy as np


class HelloWorld:
    def zero_shot(self, cgpa, iq):
        # Prepare input as a 2D array for prediction
        input_data = np.array([[cgpa, iq]])

        # Load the trained model from pickle file
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)

        # Make prediction
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            return "Placement hojayegi"
        else:
            return "Placement nahi hogi"


# # Create an instance of HelloWorld
# hello_world = HelloWorld()
#
# # Example inputs: CGPA=8.5, IQ=120
# placement = hello_world.zero_shot(8.5, 120)
#
# # Output the placement result
# print(f"Predicted Placement: {placement}")
