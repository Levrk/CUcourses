from django.core.management.base import BaseCommand, CommandError
from reviews.models import department
#auto updates the database with all the department
#this is not intended to be ran often.


class Command(BaseCommand):
    help = 'Update department data from .txt file'

    def add_arguments(self, parser):
        parser.add_argument('txt_file', type=str, help='Path to txt file')

    def handle(self, *args, **options):
        txt_file = options['txt_file']
        
        # Update dept model data from temporary text file
        with open(txt_file, 'r') as f:
            for line in f:
                # Split the line into dept code and name
                dept_data = line.strip().split(',')
                dept_code = dept_data[0].strip()
                dept_name = dept_data[1].strip()
                
                # Get or create the depatment object with the dept code
                newdept, created = department.objects.get_or_create(deptCode=dept_code)

                # Update the dept name
                newdept.deptCode = dept_code
                newdept.deptName = dept_name

                # Save the updated dept object
                newdept.save()

                # Print a message for each updated dept object
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created department: {dept_code} - {dept_name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated department: {dept_code} - {dept_name}'))
                    
#python manage.py deptUpdate "path/to/dept/file.txt"
