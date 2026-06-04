from sklearn.ensemble import IsolationForest

data = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [100]
]

model = IsolationForest(
    random_state=42
)

model.fit(data)

predictions = model.predict(data)

for value, prediction in zip(data, predictions):

    if prediction == -1:
        print(
            f"{value[0]} -> ANOMALY"
        )
    else:
        print(
            f"{value[0]} -> NORMAL"
        )