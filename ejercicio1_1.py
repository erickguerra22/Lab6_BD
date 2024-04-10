from neo4j import GraphDatabase

'''
    Funciones para creacion de grafos en Neo4j
    Autores:
        José Pablo Kiesling Lange - 21581
        Diego Andrés Morales Aquino - 21762
        Pablo Andrés Zamora Vásquez - 21780
        Elías Alberto Alvarado Raxón - 21808
        Erick Stiv Junior Guerra Muñoz - 21781
'''

# Variables globales
uri = "neo4j+s://5a32184b.databases.neo4j.io"
user = "neo4j"
password = "a_gsNu6HtA4WuKmOKPpDs12AlWPAkQvNVaLg1atOjjc"

def formatDict(dictionary):
    result = ', '.join(["{}: '{}'".format(k, v.replace("'", "\\'")) for k, v in dictionary.items()])
    return result


# Funciones
def openConnection():
    return GraphDatabase.driver(uri, auth=(user, password))

def closeConnection(driver):
    driver.close()
    
def createNode(driver, labels, properties):
    session = driver.session()
    if type(labels) == str:
        labels = [labels]
    try:
        labels_str = ":".join(labels)
        query = f"MERGE (n:{labels_str} {{{formatDict(properties)}}})"
        result = session.run(query)
        return result
    except Exception as e:
        print('¡Error al crear nodo!')
    finally:
        session.close()
        
def find(driver, label_1, properties_1, label_2, properties_2, ):
    session = driver.session()
    try:
        query = f"MERGE (n:{label} {{{formatDict(properties)}}})"
        result = session.run(query)
        return result
    except Exception as e:
        print('¡Error al crear nodo!')
    finally:
        session.close()

    
def createRelation(driver, label_1, properties_1, label_2, properties_2, relationType, relationProperties):
    session = driver.session()
    try:
        query = f"""
                MATCH (n1:{label_1} {{{formatDict(properties_1)}}})
                MATCH (n2:{label_2} {{{formatDict(properties_2)}}})
                MERGE (n1)-[r:{relationType} {{{formatDict(relationProperties)}}}]->(n2)
                RETURN r
                """
        result = session.run(query)
        return result
    except Exception as e:
        print('¡Error al crear relación!')
    finally:
        session.close()
    
# Programa principal
if __name__ == "__main__":
    driver = openConnection()
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

    except Exception as e:
        print(e)
    finally:
        closeConnection(driver)