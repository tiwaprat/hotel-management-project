import subprocess

# Open and read the requirements.txt file
with open('requirements.txt') as f:
    packages = f.read().splitlines()

# Loop through each package listed in requirements.txt
for package in packages:
    # Split on '==' to get the package name, ignoring the version number if present
    package_name = package.split('==')[0].strip()  # Strip any surrounding whitespace
    # Uninstall the package using pip
    subprocess.call(['pip', 'uninstall', '-y', package_name])
