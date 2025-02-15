from django.db import models
from django.contrib.auth.models import User


# User Profile Model
class Profile(models.Model):
    USER_TYPES = [
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Freelancer(models.Model):
    CATEGORY_CHOICES = [
        ("UI/UX & Web Designers", "UI/UX & Web Designers"),
        ("Graphic & Visual Designers", "Graphic & Visual Designers"),
        ("Digital & Marketing Designers", "Digital & Marketing Designers"),
        ("Multimedia & Video Designers", "Multimedia & Video Designers"),
        ("Industrial & Product Designers", "Industrial & Product Designers"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='freelancers')
    portfolio_url = models.URLField(blank=True, null=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subcategory}"


# Skill Model
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

# Job Posting Model
class Job(models.Model):
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'client'})
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Proposal Model
class Proposal(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='proposals')
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.freelancer.profile.user.username} - {self.job.title}"

# Review Model
class Review(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, related_name='reviews')
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'client'})
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.user.username} → {self.freelancer.profile.user.username} ({self.rating})"

# Messages between Client and Freelancer
class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.user.username} to {self.receiver.user.username}"

