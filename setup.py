from setuptools import setup
setup(name='MongoGraph',
        version='1.0',
        author='Abhishek Pawaskar',
        description='Use Graph Easily',
        long_description='Conduct CRUD operations on Graph DataBase without learning Gremlin',
        url='https://github.com/AbhishekPawaskar/',
        keywords='grepheasy, graph_easy, GRAPH_EASY',
        python_requires=">=3.10",
        platforms=["Windows", "Linux"],
        install_requires=['pymongo==4.3.3','dnspython==2.3.0'],
        packages=['MongoGraph'],
        setup_requires=['wheel'])