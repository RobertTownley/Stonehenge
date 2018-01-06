def print_usage(msg=None):
    '''Print out a message for a user who misused the CLI command'''
    if msg is not None:
        print(msg)

    print('''\tWelcome to the Stonehenge project builder!\n
            To use this utility, you'll first create a configuration file, and
            then build the project based off of that configuration.\n\n

            You can either create the config file (stonehenge_config.py)
            yourself, or you can run "stonehenge new" to generate a file with
            some helpful pre-populated defaults.\n

            Once the file has been created, you can run "stonehenge build" to
            create your project.\n

            For more information, or for usage examples, visit
            https://github.com/RobertTownley/Stonehenge.
    ''')
