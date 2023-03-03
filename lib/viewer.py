class Viewer:


    # 3 initialization of username
    def __init__(self, username):
        self.username = username
        
        # 9 and 10 README is asking for some empty lists
        self.reviews = []
        self.reviewed_movies = []


    # 4 username property goes here with conditions and Exception
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and 5 < len(username) < 17:
            self._username = username

        else:
            raise Exception("this username must be a string between 5 and 17 characters")
        

    # 13 Returns True if the Viewer has reviewed this Movie
    # (if there is a Review instance that has this Viewer and Movie), returns False otherwise
    def reviewed_movie(self, movie):
        if self.username in movie.reviewers:
            return True
        else:
            return False


    # 14 A Movie instance and a rating (number) are passed in as arguments
    # f the Viewer instance and the passed Movie instance are not already associated
    # if the viewer instance isn't already in the self.viewers list in Movie class
    # this method should create a new Review instance
    # If this Viewer has already reviewed this Movie, assigns the new rating to the existing Review instance
    def rate_movie(self, movie, rating):
        if self not in movie.reviewers:
            from lib.review import Review
            Review(self, movie, rating)
        else:
            movie.rating = rating