from django.db import models

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='sub_departments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Letter Model
class Letter(models.Model):
    LETTER_TYPES = [
        ('maktob', 'Maktob'),
        ('estilam', 'Estilam'),
        ('peshnihad', 'Peshnihad'),
    ]

    number_sadira = models.CharField(max_length=100, unique=True)
    number_warida = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=255)
    sender_department = models.ForeignKey(Department, related_name='sent_letters', on_delete=models.CASCADE)
    receiver_department = models.ForeignKey(Department, related_name='received_letters', on_delete=models.CASCADE)
    content = models.TextField()
    letter_type = models.CharField(max_length=20, choices=LETTER_TYPES)
    create_date = models.DateField(auto_now_add=True)
    sender_date = models.DateField()
    receiver_date = models.DateField()
    
    # 🔥 New field to attach physical letter (PDF, image, etc.)
    attach = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.subject} ({self.letter_type})"


# Letter Tracking Model
class LetterTracking(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('received', 'Received'),
        ('delivered', 'Delivered'),
    ]

    letter = models.ForeignKey(Letter, related_name='tracking_records', on_delete=models.CASCADE)
    sender_department = models.ForeignKey(Department, related_name='tracking_sent', on_delete=models.CASCADE)
    receiver_department = models.ForeignKey(Department, related_name='tracking_received', on_delete=models.CASCADE)
    sent_date = models.DateField()
    received_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Track {self.letter.subject} [{self.status}]"
