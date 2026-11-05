from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PromoCode, ProjectGallery
from random import randint

from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

from django.core.mail import send_mail

# створений сигнал
@receiver(post_save, sender=User)
def create_promo_code(sender, instance, created, **kwargs): 
    if created:
        random_int = randint(100000, 999999)
        promo_str = f"PROMO_{random_int}"
        PromoCode.objects.create(
            user=instance,
            code=promo_str
        )


@receiver(post_save, sender=ProjectGallery)
def post_project_gallery(sender, instance, created, **kwargs): 
    if created:
        update_fields = []
        instance.alt_text = f"{instance.project.name} gallery image"
        instance.save(update_fields=['alt_text'])
        if instance.original_image:
            try:
                img = Image.open(instance.original_image.path)
                print(f"Image Opened {img}")
                if img.mode in ("RGBA", "P"):
                    print(f"Image's mode ({img.mode}) being converted into RGB")
                    img = img.convert("RGB")

                def resize_and_save(field_name, size):
                    temp_img = img.copy()
                    temp_img.thumbnail(size)
                    
                    buffer = BytesIO()
                    temp_img.save(buffer, format='JPEG', quality=85)
                    buffer.seek(0)
                    
                    file_name = f"project_{instance.pk}_{size[0]}x{size[1]}.jpg"
                    field = getattr(instance, field_name)
                    field.save(file_name, ContentFile(buffer.read()), save=False)
                    print(f"Saved {file_name} in {size[0]}px x {size[1]}px")

                # Generate variants
                resize_and_save('thumbnail', (150, 150))
                print("Trying to save image for thumbnail")
                resize_and_save('medium_image', (600, 400))
                print("Trying to save image for medium_image")
                resize_and_save('large_image', (1200, 800))
                print("Trying to save image for large_image")

                update_fields.extend(['thumbnail', 'medium_image', 'large_image'])
                print("Added fields to update_fields")
            except Exception as e:
                print(f"Error processing image for ProjectGallery {instance.pk}: {e}")

        if update_fields:
            instance.save(update_fields=update_fields)
            print(f"Saved the resized images for {instance}")

        if instance.project.user.email:
            send_mail(
                subject="Gallery for your Project",
                message="Your gallery has been saved successfuly",
                from_email=None,  # Defaults to DEFAULT_FROM_EMAIL in settings.py
                recipient_list=[instance.project.user.email],
                fail_silently=False,  # Set to True if you want to suppress errors
            )