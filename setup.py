from setuptools import setup, find_packages

setup(
   name='terrashire',
   version='1.0',
   description='Homelab Tool',
   author='Moses',
   author_email='',
   packages=find_packages(),  #same as name
   install_requires=['paprika', 'paramiko', 'typer', 'watchdog'], #external packages as dependencies
   include_package_data=True, # This is crucial
)
