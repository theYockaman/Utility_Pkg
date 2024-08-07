from setuptools import setup, find_packages

setup(
    name = "utils"
    , version = "0.1.0"
    , author = "Nathan Yockey"
    , author_email = 'n8teyock@gmail'
    , url = ''
    , description = "Utils Package is universal across building of other Python Projects"
    , packages = find_packages()
    , include_package_data=True
    , package_data = {
        'utils': ['templates/HTML/*'
                  ,'templates/CSS/*'
                  ,'templates/CSS/Basics/*'
                  ,'templates/JS/*'
                  ,'templates/PHP/*'
                  ,'templates/MD/*'
                  ,'templates/Templates/*'
        ]
    }
    , long_description = open("README.md").read()
    , long_description_content_type = 'text/markdown'
    
)