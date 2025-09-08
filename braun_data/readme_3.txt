readme file for the main directory of:

Kormos, Patrick R.; Marks, Danny G.; Boehm, Alex R.; Havens, Scott; Hedrick, Andrew; 
   Pierson, Fred; Williams, C. Jason; Hardegree, Stuart P.; Glenn, Nancy F.; Bates, 
   Jonathan D.; Svejcar, Anthony J. (2016). Data From: Weather, Snow, and Streamflow data 
   from four western juniper-dominated Experimental Catchments in south western Idaho, 
   USA. Ag Data Commons. http://dx.doi.org/10.15482/USDA.ADC/1254010.

spatial data projection information:
   Universal Transverse Mercator (Zone 11)
   1983 North American Datum and Geodetic Reference System 1980 ellipsoid

this dataset includes the following information:
   
   DATA SET CONTENTS:
   10 processed time series files, comma delimited ascii text with 1 header row
    8 raw time series files, comma delimited ascii text with 1 header row
    1 measurement station coordinate file, comma delimited ascii text with 1 header row
    3 compressed elevation datasets as .zip files containing data .txt files and
      projection information as .prj files

TIME SERIES FILES

General Information:
All data were collected within the South Mountain Experimental Catchments between October 1, 
2007 and October 1, 2013. Processed data files, indicated by the â_final.csvâ suffix, quality checked and gap filled time series data. Raw data files, indicated by the â_raw.csvâ suffix are provided and include data as collected by the weather station instruments and datalogers, with minimal data flagging and removal as described in each data raw file description below. The abbreviations used in the one-line header are defined below. The first part of each record is the date-time (water year, month, day of month, calendar year, hour). Missing values are represented by "NaN". Each file is described in more detail below. There are six weather stations located at the following coordinates (see above for spatial reference system).

station_id   easting (m)   northing (m)   elevation (masl)sme2         508301        4724419        1866smf1         507353        4723062        1702smg1         507326        4722047        1672smg2         507866        4722811        1774smm1         507174        4724133        1691smm2         507620        4723692        1806

There are four stream gauging stations located at the following coordinates (see above for spatial reference system).

station_id   easting (m)   northing (m)   elevation (masl) contributing area (acres)
sme          507382        4724433        1704             140.203146 
smf          507283        4722975        1692             139.76058
smg          507254        4722022        1665             178.395823
smm          507196        4724137        1687             51.862477

Time Series File Header Abbreviations:

water_year      Water year (October 1st to September 30th)
month           Month
day             Day of month
calendar_year   Calendar year
hour            Hour in 24 hour format (1pm is 13)
station_id      The name of the weather station
easting         Easting of geographic position of weather station in meters (UTM Zone 11, NAD83)
northing        Northing of geographic position of weather station in meters (UTM Zone 11, NAD83)
elevation       Elevation of weather station in meters above sea level
sample          Snow course sample number
snowdepth_in           Snow depth in inches
corelength_in   Core length of snow course sample in inches
wt_total_in     Total weight of snow tube and snow sample in inches of water
wt_tube_in      Weight of the empty snow tube in inches of water
bulk_y_n        Indicates whether a snow course sample is a bulk sample (y) or not (n).

sme_q_mm        Stream discharge in mm from stream gauge sme
smf_q_mm        Stream discharge in mm from stream gauge smf
smg_q_mm        Stream discharge in mm from stream gauge smg
smm_q_mm        Stream discharge in mm from stream gauge smm

sme2_dpt_C      Dew point temperature in degrees celsius from weather station sme2
smf1_dpt_C      Dew point temperature in degrees celsius from weather station smf1
smg1_dpt_C      Dew point temperature in degrees celsius from weather station smg1
smg2_dpt_C      Dew point temperature in degrees celsius from weather station smg2
smm1_dpt_C      Dew point temperature in degrees celsius from weather station smm1
smm2_dpt_C      Dew point temperature in degrees celsius from weather station smm2

