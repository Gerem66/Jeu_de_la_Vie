# Jeu de la Vie

Une implémentation du jeu de la vie de Conway, un automate cellulaire où les cellules évoluent selon des règles simples :
- Une cellule vivante avec moins de deux voisins meurt (sous-population)
- Une cellule vivante avec deux ou trois voisins survit
- Une cellule vivante avec plus de trois voisins meurt (surpopulation)
- Une cellule morte avec exactement trois voisins devient vivante (reproduction)

## Versions

* V1 - Version simple
    - Version de test basique en console
    - État initial aléatoire
    - ~50 lignes

* V2 - Version minimale
    - Amélioration des performances
    - Code optimisé
    - ~30 lignes

* V3 - Version Éditable
    - Interface graphique dans la console
    - Ajout de l'édition du tableau
    - ~220 lignes

* V4 - Version complète
    - Interface graphique avec TKinter
    - Édition simplifiée à la souris
    - Contrôles interactifs
    - ~280 lignes

* V5 - Version complète optimisée
    - Interface graphique avec TKinter
    - Animation plus fluide et plus stable
    - Performance et interface optimisées

* VC - Version C
    - Implémentation en console
    - Performance optimisée
    - Gestion mémoire personnalisée

## Prérequis

### Versions Python
- Python 3.x
- Tkinter (pour V4 et V5)

### Version C
- Compilateur GCC
- Make

## Utilisation

### Versions Python
```bash
# Version basique
python V2/main.py

# Version graphique
python V5/main.py
```

### Version C
```bash
cd VC
make
./main
