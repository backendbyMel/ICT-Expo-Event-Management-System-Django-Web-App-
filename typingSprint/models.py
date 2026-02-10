from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

class Challenger(models.Model):
    """
    Stores typing sprint challengers and their results.
    Each record is linked to the staff user who entered it.
    """

    # --- Challenger Info ---
    name = models.CharField(
        max_length=100,
        help_text="Full name of the challenger"
    )

    section = models.CharField(
        max_length=50,
        help_text="Student year and section"
    )

    speed_score = models.PositiveIntegerField(
        help_text="Typing net speed in Words Per Minute (WPM)"
    )
    photo = models.ImageField(upload_to='challenger_photos/', null=True, blank=True)
    # photo = models.ImageField(
    #     upload_to='challengers/',
    #     blank=True,
    #     null=True,
    #     help_text="Optional photo (Top 10 challengers only)"
    # )

    # --- Staff Tracking ---
    entered_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='typed_challengers',
        help_text="ICT staff who entered this record"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the challenge was taken"
    )

    class Meta:
        ordering = ['-speed_score', 'created_at']
        verbose_name = "Typing Challenger"
        verbose_name_plural = "Typing Challengers"

    def __str__(self):
        return f"{self.name} ({self.section}) - {self.speed_score} WPM"

    # -----------------------------
    # Utility Method
    # -----------------------------
    def is_in_top_10(self):
        """
        Returns True if this challenger belongs to the current Top 10.
        Ranking is computed dynamically.
        """
        top_10_ids = (
            Challenger.objects
            .order_by('-speed_score', 'created_at')
            .values_list('id', flat=True)[:10]
        )
        return self.id in top_10_ids
    
    def get_absolute_url(self):
        return reverse('typingSprint-home')