sme2_ppt_mm     Precipitation in millimeters from weather station sme2
smf1_ppt_mm     Precipitation in millimeters from weather station smf1
smg1_ppt_mm     Precipitation in millimeters from weather station smg1
smg2_ppt_mm     Precipitation in millimeters from weather station smg2
smm1_ppt_mm     Precipitation in millimeters from weather station smm1
smm2_ppt_mm     Precipitation in millimeters from weather station smm2

sme2_rh         Relative humidity in fraction of saturation from weather station sme2
smf1_rh         Relative humidity in fraction of saturation from weather station smf1
smg1_rh         Relative humidity in fraction of saturation from weather station smg1
smg2_rh         Relative humidity in fraction of saturation from weather station smg2
smm1_rh         Relative humidity in fraction of saturation from weather station smm1
smm2_rh         Relative humidity in fraction of saturation from weather station smm2

sme2_sd_mm      Snow depth in millimeters from weather station sme2
smf1_sd_mm      Snow depth in millimeters from weather station smf1
smg1_sd_mm      Snow depth in millimeters from weather station smg1
smg2_sd_mm      Snow depth in millimeters from weather station smg2
smm1_sd_mm      Snow depth in millimeters from weather station smm1
smm2_sd_mm      Snow depth in millimeters from weather station smm2

sme2_sin_w/m2   Incoming solar radiation in watts per square meter from weather station sme2
smf1_sin_w/m2   Incoming solar radiation in watts per square meter from weather station smf1
smg1_sin_w/m2   Incoming solar radiation in watts per square meter from weather station smg1
smg2_sin_w/m2   Incoming solar radiation in watts per square meter from weather station smg2
smm1_sin_w/m2   Incoming solar radiation in watts per square meter from weather station smm1
smm2_sin_w/m2   Incoming solar radiation in watts per square meter from weather station smm2

sme2_swe_mm     Snow water equivalent in millimeters from weather station sme2
smf1_swe_mm     Snow water equivalent in millimeters from weather station smf1
smg1_swe_mm     Snow water equivalent in millimeters from weather station smg1
smg2_swe_mm     Snow water equivalent in millimeters from weather station smg2
smm1_swe_mm     Snow water equivalent in millimeters from weather station smm1
smm2_swe_mm     Snow water equivalent in millimeters from weather station smm2

sme2_ta_C       Air temperature in degrees celsius from weather station sme2
smf1_ta_C       Air temperature in degrees celsius from weather station smf1
smg1_ta_C       Air temperature in degrees celsius from weather station smg1
smg2_ta_C       Air temperature in degrees celsius from weather station smg2
smm1_ta_C       Air temperature in degrees celsius from weather station smm1
smm2_ta_C       Air temperature in degrees celsius from weather station smm2

sme2_vp_Pa      Vapor pressure in pascals from weather station sme2
smf1_vp_Pa      Vapor pressure in pascals from weather station smf1
smg1_vp_Pa      Vapor pressure in pascals from weather station smg1
smg2_vp_Pa      Vapor pressure in pascals from weather station smg2
smm1_vp_Pa      Vapor pressure in pascals from weather station smm1
smm2_vp_Pa      Vapor pressure in pascals from weather station smm2

sme2_wd_deg     Wind direction in degrees from weather station sme2
smf1_wd_deg     Wind direction in degrees from weather station smf1
smg1_wd_deg     Wind direction in degrees from weather station smg1
smg2_wd_deg     Wind direction in degrees from weather station smg2
smm1_wd_deg     Wind direction in degrees from weather station smm1
smm2_wd_deg     Wind direction in degrees from weather station smm2

sme2_ws_m/s     Wind speed in meters per second from weather station sme2
smf1_ws_m/s     Wind speed in meters per second from weather station smf1
smg1_ws_m/s     Wind speed in meters per second from weather station smg1
smg2_ws_m/s     Wind speed in meters per second from weather station smg2
smm1_ws_m/s     Wind speed in meters per second from weather station smm1
smm2_ws_m/s     Wind speed in meters per second from weather station smm2


Time Series Data File Descriptions:

