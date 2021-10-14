from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='qikdb',
  version='4.0.1',
  description='An easy to use JSON centered Python database module, made to make data storage easier.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/kunostaken77/qikdb/tree/Main',  
  author='Andrew Bordis',
  author_email='andrewbordis111@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=["qikdb", "db", "database", "json"], 
  packages=find_packages(),
  install_requires=[] 
)