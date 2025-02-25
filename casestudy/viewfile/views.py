from django.http import HttpResponse
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import models
import time
import threading

# Signal 1: Synchronous execution test
@receiver(post_save, sender=User)
def my_signal_handler_1(sender, instance, **kwargs):
    print("Signal received, processing...")
    time.sleep(3)  # Simulating a delay
    print("Signal processing completed.")

# Signal 2: Thread of execution test
@receiver(post_save, sender=User)
def my_signal_handler1(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

print(f"Main thread: {threading.current_thread().name}")

# Signal 3: Transaction block test
@receiver(post_save, sender=User)
def my_signal_handler2(sender, instance, **kwargs):
    print(f"Signal inside transaction: {transaction.get_connection().in_atomic_block}")

def test_signals():
    # Test 1 & 2: Creating a new user outside a transaction
    new_user = User.objects.create(username="test_user1")
    print("User creation completed outside transaction.\n")

    # Test 3: Creating a new user inside a transaction
    with transaction.atomic():
        new_user = User.objects.create(username="test_user2")
        print("User creation completed inside transaction.\n")

def home(request):
    # Call our test function to trigger the signals
    test_signals()
    return HttpResponse("Signals have been triggered. Check your console for output.")


def rect(request):
    rect = models.Rectangle(2,3)    
    return HttpResponse(list(attribute for attribute in models.Rectangle.iterater(rect)))