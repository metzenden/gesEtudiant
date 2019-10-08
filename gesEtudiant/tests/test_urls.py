from django.urls import reverse, resolve


class testUrls:
    def test_detail_url(self):
        path = reverse('details', kwargs={'pk': 1})
        assert resolve(path).view_name == "detail"