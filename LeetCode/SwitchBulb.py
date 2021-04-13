// MIN_LEVEL = 5
// MAX_LEVEL = 15

// Light switch | Bulb brightness
// Dimmer level | 5 watt  | 10 watt  | 20 watt 
// 5            | 0       | 0        | 0       
// 10           | 2.5     | 5        | 10      
// 15           | 5       | 10       | 20      

// new dimmer_switch
// new light_bulb 20_watt
// connect light_bulb -> dimmer_switch
// set_level dimmer_switch 10
// get_brightness light_bulb 10


class Dimmer:
  def __init__(self,max_dim,min_dim):
    self.max_dim = max_dim
    self.min_dim = min_dim

class Bulb(Dimmer):
  def __init__(self, watt,dim_lev,dimmer):
    self.watt = watt
    self.dim_lev = dim_lev
    super().__init__(dimmer.max_dim,dimmer.min_dim)

  def get_brightness(self):
    print(self.min_dim)
    res = ((self.dim_lev - self.min_dim) / (self.max_dim - self.min_dim)) * self.watt
  return res

new_dimmer = Dimmer(15,5)
new_bulb = Bulb(5,13,new_dimmer)
res = new_bulb.get_brightness()
print(res)
