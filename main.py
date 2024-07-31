import bibtext


def main():
    #path = r'C:\Users\T.Mukhin\OneDrive - Universite de Liege\APPLICATIVES\sample'
    path = '.'
    for path in bibtext.target_file_crawler(path):
        #print(path)
        for entry in bibtext.export_bib_entries(path):
            print(entry)


if __name__ == '__main__':
    main()
