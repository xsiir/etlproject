from file.file_loader import FileLoader
from utils.properties_util import get_property
from dao.song_dao import SongDAO
from utils import constants


def main():
    """
        Pomysł na wykonanie projektu:
            1) Niech istnieje klasa (FilelLoader) będąca odpowiedzialna za różne opracje na plikach.
                - u nas będzie to wczytanie danych z pliku .txt i zapis tychże danych do bazy.
            2) Niech cała aplikacja korzysta tylko z jednego połączenia do bazy danych (DatabaseManager).
                Niech klasa to obslugujaca bedzie singletonem. Kazda operacja na bazie danych powinna przechodzic przez ta klase.
            3) Wszystkie bardziej zlozone polecenia SQL tudziez inne bloki tekstowe niech beda sie znajdowac w jednym miejscu.
                - plik ten nazwalem 'constants'
            4) Wszystkie dane konfiguracyjne niech beda trzymane w pliku properties a dostep do nich bedzie mozliwy poprzez
                jedno narzedzie (tu: metoda) dla calej aplikacji


        Wczytywanie danych z pliku do bazy danych trwa ~11:47
    """

    print("Prace przygotowal: Sienkiewicz Maciej")
    encoding_format = get_property(constants.FILE_CONFIG_DOMAIN, constants.ENCODING_FORMAT_KEY)
    field_separator = get_property(constants.FILE_CONFIG_DOMAIN, constants.FIELD_SEPARATOR_KEY)
    file_loader = FileLoader(encoding_format, field_separator)

    print("Zaladujmy pierwszy plik do bazy...")
    first_file_path = get_property(constants.FILE_PATHS_DOMAIN, constants.UNIQUE_TRACKS_PATH)
    file_loader.to_database_from_file(first_file_path, "model.dbo.Covers", 4)
    print("Ladowanie skonczone...")

    print("Zaladujmy drugi plik do bazy...")
    second_file_path = get_property(constants.FILE_PATHS_DOMAIN, constants.PLAYLIST_HISTORY_PATH)
    file_loader.to_database_from_file(second_file_path, "model.dbo.PlaylistHistory", 3)
    print("Ladowanie skonczone...")

    song_dao = SongDAO()
    for row in song_dao.find_most_popular_artists('5'):
        print('Utworty artysty: {} zostaly odtworzone {} razy'.format(row[0], row[1]))

    for row in song_dao.find_most_popular_tiles('5'):
        print('Utwor {} zostal odtworzone {} razy'.format(row[0], row[1]))


main()
