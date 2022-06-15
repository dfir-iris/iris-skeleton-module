from setuptools import setup

setup(
    name='{{ cookiecutter.module_name }}',
    python_requires='>{{ cookiecutter.minimal_python_version }}',
    version='{{ cookiecutter.version }}',
    packages=['{{ cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_') }}', '{{ cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_') }}.{{ cookiecutter.artefact.lower() }}_handler'],
    url='https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.module_name }}',
    license='{{ cookiecutter.license }}',
    author='{{ cookiecutter.organization }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.module_description }}',
    install_requires=[]
)
