#/bin/python
import subprocess

# I use this for bemenu since sway won't pick up it up
MENU_OPTIONS = ''
# MENU_OPTIONS = '-H 32 -I 0 -i -m 0 --fn "Hack:14" --fb "#323232" --ff "#ffffff" --nb "#323232" --nf "#ffffff" --sf "#ffffff" --sb "#81a2be" --af "#ffffff" --ab "#323232" --tb "#81a2be" --tf "#ffffff" --hb "#81a2be" --hf "#ffffff"'

sp = subprocess.run(['wpctl', 'status'], stdout=subprocess.PIPE).stdout.decode('utf-8')\
        .split("Sinks")[1].split('├─')[0]
newsp = []

for line in sp.split('\n'):
    if '.' in line:
        newsp.append(line.replace(' ', '')[1:])

devices = {}  # name: id
for line in newsp:
    line = line.split('.')
    devices[line[1].split('[vol')[0]] = line[0].replace('*', '')

devices_list = '\\n'.join(devices.keys())

device_choise = subprocess.Popen(f'echo -e \"{devices_list}\" | dmenu -p "Choose Device"' + MENU_OPTIONS, shell=True,stdout=subprocess.PIPE)\
        .stdout.read().decode('utf-8')
device_choise = device_choise.replace('\n', '')
device_choise = devices[device_choise]

subprocess.Popen('wpctl set-default '+str(device_choise), shell=True,stdout=subprocess.PIPE)
