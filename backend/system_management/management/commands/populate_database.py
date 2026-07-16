from django.db.models import Q
from django.core.management.base import BaseCommand

import global_app.constants as constant

from system_management.models import (
    Role,
    Race,
    Title,
    Gender,
    Province,
)


class Command(BaseCommand):

    help = 'Create contant class instances for static data e.g. user roles'

    def create_user_types(self):
        roles = [
            constant.USER,
            constant.SYSTEM_ADMIN,
        ]
        Role.objects.filter(~Q(role__in=roles)).delete()
        for role in roles:
            Role.objects.get_or_create(role=role)

    def create_province(self):
        provinces = [
            constant.GAUTENG,
            constant.LIMPOPO,
            constant.FREE_STATE,
            constant.MPUMALANGA,
            constant.NORTH_WEST,
            constant.WESTERN_CAPE,
            constant.EASTERN_CAPE,
            constant.NORTHERN_CAPE,
            constant.KWAZULU_NATAL,
        ]
        Province.objects.filter(~Q(province__in=provinces)).delete()
        for province in provinces:
            Province.objects.get_or_create(province=province)

    def create_gender(self):
        genders = [constant.MALE, constant.FEMALE]
        Gender.objects.filter(~Q(gender__in=genders)).delete()
        for gender in genders:
            Gender.objects.get_or_create(gender=gender)

    def create_race(self):
        races = [
            constant.AFRICAN,
            constant.WHITE,
            constant.COLOURED,
            constant.INDIAN,
            constant.ASIAN,
        ]

        Race.objects.filter(~Q(race__in=races)).delete()
        for race in races:
            obj, created = Race.objects.get_or_create(race=race)
            print(f"{'Created' if created else 'Exists'}: {obj.race}")

    def create_title(self):
        titles = [constant.MR, constant.MRS, constant.MS]

        Title.objects.filter(~Q(title__in=titles)).delete()
        for title in titles:
            Title.objects.get_or_create(title=title)

    def handle(self, *args, **options):


        self.stdout.write(self.style.NOTICE('Populating User Roles...'))
        self.create_user_types()

        self.stdout.write(self.style.NOTICE('Populating Provinces...'))
        self.create_province()

        self.stdout.write(self.style.NOTICE('Populating Genders...'))
        self.create_gender()

        self.stdout.write(self.style.NOTICE('Populating Races...'))
        self.create_race()

        self.stdout.write(self.style.NOTICE('Populating Titles...'))
        self.create_title()

        self.stdout.write(self.style.NOTICE('-----------------------------------------'))

        self.stdout.write(self.style.SUCCESS('🎉 Database have been populated successfully!'))