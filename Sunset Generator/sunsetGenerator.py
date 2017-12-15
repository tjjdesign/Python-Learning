def slowSunset(directory):
  canvas = makePicture("landscape.jpg")
  for num in range(1,100): #99 frames
    printNow("Frame number: "+str(num))
    makeSunset(canvas)
    writeFrame(num, directory, canvas)

def makeSunset(picture):
  for p in getPixels(picture):
    value = getBlue(p)
    setBlue(p,int(value*0.99))
    value = getGreen(p)
    setGreen(p,int(value*0.99))

def writeFrame(num,dir,pict):
  #have to deal with many digits
  numStr = str(num)
  if num < 10:
    writePictureTo(pict,dir+"//frame00"+numStr+".jpg")
  if num >= 10 and num < 100:
    writePictureTo(pict,dir+"//frame0"+numStr+".jpg")
  if num >= 100:
    writePictureTo(pict,dir+"//frame"+numStr+".jpg")

slowSunset(setMediaFolder())
