Project 2 - UFO database

Data Source-  A csv file from NUFORC (National UFO Reporting Center) containing 112,000 documented sightings going back a far as 1950, in Canada and the US was used as the primary source of data.	  The CSV file use was obtained from [Tim Renner]( https://data.world/timothyrenner/ufo-sightings)

The database has many entries that have holes in the data. Sightings that were reported by adults about events they witnessed as children, for example, often do not have definitive data, or location.  So, using Pandas Dataframes to clean the data, the total number of records that have been included in this analysis is around 80,000.  Additional steps could be taken to vet some of the records that were filtered out, but with so many records available it was decided 80,000+ was sufficient.



