from colorama import Fore, Style
from collections import Counter

movies = []
next_id = 1

def menu():
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print("         Movie Manager CLI         ")
    print("=" * 40 + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Add a movie")
    print("2. Search for a movie")
    print("3. Sort movies")
    print("4. Remove a movie")
    print("5. Display all movies")
    print("6. Statistics")
    print("7. Fake data mode")
    print("8. Exit" + Style.RESET_ALL)

def add_movie():
    global next_id
    title = input("Enter movie title: ")
    year = input("Enter movie year: ")
    genre = input("Enter movie genre: ")
    for movie in movies:
        if movie["title"].lower() == title.lower() and movie["year"] == year:
            print(Fore.RED + f"Movie '{title}' ({year}) already exists." + Style.RESET_ALL)
            return
    movies.append({
        "id": next_id,
        "title": title,
        "year": year,
        "genre": genre
    })
    print(Fore.GREEN + f"Movie '{title}' added with ID {next_id}." + Style.RESET_ALL)
    next_id += 1

def search_movie():
    if not movies:
        print(Fore.RED + "No movies to search." + Style.RESET_ALL)
        return
    term = input("Enter movie title to search: ").lower()
    found = [m for m in movies if term in m["title"].lower()]
    if found:
        print(Fore.GREEN + f"{len(found)} match(es) found:" + Style.RESET_ALL)
        for m in found:
            print(f"{m['id']}: {m['title']} ({m['year']}) - {m['genre']}")
    else:
        print(Fore.RED + f"No matches found for '{term}'." + Style.RESET_ALL)

def sort_movies():
    if not movies:
        print(Fore.RED + "No movies to sort." + Style.RESET_ALL)
        return
    field = input("Sort by (title/year/genre): ").lower()
    if field not in ["title", "year", "genre"]:
        print(Fore.RED + "Invalid sort field." + Style.RESET_ALL)
        return
    movies.sort(key=lambda m: m[field])
    print(Fore.BLUE + f"Movies sorted by {field}." + Style.RESET_ALL)

def remove_movie():
    global movies
    if not movies:
        print(Fore.RED + "No movies to remove." + Style.RESET_ALL)
        return
    try:
        movie_id = int(input("Enter movie ID to remove: "))
    except ValueError:
        print(Fore.RED + "Invalid ID." + Style.RESET_ALL)
        return
    before = len(movies)
    movies = [m for m in movies if m["id"] != movie_id]
    after = len(movies)
    if before == after:
        print(Fore.RED + f"No movie with ID {movie_id} found." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"Movie with ID {movie_id} removed." + Style.RESET_ALL)

def display_movies():
    if not movies:
        print(Fore.RED + "No movies to display." + Style.RESET_ALL)
        return
    print(Fore.MAGENTA + Style.BRIGHT + "\nMovie List" + Style.RESET_ALL)
    for m in movies:
        print(f"{m['id']:>3} | {m['title']:<20} | {m['year']} | {m['genre']}")

def statistics():
    if not movies:
        print(Fore.RED + "No movies for statistics." + Style.RESET_ALL)
        return
    years = [int(m["year"]) for m in movies]
    genres = [m["genre"] for m in movies]
    genre_counts = Counter(genres)
    most_common_genre = genre_counts.most_common(1)[0][0]
    oldest = min(movies, key=lambda m: int(m["year"]))
    newest = max(movies, key=lambda m: int(m["year"]))
    print(Fore.MAGENTA + Style.BRIGHT + "\nStatistics" + Style.RESET_ALL)
    print(f"Total movies: {len(movies)}")
    print(f"Most common genre: {most_common_genre}")
    print(f"Oldest movie: {oldest['title']} ({oldest['year']})")
    print(f"Newest movie: {newest['title']} ({newest['year']})")

def fake_data_mode():
    global movies, next_id
    movies = [
        {"id": next_id + i, "title": f"Sample {i+1}", "year": str(2000 + i), "genre": "Drama" if i % 2 == 0 else "Action"}
        for i in range(10)
    ]
    next_id += 10
    print(Fore.CYAN + "Fake data mode: 10 movies loaded." + Style.RESET_ALL)

def main():
    while True:
        menu()
        choice = input("Choose an option (1-8): ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            search_movie()
        elif choice == "3":
            sort_movies()
        elif choice == "4":
            remove_movie()
        elif choice == "5":
            display_movies()
        elif choice == "6":
            statistics()
        elif choice == "7":
            fake_data_mode()
        elif choice == "8":
            print(Fore.CYAN + "Exiting Movie Manager. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option. Try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
# This code implements a simple movie management system with functionalities to add, search, sort, remove