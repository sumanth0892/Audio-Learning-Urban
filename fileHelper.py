import struct 

class waveHelper():
	def readFileProps(self,fileName):
		#Read the properties of the audio file
		waveFile = open(fileName,'rb')

		riff = waveFile.read(12)
		Format = waveFile.read(36)

		nChannels = Format[10:12]
		nChannels = struct.unpack('<H', nChannels)[0]

		sampleRate = Format[12:16]
		sampleRate = struct.unpack('<I', sampleRate)[0]

		bitDepth = Format[22:24]
		bitDepth = struct.unpack('<H', bitDepth)[0]

		return (nChannels,sampleRate,bitDepth)


