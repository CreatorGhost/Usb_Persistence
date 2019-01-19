import subprocess
dev=raw_input('[+] Enter Device Name')
subprocess.call('mkfs.ext3 -L persistence ' + dev, shell=True)
subprocess.call("e2label " + dev + " persistence", shell=True)
subprocess.call("mkdir -p /mnt/my_usb", shell=True)
subprocess.call("mount " + dev +" /mnt/my_usb", shell=True)
subprocess.call("echo ""/ union"" > /mnt/my_usb/persistence.conf", shell=True)
subprocess.call("umount " + dev, shell=True)
