from setuptools import setup, find_packages

setup(
    name='superpokerdex',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=4.0',
        'requests',
        
        # ajoute ici les autres libs que tu utilises si besoin
    ],
    entry_points={
        'console_scripts': [
            'manage = manage:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