air_temp_final.csv: Measured air temperature at 3 m in degrees celsius from the six weather stations at the South Mountain Experimental Catchments. The air temperature instrument was a Viasala HMP45 and measurements were recorded on a Campbell Scientific CR10X data logger. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and an air temperature for each weather station. Values are comma separated. This file is  error checked and gap filled using the data in air_temp_raw.csv as the starting point. Hourly measurements are averages from 10 second instantaneous air temperature measurements. The data is serially complete.

air_temp_raw.csv: File containing the raw air temperature measurements used to create air_temp_final.csv. Measured air temperature greater than 70 degrees celsius and less than -35 degrees celsius were flagged and removed. Additionally, visual inspection was performed and of blatant errors were removed. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and an air temperature for each weather station. Values are comma separated. Missing values exist. 

dewpoint_final.csv: Calculated dew point temperature from air_temp_final.cv and relative_humidity_final.csv in degrees celsius from the six weather stations at the South Mountain Experimental Catchments. Relative humidity and air temperature were converted to vapor pressure and then vapor pressure was converted to dew point temperature following methods described by Marks et al. (1999) that optimizes accuracy near 0 degrees C. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and an dew point temperature at each weather station. Values are comma separated. The data is serially complete.

incoming_solar_final.csv: Incoming solar (shortwave) radiation in watts per square meter measured at the six weather stations at the South Mountain Experimental Catchments. The instrument height was 3 m. The solar radiometer was a Kipp & Zonnen CMP3 and measurements were recorded on a Campbell Scientific CR10X data logger. The radiometer measures solar irradiance in the spectral range of 300 to 2800 nanometers. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and an incoming solar radiation value for each weather station. Values are comma separated. This file is  error checked and gap filled using the data in incoming_solar_raw.csv as the starting point. Hourly measurements are averages from 10 second instantaneous incoming solar radiation measurements. The data is serially complete.

incoming_solar_raw.csv: File containing the raw incoming solar radiation measurements used to create incoming_solar_final.csv. Measured incoming solar radiation values between sunset and sunrise are set to zero. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and an incoming solar radiation value for each weather station. Values are comma separated. Missing values exist. 

precipitation_final.csv: Wind corrected precipitation in mm from the six weather stations at the South Mountain Experimental Catchments. The instrument height was 3 m. The precipitation gauge was a 8 inch Belfort-type gauge with Alter Shield (Hanson et al., 2001) and measurements were recorded on a Campbell Scientific CR10X data logger. Cumulative precipitation was filtered following Nayak et al. (2008), differenced to get hourly precipitation mass, and wind corrected using the World Meteorological Organization protocol as described in Dingman (2002).The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and a precipitation mass for each weather station. Values are comma separated. This file is  error checked and gap filled using the data in precipitation_raw.csv as the starting point. The data is serially complete.

precipitation_raw.csv: File containing the raw cumulative precipitation measurements used to create precipitation_final.csv. Measured precipitation greater than 300 mm and less than 0 mm were flagged and removed. The file contains 631296 5-minute records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, minute, and a cumulative precipitation value in mm for each weather station. Values are comma separated. Missing values exist. 

relative_humidity_final.csv: Measured relative humidity at 3 m in fraction of saturation from the six weather stations at the South Mountain Experimental Catchments. The relative humidity instrument was a Viasala HMP45 and measurements were recorded on a Campbell Scientific CR10X data logger. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and a relative humidity for each weather station. Values are comma separated. This file is  error checked and gap filled using the data in relative_humidity_raw.csv as the starting point. Hourly measurements are averages from 10 second instantaneous relative humidity measurements. The data is serially complete.

relative_humidity_raw.csv: File containing the raw relative humidity measurements used to create relative_humidity_final.csv. Measured relative humidity greater than 1.10 and less than 0 were flagged and removed. Additionally, visual inspection was performed and of blatant errors were removed. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and a relative humidity for each weather station. Values are comma separated. Missing values exist. 

snow_course_final.csv: Manually measured snow water equivalent in millimeters from within 30 meters of the six weather stations at the South Mountain Experimental Catchments. Snow water equivalent was measured using a federal sampler type snow tube. The file contains 17 daily records. Each record contains the water year, month, day of month, calendar year, and a snow water equivalent measurement for each weather station. Values are comma separated. Snow water equivalent data are averages of five measurements along a transect, which are provided in snow_course_raw.csv.

