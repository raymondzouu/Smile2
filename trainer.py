from sklearn import metrics
import numpy
import pickle
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from numpy import *
import cv2
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import datasets


# def train_and_evaluate(clf, X_train, X_test, y_train, y_test):
#     clf.fit(X_train, y_train)
#
#     print("Accuracy on training set:")
#     print(clf.score(X_train, y_train))
#     print("Accuracy on testing set:")
#     print(clf.score(X_test, y_test))
#
#     y_pred = clf.predict(X_test)
#
#     print("Classification Report:")
#     print(metrics.classification_report(y_test, y_pred))
#     print("Confusion Matrix:")
#     print(metrics.confusion_matrix(y_test, y_pred))


# def predict_face_is_smiling(extracted_face):
#     return svc_1.predict(extracted_face)


# svc_1 = SVC(kernel='linear')
# faces = datasets.fetch_olivetti_faces()
#
# results = {'0': '0', '1': '0', '2': '0', '3': '0', '4': '0', '5': '0', '6': '0', '7': '0', '8': '0', '9': '0', '10': '0', '11': '0', '12': '0', '13': '0', '14': '0', '15': '0', '16': '0', '17': '0', '18': '0', '19': '0', '20': '1', '21': '1', '22': '0', '23': '0', '24': '0', '25': '0', '26': '1', '27': '1', '28': '0', '29': '0', '30': '0', '31': '0', '32': '0', '33': '0', '34': '0', '35': '0', '36': '0', '37': '0', '38': '0', '39': '0', '40': '1', '41': '1', '42': '1', '43': '1', '44': '1', '45': '1', '46': '1', '47': '1', '48': '1', '49': '1', '50': '0', '51': '1', '52': '0', '53': '0', '54': '0', '55': '0', '56': '0', '57': '0', '58': '0', '59': '0', '60': '1', '61': '1', '62': '1', '63': '1', '64': '0', '65': '1', '66': '0', '67': '0', '68': '0', '69': '1', '70': '0', '71': '0', '72': '0', '73': '0', '74': '1', '75': '1', '76': '0', '77': '1', '78': '0', '79': '0', '80': '0', '81': '1', '82': '0', '83': '1', '84': '1', '85': '0', '86': '0', '87': '0', '88': '0', '89': '0', '90': '1', '91': '1', '92': '1', '93': '1', '94': '0', '95': '0', '96': '0', '97': '0', '98': '1', '99': '0', '100': '0', '101': '1', '102': '1', '103': '0', '104': '0', '105': '0', '106': '0', '107': '0', '108': '0', '109': '0', '110': '0', '111': '1', '112': '0', '113': '0', '114': '0', '115': '0', '116': '1', '117': '0', '118': '0', '119': '1', '120': '0', '121': '0', '122': '0', '123': '0', '124': '0', '125': '0', '126': '0', '127': '0', '128': '1', '129': '1', '130': '0', '131': '0', '132': '0', '133': '0', '134': '0', '135': '0', '136': '0', '137': '0', '138': '0', '139': '0', '140': '0', '141': '1', '142': '0', '143': '0', '144': '0', '145': '0', '146': '1', '147': '0', '148': '0', '149': '0', '150': '0', '151': '0', '152': '0', '153': '1', '154': '0', '155': '0', '156': '0', '157': '0', '158': '0', '159': '0', '160': '1', '161': '0', '162': '1', '163': '0', '164': '1', '165': '1', '166': '1', '167': '1', '168': '1', '169': '0', '170': '0', '171': '0', '172': '0', '173': '1', '174': '1', '175': '0', '176': '0', '177': '0', '178': '0', '179': '0', '180': '0', '181': '0', '182': '0', '183': '0', '184': '0', '185': '0', '186': '1', '187': '0', '188': '0', '189': '0', '190': '1', '191': '0', '192': '0', '193': '0', '194': '0', '195': '0', '196': '0', '197': '0', '198': '0', '199': '0', '200': '1', '201': '1', '202': '1', '203': '0', '204': '0', '205': '0', '206': '0', '207': '1', '208': '0', '209': '0', '210': '1', '211': '1', '212': '1', '213': '1', '214': '1', '215': '0', '216': '1', '217': '1', '218': '0', '219': '1', '220': '0', '221': '0', '222': '0', '223': '0', '224': '0', '225': '0', '226': '0', '227': '0', '228': '0', '229': '0', '230': '0', '231': '0', '232': '0', '233': '0', '234': '1', '235': '0', '236': '0', '237': '0', '238': '0', '239': '0', '240': '1', '241': '0', '242': '1', '243': '0', '244': '0', '245': '0', '246': '1', '247': '1', '248': '0', '249': '1', '250': '0', '251': '0', '252': '0', '253': '1', '254': '0', '255': '1', '256': '0', '257': '0', '258': '1', '259': '1', '260': '1', '261': '1', '262': '0', '263': '1', '264': '1', '265': '0', '266': '0', '267': '1', '268': '1', '269': '0', '270': '0', '271': '0', '272': '0', '273': '0', '274': '0', '275': '0', '276': '1', '277': '0', '278': '0', '279': '0', '280': '0', '281': '0', '282': '0', '283': '0', '284': '0', '285': '0', '286': '0', '287': '0', '288': '0', '289': '0', '290': '0', '291': '0', '292': '0', '293': '0', '294': '1', '295': '0', '296': '0', '297': '0', '298': '0', '299': '0', '300': '0', '301': '0', '302': '0', '303': '0', '304': '0', '305': '0', '306': '0', '307': '0', '308': '0', '309': '0', '310': '0', '311': '0', '312': '0', '313': '0', '314': '0', '315': '0', '316': '0', '317': '0', '318': '0', '319': '0', '320': '0', '321': '0', '322': '0', '323': '1', '324': '1', '325': '1', '326': '1', '327': '1', '328': '1', '329': '0', '330': '0', '331': '0', '332': '0', '333': '0', '334': '0', '335': '0', '336': '0', '337': '0', '338': '0', '339': '0', '340': '1', '341': '1', '342': '1', '343': '1', '344': '0', '345': '1', '346': '0', '347': '0', '348': '1', '349': '1', '350': '1', '351': '0', '352': '0', '353': '0', '354': '1', '355': '0', '356': '0', '357': '0', '358': '0', '359': '0', '360': '0', '361': '1', '362': '0', '363': '0', '364': '0', '365': '0', '366': '0', '367': '1', '368': '0', '369': '0', '370': '0', '371': '0', '372': '0', '373': '0', '374': '0', '375': '0', '376': '0', '377': '0', '378': '0', '379': '0', '380': '1', '381': '1', '382': '1', '383': '1', '384': '1', '385': '1', '386': '1', '387': '1', '388': '0', '389': '1', '390': '0', '391': '1', '392': '1', '393': '1', '394': '0', '395': '1', '396': '0', '397': '1', '398': '0', '399': '0'}

picklefile = 'smile_model'
filename = 'asdf.jpg'

infile = open(picklefile, 'rb')
svc_1 = pickle.load(infile, encoding='bytes')

face = cv2.imread(filename)
face.resize(64, 64)
print(svc_1.predict([face.ravel()]))

# indices = [i for i in range(400)]
# data = faces.data[indices, :]
# target = [results[i] for i in results]
# target = numpy.array(target).astype(int)
# X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.25, random_state=0)
# train_and_evaluate(svc_1, X_train, X_test, y_train, y_test)

outfile = open(picklefile, 'wb')
pickle.dump(svc_1, outfile)
outfile.close()