#!/bin/bash

echo "Start updating"
echo "Download last version ..."
sudo git clone https://github.com/DragonDope/temperature_pi.git
echo "done"
echo "copy files ..."
sudo cp -r ./temperature_pi/* ./
sudo rm -r ./temperature_pi/
echo "done"
echo "update finished"

