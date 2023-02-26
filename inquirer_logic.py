import inquirer

questions = [
    inquirer.List('platform',
                  message="From which platform do you want to scrap?",
                  choices=['Linkedin', 'Instagram', 'Twitter'],
                  ),
    inquirer.Text('username',
                  message="What's your username?",
                  validate=lambda _, x: len(x) > 0,
                  ),
]

answers = inquirer.prompt(questions)
print(answers)
