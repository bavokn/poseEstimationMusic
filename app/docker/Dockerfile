FROM  tensorflow/tensorflow:latest

# install python ?

#add user
RUN useradd -ms /bin/bash user \
&& echo "user:user" | chpasswd && adduser user sudo \
&& usermod -aG audio user \
&& chpasswd && adduser user sudo

# Change terminal prompt
USER user
RUN echo 'export PS1="🐳 \[\033[01;32m\]\u@$CONTAINER_NAME\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "' >> ~/.bashrc

WORKDIR /home/user/Documents/poseEstimationMusic/app
CMD ["python3", "run.py"]