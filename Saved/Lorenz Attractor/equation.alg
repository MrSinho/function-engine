dx = (self.a * (self.y - self.x)) * self.deltatime
dy = (self.x * (self.b - self.z) - self.y) * self.deltatime
dz = (self.x * self.y - self.c * self.z) * self.deltatime
self.x = self.x + dx
self.y = self.y + dy
self.z = self.z + dz