from django.core.management.base import BaseCommand, CommandError
from reviews.models import course
import openpyxl
import pandas as pd
import os

def excel_to_txt(excel_file, txt_file):
    """pulls out the data from columns B and D  of an excel document and turns it into a .txt document,
    with the data from each row being on its own line, and the data from each column being separated by
    a column.
    
    Inputs: excel_file, txt_file
    """
    # Load the workbook
    workbook = openpyxl.load_workbook(excel_file)

    # Select the worksheet
    worksheet = workbook.active

    # Read the data from columns B and D
    data = []
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        col_b, col_d = row[1], row[3]
        if col_b and col_d:
            data.append([col_b, col_d])

    # Convert the data to a DataFrame using pandas
    df = pd.DataFrame(data, columns=['col_b', 'col_d'])

    # Drop duplicates and empty lines
    df = df.drop_duplicates()
    df = df.dropna()

    # Write the data to a text file
    with open(txt_file, 'w') as f:
        for index, row in df.iterrows():
            f.write(f"{row['col_b']}\t{row['col_d']}\n")


#filepath = "Classes.txt"

# def read_data_from_file():
#     """Takes the contents of an input filepath, and returns it as a list, excluding any
#     whitespaces that may be in the .txt document. This data can be gotten from 
#     https://apps.clarku.edu/course-listings/registrarSPRING,23 With SPRING,23 Being
#     replaced by the relevant year. Copy this table into an excel document and then copy the columns
#     with the necessary information into a .txt documen.
    
#     IMPORTANT: NAME THE DOCUMENT "Classes.txt" """
    
#     with open(filepath, 'r') as f:
#         lines = f.readlines()
#     data = []
#     existing_items = set()
#     for line in lines:
#         line = line.strip()
#         if line and line not in existing_items:
#             item = process_line(line)
#             data.append(item)
#             existing_items.add(line)
#     return data

class Command(BaseCommand):
    help = 'Update course data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to Excel file')

    def handle(self, *args, **options):
        excel_file = options['excel_file']
        txt_file = "temporaryClassData.txt"

        # Convert Excel file to temporary text file
        excel_to_txt(excel_file, txt_file)

        # Update Course model data from temporary text file
        with open(txt_file, 'r') as f:
            for line in f:
                # Split the line into course code and name
                course_data = line.strip().split('\t')
                course_code = course_data[0].strip()
                course_name = course_data[1].strip()
                # courseCode, courseName = line.strip().split('\t')
                # course, created = course.objects.get_or_create(course_code=courseCode.strip())
                # course.courseName = courseName.strip()
                # course.save()
                
                # Get or create the Course object with the course code
                newcourse, created = course.objects.get_or_create(courseCode=course_code)

                # Update the course name
                newcourse.courseCode = course_code
                newcourse.courseName = course_name

                # Save the updated Course object
                newcourse.save()

                # Print a message for each updated Course object
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created course: {course_code} - {course_name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated course: {course_code} - {course_name}'))#)

        # Delete temporary text file
        #os.remove(txt_file)
        
        
        #RUN THIS IN TERMINAL VIA:
        #python manage.py courseUpdate "path/to/excel/file.xlsx"
        #instead of path/to/excel/file.xlsx, put in the file path of the excel document
        #also you NEED to install the new dependencies :)