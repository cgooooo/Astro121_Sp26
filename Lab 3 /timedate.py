import time
import datetime
import ugradio

# ----------------------------
# Location information
# ----------------------------

lat = ugradio.coord.nch.lat
lon = ugradio.coord.nch.lon
alt = ugradio.coord.nch.alt

# ----------------------------
# Time information
# ----------------------------

# Unix time (seconds since Jan 1 1970 UTC)
unix_time = time.time()

# UTC datetime
utc_datetime = datetime.datetime.utcnow()

# Local datetime
local_datetime = datetime.datetime.now()

# Julian Date
jd = ugradio.timing.julian_date()

# ----------------------------
# Print metadata
# ----------------------------

print("===== OBSERVATION METADATA =====")
print()

print("Unix Time:")
print(unix_time)
print()

print("UTC Date/Time:")
print(utc_datetime)
print()

print("Local Date/Time:")
print(local_datetime)
print()

print("Julian Date:")
print(jd)
print()

print("Observer Location:")
print("Latitude:", lat)
print("Longitude:", lon)
print("Altitude (m):", alt)
print()

# Optional: Sun coordinates (useful sanity check)
ra_sun, dec_sun = ugradio.coord.sunpos(jd)
alt_sun, az_sun = ugradio.coord.get_altaz(ra_sun, dec_sun, jd, lat, lon, alt)

print("Sun Position:")
print("RA:", ra_sun)
print("Dec:", dec_sun)
print("Alt:", alt_sun)
print("Az:", az_sun)

print()
print("================================")
