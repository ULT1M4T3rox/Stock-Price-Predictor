import pickle
with open("resources/pred_stocks.pkl","rb") as file:
    stoxdata=pickle.load(file)

print(stoxdata)