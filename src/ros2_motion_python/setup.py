import os
from glob import glob
from setuptools import setup


package_name = 'ros2_motion_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        #(os.path.join('share', package_name), glob('launch/*.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Anis Koubaa',
    maintainer_email='anis.koubaa@gmail.com',
    description='Learn about ROS2 motion',
    license='Creative Commons Non-Commercial (CC-NC)',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mover= ros2_motion_python.simple_turtlesim_motion:main',
            'cleaner= ros2_motion_python.clean:main',
            'tb3_cleaner= ros2_motion_python.tb3_clean:main',
            #'nav= ros2_motion_python.nav:main',
        ],
    },
)
