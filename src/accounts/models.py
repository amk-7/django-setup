from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from scripts.utils import remove_all_space_from_word

class Person():
    class Meta:
        abstract = True
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profil = models.ImageField(storage="users_profils", null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.EmailField(unique=True)
    SEXE_CHOISE = [
        ('F', 'Feminin'),
        ('M', 'Masculin')
    ]
    sexe = models.CharField(max_length=1, choices=SEXE_CHOISE)
    date_of_birth = models.DateField(null=True, blank=True)
    create_at = models.DateTimeField(default=datetime.now,blank=True)
    update_at = models.DateTimeField(null=True, blank=True)
    delete_at = models.DateTimeField(null=True, blank=True)
    
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.user = User.objects.create_user(username=self.phone_number, password="123456789")
        else:
            self.update_at = datetime.now()
        
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f"{self.user}"
    
    