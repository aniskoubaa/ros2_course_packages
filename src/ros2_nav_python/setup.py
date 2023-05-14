from setuptools import setup

package_name = 'ros2_nav_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'nav= ros2_nav_python.nav:main',
            'tf_demo= ros2_nav_python.tf_demo:main',
            'static_tf= ros2_nav_python.static_tf:main',
            'transform_listener= ros2_nav_python.transform_listener:main',
            'transform_broadcaster= ros2_nav_python.transform_broadcaster:main',
            'tb3_nav= ros2_nav_python.tb3_nav:main',
        ],
    },
)


