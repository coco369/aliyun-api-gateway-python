from setuptools import setup, find_packages

setup(
    name="python-aliyun-api-gateway",
    packages=find_packages(),
    version='0.0.1',
    description="aliyun api gateway",
    author="wanghaifei",
    author_email='779598160@qq.com',
    url="https://github.com/coco369",
    download_url='https://github.com/coco369',
    keywords=['command', 'line', 'tool'],
    classifiers=[],
    entry_points={
        'console_scripts': [
        'command1 = advisorhelper.cmdline:execute'
        'command2 = adviserserver.create_algorithm:run',
        'command3 = adviserserver.run_algorithm:run'
    ]
    },
    install_requires=[
    ]
)