#to install use sudo python setup.py install

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Mimi Plots',
    author='Jeremy Rothschild',
    author_email='jerben.rothschild@gmail.com',
    # Needed to actually package something
    packages=['latex_plots'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIMICO',
    description='Python Package for plotting things',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
