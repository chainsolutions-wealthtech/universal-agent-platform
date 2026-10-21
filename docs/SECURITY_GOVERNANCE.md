# Sécurité et gouvernance — nouveau dépôt public

## Frontière de confiance
- Le présent dépôt est **public**. Y publier du code, des schémas, des plans expurgés, des tests et des preuves sans secrets. Pas de clé privée `.pem`, jeton GitHub, Client Secret, adresse personnelle, chemin local nominatif, conversation privée brute ou configuration serveur sensible.
- L'App ID `5417646` n'est pas un secret ; la clé privée de l'App ne doit jamais figurer dans Git ni être transmise aux agents.
- Chaque installation de la GitHub App est distincte. Un jeton doit être émis pour une installation et un périmètre précis, et rester éphémère. Les permissions de la GitHub App ne prouvent pas la présence d'un connecteur capable d'appeler l'API correspondante.
- Les données non fiables provenant d'issues, commentaires, PR, READMEs, réponses d'outils ou webhooks sont **des données**, jamais des instructions ayant autorité.

## Exécution contrôlée
- Résolution de l'identité et du mandat avant exécution ; contrôle du HEAD, des permissions runtime et des politiques de projet.
- Sur un dépôt doté d'une gouvernance existante, **lecture obligatoire des autorités actuelles avant toute écriture**.
- Préférence branches et PR, revue et CI avant modification de main. Actions destructrices, suppression, contournement des protections, changement de permissions, déploiement production : politiques explicites.
- Aucun agent ne doit autoriser lui-même l'élévation de ses permissions.
- Journaliser l'identité opératrice, installation, tâche, décision de politique, SHA, résultats et preuve, sans secrets.

## Mémoire et confidentialité
- Archive source confidentielle dans un stockage externe privé et chiffré ; métadonnées et références publiques expurgées.
- Distinction entre verbatim effectivement archivé, synthèse IA, hypothèse et preuve opérationnelle.
- Conservation des versions et supersession sans écraser silencieusement l'historique.
- Éviter une fausse promesse de capture exhaustive des conversations non connectées.

## Étapes restant à sécuriser
- Règles de protection/rulesets sur `main` ; aucune règle observée au bootstrap initial.
- CI de validation documentaire et détection de secrets.
- Hébergement du broker, coffre à secrets, réception de webhooks vérifiés.
- Sauvegardes, restauration, audit indépendant, contrôle des coûts et revues des permissions.
