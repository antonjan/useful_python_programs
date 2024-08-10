#pip install astropy

from astropy.coordinates
import get_body, EarthLocation from astropy.time import Time
now = Time.now()
location = EarthLocation.of_site('greenwich')
planet_name = input("Enter the name of the planet: ").lower()
planet_position = get_body(planet_name, now, location)
print(f"(planet_name.capitalize() " f"Position: RA = (planet_position.ra), f"Dec = (planet_position.dec)")
