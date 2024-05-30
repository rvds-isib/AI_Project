# Arbre des serveurs et de leurs voisins avec leur temps de transit reel (ms)
world = {
    'Oslo': {'Berlin': 70, 'Helsinki': 20, 'Londres': 40, 'Stockholm': 40},
    'Londres': {'Dublin': 30, 'Paris': 50, 'Bruxelles': 20, 'Oslo': 40, 'Madrid': 60, 'Amsterdam': 40},
    'Dublin': {'Londres': 30, 'Madrid': 70},
    'Madrid': {'Lisbonne': 20, 'Dublin': 70, 'Paris': 40, 'Alger': 90, 'Londres': 60},
    'Paris': {'Londres': 50, 'Bruxelles': 10, 'Madrid': 40, 'Berlin': 60, 'Rome': 80, 'Alger': 70, 'Amsterdam': 30,
              'Vienna': 80, 'Bern': 50},
    'Rome': {'Athènes': 90, 'Bruxelles': 20, 'Alger': 100, 'Paris': 80, 'Berlin': 70,  'Vienna': 40, 'Zagreb': 30},
    'Athènes': {'Alger': 110, 'Rome': 90, 'Bucarest': 50, 'Ankara': 60, 'Sofia': 30, 'Sarajevo': 40},
    'Ankara': {'Athènes': 60, 'Bucarest': 40, 'Moscou': 80, 'Sofia': 50, 'Tbilisi': 90},
    'Bucarest': {'Rome': 80, 'Berlin': 90, 'Moscou': 100, 'Ankara': 40, 'Athènes': 50, 'Budapest': 60, 'Sofia': 30},
    'Berlin': {'Paris': 60, 'Bruxelles': 20, 'Oslo': 70, 'Moscou': 80, 'Bucarest': 90, 'Rome': 70, 'Copenhague': 30,
               'Warsaw': 50, 'Prague': 40},
    'Moscou': {'Berlin': 80, 'Helsinki': 100, 'Bucarest': 100, 'Ankara': 80, 'Warsaw': 70, 'Minsk': 60, 'Tbilisi': 120},
    'Helsinki': {'Stockholm': 30, 'Moscou': 100, 'Tallinn': 100, 'Oslo': 20},
    'Alger': {'Lisbonne': 30, 'Madrid': 90, 'Paris': 70, 'Rome': 100, 'Athènes': 110, 'Tunis': 20},
    'Stockholm': {'Oslo': 40, 'Helsinki': 30, 'Copenhague': 10, 'Tallinn': 20, 'Riga': 40},
    'Copenhague': {'Stockholm': 10, 'Berlin': 30, 'Bruxelles': 40, 'Amsterdam': 50, 'Prague': 30},
    'Lisbonne': {'Madrid': 20, 'Alger': 30, 'Paris': 70},
    'Bruxelles': {'Londres': 20, 'Paris': 10, 'Berlin': 20, 'Copenhague': 40, 'Rome': 20, 'Amsterdam': 15, 'Bern': 30},
    'Amsterdam': {'Londres': 40, 'Bruxelles': 15, 'Paris': 30, 'Copenhague': 50},
    'Warsaw': {'Berlin': 50, 'Prague': 40, 'Minsk': 50, 'Moscou': 70, 'Vienna': 60, 'Budapest': 30},
    'Prague': {'Warsaw': 40, 'Vienna': 30, 'Budapest': 20, 'Berlin': 35, 'Copenhague': 30, 'Bratislava': 10},
    'Vienna': {'Prague': 30, 'Budapest': 20, 'Rome': 40, 'Paris': 80, 'Warsaw': 60, 'Sofia': 45, 'Bratislava': 10},
    'Budapest': {'Vienna': 20, 'Bucarest': 60, 'Prague': 20, 'Belgrade': 30, 'Warsaw': 30, 'Bratislava': 20},
    'Tallinn': {'Helsinki': 100, 'Stockholm': 20, 'Riga': 30},
    'Riga': {'Tallinn': 30, 'Vilnius': 20, 'Stockholm': 40},
    'Vilnius': {'Riga': 20, 'Warsaw': 40, 'Minsk': 30},
    'Minsk': {'Moscou': 60, 'Warsaw': 50, 'Vilnius': 30},
    'Sofia': {'Athènes': 30, 'Ankara': 50, 'Vienna': 45, 'Belgrade': 25, 'Bucarest': 30},
    'Belgrade': {'Budapest': 30, 'Sofia': 25, 'Zagreb': 20, 'Sarajevo': 15},
    'Zagreb': {'Belgrade': 20, 'Rome': 30, 'Vienna': 30},
    'Sarajevo': {'Belgrade': 15, 'Athènes': 40},
    'Bern': {'Paris': 50, 'Bruxelles': 30},
    'Tunis': {'Alger': 20},
    'Tbilisi': {'Ankara': 90, 'Moscou': 120},
    'Bratislava': {'Prague': 10, 'Vienna': 10, 'Budapest': 20}
}

# Coordonnées des serveurs (latitude, longitude)
coordonees_capitales = {
    'Oslo': (59.9139, 10.7522),
    'Londres': (51.5074, -0.1278),
    'Dublin': (53.3498, -6.2603),
    'Madrid': (40.4168, -3.7038),
    'Paris': (48.8566, 2.3522),
    'Rome': (41.9028, 12.4964),
    'Athènes': (37.9838, 23.7275),
    'Ankara': (39.9334, 32.8597),
    'Bucarest': (44.4268, 26.1025),
    'Berlin': (52.5200, 13.4050),
    'Moscou': (55.7558, 37.6176),
    'Helsinki': (60.1695, 24.9354),
    'Alger': (36.7372, 3.0867),
    'Stockholm': (59.3293, 18.0686),
    'Copenhague': (55.6761, 12.5683),
    'Lisbonne': (38.7223, -9.1393),
    'Bruxelles': (50.8503, 4.3517),
    'Amsterdam': (52.3676, 4.9041),
    'Warsaw': (52.2297, 21.0122),
    'Prague': (50.0755, 14.4378),
    'Vienna': (48.2082, 16.3738),
    'Budapest': (47.4979, 19.0402),
    'Tallinn': (59.4370, 24.7535),
    'Riga': (56.9496, 24.1052),
    'Vilnius': (54.6872, 25.2797),
    'Minsk': (53.9045, 27.5615),
    'Sofia': (42.6977, 23.3219),
    'Belgrade': (44.7866, 20.4489),
    'Zagreb': (45.8150, 15.9819),
    'Sarajevo': (43.8563, 18.4131),
    'Bern': (46.9481, 7.4474),
    'Tunis': (36.8065, 10.1815),
    'Tbilisi': (41.7151, 44.8271),
    'Bratislava': (48.1486, 17.1077)
}