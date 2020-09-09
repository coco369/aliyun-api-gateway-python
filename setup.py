from setuptools import setup, find_packages

with open('readme.rst') as f:
    readme = f.read()

setup(
    name="python-aliyun-api-gateway",
    packages=find_packages(),
    version='0.0.2',
    description="aliyun api gateway",
    long_description=readme,
    author="wanghaifei",
    author_email='779598160@qq.com',
    url="https://github.com/coco369/aliyun-api-gateway-python",
    download_url='https://github.com/coco369/aliyun-api-gateway-python',
    keywords=['command', 'line', 'tool'],
    classifiers=[],
    entry_points={
        'console_scripts': [

        ]
    },
    install_requires=[
        'python3.7.6',
    ]
)
