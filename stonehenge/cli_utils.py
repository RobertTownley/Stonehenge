import os
import subprocess


def create_new_project_file():
    '''Returns the default file contents for a new project

    Output from this command is saved to the stonehenge.py file that a new
    user will execute to create, initialize, and deploy their new project.
    '''

    # Gather default file contents
    stonehenge_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(
        stonehenge_dir,
        "templates/stonehenge.py",
    )
    with open(filepath) as project_file:
        contents = project_file.read()

    # Save the new file to the expected filepath
    filename = "build_stonehenge.py"
    with open(filename, "w") as new_file:
        new_file.write(contents)

    # Set the new file as executable
    filepath = os.path.join(
        os.getcwd(),
        filename,
    )
    subprocess.call(['chmod', '+x', filepath])
