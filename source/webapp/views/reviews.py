from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import UserReviewForm


class CreateReviewVies(CreateView):
    form_class = UserReviewForm
    template_name = "reviews/create_review.html"


    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.product.pk})
