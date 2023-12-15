class NationalPark:
    def __init__(self, name):
        self.name = name
        self.current_visitations = {}
        self.trips = []
        self.visitors = []

    @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self,name):
        if hasattr(self, 'name') or not isinstance(name,str):
            raise Exception
        self._name = name
        
    def access_current_trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self.trips.append(new_trip)
        return self.trips
    
    
    def access_current_visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor):
            self.visitors.append(new_visitor)
        return list(set(self.visitors))
    
    def calculate_all_trips(self):
        return(len(self.trips))
    
    
    def check_most_frequent_visitor(self):
        return max(self.visitors, key=self.visitors.count)