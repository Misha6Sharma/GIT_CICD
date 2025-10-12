from app.main import model
from sklearn.datasets import load_iris

def test_model_predict():
    iris = load_iris()
    X = iris.data
    preds = model.predict(X)
    assert len(preds) == len(X)
