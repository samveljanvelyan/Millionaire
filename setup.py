import platform
import subprocess
from distutils.command.build import build as _build

from setuptools import setup, find_packages, Command


class build(_build):
    sub_commands = _build.sub_commands + [('CustomCommands', None)]


class CustomCommands(Command):
    """A setuptools Command class able to run arbitrary commands."""

    def RunCustomCommand(self, command_list):
        print('Running command: %s' % command_list)

        p = subprocess.Popen(
            command_list,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout_data, _ = p.communicate(input='y\n'.encode())
        print('Command output: %s' % stdout_data)
        if p.returncode != 0:
            raise RuntimeError(
                'Command %s failed: exit code: %s' % (command_list, p.returncode))

    def run(self):
        for command in commands:
            self.RunCustomCommand(command)


system = platform.system()
if system == 'Linux':
    commands = [['pip install -r requirements.txt'],
                ['cd Millionaire/'], ['python manage.py makemigrations'],
                ['python manage.py migrate'], ['python database_connector.py']]

setup(name='Millionaire',
      author='Samvel Janvelyan',
      packages=find_packages(),
      version='1.0',
      scripts=['Millionaire/database_connector.py'],
      description='Who wants to be a millionaire, implemented with django models.',
      url='https://github.com/samveljanvelyan/Millionaire',
      download_url='https://github.com/samveljanvelyan/Millionaire.git',
      classifiers=[],
      cmdclass={
          'build': build,
          'CustomCommands': CustomCommands
      }
      )
