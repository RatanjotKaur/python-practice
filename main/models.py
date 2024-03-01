from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Items(models.Model):
    todoList = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length = 300)
    completed = models.BooleanField()

    def __str__(self):
        return self.text
