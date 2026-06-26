import os
import onnx
import onnxruntime as ort

def loadModel(model_path: str): 
    """Load a ML model from a given path."""
    model = onnx.load(model_path)
    onnx.checker.check_model(model)
    return model