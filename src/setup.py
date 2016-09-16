from setuptools import setup
import os

PROJECT_ROOT, _ = os.path.split(__file__)
REVISION = '0.0.1'
PROJECT_NAME = 'pyventure'
PROJECT_AUTHORS = 'Salim Fadhley'
# Please see readme.rst for a complete list of contributors
PROJECT_EMAILS = 'salimfadhley@gmail.com'
PROJECT_URL = 'https://github.com/salimfadhley/jenkinsapi'
SHORT_DESCRIPTION = (
    'A Python API for accessing resources on a Jenkins '
    'continuous-integration server.'
)

try:
    DESCRIPTION = open(os.path.join(PROJECT_ROOT, 'README.rst')).read()
except IOError:
    DESCRIPTION = SHORT_DESCRIPTION

GLOBAL_ENTRY_POINTS = {
    'console_scripts': [
        'start_pyventure=pyventure.pyventure:main',
    ]
}

setup(
    name=PROJECT_NAME.lower(),
    version=REVISION,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    packages=[
        'pyventure',
        'pyventure_tests',
    ],
    zip_safe=True,
    include_package_data=False,
    install_requires=['click'],
    test_suite='nose.collector',
    tests_require=['mock', 'nose', 'coverage'],
    entry_points=GLOBAL_ENTRY_POINTS,
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    license='MIT',
)