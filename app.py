from clases import DocumentHandler
import sys


class App:
    def __init__(self):
        self.handler = DocumentHandler()
        self.options = {
            'p': self.get_docs_owner,
            's': self.get_docs_directory,
            'l': self.show_all_docs,
            'ad': self.create_document,
            'ads': self.create_new_dir,
            'q': self.quit
        }

    def run(self):
        while True:
            choice = input('Please enter command: ')
            action = self.options.get(choice)
            if action:
                action()
            else:
                print('Incorrect input!')
            pass

    def get_docs_owner(self):
        print(self.handler.get_docs_value('owner'))

    def get_docs_directory(self):
        print(self.handler.get_docs_value('directory'))

    def show_all_docs(self):
        print(self.handler.show_all_docs())

    def create_document(self):
        doc_num = input('Provide docs number: ')
        doc_type = input('Provide docs type: ')
        doc_owner = input('Provide docs owner: ')
        dir_num = int(input('Provide number of directory: '))

        print(self.handler.create_document(dir_num, doc_type, doc_num, doc_owner) + 'Current documents:')
        self.show_all_docs()

    def create_new_dir(self):
        print(self.handler.add_directory(int(input('Provide number of directory: '))) + str(self.handler))

    def quit(self):
        print('Thanks for coming!')
        sys.exit(0)
