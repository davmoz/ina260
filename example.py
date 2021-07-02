from lib.ina260 import INA260

c = INA260()

print("Bus voltage: {} V").format(c.voltage())
print("Bus current: {} A").format(c.current())
print("Bus power: {} W").format(c.power())
