import pytest

# TODO: add necessary import
import numpy as np
from ml.model import train_model, compute_model_metrics
from ml.data import apply_label
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_apply_label():
    """
    Test that apply_label returns correct income label based on binary input.
    """
    assert apply_label(np.array([1])) == ">50K"
    assert apply_label(np.array([0])) == "<=50K"


# TODO: implement the second test. Change the function name and input as needed
def test_train_model_type():
    """
    Test that train_model returns a RandomForestClassifier.
    """
    X_dummy = np.array([[0, 1], [1, 0]])
    y_dummy = np.array([0, 1])
    model = train_model(X_dummy, y_dummy)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics_type():
    """
    Test that compute_model_metrics returns three floats.
    """
    y_true = np.array([1, 0, 1, 1])
    y_pred = np.array([1, 0, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)
