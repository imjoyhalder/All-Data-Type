

list3 = ["asdfj","dsf"]
list3.reverse()
print(list3)

import shutil

# Specify the path and required space
path = "/"  # Replace with the desired directory path
required_space_gb = 10

# Get disk usage of the specified path
usage = shutil.disk_usage(path)

# Convert required space to bytes
required_space_bytes = required_space_gb * (1024 ** 3)

# Check if there is enough space available
if usage.free >= required_space_bytes:
    print("There is enough space available.")
else:
    print("Insufficient space.")
