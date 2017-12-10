#TJames Moving Rectangle Generator
#Generates a series of movie frames to be compiled into a video

def makeMovieFrame(directory):
  for num in range(1,30): #29 frames, 1 to 29
    canvas = makeEmptyPicture(640,480)
    addRectFilled(canvas, num * 10, num * 5, 50,50, red)
    #convert the number to a string
    numStr = str(num)
    if num < 10:
      writePictureTo(canvas, directory+"\\frame0"+numStr+".jpg")
    if num >= 10:
      writePictureTo(canvas, directory+"\\frame"+numStr+".jpg")
  movie = makeMovieFromInitialFile(directory+"\\frame00.jpg");
  return movie

movieLoc = setMediaFolder()
rectM = makeMovieFrame(movieLoc)
playMovie(rectM)