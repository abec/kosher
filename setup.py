from setuptools import setup, find_packages
import sys

module = __import__('kosher')

readme_file = 'README.mkd'
try:
    long_description = open(readme_file).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

setup(name='kosher',
      version=module.get_version(),
      description='Virtual environment, project information, and utilities handling for fabric.',
      long_description=long_description,
      zip_safe=False,
      author='Abraham Elmahrek',
      author_email='abraham@elmahrek.com',
      packages = find_packages(),
      include_package_data=True,
      install_requires = [
        'fabric', 'cuisine'
      ],
      classifiers = ['Development Status :: 1 - Planning',
                     'Environment :: Console',
                     'Framework :: Fabric',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Software Development :: Build Tools'],
      )
