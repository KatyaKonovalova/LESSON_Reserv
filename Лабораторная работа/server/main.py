from console import Console
from organization import *
import datetime

address = Address('street1', 'city1')
location = Location(0.0, 1.0, 0.0, 'Локация1')
coordinates = Coordinates(1.5, 2.5)
organization = Organization('organization1', coordinates,
                            datetime.datetime.strptime('2024-01-01', '%Y-%m-%d'), 100,
                            'full_name', 100, OrganizationType.PUBLIC, address)
Console.start(organization)
