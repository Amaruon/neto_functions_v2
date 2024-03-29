class Document:
    def __init__(self, d_type, d_number, owner, directory):
        self.d_number = d_number
        self.d_type = d_type
        self.owner = owner
        self.directory = directory

    def __str__(self):
        return f'№: {self.d_number}, type: {self.d_type}, owner: {self.owner}, directory: {self._directory.number}'

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
            return f'There is no documents with such number ({num})'

    def all_documents(self):
        for document in self.documents:
            return document


class DocumentHandler:
    def __init__(self):
        self.directories = []

    def __str__(self):
        return f'Current active directories: {(", ".join(map(str, self.directories)))}'

    def add_directory(self, num):
        if isinstance(self.fetch_directory(num), Directory):
            return f'Number {num} is already used! '
        else:
            self.directories.append(Directory(num))
            return f'Directory №{num} was successfully added. '

    def fetch_directory(self, num):
        for directory in self.directories:
            if directory.number == num:
                return directory
        return f'There is no directory with such number ({num})!'

    def create_document(self, dir_num=None, doc_type=None, doc_num=None, doc_owner=None):
        directory = self.fetch_directory(dir_num)
        if isinstance(directory, Directory):
            directory.add_document(doc_type, doc_num, doc_owner, directory)
            return 'Document was added. '
        else:
            return f'There is no directory with number {dir_num}!\n' + str(self.show_all_docs())

    def show_all_docs(self):
        for directory in self.directories:
            return directory.all_documents()

    def get_docs_value(self, value):
        num = input('Enter number of document: ')
        result = ''
        for directory in self.directories:
            result = directory.fetch_document(num)
            if isinstance(result, Document):
                if value == 'owner':
                    return f'Owner: {result.owner}'
                elif value == 'directory':
                    return f'Directory: {directory.number}'
        return result




