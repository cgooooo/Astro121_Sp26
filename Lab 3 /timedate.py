import time
import datetime
import ugradio

lat = ugradio.coord.nch.lat
lon = ugradio.coord.nch.lon
alt = ugradio.coord.nch.alt

unix_time = time.time()

utc_datetime = datetime.datetime.utcnow()

local_datetime = datetime.datetime.now()

jd = ugradio.timing.julian_date()


# Sun position

ra_sun, dec_sun = ugradio.coord.sunpos(jd)
alt_sun, az_sun = ugradio.coord.get_altaz(ra_sun, dec_sun, jd, lat, lon, alt)

# Moon position

ra_moon, dec_moon = ugradio.coord.moonpos(jd, lat, lon, alt)
alt_moon, az_moon = ugradio.coord.get_altaz(ra_moon, dec_moon, jd, lat, lon, alt)

# metadata

print("OBSERVATION METADATA")
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

print("----- Sun Position -----")
print("RA:", ra_sun)
print("Dec:", dec_sun)
print("Alt:", alt_sun)
print("Az:", az_sun)
print()

print("----- Moon Position -----")
print("RA:", ra_moon)
print("Dec:", dec_moon)
print("Alt:", alt_moon)
print("Az:", az_moon)
print()
