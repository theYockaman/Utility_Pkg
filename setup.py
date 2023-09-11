from setuptools import setup, find_packages

setup(
    name = "utils"
    , version = "0.0.1"
    , author = "Nathan Yockey"
    , author_email = 'n8teyock@gmail'
    , url = ''
    , description = "Utils Package is universal across building of other Python Projects"
    , packages = find_packages()
    , install_requires=[
        'pandas'
        , 'sqlite3'
        , 'os'
        , 'json'
        , 'abc'
        , 'traceback'
        , 'sys'
        , 'time'
    ]
    , long_description = open("README.md").read()
    , long_description_content_type = 'text/markdown'
    
)