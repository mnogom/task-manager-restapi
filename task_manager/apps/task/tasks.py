from celery import shared_task
from django.core.mail import send_mail
from django.template import Template, Context
from task_manager.apps.user.models import User
from .models import Task


TASK_TEMPLATE = """
Tasks:

{% for task in tasks %}
        "{{ task.name }}"
{% endfor %}
"""


@shared_task
def send_list_task(user_id):
    user = User.objects.get(pk=user_id)
    template = Template(TASK_TEMPLATE)
    tasks = Task.objects.filter(author=user_id)

    send_mail(
        'All your Tasks',
        template.render(context=Context({'tasks': tasks})),
        None,
        [user.email],
        fail_silently=False,
    )
