from setuptools import setup

setup(
    name='{{ cookiecutter.module_name }}',
    python_requires='>=3.9',
    version='{{ cookiecutter.version }}',
    packages=['{{ cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_') }}', '{{ cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_') }}.{{ cookiecutter.keyword.lower() }}_handler'],
    url='https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.module_name }}',
    license='{{ cookiecutter.license }}',
    author='{{ cookiecutter.organization }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.module_description }}',
    install_requires=[]
)
