import bibtexparser  # >= 2.0.0
import docx2txt
import os.path
from collections.abc import Iterator


class MyBibEntry:
    """ Bibtex entry class """

    def __init__(self, key: str, entry_type: str, fields: dict) -> None:
        """
        :param key: bib entry key
        :param entry_type: bib entry type
        :param fields: dictionary of all fields
        """
        self.key = key
        self.entry_type = entry_type
        self.fields = fields

    def __str__(self) -> str:
        """
        :return: string in writable format
        """
        first_line = f'@{self.entry_type}{{{self.key},'
        body = '\n\t'.join([f'{key} = "{value.replace('"', '')}",' for key, value in self.fields.items()])
        final_line = '}'
        return '\n\t'.join([first_line, body, final_line])


def target_file_crawler(working_folder: str = '.') -> Iterator[str]:
    """
    Search for language reports and return their paths.
    :param working_folder: working path
    :return: generator with relevant paths
    """

    macroareas = ('Africa',
                  'North America',
                  'South America',
                  'Southeast Asia & Oceania',
                  'Australia & New Guinea',
                  'Eurasia')
    print(os.path.abspath(working_folder))
    for path, directories, files in os.walk(working_folder):
        if any(macroarea in path for macroarea in macroareas):
            for file in files:
                if 'language_report' in file:
                    yield os.path.join(path, file)


def export_bib_entries(filename: str) -> Iterator[str]:
    """
    Search for bib entries in the file and return them in writable format.
    :param filename: file for search
    :return: generator with writable bib entries
    """
    language_report = docx2txt.process(filename)
    library = bibtexparser.parse_string(language_report)

    for entry in library.entries:
        yield format_bib_entry(entry)


def format_bib_entry(bib_entry: bibtexparser.model.Entry) -> str:
    """
    Format a bib entry and make it writable.
    :param bib_entry: bib entry as it is returned by the bibtexparser package parser
    :return: bib entry in writable format
    """
    entry_fields = {}
    for field in bib_entry.fields:
        entry_fields[field.key] = field.value

    bib_entry_string = MyBibEntry(bib_entry.key,
                                  bib_entry.entry_type,
                                  entry_fields)

    return str(bib_entry_string)
