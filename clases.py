class Document:
    def __init__(self, d_type, d_number, owner, directory):
        self.d_number = d_number
        self.d_type = d_type
        self.owner = owner
        self.directory = directory

    def __str__(self):
        return f'№: {self.d_number}, тип: {self.d_type}, владелец: {self.owner}, директория: {self._directory.number}'

    @property
    def directory(self): return self._directory

    @directory.setter
    def directory(self, value):
        if not isinstance(value, Directory):
            raise TypeError('directory must be an instance of Directory()!')
        self._directory = value


class Directory:
    def __init__(self, number):
        self.number = number
        self.documents = []

    def __str__(self):
        return f'{self.number}'

    @property
    def number(self): return self._number

    @number.setter
    def number(self, value):
        self._number = int(value)

    def add_document(self, d_type, number, owner, directory):
        self.documents.append(Document(d_type, number, owner, directory))

    def fetch_document(self, num):
        for document in self.documents:
            if document.d_number == num:
                return document
        else:
            return f'Документа с номером {num} не существует!'

    def all_documents(self):
        for document in self.documents:
            print(document)

    def delete_document(self, document):
        self.documents.remove(document)
        return f'Документ удален. '


class DocumentHandler:
    def __init__(self):
        self.directories = []

    def __str__(self):
        return f'Текущие директории: {(", ".join(map(str, self.directories)))}'

    def add_directory(self, num):
        if isinstance(self.fetch_directory(num), Directory):
            return f'Директория с номером {num} уже существует! {self.__str__()}'
        else:
            self.directories.append(Directory(num))
            return f'Директория №{num} была успешно добавлена. {self.__str__()}'

    def fetch_directory(self, num):
        for directory in self.directories:
            if directory.number == num:
                return directory
        return f'Директории с номером {num} не существует! {self.__str__()}'

    def create_document(self, dir_num=None, doc_type=None, doc_num=None, doc_owner=None):
        directory = self.fetch_directory(dir_num)
        if isinstance(directory, Directory):
            directory.add_document(doc_type, doc_num, doc_owner, directory)
            return f'Документ успешно создан'
        else:
            return directory

    def show_all_docs(self):
        print('Текущие документы: ')
        for directory in self.directories:
            directory.all_documents()

    def get_doc(self, value=None, num=None):
        result = ''
        for directory in self.directories:
            result = directory.fetch_document(num)
            if isinstance(result, Document):
                if value == 'owner':
                    return f'Owner: {result.owner}'
                elif value == 'directory':
                    return f'Directory: {directory.number}'
                elif value == 'delete':
                    return f'{directory.delete_document(result)} \n' + str(self.show_all_docs())
                elif value == 'change_dir':
                    new_dir = self.fetch_directory(int(input('Новая директория: ')))
                    print(new_dir)
                    try:
                        result.directory = new_dir
                        return f'Документ был перемещен в новую директорию. \n{self.show_all_docs()}'
                    except TypeError:
                        return ''
        return f'{result}'

    def delete_directory(self, num):
        d = self.fetch_directory(num)
        if isinstance(d, Directory):
            if not d.documents:
                self.directories.remove(d)
                return f'Директория {num} была успешно удалена. {self.__str__()}'
            else:
                return f"Директория {num} не пуста! {self.__str__()}"
        else:
            return d

