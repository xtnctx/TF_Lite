import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Parameters
x_len = 200         # Number of points to display
y_range = [-1, 1]  # Range of possible Y values to display

# Create figure for plotting
plt.style.use('fivethirtyeight')
fig = plt.figure()
accelerometer = fig.add_subplot(3, 1, 1)
gyroscope = fig.add_subplot(3, 1, 2)
distance = fig.add_subplot(3, 1, 3)


xs = list(range(0, 200))

ax = [0] * x_len
ay = [0] * x_len
az = [0] * x_len
accelerometer.set_ylim(y_range)

gx = [0] * x_len
gy = [0] * x_len
gz = [0] * x_len
gyroscope.set_ylim(y_range)

dist = [0] * x_len
distance.set_ylim(y_range)

# Create a blank line. We will update the line in animate
ax_line, = accelerometer.plot(xs, ax)
ay_line, = accelerometer.plot(xs, ay)
az_line, = accelerometer.plot(xs, az)

gx_line, = gyroscope.plot(xs, gx)
gy_line, = gyroscope.plot(xs, gy)
gz_line, = gyroscope.plot(xs, gz)

dist_line, = distance.plot(xs, dist)

# Add labels
accelerometer.set_title('Accelerometer')
accelerometer.set(xticklabels=[], yticklabels=[])

gyroscope.set_title('Gyroscope')
gyroscope.set(xticklabels=[], yticklabels=[])

distance.set_title('Distance')
distance.set(xticklabels=[], yticklabels=[])

data = pd.read_csv('data.csv')
x = data['t']
ax_val = data['ax']
ay_val = data['ay']
az_val = data['az']

gx_val = data['gx']
gy_val = data['gy']
gz_val = data['gz']

dist_val = data['dist']

# This function is called periodically from FuncAnimation

def animate(i, ax, ay, az, gx, gy, gz, dist):

# ///// ACCELEROMETER /////
    # X-axis
    ax.append(ax_val[i])
    ax = ax[-x_len:]
    ax_line.set_ydata(ax)
    ax_line.set_linewidth(1)
    ax_line.set_color('#5DADE2')

    # Y-axis
    ay.append(ay_val[i])
    ay = ay[-x_len:]
    ay_line.set_ydata(ay)
    ay_line.set_linewidth(1)
    ay_line.set_color('m')

    # Z-axis
    az.append(az_val[i])
    az = az[-x_len:]
    az_line.set_ydata(az)
    az_line.set_linewidth(1)
    az_line.set_color('g')

# /////// GYROSCOPE ///////
    # X-axis
    gx.append(gx_val[i])
    gx = gx[-x_len:]
    gx_line.set_ydata(gx)
    gx_line.set_linewidth(1)
    gx_line.set_color('#5DADE2')

    # Y-axis
    gy.append(gy_val[i])
    gy = gy[-x_len:]
    gy_line.set_ydata(gy)
    gy_line.set_linewidth(1)
    gy_line.set_color('m')

    # Z-axis
    gz.append(gz_val[i])
    gz = gz[-x_len:]
    gz_line.set_ydata(gz)
    gz_line.set_linewidth(1)
    gz_line.set_color('g')

# /////// Distance ///////
    dist.append(dist_val[i])
    dist = dist[-x_len:]
    dist_line.set_ydata(dist)
    dist_line.set_linewidth(1)
    dist_line.set_color('c')

    return (ax_line, ay_line, az_line, 
            gx_line, gy_line, gz_line, 
            dist_line,)



# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ax,ay,az,gx,gy,gz,dist,),
    interval=50,
    blit=True)
plt.tight_layout()
plt.show()