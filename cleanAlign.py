import sys
import os
import json


def cleanAlign():
	
	numDel = 0
	srcFileName = "lm.json"
	if 1 < len( sys.argv):
		if 0 < len(sys.argv[1]):
			srcFileName = sys.argv[1]
	
	srcFile = open( srcFileName )
	srcJson = json.load( srcFile )
	dstJson = {}

	for fileName in srcJson:
		print(fileName, end="" )
		faces = srcJson[ fileName ]
		if 0 < len(faces):
			dstJson[ fileName ] = faces
			print( " -> copied")
		else:
			numDel++
			print( " -> deleted " + numDel )
	
	srcFile.close()
	
	dstFile = open( os.path.splitext( srcFileName )[ 0 ] + '_cleaned.json','w')
	json.dump(dstJson,dstFile,indent=1)
	dstFile.close()

if __name__=='__main__':
	cleanAlign()
