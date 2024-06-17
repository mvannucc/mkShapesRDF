# EvaluateRF_1J.py

import joblib
import numpy as np
import os

weight_path_electron = os.path.dirname(__file__) 
rf_0 = joblib.load(weight_path_electron+'/electron_Run3_xgboost_MVA-HWW_weights.pkl')

def load_electron_hwwmva(inputs_0):
    try:
        result = rf_0.predict_proba(np.array(inputs_0).reshape(1, -1))
        return [result[0][1]]
    except Exception as e:
        return [-99.9]

if __name__ == "__main__":
    # You can include some test code here for local testing
    test_input = [1.0, 2.0, 3.0, 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15.]
    result = load_random_forest_model(test_input)
    print("Result:", result)
