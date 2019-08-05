from os import path
from shutil import disk_usage
total_bytes, used_bytes, free_bytes = disk_usage(path.realpath('/'))
total_bytes = total_bytes / 1000000
total_bytes = total_bytes.__round__(0)

print("Disk Size", total_bytes, "MB")
print("Disk Used", used_bytes / 1000000, "MB")
print("Disk Free", free_bytes / 1000000, "MB")
