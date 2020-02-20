class Book:
    
    def __init__(self, id, score):
        self.id = id
        self.score = score
    
    def __str__(self):
        return "id: {}, score: {}".format(self.id, self.score)

class Library:
    
    def __init__(self, books, stime, scans_per_day):
        self.books = books
        self.stime = stime
        self.scans_per_day = scans_per_day
    
    def __str__(self):
        return_str =  "Signup Time: {}\nScans per day: {}".format(self.stime, self.scans_per_day)
        return_str += "\n"
        for book in books:
            return_str += str(book) + "\n"
        return return_str