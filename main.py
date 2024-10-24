import bibtext
from statistics import all_references_age


def main():
    path = r'C:\Users\T.Mukhin\OneDrive - Universite de Liege\APPLICATIVES\sample'
    #path = '.'
    number_of_entries = 0

    with open(r'C:\Users\T.Mukhin\OneDrive - Universite de Liege\APPLICATIVES\sample\bibrary.bib', 'w', encoding='utf-8') as bibtex_file:

        for path in bibtext.target_file_crawler(path):
            #print(path)
            for entry in bibtext.export_bib_entries(path):
                number_of_entries += 1
                print(entry)
                bibtex_file.write(entry + '\n')
        print(f'Number of entries: {number_of_entries}')

    print(f'90% >= {all_references_age(r'C:\Users\T.Mukhin\OneDrive - Universite de Liege\APPLICATIVES\sample\bibrary.bib', 0.08)}')

if __name__ == '__main__':
    main()
