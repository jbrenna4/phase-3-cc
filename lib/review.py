#from lib.movie import Movie
#from lib.viewer import Viewer


class Review:
    
    #5 I import the Classes that we need an instance of...
    # then initialize them
    # lol rating is just a number again. not a float or int
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        self.add_review_to_movie()


    # 6 rating property goes here!
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if type(rating) == int and 0 < rating < 6:
            self._rating = rating

        else:
            raise Exception("Invalid rating")
    

    # 7 jesus here we go... 
    # viewer property goes here!
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        from lib.viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("this viewer is not an instance of Viewer")
        
    # 8 jesus here we go... 
    # movie property goes here!
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        from lib.movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("this movie is not an instance of Movie")
        
    def add_review_to_movie(self):
        from lib.movie import Movie
        self.movie.reviews.append(self)


