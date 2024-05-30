from data import coordonees_capitales
from geopy.distance import geodesic


def distance_capitales(serveur1, serveur2):
    """
    Calcul de la distance entre deux serveurs sur base de leurs
     coordonnées géographique
    :return : La distance entre capitale1 et capitale2 en km
    """
    coord1 = coordonees_capitales[serveur1]
    coord2 = coordonees_capitales[serveur2]
    return geodesic(coord1, coord2).kilometers


def heuristic(serveur1, serveur2):
    """
    Calcul le temps de transit en millisecondes à partir de la distance en km
    :return : Heuristique entre deux serveurs
    """
    distance = distance_capitales(serveur1, serveur2) * 1000  # Convertir en mètres
    vitesse_transfert_mbps = 10 * 1000  # 10 Gbps = 10 000 Mbps
    temps_transit_msecondes = (distance / (vitesse_transfert_mbps * 10 ** 6)) * 1000

    return temps_transit_msecondes
