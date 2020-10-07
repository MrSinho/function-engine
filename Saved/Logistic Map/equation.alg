self.x = ( (self.yy*self.x) * (self.c - self.x) )
self.y += 0.01 
self.z = ( (self.yy*self.z) * (self.c - self.z) )
self.yy += 0.001
if(self.yy < 3.9999999): self.yy += 0.001
if(self.yy >= 3.999999): self.yy = 4.0