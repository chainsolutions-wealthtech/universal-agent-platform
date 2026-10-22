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

Un outil Node.js `UNIVERSAL_GATEWAY_AUDIT_V1.zip` a été **créé dans le contexte de cette conversation**, non ajouté au dépôt GitHub (à importer après revue de confidentialité/code si souhaité). Il lit `GET /app`, la liste des installations, `GET /app/hook/config` avec JWT et les paramètres Actions, règles et checks du repo à l'aide d'un jeton d'installation temporaire. Il **ne lance aucun dispatch**, ne modifie aucune permission, et écrit uniquement un rapport expurgé quand `--report-dir` est fourni.

Commandes PowerShell après extraction du ZIP dans `NNN` :

```powershell
node .\UNIVERSAL_GATEWAY_AUDIT_V1\inspect-gateway.mjs --pem '.\chainsolutions-universal-gateway.2026-10-21.private-key.pem' --report-dir '.\rapports'
```

Les éléments confidentiels restent locaux. Seuls la liste des permissions (nom/niveau), les abonnements aux événements et les résultats de contrôle sans secrets peuvent être utilisés comme preuves. L'absence de permission doit être constatée puis corrigée séparément avec approbation explicite, pas par activation aveugle.

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
