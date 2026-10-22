# ChainSolutions Universal Gateway — contrats de finalisation et gates GitHub App

**Date :** 22 octobre 2026. **État :** `BOOTSTRAP_PARTIALLY_VERIFIED`.  
**Dépôt d'accueil :** `chainsolutions-wealthtech/universal-agent-platform` (public).  
**App existante :** `ChainSolutions Universal Gateway` — App ID **5417646**.  
**Propriétaire :** organisation `chainsolutions-wealthtech`.  
**Source canonique des objectifs, lots et critères :** `docs/roadmap/ROADMAP_V5.json`, lots **D00–D14**, et plan A/B/C/D `docs/archive/PLAN_DIRECTEUR_UNIFIE_V5_20261021.md`.  
**Source canonique de la chronologie :** `docs/roadmap/PROGRAMME_CHRONOLOGIQUE_V5.md` ; ce fichier possède **seulement le contrat d'acceptation et l'audit de la passerelle GitHub App**.  
**Aucune élévation automatique :** une permission GitHub App, une installation ou une identité documentaire ne vaut pas mandat d'agent ou permission runtime sur un projet.

## 1. Résultats effectivement démontrés

| Checkpoint | Nature | État |
| --- | --- | --- |
| Identité App ID 5417646 / organisation propriétaire | Captures utilisateur + sortie locale de JWT `GET /app` | **Vérifiée localement** |
| Installation organisation : 173915815 | Journal local communiqué (All repositories) | **Vérifiée localement** |
| Installation compte Wealthtechinnovations : 173916302 | Journal local communiqué | **Vérifiée localement** |
| Installation compte Patricked-code : 173916438 | Journal local communiqué | **Vérifiée localement** |
| JWT RS256, émission IAT éphémère et API GitHub | Outil local `github-app-bootstrap.mjs`, retour utilisateur | **Testés au bootstrap** |
| Création par l'App du dépôt public cible | Journal local + repo GitHub observé | **Réalisée** |
| Ruleset dépôt 25599154 sur `main` | API GitHub live sur ce dépôt | **Actif**, sans bypass |
| Jeu **complet** des permissions GitHub App effectivement accordées | Pas d'export `GET /app` après inscription | **NON ATTESTÉ** |
| Abonnements d'événements, webhook HTTPS, réception HMAC | Pas de preuve runtime d'événements signés reçus | **NON ATTESTÉ** |
| Broker serveur JWT/IAT, rotation de secrets, coffre et logs sûrs | Script local ponctuel uniquement | **NON IMPLÉMENTÉ** |
| OAuth GitHub App user-to-server / consentement, révocation | Non exercé dans le bootstrap | **NON VALIDÉ** |
| GitHub Actions `validate` au dernier HEAD PR #1 | Anciennes CI vertes, dernière révision non attestée | **BLOQUÉ** |
| Couverture runtime des 30 domaines GitHub et D00–D14 | Seul catalogue documentaire importé | **NON ATTESTÉ** |

Les comptes personnels `Patricked-code` et `Wealthtechinnovations` restent des **autorités distinctes**. Ne pas modifier leur gouvernance, leurs dépôts ou leurs politiques pour compléter ce dépôt.

## 2. Chemin de finalisation réel — chaque gate attend sa preuve

| Gate | Lien lots V5 | Précondition | Travail et preuve requise | Sortie |
| --- | --- | --- | --- | --- |
| **GA-00** | C, D00 | App actuelle | Résoudre en lecture seule l'identité et la configuration réelle de l'App ; inventaire complet des permissions `repository/organization/account`, événements, installation et périmètre. **Ne pas extrapoler du paquet d'inscription**. | `APP_CONFIGURATION_ATTESTED` |
| **GA-01** | D01, B10 | GA-00 + politique | Définir politiques/identités GitHub pour chaque installation ; distinguer App JWT / token installation / token utilisateur OAuth, restrictions repo/action, expiration, rotation, gestion des erreurs. | `AUTH_CONTRACT_APPROVED` |
| **GA-02** | D01, B13 | GA-01 et stockage secret privé | Broker durable isolé et sécurisé, émettant des jetons avec scopes minimaux. Ne jamais publier PEM ou jetons dans Git. | `TOKEN_BROKER_VERIFIED` |
| **GA-03** | D07, B05, B11 | GA-02, contrats événement | Configurer webhook HTTPS, secret HMAC, vérification du payload et des rejouements, réception durable/ack, idempotence. Ne pas créer de bus concurrent aux autorités MCP/GRT. | `WEBHOOK_END_TO_END_VERIFIED` |
| **GA-04** | D02–D04, B09 | GA-01–03, sandbox autorisé | Exercer endpoints Git/REST/GraphQL (repo, branches, PR, Issues, Projects, CI), documenter scope réel, échecs 403/404 et idempotence. | `CORE_GITHUB_OPERATIONS_VERIFIED` |
| **GA-05** | D05–D06 | GA-04 | Scanner spécial secrets/risques, règles administration sous mandat, logs sans secret, contrôle dérive et politique de refus. | `SECURITY_ADMIN_GATES_VERIFIED` |
| **GA-06** | D08–D13 | GA-04, fonctionnalités éligibles | Releases, Packages, Pages, analytics, OAuth utilisateur **sur consentement réel**, Enterprise **si éligible**. Chaque domaine non accessible doit être noté `NOT_APPLICABLE` ou `NOT_GRANTED`, jamais simulé. | `EXTENDED_CAPABILITIES_QUALIFIED` |
| **GA-07** | D14, B24 | GA-01–06 | Audit indépendant de couverture des 30 domaines : endpoints, jetons, permission, preuves runtime, limites, revues et risques acceptés. | `GATEWAY_COVERAGE_ATTESTED` |
| **GA-08** | B25 | GA-07 + readiness | Runbook de production, monitoring, alarmes, rotation, rollback, sauvegardes de références et tests de récupération. | `GATEWAY_RELEASE_ACCEPTED` |

