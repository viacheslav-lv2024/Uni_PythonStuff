class StandardScaler:
    def __init__(self):
        self.mu = None
        self.sig = None
    def fit(self, features: list):
        self.mu = 0
        for number in features:
            self.mu += number
        self.mu /= len(features)
        
        self.sig = 0
        for number in features:
            self.sig += (number - self.mu) * (number - self.mu)
        self.sig = (self.sig/(len(features)-1))**0.5
    def transform(self, features: list):
        if self.sig == None or self.mu == None:
            raise ValueError("Scaler has not been fitted")
        local_list = []
        for i in range(len(features)):
            local_list.append((features[i] - self.mu) / self.sig)
        return local_list
    def fit_transform(self, features: list):
        self.mu = 0
        for number in features:
            self.mu += number
        self.mu /= len(features)
        
        self.sig = 0
        for number in features:
            self.sig += (number - self.mu) * (number - self.mu)
        self.sig = (self.sig/(len(features)-1))**0.5
        
        if self.sig == None or self.mu == None:
            raise ValueError("Scaler has not been fitted")
        local_list = []
        for i in range(len(features)):
            local_list.append((features[i] - self.mu) / self.sig)
        return local_list
    def __getitem__(self, key):
        if key == 0:
            return self.mu
        elif key == 1:
            return self.sig
        elif isinstance(key, int):
            raise IndexError("Index out of range")
        else:
            raise TypeError("Indices must be integers")

