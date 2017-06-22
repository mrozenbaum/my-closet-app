=====
ClosetClient
=====

ClosetClient is a simple Django app to conduct Web-based categories, and items. where users can add items to their categories and keep track of their "closet's" inventory!. For each
category, visitors can choose between a fixed number of answers(items)

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "closetclient" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'closetclient',
    ]

2. Include the closetclient URLconf in your project urls.py like this::

    url(r'^closetclient/', include('closetclient.urls')),

3. Run `python manage.py migrate` to create the closetclient models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a ClosetClient (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in ClosetClient.