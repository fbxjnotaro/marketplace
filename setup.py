import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Marketplace", # Replace with your own username
    version="0.0.1.4",
    author="functionalbox europe",
    author_email="support@functionalbox.eu",
    description="Market Place System for Django Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@github.com:fbxjnotaro/marketplace.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'django>=3',
        'django-allauth',
        'python-decouple',
        'django-crispy-forms',
        'django-extensions',
        'django-extra-views',
        'django-prices',
        'django-tagulous',
        'django-geojson[field]',
        'django-compressor',
        'django-libsass',
    ],
    #packages+=[
   #     'marketplace',
   #     'marketplace.apps.core',
   #     'marketplace.apps.board',
   #     'marketplace.apps.messaging',
   #     'marketplace.apps.social',
   # ],
    package_data={
        'marketplace': [
            'templates/marketplace/*.html', 'static/marketplace/js/*.js',
            'static/marketplace/img/*.svg', 'static/marketplace/scss/*.scss',
            'static/marketplace/scss/bootstrap4_2/*.scss',
            'static/marketplace/scss/bootstrap4_2/mixin/*.scss',
            'static/marketplace/scss/bootstrap4_2/utilities/*.scss'
        ]
    },
)
