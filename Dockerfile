FROM athackst/ros2:galactic-gazebo

ARG USERNAME=ros
ENV HOME=/home/${USERNAME}
ENV WS=${HOME}/ws
RUN mkdir -p ${WS}/src

RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy

WORKDIR $WS

COPY . src/batteryhunter

RUN colcon build --merge-install --symlink-install --cmake-args '-DCMAKE_EXPORT_COMPILE_COMMANDS=ON' '-DCMAKE_BUILD_TYPE=RelWithDebInfo' -Wall -Wextra -Wpedantic

RUN echo "if [ -f ${WS}/install/setup.bash ]; then source ${WS}/install/setup.bash; fi" >> ${HOME}/.bashrc

RUN chown -R ros:ros ${WS}
