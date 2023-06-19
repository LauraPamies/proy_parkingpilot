import os
from glob import glob
from setuptools import setup

package_name = 'proy_parkingpilot_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*.pgm')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'config'), glob('config/*.rviz')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),  
        (os.path.join('share', package_name, 'config'), glob('config/*.lua')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')), 
        (os.path.join('share', package_name, 'config'), glob('config/*.xml')) 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='laura',
    maintainer_email='laurapamiesvillagordo@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'initial_pose_pub = proy_parkingpilot_nav.initial_pose_pub:main' #añadir
            #'ex_nav_to_pose = pamies_villagordo_ex_my_nav2_system.ex_nav_to_pose:main' #añadir
            'action_server = proy_parkingpilot_nav.action_server:main',
            'nav_to_pose = proy_parkingpilot_nav.nav_to_pose:main',   # incluir
            'waypoint_follower = proy_parkingpilot_nav.waypoint_follower:main'
        ],
    },
)
