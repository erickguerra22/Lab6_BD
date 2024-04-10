from db_functions import *


if __name__ == "__main__":
    driver = openConnection()
    driver.verify_connectivity()
    try:

        print('Generando grafo...')

        # Crear usuarios
        createNode(driver, "User", {"name":"Erick Guerra", "userId":"21781"})
        createNode(driver, "User", {"name":"José Kiesling", "userId":"21581"})
        createNode(driver, "User", {"name":"Elías Alvarado", "userId":"21808"})
        createNode(driver, "User", {"name":"Pablo Zamora", "userId":"21780"})
        createNode(driver, "User", {"name":"Diego Aquino", "userId":"21762"})
 
        # Nodo con más de una etiqueta
        createNode(driver, ['Person', 'Actor'], {"name": "Juan", "tmdbId": "1", "born":"2000-04-09", \
                                                 "died":"2020-01-15", "bornId":"1","url":"juan.com",\
                                                 "imdbId":"1","bio":"Actor reconocido","poster":"Poster de Juan"})

        
        # Crear películas
        createNode(driver, "Movie", {"title": "Pulp Fiction", "movieId": "1",\
                                     "year": "1994", "plot": \
                                     "Una serie de historias interrelacionadas sobre el crimen en Los Ángeles."})
        createNode(driver, "Movie", {"title": "The Shawshank Redemption", "movieId": "2",\
                                     "year": "1994", "plot": \
                                     '''La historia de un banquero encarcelado por un crimen que no cometió
                                        y su amistad única con otro preso.'''})
        createNode(driver, "Movie", {"title": "Inception", "movieId": "3", "year": "2010",\
                                     "plot": '''Un ladrón habilidoso roba secretos corporativos
                                        a través del uso de la infiltración en los sueños.'''})
        createNode(driver, "Movie", {"title": "The Godfather", "movieId": "4", "year": "1972",\
                                     "plot": '''La historia de la familia criminal Corleone y la
                                        transformación de su patriarca en un líder implacable.'''})
        createNode(driver, "Movie", {"title": "Forrest Gump", "movieId": "5", "year": "1994",\
                                     "plot": '''La vida de Forrest Gump, un hombre ingenuo pero
                                        decidido, que participa en varios eventos importantes
                                        en la historia de Estados Unidos.'''})

        # Crear relaciones
        createRelation(driver, "User", {"userId":"21781"}, "Movie", \
                       {"movieId":"5"}, "Rated", {"rating":"5", "timestamp":"1000"})
        createRelation(driver, "User", {"userId":"21781"}, "Movie", \
                       {"movieId":"3"}, "Rated", {"rating":"2", "timestamp":"2000"})
        createRelation(driver, "User", {"userId":"21780"}, "Movie", \
                       {"movieId":"2"}, "Rated", {"rating":"3", "timestamp":"3000"})
        createRelation(driver, "User", {"userId":"21780"}, "Movie", \
                       {"movieId":"1"}, "Rated", {"rating":"1", "timestamp":"400"})
        createRelation(driver, "User", {"userId":"21808"}, "Movie", \
                       {"movieId":"4"}, "Rated", {"rating":"4", "timestamp":"5000"})
        createRelation(driver, "User", {"userId":"21808"}, "Movie", \
                       {"movieId":"1"}, "Rated", {"rating":"5", "timestamp":"6000"})
        createRelation(driver, "User", {"userId":"21581"}, "Movie", \
                       {"movieId":"3"}, "Rated", {"rating":"5", "timestamp":"7000"})
        createRelation(driver, "User", {"userId":"21581"}, "Movie", \
                       {"movieId":"2"}, "Rated", {"rating":"3", "timestamp":"8000"})
        createRelation(driver, "User", {"userId":"21762"}, "Movie", \
                       {"movieId":"5"}, "Rated", {"rating":"1", "timestamp":"9000"})
        createRelation(driver, "User", {"userId":"21762"}, "Movie", \
                       {"movieId":"4"}, "Rated", {})

        print("Nodos y relación creados exitosamente.")

        
        print("Buscar nodos: ")
        print(find_node(driver, "User", {"userId":"21808"}))
        print(find_node(driver, "Movie", {"title":"Forrest Gump"}))

        print("\nBuscar nodos con relaciones: ")

        res = find_node_with_relation(driver, "User", {}, "Movie", {"movieId":"5"}, "Rated", {"rating":"1"})
        print(res)
        
    except Exception as e:
        print(e)
    finally:
        closeConnection(driver)