**Important :** ce sous-parcours de GitHub App est une *vue spécialisée* du graphe V5 ; il ne replanifie pas les 46 lots et n'en change pas les dépendances. Les gates GA-03/GA-04 ne doivent pas être déclarés terminés avant B05/B09/B10/B11 selon le graphe général. La première tranche LAB peut simuler des composants, jamais valider les lots industriels complets par anticipation.

## 3. Audit local sans secrets

Un outil Node.js `UNIVERSAL_GATEWAY_AUDIT_V1_1.zip` (version corrigée, archive SHA-256 `ec639b182801c5fff6fd5e4d1aca62344b4705f1e68b8af8f3a0d53455e27599`, **3/3 tests hors ligne réussis**, syntaxe Node vérifiée) a été **créé dans le contexte de cette conversation**, non ajouté au dépôt GitHub (à importer après revue de confidentialité/code si souhaité). Il lit `GET /app`, la liste des installations, `GET /app/hook/config` avec JWT et les paramètres Actions, règles et checks du repo à l'aide d'un jeton d'installation temporaire. Il **ne lance aucun dispatch**, ne modifie aucune permission, et écrit uniquement un rapport expurgé quand `--report-dir` est fourni.

Commandes PowerShell après extraction du ZIP dans `NNN` :

```powershell
node .\UNIVERSAL_GATEWAY_AUDIT_V1_1\inspect-gateway.mjs --pem '.\chainsolutions-universal-gateway.2026-10-21.private-key.pem' --report-dir '.\rapports'
```

La V1 historique comportait un mauvais alignement des réponses des appels API ; la V1.1 répare l'alignement et supprime la lecture basée sur un ancien SHA codé en dur. Le ZIP V1 demeure historique et **est superseded pour l'exécution** par V1.1. Aucune validation de configuration privée n'a été exécutée dans cette conversation.\n\nLes éléments confidentiels restent locaux. Seuls la liste des permissions (nom/niveau), les abonnements aux événements et les résultats de contrôle sans secrets peuvent être utilisés comme preuves. L'absence de permission doit être constatée puis corrigée séparément avec approbation explicite, pas par activation aveugle.

## 4. Blocage particulier CI de la PR #1

La création d'un workflow sur une branche de PR ne prouve pas son exécution au HEAD courant. La CI `validate` est exigée par le ruleset `25599154`, alors que la dernière exécution réussie appartient à une révision précédente. Les autorisations et réglages GitHub Actions doivent être contrôlés **via l'audit local** avant toute modification du ruleset.

Ne pas substituer `workflow_dispatch` comme garantie d'un check requis : GitHub documente des événements admissibles spécifiques pour les checks évalués dans une PR, et un dispatch manuel n'en fait pas nécessairement partie. Un P1 indépendant concerne aussi l'exécution du validateur depuis la PR elle-même : **aucun check de sécurité contrôlé par le code non approuvé ne suffit, à lui seul, à certifier les secrets**. Exiger une revue indépendante de la politique et une source de validation de confiance avant tout merge.

- Documentation API : https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation
- Configuration webhook : https://docs.github.com/en/rest/apps/webhooks
- Required checks : https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks

## 5. NEXT_ACTION par chantier

- **Bootstrap PR #1 :** `RESTORE_REQUIRED_GITHUB_ACTIONS_VALIDATE_ON_PR_1_HEAD` + revue de tous les fils encore ouverts et preuve d'intégration admissible.
- **App en lecture seule :** `AUDIT_EFFECTIVE_GITHUB_APP_CAPABILITIES_GA_00` (aucune recréation, aucun partage du PEM).
- **Runtime futur :** GA-01 puis GA-02 etc. selon les dépendances; **aucune déclaration de GitHub App « totalement finie » avant GA-08.**


