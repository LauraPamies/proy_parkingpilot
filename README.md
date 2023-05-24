# PROYECTO PARKING PILOT

En este proyecto de ROS2 se crea un entorno donde el robot va a poder navegar y visualizar a través de una cámara implementada.

## Instalación

A continuación se detallan los pasos necesarios para instalar y configurar el proyecto en el entorno de desarrollo.

Clona este repositorio:
git clone https://github.com/LauraPamies/proy_parkingpilot.git

## Paquetes del proyecto
### Mundo
En este paquete se encuentra el mundo de gazebo por el que el robot va a navegar de manera automática en forma de simulación.
Este mundo ha sido escaneado de manera que el robot va a poder acceder a todas las zonas, a parte va a tener una cámara capaz de captar su visión del entorno.

### Navegación
En este paquete se encuentra la navegación automática del robot, el cual va a poder navegar por el entorno de gazebo siguiendo una ruta de puntos de manera automática.


## Uso

### Para compilar el paquete del mundo:
1. Compila el paquete deseado:
colcon build --packages-select proy_parkingpilot_mundo
source /opt/ros/galactic/setup.bash
source install/setup.bash
export GAZEBO_MODEL_PATH=$HOME/turtlebot3_ws/src/my_world/models:$GAZEBO_MODEL_PATH

2. Lanza el paquete deseado:
ros2 launch proy_parkingpilot_mundo proy_parkingpilot_mundo.launch.py

### Para compilar el paquete de navegación:
1. Compila el paquete deseado:
colcon build --packages-select proy_parkingpilot_nav
source /opt/ros/galactic/setup.bash
source install/setup.bash

2. Lanza el paquete deseado:
ros2 launch proy_parkingpilot_nav proy_parkingpilot_nav.launch.py

3. Carga el mapa:
ros2 service call /map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_parkingpilot/proy_parkingpilot_nav/config/my_map.yaml}"





## Manejo de ramas

En cada sprint se usará una rama donde se encontrarán los cambios finales. Para navegar entre ellas hay que utilizar el comando
git checkout release0X , donde X corresponde al número del sprint.




