class Movie:

    # 1 just initializing my title
    def __init__(self, title):
        self.title = title


        # 11 and 12 README is asking for some empty lists
        self.reviews = []
        self.reviewers = []

    # 2 making a property for the title. it has two conditions
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title

        else:
            raise Exception("this title must be a string")
        


    # 15 Returns the average of all ratings for the Movie instance
    # 
    def average_rating(self):
        total = 0
        for review in self.reviews:
            total += review
        
        average = total / len(self.reviews)

        return average


    # 16 Returns the Movie instance with the highest average rating.
    # ugh i know this is wrong. we need to sort a list and get the last element of it
    @classmethod
    def highest_rated(cls, reviews):
        reviews.sort()
        return reviews[-1]
