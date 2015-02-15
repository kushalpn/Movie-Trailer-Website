
class Movies():
	''' The class Movies is a class file that describes the way the object will 
	be constructed. __init__ method will initialize the object movie with the parameters 
	given by the user. ''' 

	
	def __init__(self,movie_title,poster_image_url,trailer_youtube_url):
		self.title = movie_title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		# print("Movie object created")
	



