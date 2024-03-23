from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


x = data[data.columns.difference(['likes'])]
y = data['likes']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=6)


model = LinearRegression()
model.fit = model.fit(x_train, y_train)
accuracy = model.fit.score(x_test, y_test)
print(accuracy)

y_pred = model.predict(x_test)
