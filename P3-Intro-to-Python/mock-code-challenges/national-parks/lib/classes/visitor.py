class Visitor:    
    def __init__(self, name):
        self.name = name
        self.trips = []
        self.parks = []

    @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self,name):
        if hasattr(self, 'name') or not isinstance(name,str) or 1>len(name)>15:
            raise Exception
        self._name = name
        

        
    def access_current_trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self.trips.append(new_trip)
        return self.trips

    
    def access_current_parks(self, new_park=None):
        from classes.nationalpark import NationalPark
        if isinstance(new_park, NationalPark) and new_park not in self.parks:
            self.parks.append(new_park)
            return self.parks
        pass