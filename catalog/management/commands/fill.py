from django.core.management import BaseCommand

from catalog.models import Student


class Command(BaseCommand):

    def handle(self, *args, **option):
        student_list = [
            {'last_name': 'Давыдов', 'first_name': 'Андрей'},
            {'last_name': 'Калинин', 'first_name': 'Алексей'},
            {'last_name': 'Иванов', 'first_name': 'Петр'},
            {'last_name': 'Творогов', 'first_name': 'Семен'},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        student_for_create = []
        for student_item in student_list:
            student_for_create.append(
                Student(**student_item)
            )

        # print(student_for_create)
        Student.objects.bulk_create(student_for_create)
