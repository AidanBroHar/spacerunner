from modelLoader import loadModel

def compile(model_path):
    """Compile a ML model from a given path."""
    loaded_model = loadModel(model_path)
    #optimize, quantize, loadgen
    return {
        "model_bin": ...,
        "c_runtume": ...,
        "model_metadata": ...
    }

