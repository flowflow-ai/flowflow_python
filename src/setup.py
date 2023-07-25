from setuptools import setup, find_packages

setup(
    name='flowflow_client',
    version='0.0.3',
    description='A Python client for FlowFlow.ai',
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
