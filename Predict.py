from sklearn.externals import joblib
clf = joblib.load('Tengen_Toppa_mega_faggot.pkl')

def predict(txt):
    result = clf.predict([txt])[0]
    return result