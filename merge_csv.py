import csv
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
headers.append("postal_link")

with open("final.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open('movie_links.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies_links = data[1:]

for movie_items in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movies_links:
            if movie_items[8] == movie_link_item[0]:
                movie_items.append(movie_link_item[1])
                if len(movie_items)==28:
                    with open("final.csv","a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_items)
