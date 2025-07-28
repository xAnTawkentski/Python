#task1
import json

# Path to the JSON file
filename = 'students.json'

try:
    # Open and load the JSON file
    with open(filename, 'r') as file:
        students_data = json.load(file)
    
    # Check if the data is a list of students
    if isinstance(students_data, list):
        for idx, student in enumerate(students_data, start=1):
            print(f"Student {idx}:")
            for key, value in student.items():
                print(f"  {key}: {value}")
            print()  # Blank line between students
    else:
        print("Expected a list of student records in the JSON file.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except json.JSONDecodeError as e:
    print(f"Error: Failed to parse JSON - {e}")
  

#task2
import requests

# Replace this with your actual OpenWeatherMap API key
API_KEY = '11737152541865'
CITY = 'Tashkent'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

try:
    response = requests.get(URL)
    response.raise_for_status()  # Raises an error for bad responses (4xx/5xx)
    data = response.json()

    # Extract and print weather information
    print(f"Weather in {CITY}:")
    print(f"  Temperature: {data['main']['temp']} °C")
    print(f"  Feels Like: {data['main']['feels_like']} °C")
    print(f"  Humidity: {data['main']['humidity']}%")
    print(f"  Weather Description: {data['weather'][0]['description'].title()}")
    print(f"  Wind Speed: {data['wind']['speed']} m/s")

except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
except KeyError:
    print("Error parsing weather data. Check if city or API key is correct.")


#task3
import json
import os

FILENAME = 'books.json'

def load_books():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

def save_books(books):
    with open(FILENAME, 'w') as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()
    new_id = max((book["id"] for book in books), default=0) + 1
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter year: "))
    
    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year
    }
    books.append(new_book)
    save_books(books)
    print("Book added.")

def update_book():
    books = load_books()
    book_id = int(input("Enter the ID of the book to upda_


                        
#task4
import requests
import random

# Replace this with your actual OMDb API key
API_KEY = 'your_api_key_here'
OMDB_URL = 'http://www.omdbapi.com/'

# Predefined list of popular movies per genre (you can expand this)
MOVIES_BY_GENRE = {
    "action": ["Mad Max: Fury Road", "Die Hard", "Gladiator", "John Wick"],
    "comedy": ["Superbad", "The Grand Budapest Hotel", "Step Brothers", "The Hangover"],
    "drama": ["The Shawshank Redemption", "Fight Club", "Forrest Gump", "The Godfather"],
    "sci-fi": ["Inception", "Interstellar", "The Matrix", "Blade Runner 2049"],
    "horror": ["The Conjuring", "Hereditary", "Get Out", "A Quiet Place"]
}

def fetch_movie_data(title):
    params = {
        't': title,
        'apikey': API_KEY
    }
    response = requests.get(OMDB_URL, params=params)
    data = response.json()

    if data.get("Response") == "True":
        return {
            "Title": data["Title"],
            "Year": data["Year"],
            "Genre": data["Genre"],
            "Plot": data["Plot"],
            "IMDB Rating": data.get("imdbRating", "N/A")
        }
    else:
        return None

def recommend_movie_by_genre():
    genre = input("Enter a genre (action, comedy, drama, sci-fi, horror): ").strip().lower()

    if genre not in MOVIES_BY_GENRE:
        print("Sorry, we don't have recommendations for that genre.")
        return

    title = random.choice(MOVIES_BY_GENRE[genre])
    movie = fetch_movie_data(title)

    if movie:
        print("\n🎬 Recommended Movie:")
        for key, value in movie.items():
            print(f"{key}: {value}")
    else:
        print("Sorry, couldn't fetch movie details.")

if __name__ == "__main__":
    recommend_movie_by_genre()