## 6. Audit GA-00 — situation observée et lacunes vérifiables

**Date :** 22 octobre 2026. **Portée :** lecture seule depuis les ressources publiques GitHub et les captures/sorties locales **déjà communiquées**. **Verdict :** `PARTIAL_EVIDENCE — NOT COMPLETE`. Aucun accès privé direct à la configuration de l'App #5417646 n'a été attesté dans ce contrôle. On ne peut pas conclure que « toutes les permissions » sont accordées.

**Contrat des besoins complet :** `docs/github-app/CAHIER_DES_CHARGES_COMPLET.md` (53 exigences, 30 domaines et chaîne d'exécution en 20 étapes). **Le cahier des charges possède la cible**, le présent fichier possède les **preuves/écarts/gates** : deux responsabilités sans conflit.

| Sujet | Observé ou attesté | Écart / statut | Prochaine preuve requise |
| --- | --- | --- | --- |
| Identité de l'App | App `ChainSolutions Universal Gateway`, ID `5417646`, propriétaire `chainsolutions-wealthtech` ; captures et sortie de bootstrap utilisateur | `USER_EVIDENCE_AT_BOOTSTRAP` | `GET /app` courant depuis la clé locale, rapport expurgé |
| Installations | Trois installations déclarées : `173915815`, `173916302`, `173916438` | `USER_EVIDENCE_AT_BOOTSTRAP` | `GET /app/installations`, vérifier comptes, statut, sélection de dépôts, permissions par installation |
| Couverture des repositories | Inventaire historique de 12/13/15 repos au moment des tests locaux | `HISTORICAL_SNAPSHOT`, pas un inventaire courant | Liste paginée de repos effectivement accordés par installation, y compris nouveaux dépôts |
| Permissions maximales | Document de préparation évoquant 100 candidats ; capture du formulaire affichant 12 Repository et 2 Organization sélectionnées à un instant historique | `REQUESTED_CANDIDATES_NOT_EQUAL_GRANTED` | Export `GET /app`, permissions courantes, classification officielle Repository/Organization/Account/Enterprise, niveaux read/write |
| API et jetons | Création JWT et jeton d'installation testés en local, dépôt universel créé via la procédure bootstrap | `PARTIALLY_PROBED` | Probes anonymisées par endpoint/type IAT/UAT/installation ; aucun jeton publié |
| Account OAuth | Fonctionnalités désirées, mais aucun cycle complet user-to-server avec consentement/révocation vérifié | `NOT_VERIFIED` | Tests sur compte consentant avec capture limitée de statut, sans exposer le jeton |
| Enterprise | Aucun entitlement Enterprise démontré pour les espaces cibles | `ELIGIBILITY_UNKNOWN` | Vérifier offre/installations ; `N/A` si inéligible |
| Événements/webhook | Abonnements, URL de réception, secret HMAC et deliveries récents non attestés | `NOT_VERIFIED` | `GET /app`, config webhook expurgée, test signature/livraison/replay en environnement LAB |
| Broker permanent | Script ponctuel de bootstrap, pas de service durable doté d'un coffre approuvé | `NOT_IMPLEMENTED` | Service, tests d'expiration/réduction de droits, journaux sans secrets, procédure rotation |
| Couverture des 30 domaines | Catalogue original avec `verified_runtime:false` pour les 30 domaines | `DOCUMENTED_NOT_RUNTIME` | Matrice `capability_id → endpoint → token → permission → account → probe → proof`, sans faux statut `READY` |
| Repository universel | Dépôt public GitHub `universal-agent-platform` observable, `main` HEAD `0b8b2e01e826b915a0c593d5d6545681e9316567` lors du contrôle | `GITHUB_LIVE_VERIFIED` | Recontrôle du HEAD avant toute opération |
| Protection de `main` | Ruleset `25599154` actif, PR et check `validate` requis, sans acteur bypass | `GITHUB_LIVE_VERIFIED` | Maintenir protection et revue indépendante |
| Fondation V5 | PR #1 sur `bootstrap/canonical-v5-foundation` encore ouverte, documents + tests proposés | `NOT_MERGED` | Review/résolution de tous les fils ouverts ; preuve CI sur dernier HEAD |
| CI de la PR #1 | Dernière exécution `validate` réussie observée sur l'ancien SHA `fbf4c81f50396f157d69c8d668b3c19262d8ad20` | `LATEST_HEAD_NOT_VERIFIED` | Diagnostiquer déclenchements GitHub Actions et checks sur la révision actuelle, sans bypass |
| Autorité des agents et mémoire durable | Contrats prévus mais registre et engine runtime non établis | `NOT_IMPLEMENTED` | B02/B03/B05/B08/B09/B10/F00–F03 selon dépendances V5 |
| Contrôles des demandes hostiles | Politique documentaire de refus des instructions issues du contenu GitHub | `SPECIFIED_NOT_SECURITY_CERTIFIED` | Moteur de policy, tests de prompt injection et source d'exécution des validateurs réellement protégée |

### 6.1 Séquence d'audit GA-00 sans modification de configuration

1. Observer `GET /app` et identité réelle (ID, slug, permissions, événements). Le slug n'est pas garanti par le simple nom de fichier PEM.
2. Observer `GET /app/installations` et les dépôts accessibles pour chacune des trois installations, en suivant pagination et décalages temporels.
3. Confronter les permissions aux références GitHub officielles, au catalogue V5 et à toutes les familles pertinentes ; distinguer permissions absentes, versions non disponibles et droits non applicables.
4. Observer la configuration et la livraison des webhooks **sans révéler l'URL privée si elle contient des secrets, ni le secret HMAC**, puis démontrer ultérieurement une livraison signée en LAB.
5. Pour chaque capacité, prévoir ensuite un probe réversible avec type de token approprié ; **ne pas exécuter une mutation pour « tester » une permission dans la phase de lecture seule**.
6. Produire un rapport horodaté **expurgé**, ses références de preuve et la liste d'écarts. Ne proposer une modification de permissions qu'après séparation des risques, approbation de chaque installation concernée et contrôle des permissions réelles.
7. Après audit, **réconcilier** ce chapitre sans remplacer le cahier des charges : `APP_CONFIGURATION_ATTESTED` seulement si couverture et sources suffisamment exhaustives.

### 6.2 Conditions de blocage

- Les vues GitHub fournies par le connecteur ChatGPT de la conversation ne constituent **pas** les identifiants/permissions de `ChainSolutions Universal Gateway`. Ne pas confondre ces Apps.
- L'impossibilité d'interroger en direct `GET /app` avec notre App signifie **`NOT_VERIFIED`**, pas « permission absente ».
- Aucun mot de passe, clé PEM, token, secret webhook ou archive de conversations privées ne doit être publié dans le dépôt public, les commentaires GitHub ou cette conversation.
- Une preuve de création de dépôt, un ruleset actif et un catalogue des 30 domaines ne suffisent pas à déclarer le **broker, OAuth, les webhooks ou la plateforme autonomes opérationnels**.
- L'audit GA-00 peut continuer **en lecture seule** malgré le blocage de la CI de PR #1 ; les déploiements/activations sensibles restent sous gates de gouvernance.

### 6.3 NEXT_ACTIONs distinctes

- **Cahier des charges :** vérifier et conserver les 53 exigences dans `CAHIER_DES_CHARGES_COMPLET.md` sans écraser les sources V5.
- **Audit App :** `AUDIT_EFFECTIVE_GITHUB_APP_CAPABILITIES_GA_00` via une collecte locale en lecture seule, avec le PEM conservé localement.
- **Intégration PR :** `RESTORE_REQUIRED_GITHUB_ACTIONS_VALIDATE_ON_PR_1_HEAD`, puis revue indépendante et résolution de tous les fils ouverts avant merge.
- **Construction runtime :** seulement après les prérequis réels et les décisions d'architecture admissibles, commencer GA-01 et les lots B/F/D dépendants.


## 7. Priorité exclusive de finalisation — couverture maximale de permissions

**Décision utilisateur :** concentrer le chantier courant sur **la GitHub App complète, puissante, avec toutes les permissions admissibles**, plutôt que commencer prématurément le runtime général de la plateforme. L'ambition couvre les permissions historiques, les nouvelles permissions GitHub et les événements, mais aucun droit inconnu, dangereux ou indisponible ne sera déclaré octroyé par hypothèse.

### 7.1 Inventaire documentaire actualisé à partir de GitHub (22/10/2026)

La source utilisateur `REGISTER_UNIVERSAL_GITHUB_APP_V5.zip` fournit **100 candidats historiques** (41 Repository, 38 Organization, 20 Account, 1 Enterprise). La rubrique **Permissions required for GitHub Apps** de la référence REST GitHub consultée le 22 octobre 2026 présente **80 rubriques indexées** pour les endpoints REST (33 Repository, 32 Organization, 14 User/Account, 1 Enterprise). Ces deux nombres décrivent **des référentiels de nature différente** ; **80 n'est pas le nombre total démontré de permissions du formulaire GitHub** et les différences ne sont pas des suppressions confirmées. Les 80 intitulés sont transcrits dans `CAHIER_DES_CHARGES_COMPLET.md` § 10, avec leur nature documentaire.

**Sources officielles :**
- https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps
- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
- https://docs.github.com/en/apps/maintaining-github-apps/modifying-a-github-app-registration
- https://docs.github.com/en/rest/apps/apps
- https://docs.github.com/en/rest/apps/webhooks

### 7.2 Registre d'actions focalisé — avant toute élévation

| Ordre | Code | Action réelle | Vérification et preuve attendue | État |
| --- | --- | --- | --- | --- |
| 01 | `GH-MAX-01` | Comparer les 100 candidats historiques aux permissions officielles REST, GraphQL, Git et aux formulaires actuels | Matrice ancien nom → nom officiel/type de jeton/version/entitlement, anomalies et inconnues | `DOCUMENTARY_PARTIAL` |
| 02 | `GH-MAX-02` | Auditer **l'App #5417646** avec JWT en lecture seule : `GET /app` | ID, slug confirmé, permissions actuelles, événements et métadonnées **expurgées** | `NOT_VERIFIED_PRIVATE` |
| 03 | `GH-MAX-03` | Auditer chaque installation : `GET /app/installations` et dépôts accessibles avec pagination | ID, compte, `repository_selection`, `permissions`, `events`, repo scope, suspension/approbation | `NOT_VERIFIED_CURRENT` |
| 04 | `GH-MAX-04` | Produire le delta **souhaité ↔ réellement configurable ↔ demandé ↔ approuvé** par compte | Diff pour les 4 familles, risques, prérequis et plan d'approbation ; ne pas confondre App et utilisateurs | `BLOCKED_BY_GH-MAX-02/03` |
| 05 | `GH-MAX-05` | Définir profils `NORMAL_OPERATIONS`, `SECURITY_ADMIN`, `GOVERNANCE_ADMIN`, `USER_DELEGATED`, `ENTERPRISE_OPTIONAL` | Matrice de risque, politique, coffre et isolation des droits sensibles | `PLANNED` |
| 06 | `GH-MAX-06` | Modifier les permissions de l'**App existante** après revue/autorité, sans créer de nouvelle App | Journal des modifications, consentements/approbations de chaque installation et utilisateur requis | `NOT_STARTED` |
| 07 | `GH-MAX-07` | Recontrôler la configuration et les événements après les approbations | `GET /app` + installations et webhooks, écarts, nouvelles preuves datées | `NOT_STARTED` |
| 08 | `GH-MAX-08` | Développer broker JWT/IAT/UAT durable et récepteur webhook sécurisé, puis tester en LAB | Tests d'isolation du mandat, HMAC, expiration, idempotence, refus par défaut | `NOT_IMPLEMENTED` |
| 09 | `GH-MAX-09` | Tester chaque famille/capacité admissible en LAB et construire le tableau de couverture | `requested→granted→probed→policy-allowed`, succès/échec, preuve ; 30 domaines V5 | `NOT_IMPLEMENTED` |
| 10 | `GH-MAX-10` | Audit indépendant final et livraison selon GA-07/08 | Vérifications de sécurité, droits, révocation, restauration, fonctionnement et non-régression | `NOT_IMPLEMENTED` |

### 7.3 Différences entre permissions natives et autonomie totale

Le « droit maximal » concerne les **permissions configurables et approuvées GitHub**, pas un pouvoir illimité du modèle IA. Les fonctionnalités de mémoire, orchestration, agents, bus, infrastructure et contrôle métier seront développées **autour** de l'App selon les lots V5, en conservant les autorités tierces distinctes. Une permission Repository/Organization approuvée ne donne pas automatiquement les permissions Account/Enterprise ; de même les permissions App ne remplacent pas l'autorisation de l'agent.

GitHub précise qu'après ajout de permissions Repository/Organization, **chaque installation doit accepter les changements**, et après ajout de permissions de compte, **chaque utilisateur autorisant l'App doit approuver**. En attendant, l'installation conserve ses anciens droits. Les événements accessibles dépendent aussi des permissions sélectionnées. Aucune opération de modification de permissions ne sera revendiquée avant ce mécanisme d'approbation.

### 7.4 Premier résultat d'audit sur les preuves effectivement présentes

**`GH-MAX-01` commencé en mode documentaire**, références historiques et GitHub officiel identifiées. **`GH-MAX-02` / `GH-MAX-03` non vérifiables ici** sans identité JWT de **cette App précise**, qui ne doit pas être confondue avec le connecteur GitHub de ChatGPT. Il faut utiliser le processus local read-only, puis importer uniquement le rapport expurgé. Aucune permission n'a été accordée, supprimée ou changée par cette lecture.

**Prochaine opération du chantier focalisé :** `AUDIT_EFFECTIVE_GITHUB_APP_CAPABILITIES_GA_00`, sous-étapes `GH-MAX-02` et `GH-MAX-03` en lecture seule. Le gate CI de la PR #1 reste bloquant **pour la fusion**, mais n'empêche pas d'inventorier l'App sans écriture.

### 7.5 Contrat machine GH-MAX — projection du plan, non nouveau registre d'état

Pour rendre les dix opérations précédentes interprétables par un futur orchestrateur, le fichier `docs/github-app/GH_MAX_EXECUTION_PLAN.json` contient **exactement** les identifiants `GH-MAX-01` à `GH-MAX-10`, dans l'ordre de leur tableau § 7.2. Il définit dépendances explicites, types d'actions, exigences, preuves, causes de blocage, garde-fous, transitions d'état proposées et champs de checkpoint. **Le présent document reste propriétaire de l'état audité et des gates ; le JSON n'en est qu'une projection technique prospective.**

- **Statut de la projection :** `DRAFT_NOT_APPROVED_NOT_RUNTIME`.
- **Exécution :** `execution_enabled=false`, `mutations_enabled=false`, tous les `admitted=false`. Aucun mandat, jeton, session, worker ni tâche runtime n'en résulte.
- **Lecture technique :** `python3 scripts/check_gateway_execution_plan.py` valide le graphe sans réseau. `python3 scripts/check_gateway_execution_plan.py --next` simule les candidats qui n'ont pas de dépendances documentaires, **sans** les admettre ni les lancer.
- **Tests :** `tests/test_gateway_execution_plan.py` vérifie notamment la protection contre un déverrouillage d'exécution, les cycles, la demande de privilèges sans approbation, les preuves et la correspondance au registre canonique.
- **Arrêt sûr :** absence de preuve, approbation, autorisation de projet, jeton local approprié ou CI fiable → état bloqué/en attente, jamais élévation implicite de droits.
- **Reprise future :** relire `state/CURRENT_STATE.json`, la configuration GitHub et les preuves, résoudre la même identité/tâche/mandat puis traiter le prochain élément admissible. Le futur runtime possédera ses états et événements sous stockage privé plutôt que modifier ce JSON pour se déclarer terminé.
- **Contrainte actuelle :** le validateur et les tests sont committés sur la PR #1, mais **aucun succès GitHub Actions sur son HEAD courant n'est encore attesté**. La projection ne vaut pas validation indépendante.

### 7.6 Première confrontation GH-MAX-01 reproductible — état provisoire

**Lecture documentaire :** le rapprochement **des noms normalisés** des 100 candidats historiques contre les **80 intitulés REST** disponibles au § 10 du cahier des charges fournit :

| Sous-ensemble | Candidats historiques | Correspondances de libellé | Sans correspondance de libellé REST |
| --- | ---: | ---: | ---: |
| Repository | 41 | 31 | **10** |
| Organization | 38 | 26 | **12** |
| Account/User | 20 | 12 | **8** |
| Enterprise | 1 | 1 | **0** |
| **Total** | **100** | **70** | **30** |

**Ces 70 correspondances ne prouvent pas l'identité sémantique des droits, leur caractère disponible ou leur octroi.** Les **30 sans correspondance REST ne sont PAS considérés comme supprimés** : recherche GraphQL, Git, documentation propre à chaque produit, alias de vocabulaire et vérification du formulaire actuel encore requises. Aucun résultat `APPROVED`, `GRANTED`, `READY` ou `DONE` n'est établi.

**Candidats à examiner (30), séparés par périmètre :**

- **Repository (10) :** `agent_tasks`, `statuses`, `discussions`, `license_compliance_alerts`, `merge_queues`, `packages`, `repository_projects`, `repository_license_policy`, `secret_scanning_alert_dismissal_requests`, `secret_scanning_push_protection_bypass_requests`.
- **Organization (12) :** `organization_user_blocking`, `organization_copilot_requests`, `organization_custom_org_roles`, `organization_custom_roles`, `organization_external_properties_for_repos`, `organization_copilot_seat_management`, `organization_models`, `organization_announcement_banners`, `organization_credentials`, `organization_plan`, `organization_actions_variables`, `organization_hooks`.
- **Account/User (8) :** `blocking`, `copilot_chat`, `copilot_editor_context`, `user_events`, `user_issue_fields`, `user_issue_types`, `models`, `plugin_gateway_connections`.

**Outils de reproduction sur la branche, en lecture seule :**

```bash
python3 scripts/reconcile_gateway_permissions.py
python3 scripts/reconcile_gateway_permissions.py --json
python3 scripts/check_gateway_execution_plan.py --next
python3 -m unittest discover -s tests -p 'test_gateway_*py' -v
```

- `scripts/reconcile_gateway_permissions.py` produit un rapport JSON dérivé du **propriétaire de source** `CAHIER_DES_CHARGES_COMPLET.md`, et **n'écrit aucun statut runtime** ; il ne s'agit pas d'un second inventaire canonique.
- `tests/test_gateway_permission_reconciliation.py` ajoute neuf contrôles négatifs et structurels, notamment zéro privilège accordé par déduction.
- Le workflow `canonical-documentation.yml` exécute désormais en principe les deux validateurs documentaires sur sa branche avant la suite de tests, **sous réserve d'une CI réelle sur le HEAD actuel**.
- Vérification structurelle depuis les fichiers GitHub effectuée dans cette conversation ; **aucune exécution CI au dernier HEAD ni audit privé de l'App** encore attestés.
- **GH-MAX-01 reste `DOCUMENTARY_PARTIAL`**, jusqu'à la réconciliation GraphQL/autres API et la validation indépendante des 30 cas.


### 7.7 Deuxième source officielle — amélioration de la réconciliation à 84 / 100

Le § 11 du cahier des charges conserve **57 champs techniques de permissions** listés dans la documentation GitHub sous **`POST /app/installations/{installation_id}/access_tokens`**, champ `permissions` (API version `2026-03-10`, consultation du 22 octobre 2026). C'est un **inventaire de champs documentés**, **pas** un registre d'octroi effectif ni le catalogue complet des permissions GitHub.

L'outil `scripts/reconcile_gateway_permissions.py` croise à présent **deux références différentes** avec les 100 candidats : 80 rubriques REST par endpoint + 57 champs de demande de jeton d'installation. Le résultat de rapprochement par nom exact/normalisé est :

| Ensemble documentaire | Nombre de candidats |
| --- | ---: |
| Correspondance dans REST **et** schéma de jeton | **34** |
| Correspondance REST uniquement | **36** |
| Correspondance dans le schéma de jeton uniquement | **14** |
| Absence de correspondance directe dans ces deux références | **16** |
| **Total candidats historiques conservés** | **100** |

**14 cas supplémentaires** sont documentés en termes de nom de champ grâce au schéma des jetons. Les 16 restants doivent être recherchés dans les permissions de l'interface, GraphQL, produits GitHub spécialisés ou plans/aperçus, sans conclure à leur inexistence.

**16 paramètres encore sans correspondance littérale dans les deux sources :**

- Repository (5) : `agent_tasks`, `license_compliance_alerts`, `repository_license_policy`, `secret_scanning_alert_dismissal_requests`, `secret_scanning_push_protection_bypass_requests`.
- Organization (3) : `organization_models`, `organization_credentials`, `organization_actions_variables`.
- Account/User (8) : `blocking`, `copilot_chat`, `copilot_editor_context`, `user_events`, `user_issue_fields`, `user_issue_types`, `models`, `plugin_gateway_connections`.
- Enterprise (0). **Attention :** `enterprise_copilot_metrics` correspond à une rubrique REST ; ce fait ne prouve aucune installation Enterprise.

**Précision sur les niveaux :** certains champs documentés admettent `read`, `write` ou `admin`; d'autres n'admettent que `read` ou `write`. Les niveaux historiques de l'archive sont des **candidats**, et la couverture maximale demandée n'implique pas que `write` existe ou soit admissible sur chaque famille.

**Contrôle de régression :** `tests/test_gateway_permission_reconciliation.py` contient maintenant **11 tests déclarés** couvrant les comptes des trois ensembles, les échecs de suppression de paramètres, les statuts non octroyés et la séparation des scopes. Le workflow GitHub est configuré pour l'exécuter mais **n'a pas encore de `validate: success` sur le dernier HEAD**.

**Source officielle :** https://docs.github.com/en/rest/apps/apps ; `POST /app/installations/{installation_id}/access_tokens` documente aussi la limitation de durée des jetons d'installation et l'impossibilité d'accorder via un jeton des droits supérieurs à ceux de l'App. Les requêtes de jeton ne doivent pas être employées pour « tester » une élévation des droits.

**Statut d'exécution :** `GH-MAX-01 DOCUMENTARY_PARTIAL`. Les correspondances documentaires sont **84/100**, mais aucune des 100 permissions n'est passée au statut `GRANTED` ou `RUNTIME_PROBED` en l'absence d'un audit privé de l'App.


### 7.8 Sources spécialisées — 89 candidats rattachés à au moins une référence officielle

Le cahier des charges § 12 possède **cinq références spécialisées GitHub** concernant `agent_tasks`, `license_compliance_alerts`, `repository_license_policy`, `secret_scanning_alert_dismissal_requests` et `secret_scanning_push_protection_bypass_requests`. Ce sont des **preuves de documentation et d'éligibilité conditionnelle**, non des preuves de droits réellement accordés à notre App.

| Réconciliation des 100 candidats | Nombre |
| --- | ---: |
| Trouvés dans les deux index généraux | 34 |
| REST uniquement | 36 |
| Paramètres de jeton uniquement | 14 |
| Documents GitHub spécialisés uniquement | **5** |
| **Au moins une source GitHub officielle** | **89** |
| **Encore sans correspondance dans ces trois familles de sources** | **11** |

**Les 11 cas à étudier :**

- Organization (3) : `organization_models`, `organization_credentials`, `organization_actions_variables`.
- Account (8) : `blocking`, `copilot_chat`, `copilot_editor_context`, `user_events`, `user_issue_fields`, `user_issue_types`, `models`, `plugin_gateway_connections`.

**Exigence particulière** : `agent_tasks` concerne le service Copilot cloud et ses endpoints exigeant un **UAT** et, pour certaines actions, un abonnement Copilot Business/Enterprise. **Ne jamais substituer un IAT, ni rendre Copilot/Codex obligatoires pour la plateforme.** Les autres références spécialisées impliquent aussi des exigences de produit, permission ou mandat.

Le script `scripts/reconcile_gateway_permissions.py` consomme désormais les **trois sections canoniques** (§ 9/10/11/12) et conserve `live_app_grant=NOT_VERIFIED` et `agent_policy_status=NOT_AUTHORIZED_BY_THIS_REPORT` sur tous les candidats. `tests/test_gateway_permission_reconciliation.py` déclare **13 tests** dédiés (aucune réussite Actions au HEAD n'est attestée).

**Verdict :** `GH-MAX-01 DOCUMENTARY_PARTIAL` tant que les 11 derniers paramètres, la configuration effective de l'App et les preuves des installations ne sont pas vérifiés. Le nombre 89 n'est **pas** un niveau d'activation des permissions.



### 7.9 Deux alias d'API GitHub App prouvés — 91 candidats documentés et neuf ouverts

**Contrôle documentaire complémentaire du 22 octobre 2026** : dans les neuf familles d'évidence, conserver explicitement la différence entre **nom technique historique** et **libellé de capacité GitHub App réellement documentée**.

| Candidat historique | Capacité officielle, endpoint et jeton | Conclusion |
| --- | --- | --- |
| `account/blocking` | **Block another user** ; `GET /user/blocks` (UAT/read) et `PUT /user/blocks/{username}` (UAT/write) ; https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps et https://docs.github.com/en/apps/sharing-github-apps/registering-a-github-app-using-url-parameters | `OFFICIAL_GITHUB_APP_CAPABILITY_DOCUMENTED`, pas autorisation de bloquer un utilisateur |
| `organization/organization_actions_variables` | **Variables** organisation ; `GET /orgs/{org}/actions/variables/{name}` (IAT/UAT/read) et mises à jour autorisées en write ; https://docs.github.com/en/rest/actions/variables | `OFFICIAL_GITHUB_APP_CAPABILITY_DOCUMENTED`, le nom exact de permission doit encore être validé sur l'App |

**Bilan cumulé :** **34** correspondances REST+schema, **36** REST seules, **14** schéma de jeton seul, **5** sources spécialisées, **2** alias d'endpoints GitHub App, **9** sans correspondance directe probante dans ces sources = **100 candidats historiques intacts** ; **91 disposent d'au moins une correspondance documentaire**. **Zéro autorisation effective** constatée lors de cette opération.

**Neuf cas conservés pour l'audit approfondi :**
- Organization (2) : `organization_models`, `organization_credentials`.
- Account (7) : `copilot_chat`, `copilot_editor_context`, `user_events`, `user_issue_fields`, `user_issue_types`, `models`, `plugin_gateway_connections`.

**Réserve essentielle :** la documentation GitHub de gestion des **Personal Access Tokens (PAT)** mentionne certains paramètres portant des noms comparables (notamment `organization_models`, `copilot_editor_context`, `user_events`, `user_models` et `copilot_messages`). Elle ne prouve **pas** leur disponibilité pour **notre GitHub App**. Ne pas importer les permissions de PAT comme permissions d'installation ! Le nom historique `copilot_chat` pourrait être un alias de `copilot_messages` mais **ce rapprochement n'est pas encore attesté**.

**Validation automatisable :** `scripts/reconcile_gateway_permissions.py` lit désormais le §13 du cahier des charges en plus des trois sources précédentes. `tests/test_gateway_permission_reconciliation.py` contient **15 méthodes de test déclarées**, dont le refus de considérer une correspondance comme une permission accordée. Les tests ne sont **pas attestés exécutés dans GitHub Actions au HEAD de PR #1**.

**Verdict GH-MAX-01 :** `DOCUMENTARY_PARTIAL`. **NEXT_ACTION technique incontournable :** `GET /app` puis `GET /app/installations` avec l'identité réelle de l'App #5417646 en lecture seule, sur le poste où sa clé privée est conservée. Toute élévation effective reste interdite en l'absence de la preuve et des approbations nécessaires.

