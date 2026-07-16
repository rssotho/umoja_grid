import json

from rest_framework import status
from rest_framework.response import Response

from system_management.packages.populate_package import (
    PopulateRacePackage,
    PopulateRolePackage,
    PopulateTitlePackage,
    PopulateGenderPackage,
    PopulateProvincePackage,
)


class PopulateService:

    def __init__(
        self,
        request
    ) -> None:

        self.request = request

    def view_races(self):

        races =  PopulateRacePackage(
            
        )
