#Let's analyze each audio file in more detail 
import os 
import pandas as pd
import librosa as lb 
from fileHelper import waveHelper 

helper = waveHelper()

audioData = []
metaFile = '/Users/computer/Documents/audioLearning/UrbanSound8K/UrbanSound8K.csv'
metadata = pd.read_csv(metaFile)
dataSetPath = '/Users/computer/Documents/audioLearning/UrbanSound8K/'

for index,row in metadata.iterrows():
	fileName = os.path.join(os.path.abspath(dataSetPath),'fold'+str(row["fold"])+'/',str(row["slice_file_name"]))
	data = helper.readFileProps(filename)
	audioData.append(data)

#Convert into a dataframe 
audioDF = pd.DataFrame(audioData,columns = [nChannels,sampleRate,bitDepth])


