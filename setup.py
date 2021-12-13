from setuptools import setup, find_packages
import versioneer

setup(
    name='redkite-pbi-tools',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Redkite DevOps tools for working with PBI',
    long_description=open('README.md').read(),
    install_requires=['gitpython'],
    dependency_links=['git+https://github.com/thomas-daughters/pbi-tools.git#1.1.0'],
    url='https://github.com/thomas-daughters/redkite-pbi-tools',
    author='Sam Thomas',
    author_email='sam.thomas@redkite.com'
)
