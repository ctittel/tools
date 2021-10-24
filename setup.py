from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    install_requires=['pydantic',
                      'argparse',
                      'humanfriendly',
                      ],
    extras_require={
    },
    scripts=[
        'scripts/ct_note',
        'scripts/ct-git-sync'
        ]
)
