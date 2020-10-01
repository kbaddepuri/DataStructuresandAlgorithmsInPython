from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='DataStructuresandAlgorithmsInPython',
    version='0.1.0',
    description='DataStructures and Algorithms using Python',
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: BSD 3-Clause License',

        # Social choice theory
        'Topic :: Computer Science :: Algorithms :: Data Structures',
        'Topic :: DS and Algos',

        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    author_email='kranthikumar6789@gmail.com',
    url='https://github.com/kbaddepuri/DataStructuresandAlgorithmsInPython',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'examples')),
    tests_require=[
        'pytest',
    ],
)