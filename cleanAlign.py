import sys
import os
import json


def cleanAlign():
	
	numDel = 0
	numCop = 0

	srcFileName = "lm.json"
	if 1 < len( sys.argv ):
		if 0 < len( sys.argv[ 1 ] ):
			srcFileName = sys.argv[ 1 ]
	
	srcFile = open( srcFileName )
	srcJson = json.load( srcFile )
	dstJson = {}

	for fileName in srcJson:
		print( fileName, end="" )
		faces = srcJson[ fileName ]
		if 0 < len( faces ):
			dstJson[ fileName ] = faces
			numCop += 1
			print( " -> copied " + str( numCop ) )
		else:
			numDel += 1
			print( " -> deleted " + str( numDel ) )
	
	print( "Original " + str( numCop + numDel ) + " - Deleted " + str( numDel )+ " -> New " + str( numCop ) )

	srcFile.close()
	
	dstFile = open( os.path.splitext( srcFileName )[ 0 ] + '_cleaned.json', 'w' )
	json.dump( dstJson, dstFile, indent=1 )
	dstFile.close()

if __name__=='__main__':
	cleanAlign()
