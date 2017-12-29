from setuptools import setup

setup(
    name="simcalc",                #name of command
    version='10.0',              #use different veesion name for each
    py_modules=['simcalc'],        #python script to be included
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        simcalc=simcalc:simcalc        
    ''',
)
 #'command'='python_script':'function_name'
