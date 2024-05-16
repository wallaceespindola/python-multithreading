from setuptools import setup, find_packages

# Read the requirements from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='python_multithreading',
    version='0.1.0',
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'python_multithreading=python_multithreading.main_module:main',
        ],
    },
)
