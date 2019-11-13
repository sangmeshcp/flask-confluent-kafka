# please install python if it is not present in the system
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
 name='flask-confluent-kafka',
 version='0.0.5',
 packages=['flask-confluent-kafka'],
 install_requires=['confluent-kafka'],
 license='MIT',
 description='An easy to use kafka consumer that uses the confluent-kafka-python library,'
             'it runs concurrently with your flask server',
 author='sangamesh patil',
 author_email='sangmeshcp@gmail.com',
 keywords = ['kafka', 'consumer', 'kafkaesque', 'flask', 'simple', 'consumer', 'flask style', 'decorator',
             'confluent-kafka'],
 long_description=long_description,
 long_description_content_type="text/markdown",
 url="https://github.com/sangmeshcp/flask-confluent-kafka",
 include_package_data=True,
)