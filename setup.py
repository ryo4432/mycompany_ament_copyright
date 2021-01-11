from setuptools import find_packages
from setuptools import setup

package_name = 'mycompany_ament_copyright'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    package_data={'': [
        'template/*',
    ]},
    zip_safe=False,
    maintainer='Ryo Yoshimitsu',
    maintainer_email='ryoyoshimitsu@gmail.com',
    description='For creation of original copyright',
    long_description="""\
The ability to check sources file for copyright and license information.""",
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'mycompany_ament_copyright.copyright_name': [
            'mycompany = mycompany_ament_copyright.copyright_names:mycompany',
        ],
        'mycompany_ament_copyright.license': [
            'mycompany = mycompany_ament_copyright.licenses:mycompany',
        ],
        'console_scripts': [
            'mycompany_ament_copyright = mycompany_ament_copyright.main:main',
        ],
        'pytest11': [
            'ament_copyright = ament_copyright.pytest_marker',
        ],
    },
)
