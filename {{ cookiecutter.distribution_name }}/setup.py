from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.distribution_name }}',
    version='{{ cookiecutter.version }}',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    description='{{ cookiecutter.description_short }}',
    url='{{ cookiecutter.url }}',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points='''
    ''',
    install_requires=(
    ),
    zip_safe=False,
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    )
)

