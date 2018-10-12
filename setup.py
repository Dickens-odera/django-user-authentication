from setuptools import setup, find_packages

NAME = 'django authentication system'
DESCRIPTION = 'This system enables users to register, login and logout of the system'
AUTHOR = 'dickens odera'
AUTHOR_EMAIL = 'dickensodera9@gmal.com'
PROJECT_URL = 'https://github.com/Dickens-odera/django-user-authentication.git'

setup(
    name = NAME,
    description = DESCRIPTION,
    author = AUTHOR,
    email = AUTHOR_EMAIL,
    url = PROJECT_URL,
    version = '1.0.1',
    packages = find_packages()
    
)

