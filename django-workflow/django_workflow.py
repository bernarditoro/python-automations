import sys, subprocess, os


class DjangoWorkflow:
    def __init__(self, project_name: str):        
        try:
            self.create_venv()

            self.check_venv_activated()

            self.install_packages()

            self.create_django_project(project_name)

            self.create_env_file()

            self.create_requirements_file()

            print(f"\033[92mDjango project `{project_name}` created successfully!\033[0m")

        except RuntimeError as e:
            print(f"\033[91m{e}\033[0m") # Print error in red without need for extra packages using ANSI Escape Sequences

        except Exception as e:
            print(f"\033[91m{e}\033[0m")

    def create_venv(self, venv_name='venv') -> None:
        if not os.path.isdir(venv_name):
            subprocess.run([sys.executable, '-m', 'venv', venv_name], check=True)

            print('Virtual environment created successfully!')

        else:
            print('Virtual environment is already created.')

    def check_venv_activated(self) -> bool:
        if sys.base_prefix != sys.prefix:
            print('Virtual environment is activated.')

            return True
        
        else:
            raise RuntimeError('This script must be run within a virtual environment. Please activate a virtual environment and try again.')

    def install_packages(self) -> None:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'django', 'python-decouple', 'requests'], check=True)

        print('Installed packages: Django, python-decouple, requests')

    def create_django_project(self, project_name) -> None:
        subprocess.run(['django-admin', 'startproject', project_name, '.'], check=True)

        print(f'Django project `{project_name}` has been initialised!')

    def create_env_file(self) -> None:
        with open('.env', 'w') as f:
            f.write('# Environmental variables\n')

        print('.env file has been created.')

    def create_requirements_file(self) -> None:
        with open('requirements.txt', 'w') as f:
            subprocess.run([sys.executable, '-m', 'pip', 'freeze'], stdout=f, check=True)

        print('Installed packages have been written to requirements.txt.')


if __name__ == '__main__':
    workflow = DjangoWorkflow('polls')