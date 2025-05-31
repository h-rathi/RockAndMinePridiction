import pickle
import numpy as np
# Load the model
with open(r"C:\Users\himan\OneDrive\Desktop\RockMine\model.pkl", "rb") as f:
    model = pickle.load(f)
#take user input 
user_input=input("enter values separated by commas to predict rock or mine :")
# make array from user input 
user_input=user_input.split(",")
for i in range(len(user_input)):
  user_input[i]=float(user_input[i])
#convert the array to numpy array
input_np=np.asarray(user_input)
new_input_np=input_np.reshape(1,-1)
#predict the result and print 
result=model.predict(new_input_np)
if result[0]=='R':
  print("The detected object is Rock ")
else:
  print("The detected object is Mine")
input("enter any key to exit")
