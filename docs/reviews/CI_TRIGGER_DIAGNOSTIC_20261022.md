# Diagnostic — contrôle GitHub Actions `validate` absent sur la PR #1

**Date :** 22 octobre 2026.  
**Portée :** `chainsolutions-wealthtech/universal-agent-platform` exclusivement.  
**Statut :** `BLOCKED_PENDING_GITHUB_ACTIONS_RUN_ON_FINAL_HEAD`. Ce document ne constitue pas un succès de CI et ne justifie pas la fusion.

## État observé

- PR #1 sur `bootstrap/canonical-v5-foundation`, ouverte, non fusionnée.
- `main` reste au SHA `0b8b2e01e826b915a0c593d5d6545681e9316567`, ruleset dépôt `25599154` actif, contrôle GitHub Actions `validate` requis.
- Dernier run `validate` public observé : `39693813473`, succès sur l'ancien commit `fbf4c81f50396f157d69c8d668b3c19262d8ad20`.
- Les commits postérieurs, notamment les ajouts des tests au workflow et les durcissements de sécurité, **n'ont pas déclenché d'exécution `validate` visible dans les résultats consultés**. Ne pas attribuer une ancienne réussite au nouveau HEAD.
- Le workflow contient `pull_request` avec `opened,reopened,synchronize,ready_for_review,edited`, `push` sur main et `workflow_dispatch`. Il est pour l'instant **sur la branche PR, et non sur la branche par défaut**.
- Modification du corps de la PR effectuée lors du diagnostic ; aucune nouvelle exécution de validation observée alors.
- Une revue automatisée GitHub s'est néanmoins déclenchée sur un commit récent ; elle **n'est pas un test CI** et n'est pas une approbation GitHub indépendante.

## Cause racine

**Non établie.** Hypothèses qui nécessitent un contrôle de configuration GitHub côté organisation : workflow désactivé, exécutions en attente d'approbation, gestion des événements produits par un token d'automatisation, quotas ou files d'attente, problèmes de déclenchement et filtres effectifs. Éviter d'annoncer l'une de ces hypothèses comme fait acquis.

Les fonctions GitHub connectées dans cette conversation n'exposent pas la gestion administrative des workflows et ne permettent pas de déclencher un `workflow_dispatch` pour ce dépôt. Selon la documentation GitHub, un déclenchement manuel nécessite la présence du workflow sur la branche par défaut ; il n'est donc pas acquis à ce stade qu'un dispatch direct de ce nouveau fichier réussisse.

## Contrôle de sécurité amélioré

Les nouveaux correctifs sur cette PR permettent notamment :
- Vérification des `ghr_` et des suffixes avec `_` pour les formats de jetons GitHub.
- Rejet des fichiers sensibles même sous des dossiers `__pycache__`.
- Contrôle du répertoire **avant** d'exécuter les tests fournis par la PR, puis contrôle à nouveau après.
- Ajout de `sources/SOURCE_MANIFEST.json`, la référence historique exacte du V5, avec l'empreinte et la taille de la source canonique.

**Aucune de ces modifications ne doit être présentée comme validée par GitHub Actions tant que le dernier HEAD ne possède pas de `validate: success`.**

## NEXT_ACTION

`RESTORE_REQUIRED_GITHUB_ACTIONS_VALIDATE_ON_PR_1_HEAD`

1. Vérifier l'onglet Actions du dépôt et tout bandeau de validation en attente (approval-required) pour la PR #1 ; vérifier les paramètres Actions du dépôt et de l'organisation.
2. Confirmer si `validate` est activé et déclenché, observer le run et ses logs, ou documenter le blocage avec preuve.
3. Si nécessaire, utiliser une procédure administrativement autorisée (sans contournement du ruleset) pour relancer le workflow sur le HEAD courant.
4. Faire recontrôler les observations de revue encore ouvertes, par un intervenant distinct de l'éditeur.
5. Ne fusionner qu'après réussite effective du check requis et résolution gouvernée des discussions.

Documentation officielle utile :
- https://docs.github.com/en/actions/how-tos/troubleshoot-workflows
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow

Ce document est une preuve documentaire versionnée et non une autorité runtime ni une permission administrative.
