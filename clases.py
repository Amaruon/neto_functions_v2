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

    def delete_document(self, document):
        self.documents.remove(document)
        return f'Document is deleted. '


class DocumentHandler:
    def __init__(self):
        self.directories = []

    def __str__(self):
        return f'Current active directories: {(", ".join(map(str, self.directories)))}'

    def add_directory(self, num):
        if isinstance(self.fetch_directory(num), Directory):
            return f'Number {num} is already used! {self.__str__()}'
        else:
            self.directories.append(Directory(num))
            return f'Directory №{num} was successfully added. {self.__str__()}'

    def fetch_directory(self, num):
        for directory in self.directories:
            if directory.number == num:
                return directory
        return f'There is no directory with such number ({num})! {self.__str__()}'

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

    def get_doc(self, value=None):
        num = input('Enter number of document: ')
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
                    new_dir = self.fetch_directory(int(input('New directory: ')))
                    print(new_dir)
                    try:
                        result.directory = new_dir
                        return f'Document was moved to new directory. \n{self.show_all_docs()}'
                    except TypeError:
                        return ''
        return f'{result}\n {str(self.show_all_docs())}'

    def delete_directory(self, num):
        d = self.fetch_directory(num)
        if isinstance(d, Directory):
            if not d.all_documents():
                self.directories.remove(d)
                return f'Directory {num} is deleted. '
            else:
                return f"Directory {num} isn't empty! "
        else:
            return d

