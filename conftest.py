import django
from django.conf import settings

def pytest_configure(config):
    """Configura o ambiente Django para os testes"""
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',

            "gastos",
        ],
        
    )
    django.setup()