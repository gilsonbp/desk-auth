from setuptools import setup

setup(
    name="Desk Auth",
    version="0.0.1",
    description="A Django application for user authentication.",
    long_description="file: README.md",
    url="http://www.desksytems.com.br",
    install_requires=[],
    author="Gilson Paulino",
    author_email="gilsonbp@gmail.com",
    license="MIT",
    packages=["desk_auth"],
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Framework :: Django :: 2.x",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: MIT",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
