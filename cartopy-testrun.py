
# coding: utf-8

#  - **Authors**: Elliott Sales de Andrade
#  - **Research field**: Seismology
#  - **Lesson topic**: cartography, maps, projections, Python
#  - **Lesson content URL**: https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/python/cartography
# 

# In[1]:

# Default imports
import numpy as np
import matplotlib.pyplot as plt


# ## Setup
# We will be using Cartopy for this lesson, so let's import that.
# The common convention is to import it as follows:

# In[2]:

import cartopy.crs as ccrs




# An arbitrary choice.
canada_east = -20
canada_west = 100
canada_north = 72.88
canada_south = -1

standard_parallels = (49, 77)
central_longitude = -(91 + 52 / 60)



# Here we can see two things:
#
#   1. The stock image and coastlines are not very high resolution.
#   2. The coastlines only show the oceanic coast; no lakes or rivers, and certainly no countries.
#
# Cartopy provides various "features" that can provide some or all of this content
# at varying resolutions. Some simple shortcuts to [Natural Earth data](http://www.naturalearthdata.com/)
# are provided in the `cartopy.feature` module and can be added via `ax.add_feature`.
# These are downloaded and cached on the fly, so there may be some issues if the
# WiFi is being flaky in MP408.

# In[13]:

import cartopy.feature as cfeature


# In[14]:



# These are all defined on the 1:110m(illion) scale, but what if we want
# something a bit higher resolution? Well, the above were just shortcuts
# and we can use `cfeature.NaturalEarthFeature` directly with its
# `scale` argument.

# In[17]:

land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m',
                                        edgecolor='k',
                                        facecolor=cfeature.COLORS['land'])
borders_10m = cfeature.NaturalEarthFeature('cultural', 'admin_0_boundary_lines_land', '10m',
                                        edgecolor='k',
                                        facecolor=cfeature.COLORS['land'])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1,
                     projection=ccrs.PlateCarree())
#ax.set_extent([canada_west, canada_east, canada_south, canada_north])
#ax.add_feature(land_10m)
ax.add_feature(borders_10m)


plt.show()