snow_course_raw.csv: File containing the raw snow course measurements used to create snow_course_final.csv. Snow course measurements consist of 5 samples taken along a transect. The file contains 345 records. Each record contains the water year, month, day of month, calendar year, weather station (station_id), sample number, measured snow depth, measured snow core length, total weight of the snow tube and snow sample, weight of the empty snow tube, and whether it was a bulk sample or not. Bulk samples are taken when there is insufficient snow at a location to get good individual samples. In these cases, several snow samples are taken without emptying the snow tube, so you accumulate sufficient snow to weight. Bulk samples only have one weight, which is distributed among the number of samples taken (usually 5) Values are comma separated.

snow_depth_final.csv: Measured snow depth in millimeters from the six weather stations at the South Mountain Experimental Catchments. The snow depth sensor was a Judd Depth Sensor and measurements were recorded on a Campbell Scientific CR10X data logger. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and a snow depth for each weather station. Values are comma separated. Snow depth data in this file has undergone extensive manual error flagging, smoothing, and gap filled using the data in snow_depth_raw.csv as the starting point. Data was smoothed by a robust local regression using weighted linear least squares and a 2nd degree polynomial model, which assigns lower weight to outliers in the regression. The method also assigns zero weight to data outside six mean absolute deviations. Smoothing windows were manual chosen and vary from site to site and within years. Missing data exists.

snow_depth_raw.csv: File containing the raw snow depth measurements in millimeters used to create snow_depth_final.csv. The file contains 210432 15-minute records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, minute, and a snow depth for each weather station. Values are comma separated. Missing values exist. 

station_coords.csv: Station coordinates and elevations of weirs (sme, smf, smg, smm) and weather stations (sme2, smf1, smg1, smg2, smm1, smm2) in meters. Coordinates were measured using a Garmin hand held GPS with approximately 3 m accuracy. Elevations are obtained from a 1 meter Liar-derived digital elevation model corresponding to the coordinates. See above for spatial reference information.

stream_discharge_final.csv: Measured stream discharge in millimeters from four stream gauging stations at the South Mountain Experimental Catchments. Stream stage is measured at four drop box v-notch weirs (Bonta and Pierson, 2003), which define the South Mountain Experimental Catchments. Measured depth is converted to discharge based on well defined rating curves. Catchment areas are then used to convert to millimeters. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and a stream discharge for each stream gauging station. Values are comma separated. Stream flow data in this file has undergone extensive manual error flagging, gap filling, and correction. 

vapor_pressure_final.csv: Calculated vapor pressure from air_temp_final.cv and relative_humidity_final.csv in degrees pascals from the six weather stations at the South Mountain Experimental Catchments. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and vapor pressure at each weather station. Values are comma separated. The data is serially complete.

wind_dir_raw.csv: File containing the raw wind direction measurements in degrees from 3 meters. Measurements were made using a Met One 023 wind vane. Hourly measured wind directions are resultants of 10 second instantaneous wind direction measurements. Wind directions from hours where the standard deviation of wind direction is zero were assumed erroneous, flagged, and removed. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and a wind direction for each weather station. Values are comma separated. Missing values exist. We did not attempt to gap fill this data.

