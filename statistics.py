from re import findall
from numpy import quantile, mean, median


def all_references_age(filename: str, quantile_value: float = 0.25) -> int:
    """
    Find all year fields and return quantile
    :param filename: file with all bibtex entries
    :param quantile_value: quantile value
    :return: year corresponding to the input quantile value
    """
    with open(filename, 'r', encoding='utf-8') as bibtex_file:
        bib_entries = bibtex_file.read()

    all_years = [int(year) for year in findall(r'year = "(\d+)"', bib_entries)]

    return int(quantile(all_years, quantile_value))
