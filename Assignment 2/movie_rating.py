import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # Подсчет количества оценок от каждого пользователя
    user_ratings_count = movie_rating.groupby(
        'user_id').size().reset_index(name='rating_count')

    # Соединяем с таблицей пользователей для получения имен
    user_ratings_count = pd.merge(
        user_ratings_count, users, on='user_id', how='inner')

    # Находим пользователя с максимальным количеством оценок
    max_ratings = user_ratings_count['rating_count'].max()
    top_users = user_ratings_count[user_ratings_count['rating_count'] == max_ratings]

    # Выбираем имя пользователя с наибольшим количеством оценок, лексикографически первым
    top_user_name = top_users['name'].min()

    # Преобразуем даты в формат datetime
    movie_rating['created_at'] = pd.to_datetime(movie_rating['created_at'])

    # Фильтруем рейтинги за февраль 2020 года
    february_ratings = movie_rating[(
        movie_rating['created_at'] >= '2020-02-01') & (movie_rating['created_at'] <= '2020-02-29')]

    # Рассчитываем средний рейтинг для каждого фильма за февраль
    avg_february_ratings = february_ratings.groupby(
        'movie_id')['rating'].mean().reset_index(name='avg_rating')

    # Соединяем с таблицей фильмов для получения названий фильмов
    avg_february_ratings = pd.merge(
        avg_february_ratings, movies, on='movie_id', how='inner')

    # Находим фильм с максимальным средним рейтингом
    max_avg_rating = avg_february_ratings['avg_rating'].max()
    top_movies = avg_february_ratings[avg_february_ratings['avg_rating']
                                      == max_avg_rating]

    # Выбираем название фильма с максимальным рейтингом, лексикографически первым
    top_movie_title = top_movies['title'].min()

    # Формируем результат
    result = pd.DataFrame({
        'results': [top_user_name, top_movie_title]
    })

    return result


# Данные
data = {
    'movies_data': {
        'movie_id': [1, 2, 3],
        'title': ['Avengers', 'Frozen 2', 'Joker']
    },
    'users_data': {
        'user_id': [1, 2, 3, 4],
        'name': ['Daniel', 'Monica', 'Maria', 'James']
    },
    'movie_rating_data': {
        'movie_id': [1, 1, 1, 1, 2, 2, 2, 3, 3],
        'user_id': [1, 2, 3, 4, 1, 2, 3, 1, 2],
        'rating': [3, 4, 2, 1, 5, 2, 2, 3, 4],
        'created_at': ['2020-01-12', '2020-02-11', '2020-02-12', '2020-01-01',
                       '2020-02-17', '2020-02-01', '2020-03-01', '2020-02-22', '2020-02-25']
    }
}

# Создание DataFrame на основе данных
movies = pd.DataFrame(data['movies_data'])
users = pd.DataFrame(data['users_data'])
cmovie_rating = pd.DataFrame(data['movie_rating_data'])

# Вызов функции
result = movie_rating(movies, users, cmovie_rating)
print(result)
