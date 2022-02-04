class MarkdownEditor:

    def __init__(self):
        self.formatters = {"plain": self.plain,
                           "bold": self.bold,
                           "italic": self.italic,
                           "header": self.header,
                           "link": self.link,
                           "inline-code": self.inline_code,
                           "new-line": self.new_line,
                           "ordered-list": self.lists,
                           "unordered-list": self.lists}
        self.commands = ['!help', '!done']
        self.user_choice = None
        self.all_text = []

    def help(self):
        print(f'Available formatters:', *self.formatters.keys())
        print('Special commands:', *self.commands)

    def done(self):
        output = open('output.md', 'w', encoding='utf-8')
        output.writelines(self.all_text)
        output.close()

    def plain(self):
        text = input('Text:')
        self.all_text.append(text)

    def bold(self):
        text = input('Text:')
        self.all_text.append(f'**{text}**')

    def italic(self):
        text = input('Text:')
        self.all_text.append(f'*{text}*')

    def header(self):
        while True:
            level = int(input('Level:'))
            if level not in range(1, 7):
                print('The level should be within the range of 1 to 6')
            else:
                break
        text = input('Text:')
        self.all_text.append('#' * level + f' {text}\n')

    def link(self):
        label = input('Label:')
        url = input('URL:')
        self.all_text.append(f'[{label}]({url})')

    def inline_code(self):
        text = input('Text:')
        self.all_text.append(f'`{text}`')

    def new_line(self):
        self.all_text.append('\n')

    def lists(self):
        while True:
            rows = int(input('Number of rows:'))
            if rows <= 0:
                print('The number of rows should be greater than zero')
            else:
                break

        for r in range(1, rows + 1):
            text = input(f'Row #{r}:')
            if self.user_choice == 'ordered-list':
                self.all_text.append(f'{r}. {text}\n')
            else:
                self.all_text.append(f'* {text}\n')

    def choice(self):
        while True:
            user_choice = input('Choose a formatter: ')
            if user_choice in self.commands:
                self.user_choice = user_choice
                if self.user_choice == '!help':
                    self.help()
                elif self.user_choice == '!done':
                    self.done()
                    break
            elif user_choice in self.formatters:
                self.user_choice = user_choice
                self.formatters[user_choice]()
                print("".join(self.all_text))
                continue
            else:
                print('Unknown formatting type or command')


my_editor = MarkdownEditor()
my_editor.choice()