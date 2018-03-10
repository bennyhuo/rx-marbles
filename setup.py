import setuptools

setuptools.setup(name='rxmarbles',
      version='0.2',
      description='Marbles diagram generator',
      url='https://bitbucket.org/achary/rx-marbles/',
      author='Adam Charytoniuk',
      author_email="adam.charytoniuk@gmail.com",
      keywords = ['marbles', 'rx', 'diagrams','reactive'],
      license='MIT',
      packages=setuptools.find_packages(),
       entry_points={
          'console_scripts': [
              'marblesgen = rxmarbles.__main__:main'
          ]
      },
      zip_safe=False)