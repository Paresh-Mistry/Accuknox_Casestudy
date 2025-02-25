from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
import threading

# Question 1: By default, are Django signals executed synchronously or asynchronously?
@receiver(post_save, sender=User)
def my_signal_handler_1(sender, instance, **kwargs):
    print("Signal received, processing...")
    time.sleep(3)  # Simulating a delay
    print("Signal processing completed.")
new_user = User.objects.create(username="test_user")
print("User creation completed.")


# Question 2: Do Django signals run in the same thread as the caller?
@receiver(post_save, sender=User)
def my_signal_handler1(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")
print(f"Main thread: {threading.current_thread().name}")
new_user = User.objects.create(username="test_user")


# Question 3: By default, do Django signals run in the same database transaction as the caller?
@receiver(post_save, sender=User)
def my_signal_handler2(sender, instance, **kwargs):
    print(f"Signal inside transaction: {transaction.get_connection().in_atomic_block}")

# Test: Creating a new user inside a transaction
with transaction.atomic():
    new_user = User.objects.create(username="test_user")


