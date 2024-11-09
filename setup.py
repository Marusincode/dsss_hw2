from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    author="Mariia",
    author_email="mary.svimonishvili@gmail.com",
    description="DSSS homework 2",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Marusincode/dsss_hw2.git",
    license="Apache License",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'math-quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
)