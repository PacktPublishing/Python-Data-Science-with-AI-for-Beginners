x = np.array(range(1, 19))
y = np.array([
 147026,
 144272,
 140020,
 143801,
 146233,
 144539,
 141273,
 135389,
 142500,
 139452,
 139722,
 135300,
 137289,
 136511,
 132884,
 125683,
 127255,
 124275
])
[a, b] = np.polyfit(x, y, 1)
[-1142.0557275541753, 148817.5294117646]
import matplotlib.pyplot as plot
plot.scatter( x, y )
plot.plot( [0, 30], [b, 30*a+b] )
plot.show()
