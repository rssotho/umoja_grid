from django.core.management.base import BaseCommand

from global_app import constants as constant
from system_management.models import (
    User,
    Profile,
)


class Command(BaseCommand):
    help = 'Create a superuser with custom options'

    def get_valid_input(self, prompt, error_message):
        while True:
            user_input = input(prompt)
            if user_input:
                return user_input
            else:
                self.stdout.write(self.style.ERROR(error_message))

    def handle(self, *args, **options):
        """
        Problem:
            Create custom super user for proba application.

        Solution:
            Use Django command lines for custom user creation.

        Return:
            Terminal output of user created, or error message.

        Logic:
            1. Prompt user for following fields:
                - Email
                - First Name
                - Last Name
                - Phone Number
                - Password
                - Confirm Password
            2. Check if email already exists
            3. Check if phone number already exists
            4. Check if passwords match
            5. Create user with provided data
            6. Print success message
            7. Exit command line
        
        Raise:
            None
        """
        email = self.get_valid_input(
            'Email address: ',
            'Please provide email address.'
        )

        email_exists = User.objects.filter(
            email=email
        ).exists()

        while email_exists:
            self.stdout.write(
                self.style.ERROR('Email already exists')
            )

            email = self.get_valid_input(
                'Email address: ',
                'Please provide an email address.'
            )

            email_exists = User.objects.filter(
                email=email
            ).exists()

        first_name = self.get_valid_input(
            'First Name: ',
            'Please provide first name.'
        )

        last_name = self.get_valid_input(
            'Last Name: ',
            'Please provide last name.'
        )

        phone_number = self.get_valid_input(
            'Phone number: ',
            'Please provide a phone number.'
        )

        phone_number_exists = User.objects.filter(
            phone_number=phone_number
        ).exists()

        while phone_number_exists:
            self.stdout.write(
                self.style.ERROR('Phone number already exists')
            )

            phone_number = self.get_valid_input(
                'Phone number: ',
                'Please provide a phone number.'
            )

            phone_number_exists = User.objects.filter(
                phone_number=phone_number
            ).exists()

        password = self.get_valid_input(
            'Password: ',
            'Please provide a password.'
        )

        confirm_password = self.get_valid_input(
            'Confirm password: ',
            'Please confirm your password.'
        )

        while password != confirm_password:
            self.stdout.write(
                self.style.ERROR('Passwords do not match.')
            )

            password = self.get_valid_input(
                'Password: ',
                'Please provide a password.'
            )

            confirm_password = self.get_valid_input(
                'Confirm password: ',
                'Please confirm your password.'
            )

        # Create the superuser and related objects
        User.objects.create_superuser(
            email = email,
            password = password,
            last_name = last_name,
            first_name = first_name,
            phone_number = phone_number,
        )

        self.stdout.write(self.style.SUCCESS(f'Superuser created successfully!'))
