import os
import glob
import os.path


class Sata(object):
    def __init__(self):
        pass

    @property
    def is_powersave(self):
        for path_device in self.devices:
            if os.path.isfile(path_device):
                if 'min_power' not in self._run("cat %s" % path_device):
                    return False
        return True

    @property
    def devices(self):
        for path_device in glob.glob("/sys/class/scsi_host/host*"):
            yield "%s/link_power_management_policy" % path_device

    def powersave(self):
        for path_device in self.devices:
            if os.path.isfile(path_device):
                yield "echo 'min_power' > '%s';" % path_device

    def perfomance(self):
        for path_device in self.devices:
            if os.path.isfile(path_device):
                yield "echo 'medium_power' > '%s';" % path_device

    def _run(self, command):
        return os.popen(command).read()

    def __str__(self):
        return "SATA switcher"


if __name__ == "__main__":
    print((Sata()))
    print((Sata()).is_powersave)
    print([str(device) for device in (Sata()).devices])
    print([str(device) for device in (Sata()).powersave()])
    print([str(device) for device in (Sata()).perfomance()])