wind_speed_final.csv: Measured wind speed corrected to 5 m in meters per second from the six weather stations at the South Mountain Experimental Catchments. Wind speeds less than 0.477 m/s were set to 0.477 m/s (the minimum wind speed required to turn the anemometer. The wind speed instrument was a Met One 013 cup anemometer and measurements were recorded on a Campbell Scientific CR10X data logger. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and a wind speed for each weather station. Values are comma separated. This file is  error checked and gap filled using the data in wind_speed_raw.csv as the starting point. Hourly measurements are averages from 10 second wind measurements (from number of anemometer rotations). The data is serially complete.

wind_speed_raw.csv: File containing the raw wind speed measurements from 3 meters used to create wind_speed_final.csv. Hourly measured wind speeds are averages of calculated wind speeds from 10 second rotation counts. Runs of zero wind speed measurements for 12 hours or more were assumed erroneous, flagged, and removed. The file contains 52608 hourly records beginning on October 1, 2007. Each record contains the water year, month, day of month, calendar year, hour, and a wind speed for each weather station. Values are comma separated. Missing values exist. 

SPATIAL DATA FILES

As noted above, spatial data projection information:
   Universal Transverse Mercator (Zone 11)
   1983 North American Datum and Geodetic Reference System 1980 ellipsoid

Elevation Datasets General Information:
One meter and 10 m bare earth elevation models, one and 10 m mean vegetation height, and 1 m maximum vegetation height data are contained in .zip files with an ascii file containing the data and a .prj file containing the geographic information. All elevations are in meters. Areas outside the catchments are filled with -9999. Each ascii grid has 6 header lines as follows:

ncols         1754
nrows         3276
xllcorner     506908.84178564
yllcorner     4721629.1744471
cellsize      1
NODATA_value  -9999

Point, Line, and Polygon File General Information:
Catchment boundaries, streams, and the locations of weather stations and weirs are stored as shapefiles and are contained in .zip files with the corresponding .cpg, .dbf, .prj, .sbn, .sbx, .shp, .shp.xml, and .shx files for each dataset.

Spatial Data File Descriptions:

bare_earth_dem_1m.zip: Compressed file containing bare_earth_1m.txt and bare_earth_1m.prj. This is a 1 m grid of bare earth elevation in meters above sea level of the South Mountain Experimental Catchments. Elevations are derived from an airborne lidar survey acquired in November 2007. The lidar point density was 7 points per square meter resulting in a vertical accuracy of approximately 3 cm. Processing of the lidar dataset to obtain the bare earth elevation was done using tools developed by the Boise Center Aerospace Laboratory (BCAL, 2016) as describe by Streutker and Glen Streutker and Glenn (2006). 

mean_veg_ht_1m.zip: Compressed file containing mean_veg_ht_1m.txt and mean_veg_ht_1m.prj. This is a 1 m grid of mean vegetation height in meters for the South Mountain Experimental Catchments. Heights are derived from an airborne lidar survey acquired in November 2007. The lidar point density was 7 points per square meter resulting in a vertical accuracy of approximately 3 cm. Processing of the lidar dataset to obtain the maximum vegetation height was done using tools developed by the Boise Center Aerospace Laboratory (BCAL, 2016) as describe by Streutker and Glen Streutker and Glenn (2006). 

maximum_veg_ht_1m.zip: Compressed file containing maximum_veg_ht_1m.txt and maximum_veg_ht_1m.prj. This is a 1 m grid of maximum vegetation height in meters for the South Mountain Experimental Catchments. Heights are derived from an airborne lidar survey acquired in November 2007. The lidar point density was 7 points per square meter resulting in a vertical accuracy of approximately 3 cm. Processing of the lidar dataset to obtain the maximum vegetation height was done using tools developed by the Boise Center Aerospace Laboratory (BCAL, 2016) as describe by Streutker and Glen Streutker and Glenn (2006). 

bare_earth_dem_10m.zip: Compressed file containing bare_earth_dem.txt and bare_earth_dem.prj. This is the 10 m grid of bare earth elevation in meters above sea level of the South Mountain Experimental Catchments. Elevations are resampled from bare_earth_dem_1m (also included in this data set) derived from an airborne lidar survey acquired in November 2007. The lidar point density was 7 points per square meter resulting in a vertical accuracy of approximately 3 cm. Processing of the lidar dataset to obtain the bare earth elevation was done using tools developed by the Boise Center Aerospace Laboratory (BCAL, 2016) as describe by Streutker and Glen Streutker and Glenn (2006). 

maximum_veg_ht_10m.zip: Compressed file containing maximum_veg_ht_10m.txt and maximum_veg_ht_10m.prj. This is a 10 m grid of maximum vegetation height in meters derived from the 1 m maximum vegetation height model (maximum_veg_ht_1m also included in this data set) for the South Mountain Experimental Catchments. This is a mean of maximum vegetation heights from the 1 m product. Heights are derived from an airborne lidar survey acquired in November 2007. The lidar point density was 7 points per square meter resulting in a vertical accuracy of approximately 3 cm. Processing of the lidar dataset to obtain the maximum vegetation height was done using tools developed by the Boise Center Aerospace Laboratory (BCAL, 2016) as describe by Streutker and Glen Streutker and Glenn (2006). 

catchment_boundaries.zip: Compressed file containing the shapefile of the locations of catchments E (sme), F (smf), G (smg), and M (smm), otherwise known as the South Mountain Experimental Catchments. Catchment boundaries are derived from 1 m bare earth elevation model derived from an airborne lidar survey acquired in November 2007. The lidar point density was 7 points per square meter resulting in a vertical accuracy of approximately 3 cm. Processing of the lidar dataset to obtain the bare earth elevation was done using tools developed by the Boise Center Aerospace Laboratory (BCAL, 2016) as describe by Streutker and Glen Streutker and Glenn (2006). Catchment delineations were conducted in ArcMAP 10.2.2, Spatial Analyist, Hydrology Tools.

weather_stations.zip: Compressed file containing the shapefile of the locations of weirs sme, smf, smg, and smm. Coordinates and elevations are in meters. Coordinates were measured using a Garmin hand held GPS with approximately 3 m accuracy. Elevations are obtained from a 1 meter Liar-derived digital elevation model corresponding to the coordinates. The 1 m bare earth elevation model derived from an airborne lidar survey acquired in November 2007. The lidar point density was 7 points per square meter resulting in a vertical accuracy of approximately 3 cm. Processing of the lidar dataset to obtain the bare earth elevation was done using tools developed by the Boise Center Aerospace Laboratory (BCAL, 2016) as describe by Streutker and Glen Streutker and Glenn (2006).  

weirs.zip: Compressed file containing the shapefile of the locations of weirs sme, smf, smg, and smm. Coordinates and elevations are in meters. Coordinates were measured using a Garmin hand held GPS with approximately 3 m accuracy. Elevations are obtained from a 1 meter Liar-derived digital elevation model corresponding to the coordinates. The 1 m bare earth elevation model derived from an airborne lidar survey acquired in November 2007. The lidar point density was 7 points per square meter resulting in a vertical accuracy of approximately 3 cm. Processing of the lidar dataset to obtain the bare earth elevation was done using tools developed by the Boise Center Aerospace Laboratory (BCAL, 2016) as describe by Streutker and Glen Streutker and Glenn (2006). 

REFERENCES:

BCAL. BCAL LiDAR Tools ver 1.5.3., Idaho State University, Department of Geosciences, Boise 
        Center Aerospace Laboratory (BCAL), Boise, Idaho., January 2016.

Dingman, S. L. (2002), Physical Hydrology. (2nd ed.), Upper Saddle River, New Jersey, Prentice-
	Hall, Inc., isbn: 0-13-099695-5.

Hanson, C., Burgess, M. D., Windom, J. D., and Hartzmann, R. J. (2001), New Weighing Mechanism
	for Precipitation Gauges, J. Hydrol. Eng., 6, 75â77, doi:10.1061/
	(ASCE)1084-0699(2001)6:1(75).

Marks, D., J. Domingo, D. Susong, T. Link and D. Garen (1999), A spatially distributed energy 
	balance snowmelt model for application in mountain basins, Hydrol. Processes, 
	13(12-13), 1935-1959, doi:10.1002/(SICI)1099-1085(199909)13:12/13 <1935::AID-HYP868>
	3.0.CO;2-C.

Nayak, A., D. G. Chandler, D. Marks, J. P. McNamara, and M. Seyfried (2008), Correction of 
	electronic record for weighing bucket precipitation gauge measurements, Water Resour. 
	Res., 44(4), doi: 10.1029/2008wr006875.

Streutker, D. R., and Glenn, N. F. Lidar measurement of sagebrush steppe vegetation heights. 
        Remote Sensing of Environment 102, 1â2 (2006), 135â145.