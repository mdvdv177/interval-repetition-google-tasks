import api
from datetime import date, timedelta


def create_task(theme, days):
    title = f'Interval repetition of {theme}'
    note = f"{days} {['day', 'days'][days % 10 != 1]}"
    due = f'{str(date.today() + timedelta(days=days))}T12:00:00+03:00'  # not possible to set time by API, date only
    task = {
        'title': title,
        'notes': note,
        'due': due
    }
    service.tasks().insert(tasklist=list_id, body=task).execute()


list_name = open('list_name.txt').read()

service = api.connect()
user_lists = service.tasklists().list().execute()['items']

for tasks_list in user_lists:
    if tasks_list['title'] == list_name:
        list_id = tasks_list['id']
        break
else:
    raise NameError(f'Error: list "{list_name}" not found')

repeat_theme = input("Repetition theme: ")

# you can set your own repetitions (in days), may be any number of them
repeat_in = (1, 3, 7, 30)

for d in repeat_in:
    create_task(repeat_theme, d)
