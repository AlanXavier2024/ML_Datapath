import pickle
model_loaded = pickle.load(open('./model_saved', 'rb'))

def prediccion_titanic (*args):
    arguments = []
    for arg in args:
        arguments.append(arg)
    model_loaded.predict(arguments)
    return model_loaded

