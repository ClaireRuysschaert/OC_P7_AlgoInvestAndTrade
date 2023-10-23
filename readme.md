# Projet 7 : Résolvez des problèmes en utilisant des algorithmes en Python
## Algorithme d'investissement brute force et optimisé

Ces programmes ont pour but de sélectionner des actions qui permettront d’obtenir le meilleur bénéfice pour le client au bout de 2 ans en prenant en compte le budget maximum.

Attentes : 
- Chaque action ne peut être achetée qu'une seule fois.
- Chaque action doit être achetée entièrement.
- Le budget maximum est de 500 euros par client.

## Brute force 
Ce programme teste toutes les combinaisons d'action possible.
Il a l'inconvéniant d'être très gourmand avec une complexité de 0(2^n).
Il ne peut pas être utilisé sur de grands volumes de data.

## Greedy
Ce programme supprime les erreurs dans les fichiers data (prix ou profit < 0).
Ensuite, il trie les actions pas les meilleurs profits.
Puis va sélectionner les actions qui entrent dans le budget en calculant la valeur du portefeuille à chaque étape. 
Il a l'avantage d'être très rapide et permet de gérer des volumes de data très importants.
Il a l'inconvéniant de ne pas prendre en compte toutes les possibilités d'actions.

## Analyse des algorythmes

- Comparaison du nombre d'execution avec timeit (measure_execution_time.py)
- Comparaison du temps d'execution selon la taille de data (algo_complexity_comparison.py)
- Comparaison des performances (analyze.py)
