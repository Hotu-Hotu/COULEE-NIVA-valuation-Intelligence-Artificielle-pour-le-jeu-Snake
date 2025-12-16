## Partie 2 – Architecture de l’agent IA

### 1. Choix de l’architecture

Nous avons choisi de modéliser le Snake comme un **agent basé sur l’utilité**.

Un agent réactif simple est limité car il ne prend pas en compte une évaluation globale des actions.  
Un agent à buts nécessite une planification explicite, peu adaptée à un environnement dynamique comme Snake.  
Les agents apprenants (Q-learning, DQN) sont plus complexes à mettre en œuvre et nécessitent un apprentissage en ligne coûteux.

L’agent basé sur l’utilité permet d’évaluer chaque action selon une fonction de performance, ce qui est cohérent avec l’utilisation d’un algorithme génétique pour optimiser le comportement global de l’agent.

**Composants de l’architecture :**
- **Perception** : informations locales (direction, nourriture, obstacles)
- **État interne** : représentation partielle de l’environnement
- **Fonction d’utilité** : évaluation numérique des actions possibles
- **Décision** : sélection de l’action maximisant l’utilité

---

### 2. Problématique d’apprentissage

La problématique principale est un **apprentissage multi-objectifs dans un environnement partiellement observable**.

L’agent doit :
- maximiser le score,
- survivre le plus longtemps possible,
- éviter les comportements dangereux.

Ces objectifs peuvent être contradictoires, ce qui rend la prise de décision non triviale et justifie l’utilisation d’une fonction d’utilité combinant plusieurs critères.

---

### 3. Intégration avec l’algorithme génétique

L’algorithme génétique est utilisé pour **optimiser les paramètres de l’agent**.

Chaque individu de la population correspond à un agent dont le **chromosome** représente les paramètres de la fonction d’utilité (poids, seuils).

Le processus est le suivant :
- évaluation des agents sur une partie complète,
- calcul d’une fitness globale,
- sélection des meilleurs individus,
- application de croisement et de mutation,
- génération d’une nouvelle population.

Le compromis temps/performance est géré en évaluant les agents sur des épisodes complets, ce qui limite le nombre de générations mais permet une évaluation plus stable et cohérente des comportements.
