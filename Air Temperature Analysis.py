# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 00:41:42 2020

@author: Wilson
"""

# Question 1- Map of Caribbean Showing Average Air Temperature 

# importation of relevant libraries (some new ones here Lori)
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr

# using the xarray library to open the nc file
f = xr.open_dataset('C:/Users/Claudia Roye/Downloads/air.mon.mean.nc') # Roye's comp
#f = xr.open_dataset('C:/Users/Tashw/Downloads/air.mon.mean.nc')       # Wilson's comp
#print(f)                                               # just checking what's going on

# finding mean air temperature over time
    # slicing all time; surface level; specific lat and lon for Caribbean
airs=f.air[:,0,22:38,106:124]
airmean = airs.mean(dim=['time'])

# calling all the air, latitude and longitude variables in the dataset
air = f.variables['air'][:]
lat = f.variables['lat'][:];
lon = f.variables['lon'][:];

# The next set of lines are dedicated to finding 
    # the indices for the Caribbean's coordinates

# These lines convert the coordinate variables to numpy arrays
lons=np.array(lon)
lats=np.array(lat)

## This finds the actual indices of the coordinates of the Caribbean used in line 23
#lat1 = np.where(lats == 5 )
#lat2 = np.where(lats == 35 )
#lon1 = np.where(lons == 265 )
#lon2 = np.where(lons == 300 )
#print (lat1, lat2, lon1, lon2)


# Let's begin the plotting, shall we

# sets the size of the figure at larger than default
fig=plt.figure(figsize=[10,10])

# creating the plot and including the library cartopy for map related stuff
ax=plt.subplot(1,1,1,projection=ccrs.PlateCarree())

# This denotes the range of the map which corresponds to the Caribbean
    # note that these longitudes are West
ax.set_extent([-95,-60,5,30])

# This adds the coastlines of the countries
ax.coastlines(resolution="50m",linewidth=1)

# This adds the gridlines. We will soon see why we pass "False"
gl=ax.gridlines(draw_labels=False)

# This plots the mean air temp within the map of Caribbean
plt.contourf(lon[106:124], lat[22:38], airmean[:,:], transform=ccrs.PlateCarree())

# This adds and labels the colorbar  
cb=plt.colorbar(ax=ax,orientation='vertical',pad=0.1, aspect=16, shrink=0.5)
cb.set_label('Air Temperature/DegC',size=12,rotation=90,labelpad=15)
cb.ax.tick_params(labelsize=10)

# labelling axes- this is trickier than you'd think
    # The cartopy library doesn't allow for 'normal' axes labelling
    # because the gridline labels are annoying
    # but a neat workaround is to deliberately get axes ticks
    # then label the axes and it will work
    # That's why the grid labels were removed above; to avoid duplicates

# gets the predetermined ticks for each axis
ax.set_xticks(ax.get_xticks())
ax.set_yticks(ax.get_yticks())

#sets label for each axis
ax.set_ylabel("Latitude [degrees_north]")
ax.set_xlabel("Longitude [degrees_east]")

plt.title('Mean Air Temperature of the Caribbean')
plt.show()

# Question 2- Line Graph showing Monthly Average Air Temperature 

# plots line graph of  monthly mean of  Air temperature monthly mean data 
####spands enire dataset, not just caribbean
fmean = f.mean(dim=['level','lon','lat'])
m = fmean.groupby('time.month').mean()
m.air.plot()
# labels x-axis with months instead of numbers
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12], \
           ['January', 'February', 'March', 'April', 'May', 'June',\
            'July', 'August', 'September', 'October', 'November', 'December'],\
            rotation=30)
plt.ylabel("Mean Air Temperature/ Deg C")
plt.title("Monthly Air Temperature Mean from 1948 to 2020")
plt.show()


# Question 3- Shaded map of Jamaica

ax = plt.subplot(1,1,1,projection=ccrs.PlateCarree())

#specifies Jamaica's location and plots coastline
ax.set_extent([-80,-75,17.5,19])
ax.coastlines(resolution="50m",linewidth=2)

# adds default color
ax.stock_img()

gl=ax.gridlines(draw_labels=False)

# labelling the axes
ax.set_xticks(ax.get_xticks())
ax.set_yticks(ax.get_yticks())

ax.set_ylabel("Latitude [degrees_north]")
ax.set_xlabel("Longitude [degrees_east]")

plt.title("Shaded Map of Jamaica")
plt.show()

# Question 4- create contour map of Jamaica

## finding the actual indices of Ja's coordinates
#lat1 = np.where(lats == 15 )
#lat2 = np.where(lats == 20 )
#lon1 = np.where(lons == 280 )
#lon2 = np.where(lons == 285 )
#print (lat1, lat2, lon1, lon2)

# slicing all time, level = 0 and Ja's coordinates
airja=f.air[:,0,26:30,112:116]
airmeanja = airja.mean(dim=['time'])

fig=plt.figure(figsize=[10,15])
ax=plt.subplot(1,1,1,projection=ccrs.PlateCarree())
ax.set_extent([-80,-75,17.5,19])
ax.coastlines(resolution="50m",linewidth=1)
gl=ax.gridlines(draw_labels=False)

plt.contourf(lon[112:116], lat[26:30], airmeanja[:,:], transform=ccrs.PlateCarree())

cb=plt.colorbar(ax=ax,orientation='vertical',pad=0.1, aspect=16,shrink=0.2)
cb.set_label('Monthly mean of Air Temperature/DegC',size=10,rotation=90,labelpad=15)
cb.ax.tick_params(labelsize=10)

# gets the predetermined ticks for each axis
ax.set_xticks(ax.get_xticks())
ax.set_yticks(ax.get_yticks())

#sets label for each axis
ax.set_ylabel("Latitude [degrees_north]")
ax.set_xlabel("Longitude [degrees_east]")

plt.title(' Monthly Mean of Air Temperature for Jamaica')
plt.show()

# Question 5- A Map showing the Change in Climate for the 1st vs Last 20 years

# gets air values for 1st 20 years 
air0=f.air[0:21,:,:,:]
air0mean = air0.mean(dim = ['time','level'])
#print (air0mean)

# gets air values for last 20 years 
air20=f.air[53:73,:,:,:]
air20mean = air20.mean(dim = ['time','level'])
#print (air20mean)

# Compares the first 20 to the last 20
diff = (air20mean - air0mean)
#print (diff)

#plotting 
fig=plt.figure(figsize=[20,20])
ax=plt.subplot(1,1,1,projection=ccrs.PlateCarree())
ax.coastlines(resolution="50m",linewidth=1)
gl=ax.gridlines(draw_labels=False)

# This plots the mean air temp within the map of Caribbean
plt.contourf(lon[:], lat[:], diff[:,:], transform=ccrs.PlateCarree())

cb=plt.colorbar(ax=ax,orientation='vertical',pad=0.1, aspect=16, shrink=0.5)
cb.set_label('Air Temperature/DegC',size=12,rotation=90,labelpad=15)
cb.ax.tick_params(labelsize=10)

# gets the predetermined ticks for each axis
ax.set_xticks(ax.get_xticks())
ax.set_yticks(ax.get_yticks())

#sets label for each axis
ax.set_ylabel("Latitude [degrees_north]")
ax.set_xlabel("Longitude [degrees_east]")

plt.title('Comparison of First and Last 20 Years of Air Temperature')
plt.show()





