# home_guard
### rpi_4 with face regonize

> libcamera-hello -t 0 --framerate 30 --fullscreen --width 1920 --height 1080 

> libcamera-vid -t 10000 --width 1920 --height 1080 --framerate 30 -o video.h264

### 16x2 LCD

> welcome WYTU Attanences System
> time, 
> ip address
> warming servo
> warming lcd
> warming camera

> conda config --set auto_activate_base false


> camera started.

### installation 

> sudo apt install wget bzip2 libssl-dev libboost-python-dev python3-opencv 
> wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-aarch64.sh 
> /bin/bash Miniconda3-py39_4.9.2-Linux-aarch64.sh
> conda create -n face python=3.10
> conda activate face 
> pip install -r requirements.txt  
> python3 check_camera.py 
 
> v4l2-ctl --list-devices
> gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, width=1920, height=1080, framerate=30/1 ! videoconvert ! autovideosink

> vcgencmd get_mem gpu
 

> download data/ dir from google drive
> https://drive.google.com/drive/folders/1Du_ImTaQjnA5sORvMhNfQmExgIqxxS_K?usp=sharing


### Usage

> 16x2 LCD and servo are connected with RPI 4B's GPIO Pins

> Pi Bookworm Desktop version OS 2024

> dot.config directory must be located as .config dir in the home directory for startup terminal at boottime.

> There's no cronjob @reboot option

> can export attendance.csv using csv_data.py and must be delete table if you have somethings to alter table column.

> sqlite3 cannot alter existing table. so we have to delete table using table_delete.py

> data/ directory must be downloaded from G drive for AI Face Regonization. 

> startup_script.sh must be called from the previous ~/.config/autostart/startup_terminal.desktop    


### Disk Clone

> sudo pacman -S dosfstools

> sudo pacman -Rns $(pacman -Qdtq)

> sudo cfdisk /dev/sdX

> sudo mkfs.vfat -n bootfs /dev/mmcblk0p1
> sudo mkfs.ext4 -L rootfs /dev/mmcblk0p2

> sudo dd if=/dev/mmcblk0 of=/dev/sdb bs=4M status=progress
> sudo dd if=/dev/sdb of=/dev/mmcblk0 bs=4M status=progress
> sudo dd if=/dev/sdb1 of=/dev/mmcblk0p1 bs=4M status=progress
> sudo dd if=/dev/sdb2 of=/dev/mmcblk0p2 bs=4M status=progress

> sudo fsck.vfat /dev/sdb1
> sudo fsck.ext4 /dev/sdb2


> sync
