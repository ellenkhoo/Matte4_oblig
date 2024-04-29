import numpy as np 
import matplotlib.pyplot as plt 

#definerer problemet:
a = 110 #termisk diffusivitet
lengde = 50 #mm
tid = 4 #sekunder 
noder = 40 #antal punkter langs linjen 

#diskrete verdier: 
    #romlige: delta x
        #mindre x vil tilsvare bedre presisjon 
    #tidsmessig: delta t
#initialisering 
dx = lengde / noder
dy = lengde / noder
dt = min(dx**2 / (4*a), dy**2 / (4*a)) 
t_noder = int(tid/dt)

u = np.zeros((noder, noder)) + 20 #plate initialisert som 20 grader C

#randkrav
u[0, :] = np.linspace(0, 100, noder)
u[-1, :] = np.linspace(0, 100, noder)
u[:, 0] = np.linspace(0, 100, noder)
u[:, -1] = np.linspace(0, 100, noder)



#visualisering med plot
fig, axis = plt.subplots()

pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin = 0, vmax = 100)
plt.colorbar(pcm, ax=axis)

#simulering 

teller = 0
while teller < tid :
    w = u.copy()

    for i in range(1, noder - 1):
        for j in range (1, noder - 1):

            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i +1, j])/dx**2
            dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1])/dy**2

            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i , j]
    teller += dt
    print("t: {:.3f} [s], Gjennomsnittelig temperatur: {:.2f} Celcius".format(teller, np.average(u)))
    
    #oppdaterer plottet
    pcm.set_array(u)
    axis.set_title("Distribution at t: {:.3f} [s].".format(teller))
    plt.pause(0.01)

plt.show()