from clases import DocumentHandler
import sys


documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


class App:
    def __init__(self):
        self.handler = DocumentHandler()
        self.options = {
            'p': self.get_docs_owner,
            's': self.get_docs_directory,
            'l': self.show_all_docs,
            'ad': self.create_document,
            'ads': self.create_new_dir,
            'q': self.quit,
            'ds': self.delete_directory,
            'd': self.delete_document,
            'm': self.change_dir
        }

    def run(self):
        self.fill_data()

        while True:
            choice = input('Введите команду: ')
            action = self.options.get(choice)
            if action:
                action()
            else:
                print('Такой команды не существует!')
            pass

    # task 1.1
    def get_docs_owner(self):
        print(self.handler.get_doc('owner', input('Введите номер документа: ')))

    # task 1.2
    def get_docs_directory(self):
        print(self.handler.get_doc('directory', input('Введите номер документа: ')))

    # task 1.3
    def show_all_docs(self):
        self.handler.show_all_docs()

    # task 2.1
    def create_document(self):
        doc_num = input('Provide docs number: ')
        doc_type = input('Provide docs type: ')
        doc_owner = input('Provide docs owner: ')
        dir_num = int(input('Provide number of directory: '))

        print(self.handler.create_document(dir_num, doc_type, doc_num, doc_owner))
        self.show_all_docs()

    # task 1.4
    def create_new_dir(self):
        print(self.handler.add_directory(int(input('Введите номер директории: '))))

    # task 1.5
    def delete_directory(self):
        print(self.handler.delete_directory(int(input('Введите номер директории: '))))

    # task 2.2
    def delete_document(self):
        print(self.handler.get_doc('delete'))

    # task 2.3
    def change_dir(self):
        print(self.handler.get_doc('change_dir'))

    def fill_data(self):
        for key in directories.keys():
            self.handler.add_directory(key)

        for document in documents:
            dir_num = 0
            for key, docs in directories.items():
                for doc in docs:
                    if document['number'] == doc:
                        dir_num = int(key)

            self.handler.create_document(dir_num, document['type'], document['number'], document['name'])

    def quit(self):
        print('Thanks for coming!')
        sys.exit(0)
