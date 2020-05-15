from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


# one to one relationship
class Profile(models.Model):
    # CASCADE means if the user is deleted the profile is deleted
    # However, If the profile is deleted, the user is not deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user-thumb.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# # Resize the image
#     def save(self):
#         super().save()
#
#         image = Image.open(self.image.path)
#         #To resize the profile image
#         if image.height > 400 or image.width > 400:
#             output_size = (400, 400)
#             image.thumbnail(output_size)
#             image.save(self.image.path)


