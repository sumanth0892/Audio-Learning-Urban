#Librosa has an MFCC label which extracts Mel-Frequency Cepstral Coefficients
import os 
import pandas as pd
import librosa as lb
import numpy as np 

dataSetPath = '/Users/computer/Documents/audioLearning/UrbanSound8K/'
metaFile = '/Users/computer/Documents/audioLearning/UrbanSound8K/UrbanSound8K.csv'
metadata = pd.read_csv(metaFile)



def extractFeatures(fileName):
	audio,sampleRate = lb.load(fileName,res_type = 'kaiser_fast')
	mfcc = lb.feature.mfcc(y = audio,sr = sampleRate,n_mfcc = 40)
	mfccScaled = np.mean(mfccs.T,axis=0)
	return mfccScaled


def getDF(dataPath = dataSetPath):
	features = []
	for index,row in metadata.iterrows():
		fileName = os.path.join(os.path.abspath(dataPath),'fold'+str(row["fold"])+'/',str(row["slice_file_name"]))
		classLabel = row['classID']
		data = extractFeatures(fileName)
		features.append([data,classLabel])
	featuresDF = pd.DataFrame(features,columns = ['Features','ClassLabel'])
	return featuresDF
	print(featuresDf.info())

def splitDataSet():
	from sklearn.model_selection import train_test_split
	featuresDF = getDF()
	X = np.array(featuresDF.feature.tolist())
	Y = np.array(featuresDF.ClassLabel.tolist())
	return (X,Y)






 



