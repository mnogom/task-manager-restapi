"""Models."""

from django.db import models


class Task(models.Model):
    name = models.CharField(verbose_name='name',
                            max_length=300,
                            blank=False,
                            null=False,
                            unique=True,
                            error_messages={
                                'unique': 'A task with that name already exists'})
    description = models.TextField(verbose_name='description',
                                   blank=True,
                                   null=False)
    author = models.ForeignKey('user.User',
                               verbose_name='author',
                               on_delete=models.PROTECT,
                               related_name='author')
    executor = models.ForeignKey('user.User',
                                 verbose_name='executor',
                                 on_delete=models.PROTECT,
                                 related_name='executor')
    status = models.ForeignKey('status.Status',
                               verbose_name='status',
                               on_delete=models.PROTECT,
                               related_name='status')
    labels = models.ManyToManyField('label.Label',
                                    verbose_name='labels',
                                    through='TaskLabel',
                                    blank=True)
    created_at = models.DateField(verbose_name='created at',
                                  auto_now_add=True,
                                  editable=False)

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey('task.Task',
                             on_delete=models.CASCADE)
    label = models.ForeignKey('label.Label',
                              on_delete=models.PROTECT)
