
'''
    FIXME - this really needs some love
'''

import distutils.command.install_data
from distutils.core import setup


class cm_install(distutils.command.install_data.install_data):
    def run(self):
        install = self.get_finalized_command('install')
        self.install_dir = getattr(install, 'install_data')
        return distutils.command.install_data.install_data.run(self)


files = [ 'cm-watch' ]

setup (
        name             = 'cm-watch',
        version          = '0.1',
        author           = 'Nelson Marques'
        author_email     = 'nmo.marques@gmail.com',
        description      = 'A notify tool for CyanogenMod updates'
        long_description = 'A tool to check for CyanogenMod updates for a few terminals I own'
        license          = 'Public Domain'
        url              = 'https://github.com/ketheriel/cm-watch'
        packages         = [ 'cm-watch' ]
        scripts          = [ 'bin/cm-watch' ]
        package_data     = { 'cm-watch': files }
        cmdclass         = { 'install_data': cm_install }
      )
        
