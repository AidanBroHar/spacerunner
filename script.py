import spacerunner

# 1. Call your separate file functions directly from the package root
compiled = spacerunner.compile("./local_models/gptneox_Opset16.onnx")
print(compiled["graph"])