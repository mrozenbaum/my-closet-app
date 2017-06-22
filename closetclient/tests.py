from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse


from .models import Category

# Create your tests here.

class CategoryModelTests(TestCase):


    def test_was_published_recently_with_future_category(self):
        """
        was_published_recently() returns False for Categorys whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_category = Category(pub_date=time)
        self.assertIs(future_category.was_published_recently(), False)


    def test_was_published_recently_with_old_category(self):
        """
        was_published_recently() returns False for Categorys whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1)
        old_category = Category(pub_date=time)
        self.assertIs(old_category.was_published_recently(), False)


    def test_was_published_recently_with_recent_category(self):
        """
        was_published_recently() returns True for Categorys whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_category = Category(pub_date=time)
        self.assertIs(recent_category.was_published_recently(), True)

    def create_category(category_name, days):
        """
        create a Category with the given `category_name` and published the
        given number of `days` offset to now (negative for Catagorys published
        in the past, positive for Categorys that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Category.objects.create(category_name=category_name, pub_date=time)


class CategoryIndexViewTests(TestCase):

    def test_no_categorys(self):
        """
        If no Catagorys exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('closetclient:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Categorys are available.")
        self.assertQuerysetEqual(response.context['latest_category_list'], [])

    def test_past_category(self):
        """
        Categorys with a pub_date in the past are displayed on the index page.
        """
        create_category(category_name="Past category.", days=-30)
        response = self.client.get(reverse('closetclient:index'))
        self.assertQuerysetEqual(response.context['latest_category_list'],['<Category: Past category.>']
        )

    def test_future_category_and_past_category(self):
        """
        Even if both past and future Categorys exist, only past Categorys
        are displayed.
        """
        create_category(category_name="Past category.", days=-30)
        create_category(category_name="Future category.", days=30)
        response = self.client.get(reverse('closetclient:index'))
        self.assertQuerysetEqual(
            response.context['latest_category_list'],
            ['<Category: Past category.>']
        )

    def test_two_past_categorys(self):
        """
        The categorys index page may display multiple categorys.
        """
        create_category(category_name="Past Category 1.", days=-30)
        create_category(category_name="Past Category 2.", days=-5)
        response = self.client.get(reverse('closetclient:index'))
        self.assertQuerysetEqual(
            response.context['latest_category_list'],
            ['<Category: Past Category 2.>', '<Category: Past Category 1.>']
        )


class CategoryDetailViewTests(TestCase):

    def test_future_category(self):
        """
        the detail view of a Category with a pub_date in the future returns a 404 not found.
        """
        future_category = create_category(category_name='Future Category.', days=5)
        url = reverse('closetclient:detail', args=(future_category.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_category(self):
        """
        the detail view of a Category with a pub_date in the past displays the Category's text.
        """
        past_category = create_category(category_name='Past Category.', days=-5)
        url = reverse('closetclient:detail', args=(past_category.id,))
        response = self.client.get(url)
        self.assertContains(response, past_category.category_name)








      



