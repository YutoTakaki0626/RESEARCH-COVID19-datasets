import joblib

def dumpJoblib(fileName, obj):
    with open(fileName, mode="wb") as f:
        joblib.dump(obj, f, compress=3)
        
def loadJoblib(fileName):
    with open(fileName, mode="rb") as f:
        return joblib.load(f)