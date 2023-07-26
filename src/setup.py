from setuptools import setup, find_packages

setup(
    name='flowflow',
    version='0.0.4',
    description='FlowFlow.AI Python client',
    author='Mick Vermaat',
    author_email='support@flowflow.ai',
    url='https://flowflow.ai',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
