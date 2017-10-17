from setuptools import setup

setup(name='rxmarbles',
      version='0.1',
      description='Marbles diagram generator',
      url='https://achary@bitbucket.org/achary/rx-marbles.git',
      author='Adam Charytoniuk',
      author_email="adam.charytoniuk@gmail.com",
      license='MIT',
      packages=setuptools.find_packages(),
       entry_points={
          'console_scripts': [
              'marblesgen = rxmarbles.__main__:main'
          ]
      },
      zip_safe=False)
