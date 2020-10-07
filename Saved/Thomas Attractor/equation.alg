dx = (np.sin(self.y) - (self.a * self.x)) * self.deltatime
dy = (np.sin(self.z) - (self.a * self.y)) * self.deltatime
dz = (np.sin(self.x) - (self.a * self.z)) * self.deltatime
self.x = self.x + dx
self.y = self.y + dy
self.z = self.z + dz