import csv
from django.core.management.base import BaseCommand
from userportfoliyo.models import *

class Command(BaseCommand):
    help = 'Import data from CSV files to populate Django models'

    def handle(self, *args, **kwargs):
        # Define paths to your CSV files
        organizations_csv = '/home/zaza/Dev/Portfolioprojects/ujuziv2/ujuziportfoliyoproject/table_data/organizations.csv'
        institutions_csv = '/home/zaza/Dev/Portfolioprojects/ujuziv2/ujuziportfoliyoproject/table_data/institutions.csv'
        field_of_study_csv = '/home/zaza/Dev/Portfolioprojects/ujuziv2/ujuziportfoliyoproject/table_data/field_of_study.csv'
        soft_skills_csv = '/home/zaza/Dev/Portfolioprojects/ujuziv2/ujuziportfoliyoproject/table_data/soft_skills.csv'
        technology_csv = '/home/zaza/Dev/Portfolioprojects/ujuziv2/ujuziportfoliyoproject/table_data/technology.csv'
        techroles_csv = '/home/zaza/Dev/Portfolioprojects/ujuziv2/ujuziportfoliyoproject/table_data/techroles.csv'

        # Function to import organizations from CSV
        def import_organizations():
            with open(organizations_csv, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    name = row[0].strip()  # Assuming 'name' is in the first column
                    Organization.objects.get_or_create(name=name)

        # Function to import institutions from CSV
        def import_institutions():
            with open(institutions_csv, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    name = row[0].strip()  # Assuming 'name' is in the first column
                    Institution.objects.get_or_create(name=name)

        def import_field_of_study():
            with open(field_of_study_csv, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    name = row[0].strip()  # Assuming 'name' is in the first column
                    StudyField.objects.get_or_create(name=name)

        def import_soft_skills():
            with open(soft_skills_csv, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    name = row[0].strip()  # Assuming 'name' is in the first column
                    SoftSkills.objects.get_or_create(name=name)

        def import_technology():
            with open(technology_csv, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    name = row[0].strip()  # Assuming 'name' is in the first column
                    Techonology.objects.get_or_create(name=name)

        def import_techroles():
            with open(techroles_csv, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    name = row[0].strip()  # Assuming 'name' is in the first column
                    TechRole.objects.get_or_create(name=name)

        # Run import functions
        import_organizations()
        import_institutions()
        import_field_of_study()
        import_soft_skills()
        import_techroles()
        import_technology()

        self.stdout.write(self.style.SUCCESS('Data import completed successfully'))
