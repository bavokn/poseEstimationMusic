FROM  tensorflow/tensorflow:latest

RUN apt-get install -y ffmpeg libsm6 libxext6 x11-xserver-utils v4l-utils

RUN python -m pip install --upgrade pip opencv-contrib-python==4.3.0.36 numpy

#add user
RUN useradd -ms /bin/bash user \
&& echo "user:user" | chpasswd && adduser user sudo \
&& usermod -aG audio user \
&& chpasswd && adduser user sudo

# Change terminal prompt
USER user
RUN echo 'export PS1="🐳 \[\033[01;32m\]\u@$CONTAINER_NAME\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "' >> ~/.bashrc

WORKDIR /home/user/Documents/PoseMusic/poseEstimationMusic
CMD ["python", "run.py"]