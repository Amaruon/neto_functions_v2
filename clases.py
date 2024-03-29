class Document:
    def __init__(self, d_type, number, owner, directory):
        self.number = number
        self.d_type = d_type
        self.owner = owner
        self.directory = directory

    def __str__(self):
        return f'№: {self.number}, type: {self.type}, owner: {self.owner}, directory: {self.directory.number}'

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
        return f'Directory №{self._number} contains {self.documents}'

    @property
    def number(self): return self._number

    @number.setter
    def number(self, value):
        self._number = int(value)

    def add_document(self, d_type, number, owner, directory):
        self.documents.append(Document(d_type, number, owner, directory))


class DocumentHandler:
    def __init__(self):
        self.documents = []
        self.directories = []

    def add_document(self, value):
        if isinstance(value, Document):
            self.documents.append(value)

    def create_directory(self):
        self.directories.append(Directory(input('Provide directory number: ')))

    def get_directory_by_number(self):
        num = int(input('Enter directory number: '))
        for directory in self.directories:
            if directory.number == num:
                return directory

    def create_new_document(self):
        num = input('Provide number of document: ')
        type = input('Provide type of document: ')
        owner = input('Provide owner of document: ')
        directory = self.get_directory_by_number()

        doc = Document(type, num, owner, directory)
        self.documents.append(doc)
        directory.add_documents(doc)

    def get_document_by_number(self):
        num = input('Enter number of document: ')

        for doc in self.documents:
            if doc.number == num:
                return doc


class UserInputHandler:
    def __init__(self, input):
        self.input = input

    @property
    def input(self): return self._input

    @input.setter
    def input(self, value):
        self._input = value

    def document_check(self, doc):
        return doc if doc else 'Document not found!\nYou can add it using "ad" command.'

    def directory_check(self, dir):
        return dir if dir else 'Directory not found!\nYou can add it using "ads" command.'