# Protection de `main` — procédure d'activation gouvernée

**Statut :** `PREPARED_LOCAL_APPLY_REQUIRED` — document de proposition, **aucune protection effective ne doit être présumée avant vérification GitHub live**.

## Audit de départ
- Dépôt : `chainsolutions-wealthtech/universal-agent-platform` (public).
- `main` : SHA `0b8b2e01e826b915a0c593d5d6545681e9316567`, sans protection lors du contrôle.
- PR #1 : `bootstrap/canonical-v5-foundation`, brouillon, aucun merge.
- Workflow : `Canonical Documentation Validation`, job `validate`, source GitHub Actions (intégration ID `15368`).
- Le workflow a été adapté pour se déclencher sur toutes les PR et sur les push vers `main`; le validateur documentaire a été rendu compatible avec l'évolution future des lots et de l'état courant.

## Ruleset v1 ciblé sur le dépôt uniquement
- Nom : `Universal Agent Platform - Protect main v1`.
- Cible : branche par défaut `main`.
- `enforcement: active`, `bypass_actors: []`.
- PR obligatoire, conversations de revue résolues.
- `validate` requis, source GitHub Actions ; mise à jour de la branche par rapport à `main` avant intégration.
- Force-push interdit ; suppression de `main` interdite.
- **Approbations GitHub requises : 0 dans la phase initiale**, pour ne pas rendre le bootstrap dépendant d'un compte supplémentaire. Cela **ne vaut pas revue indépendante** : une validation de gouvernance séparée doit précéder la fusion initiale ; relever cette exigence dès qu'un réviseur indépendant est opérationnel.
- Aucune exception automatique donnée à l'App.

## Mode d'application
Les fonctions GitHub directes du connecteur courant n'exposent pas la création d'un ruleset administratif. Un bootstrap Node.js exécuté **sur le poste de l'utilisateur** avec la clé privée GitHub App peut activer ce ruleset par l'API GitHub. L'application est `5417646`, installation de l'organisation `173915815`. Le script livré comme artefact de conversation est : `UNIVERSAL_AGENT_MAIN_PROTECTION_V1.zip`. Il fonctionne sans dépendance NPM et n'enregistre ni clé, ni jeton.

Le script vérifie l'identité du dépôt, le SHA de `main`, le statut brouillon de PR #1, la réussite du check GitHub Actions au dernier HEAD et l'absence d'autre ruleset effectif avant écriture. **Il n'effectue aucun merge**.

Après exécution, contrôler via `GET /repos/chainsolutions-wealthtech/universal-agent-platform/rulesets` :
1. Un ruleset attendu en `enforcement: active`.
2. La condition de branche par défaut.
3. Le contrôle `validate` depuis GitHub Actions.
4. L'absence de bypass et la présence des règles PR, non-fast-forward et deletion.
5. `main` toujours inchangé ; PR #1 toujours ouverte.

## Conditions de sortie
`PROTECTION_ACTIVE` ne peut être attribué **qu'après** un retour GitHub live positif. Si l'API refuse la création, constater le blocage, ne pas remplacer silencieusement la politique par une autre, et ne pas fusionner la PR.

## Restrictions de sécurité
Ne pas envoyer la clé `.pem`, des jetons GitHub, les rapports locaux sensibles ou des données privées dans ce dépôt public. Ne pas agir sur les dépôts MCP/GRT. Une règle dans ce dépôt ne change aucune autorité des projets existants.

Référence officielle : https://docs.github.com/en/rest/repos/rules#create-a-repository-ruleset
