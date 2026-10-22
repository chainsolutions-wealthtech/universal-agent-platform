# ChainSolutions Universal Gateway — cahier des charges fonctionnel complet

**Statut :** `USER_INTENT_CANONICAL_CANDIDATE_IN_PR` — cahier des charges **consigné** pour revue, non preuve de réalisation et non autorité d'exécution.  
**Date de consignation :** 22 octobre 2026.  
**Produit :** GitHub App `ChainSolutions Universal Gateway` (App ID `5417646`), sous `chainsolutions-wealthtech`.  
**Source d'autorité de l'intention :** demandes explicites de l'utilisateur sur la **couverture maximale des droits GitHub**, le fonctionnement multi-comptes, l'autonomie des agents et la continuité, consolidées avec le **plan directeur V5**, le **texte complémentaire original de 20 sections** et le **catalogue V5 de 30 domaines**. Les détails techniques restent des **spécifications cibles**, pas une preuve d'installation ou d'exécution.

## 0. Ce qui doit être retenu sans réduction

L'utilisateur veut une GitHub App **universelle, très complète et exploitable par ChatGPT, Claude et les futures IA autorisées**, installable sur ses espaces GitHub et dotée de la **couverture maximale de permissions que GitHub permet réellement** pour chaque compte, installation, rôle et abonnement. Cette ambition comprend **TOUTES les fonctions GitHub pertinentes**, et pas seulement `Contents`, `Issues`, `Pull Requests` et `Actions`.

La finalité n'est **pas** d'accorder un pouvoir universel inconditionnel à chaque agent : l'App dispose de permissions **réellement demandées et accordées** ; chaque opération passe de plus par un contrôle **par agent, mandat, projet, ressource, politique, token et installation**. Une permission `Write` de l'App n'est jamais un droit d'agir sans mandat. Les permissions dangereuses seront isolées par broker/identités spécialisées si nécessaire, sans retirer leur objectif de couverture du catalogue.

**Une App native GitHub n'est pas toute la plateforme.** Elle est son point d'accès GitHub. Les agents, IA, mémoire, orchestration, exécution continue, bus et infrastructure externe sont des **services séparés à construire**.

## 1. Principes non négociables

1. **Réutiliser l'App existante** `ChainSolutions Universal Gateway` (ID `5417646`), sans la recréer ni changer son identité par convenance.
2. **Trois périmètres distincts** : organisation `chainsolutions-wealthtech` ; comptes personnels `Patricked-code` et `Wealthtechinnovations`. Les installations sont indépendantes et les droits sont vérifiés pour chacune.
3. **Portée future maximale** : l'inventaire documentaire doit couvrir les 4 familles `Repository`, `Organization`, `Account`, `Enterprise`, les opérations REST/GraphQL/Git et les produits GitHub éligibles, même quand l'activation est conditionnelle.
4. **Permissions effectives ≠ permissions souhaitées** : la matrice indique `CANDIDATE/REQUESTED/GRANTED/RUNTIME_PROBED/POLICY_ALLOWED/NOT_GRANTED/NOT_APPLICABLE/BLOCKED` et rattache toute affirmation à une preuve horodatée.
5. **Séparer trois jetons** : JWT d'application (administration de l'App et émission de IAT selon endpoints), IAT propre à une installation, UAT utilisateur après OAuth et consentement. Ne jamais substituer un IAT aux droits utilisateur ni l'inverse.
6. **Conserver les secrets hors Git et hors modèles** : PEM, client secret, webhook secret et jetons dans un gestionnaire privé, avec rotation, expiration, révocation, audit expurgé et segmentation.
7. **Séparer les gouvernances** : `Patricked-code/MCP` et `chainsolutions-wealthtech/Governed-Repository-Template` conservent leurs propres autorités et ne deviennent pas des sous-modules de cette plateforme.
8. **Sans dépendance obligatoire à Codex ou GitHub Copilot** : l'intégration ChatGPT/Claude/autres fournisseurs doit être indépendante du fabricant.
9. **Événements et état durable** : webhooks signés, tâches idempotentes, ledger, preuves et reprise après interruption ; aucun simple message de conversation ne constitue la mémoire runtime.
10. **Qualité avant fusion** : branche/PR admissible, sécurité, test CI sur le dernier HEAD, revue indépendante, approbation/politique et déploiement seulement si autorisé.
11. **Préserver l'historique** : texte V5 original conservé, décisions versionnées, provenance et supersession explicites ; pas de remplacement de sources historiques par une synthèse.
12. **Ne pas déclarer les permissions « toutes activées » sans audit live**. La configuration historique évoque un lot de 100 permissions candidates et un formulaire montrant 12 repository et 2 organization ; cela ne prouve aucune autorisation maximale réellement accordée.

## 2. Inventaire intégral des exigences d'intention — 53 exigences regroupées

### A — Accès universel et authentification (REQ-APP-01 à 08)

- **REQ-APP-01** — Conserver l'App existante `ChainSolutions Universal Gateway`, App ID `5417646`, propriétaire organisation `chainsolutions-wealthtech` ; n'en créer aucune concurrente.
- **REQ-APP-02** — Couvrir les installations séparées de l'organisation `chainsolutions-wealthtech` et des comptes personnels `Patricked-code`, `Wealthtechinnovations`, ainsi que les futurs espaces installant volontairement l'App.
- **REQ-APP-03** — Permettre la découverte complète des installations, dépôts, propriétaires, périmètres et droits réellement accordés ; distinguer `All repositories` envisagé d'une preuve à un instant T.
- **REQ-APP-04** — Distinguer quatre familles de permissions : Repository, Organization, Account et Enterprise optionnel ; inventorier toutes les permissions candidates pertinentes, même si leur activation n'est pas encore possible.
- **REQ-APP-05** — Intégrer les trois contextes d'authentification : JWT App, jeton d'installation IAT et jeton utilisateur UAT/OAuth, avec restrictions propres à chaque endpoint.
- **REQ-APP-06** — Construire un broker serveur privé pour générer des IAT à durée et périmètre minimaux, gérer coffre, rotation/révocation, expiration, quotas, erreurs et rate limits.
- **REQ-APP-07** — Exiger que chaque capacité passe par `REQUESTED → GRANTED_BY_INSTALLATION/USER → RUNTIME_PROBED → POLICY_ALLOWED`, sans inférer le droit d'agir d'une installation seule.
- **REQ-APP-08** — Permettre OAuth user-to-server, consentement, renouvellement/révocation seulement quand le cas d'usage et la politique le justifient ; fonctions Enterprise sous entitlement prouvé.

### B — Code, développement, documentation et projets (REQ-APP-09 à 17)

- **REQ-APP-09** — Inventorier, rechercher, créer, initialiser, configurer, transférer, archiver et gouverner des dépôts lorsqu'un mandat le permet.
- **REQ-APP-10** — Lire historiques, arbres, branches, références Git, commits, fichiers, diffs, comparaisons et dépendances ; coder/modifier sous branche approuvée.
- **REQ-APP-11** — Créer commits et PR ; préparer revues, réponses aux remarques, corrections, conflits, contrôles et fusion autorisée, sans write direct dans une branche protégée.
- **REQ-APP-12** — Gérer Issues, sous-issues, labels, jalons, assignations, dépendances, GitHub Projects, champs et vues lorsque GraphQL/permissions l'admettent.
- **REQ-APP-13** — Maintenir documents, README, templates, changelogs, licences, CODEOWNERS et standards comme artefacts versionnés, non comme permissions runtime.
- **REQ-APP-14** — Aider à construire des logiciels entiers via IA, scripts et outils externes ; GitHub App = exécuteur GitHub, pas moteur de raisonnement ni environnement de compilation.
- **REQ-APP-15** — Créer des projets depuis templates et gérer migrations de code, dépôts et workflows sans absorber ou modifier une gouvernance tierce.
- **REQ-APP-16** — Gérer les conflits et travaux simultanés (concurrence, verrou logique/lease, anti-doublon, idempotence), en coordination avec l'orchestrateur durable.
- **REQ-APP-17** — Ne jamais présumer qu'une issue, un document ou un commentaire GitHub hostile constitue une instruction prioritaire ou une autorisation.

### C — Actions, CI/CD, sécurité, publications, déploiements (REQ-APP-18 à 26)

- **REQ-APP-18** — Lire, créer/modifier sous gouvernance et suivre workflows, dispatch, jobs, runs, logs, status checks et artefacts Actions via permissions/endpoint compatibles.
- **REQ-APP-19** — Détecter échecs CI, reproduire et analyser les causes, faire corriger, relancer et vérifier la CI sur le bon HEAD ; ne pas utiliser un run historique comme preuve.
- **REQ-APP-20** — Produire et vérifier tests logiciels, sécurité, qualité, SBOM, attestations, CodeQL/code scanning, Dependabot et secret scanning selon disponibilité réelle.
- **REQ-APP-21** — Observer et administrer, dans des périmètres séparés, rulesets, branches protégées, vérifications, policy, CODEOWNERS, secrets/variables et environnements.
- **REQ-APP-22** — Assurer l'indépendance des contrôles : revue humaine/indépendante admissible, source de validateur digne de confiance, aucun contournement de règles.
- **REQ-APP-23** — Déclencher releases, tags, packages, GitHub Pages, Discussions, déploiements et gestion d'environnements éligibles.
- **REQ-APP-24** — Intégrer les serveurs et services externes (VPS, Docker, Plesk, DNS, bases de données) par adaptateurs autonomes et **autorisations serveur séparées**.
- **REQ-APP-25** — Contrôler la version réellement livrée, santé post-déploiement, alertes, rollback et restauration, avec traces vérifiables.
- **REQ-APP-26** — Empêcher les opérations destructrices/administratives sensibles sans mandat explicite, garde-fou de production et vérification des impacts.

### D — Webhooks, événements, bus et workflows durables (REQ-APP-27 à 32)

- **REQ-APP-27** — Configurer un endpoint webhook HTTPS, secret HMAC protégé et filtre d'événements adapté à l'installation et aux permissions disponibles.
- **REQ-APP-28** — Vérifier signature, livraison, auteur, événement/action, horodatage, rejouement, corrélation et provenance avant admission.
- **REQ-APP-29** — Publier dans un bus/queue durable, inbox/outbox, ACK, retry borné, dead-letter, idempotency-key et traitement concurrent sécurisé.
- **REQ-APP-30** — Réagir aux événements issue/PR/push/workflow failed/merged/security alert/installation changed, dans la mesure des événements effectivement souscrits.
- **REQ-APP-31** — Transformer l'événement en tâche après résolution du projet, de l'agent, de la mission, de l'autorisation et de l'état courant, sans créer de task duplicate.
- **REQ-APP-32** — Ne pas créer un bus concurrent ou une seconde gouvernance dans `Patricked-code/MCP` ou `Governed-Repository-Template` ; utiliser des adaptateurs et leurs autorités existantes.

### E — IA, agents, mémoire canonique, coordination (REQ-APP-33 à 40)

- **REQ-APP-33** — Permettre à ChatGPT, Claude et autres fournisseurs autorisés d'appeler les capacités GitHub via une interface serveur agnostique ; pas de dépendance obligatoire à Copilot/Codex.
- **REQ-APP-34** — Séparer identité technique GitHub App, `agent_id`, `blueprint_id`, `assignment_id`, `mandate_id`, `mission_id`, `task_id`, `session_id`, `continuity_id` et conversation.
- **REQ-APP-35** — Maintenir un registre global d'agents existants, blueprints, compétences, responsables, mandats et territoires de travail, sans duplication d'identité.
- **REQ-APP-36** — Conserver, dans un stockage privé séparé, sources originales effectivement accessibles, mémoire canonique, provenance, décisions, versions et supersessions.
- **REQ-APP-37** — Gérer checkpoints, handoffs, NEXT_ACTION, rebind de session/conversation et reprise de la même mission après crash ou changement ChatGPT/Claude.
- **REQ-APP-38** — Planifier dépendances des tâches (DAG), réservations/leases, retry, compensations, coûts, statuts et arrêt terminal ; la GitHub App appelle les API, mais n'est pas l'orchestrateur.
- **REQ-APP-39** — Faire collaborer plusieurs agents sans branche, mandat, session ou modification concurrente du même périmètre critique.
- **REQ-APP-40** — Garantir que chaque action GitHub possède attribution de l'agent, mandat, politique, installation, token-type, HEAD, résultat et preuve expurgée.

### F — Organisations, utilisateurs, Enterprise et extensions (REQ-APP-41 à 46)

- **REQ-APP-41** — Administrer les ressources d'organisations (teams, membres, projects, propriétés, règles, runners, settings) uniquement si l'installation et les rôles le permettent.
- **REQ-APP-42** — Utiliser les fonctionnalités liées à l'utilisateur (profil, ressources personnelles, éventuellement gists/Models/etc.) par UAT et consentement réel lorsqu'un IAT ne suffit pas.
- **REQ-APP-43** — Couvrir les API et fonctions Enterprise admissibles selon le plan GitHub et les contraintes de l'installation, sans inventer des droits Enterprise.
- **REQ-APP-44** — Gérer produits additionnels (Packages, Pages, Releases, Discussions, Codespaces, GitHub Models et fonctions Agent/Copilot facultatives) selon disponibilité et besoins.
- **REQ-APP-45** — Recenser REST/GraphQL/Git, endpoints, permissions read/write, coûts, limites, prérequis et tests pour une **couverture aussi exhaustive que possible**.
- **REQ-APP-46** — Distinguer possibilités documentées, permissions simplement demandées, permissions octroyées et fonctionnalités runtime réellement exercées.

### G — Observabilité, contrôle central, évolution permanente (REQ-APP-47 à 53)

- **REQ-APP-47** — Construire un Universal Control Center montrant installations, comptes, dépôts, permissions, agents, missions, messages, PR, checks, incidents, déploiements, dépenses et preuves.
- **REQ-APP-48** — Produire tableaux de bord fiables, alertes, audits historiques, analytics multi-repos, SLA et KPIs de l'usine logicielle sans inventer d'activités agent.
- **REQ-APP-49** — Versionner un catalogue de capacité GitHub avec identifiant, endpoint, famille, jeton, permissions, installation, test, droit politique, résultat et preuve.
- **REQ-APP-50** — Surveiller changements GitHub API, permissions, événements, quotas et produits ; découvrir les nouvelles possibilités sans auto-élever les droits.
- **REQ-APP-51** — Comparer configuration réelle/attendue, détecter drift et proposer corrections sous revue avec restauration possible.
- **REQ-APP-52** — Permettre simulation de décision (dry-run), mode audit, corrélation traçable de bout en bout et vérifications indépendantes.
- **REQ-APP-53** — Accepter des limites : API/abonnements, approbation, quotas, secrets non lisibles en clair et absence de garantie mathématique de zéro régression/exactement-once.

## 3. Cartographie exhaustive des trente domaines conservés du texte utilisateur

Le tableau ci-dessous reproduit les **30 identifiants et domaines du catalogue V5**, sans inventer leur preuve runtime. Source exacte des libellés et modes : `docs/roadmap/CATALOGUE_30_DOMAINES_V5.json` (propriétaire canonique), lui-même dérivé de l'annexe B du plan.

| N° source | Domaine voulu | Mode défini dans V5 | Preuve d'utilisation runtime au catalogue |
| ---: | --- | --- | --- |
| 01 | Dépôts Git | Natif | **Non attesté** |
| 02 | Code source | Natif + IA | **Non attesté** |
| 03 | Branches | Natif | **Non attesté** |
| 04 | Commits | Natif | **Non attesté** |
| 05 | Pull requests | Natif | **Non attesté** |
| 06 | Issues | Natif | **Non attesté** |
| 07 | GitHub Projects | Natif | **Non attesté** |
| 08 | GitHub Actions | Natif | **Non attesté** |
| 09 | Tests logiciels | GitHub Actions + outils | **Non attesté** |
| 10 | Sécurité | Natif + outils | **Non attesté** |
| 11 | Administration | Natif | **Non attesté** |
| 12 | Déploiement | Natif + infrastructure | **Non attesté** |
| 13 | Documentation | Natif + IA | **Non attesté** |
| 14 | GitHub Pages | Natif | **Non attesté** |
| 15 | Releases | Natif | **Non attesté** |
| 16 | Packages | Natif, selon registre | **Non attesté** |
| 17 | Webhooks | Natif + récepteur | **Non attesté** |
| 18 | Comptes utilisateurs | Autorisation utilisateur | **Non attesté** |
| 19 | Organisations | Natif | **Non attesté** |
| 20 | Enterprise | Selon offre et accès | **Non attesté** |
| 21 | Agents IA | À développer | **Non attesté** |
| 22 | Mémoire des agents | À développer | **Non attesté** |
| 23 | Communication entre agents | À développer | **Non attesté** |
| 24 | Gouvernance des agents | À développer | **Non attesté** |
| 25 | Audit continu | Natif + service | **Non attesté** |
| 26 | Automatisation inter-dépôts | Natif + orchestration | **Non attesté** |
| 27 | Migration de projets | Natif + outils | **Non attesté** |
| 28 | Gestion d'infrastructure | Intégrations externes | **Non attesté** |
| 29 | Analyse de portefeuille logiciel | API + analyse | **Non attesté** |
| 30 | Supervision autonome | À développer | **Non attesté** |

### Distinction indispensable entre deux séries `D`

- Les **30 domaines** ci-dessus sont l'annexe B du texte original, numérotée 01–30.
- Les **lots `D00` à `D14`** de `ROADMAP_V5.json` sont des lots **de réalisation du logiciel** ; les nombres ne correspondent pas 1-pour-1 aux domaines.
- Le plan directeur V5 § 6 mentionne par ailleurs des capacités fonctionnelles D01–D13 : là aussi, leurs intitulés ne sont pas les identifiants de lots du `ROADMAP_V5.json`. Ne pas convertir l'une de ces numérotations en une autre sans matrice explicite.

## 4. Modes d'authentification et contrat de décision

`client/agent → Gateway API → resolve_existing_identity → authenticate_request_origin → scope/mandate → project governance → live installation and permission → required token type → policy decision → API call → audit/ledger → checkpoint`.

Un appel GitHub admissible doit enregistrer au minimum `capability_id`, `installation_id`, `account`, `repository`, `agent_id`, `mandate_id`, `task_id`, `authorization_source`, `token_type`, `operation`, `trace_id`, `idempotency_key`, `started_at`, `final_status`, `proof_refs` et éventuellement `commit_sha/pr_number/workflow_run_id` ; **jamais** le jeton ou la clé.

- `App JWT` : identité technique de l'App, pas un jeton ayant accès universel au contenu des dépôts.
- `IAT` : installation précise, dépôts et permissions octroyés, jeton temporaire limité au strict nécessaire quand GitHub permet cette réduction.
- `UAT` : consentement explicite et intersection des droits de l'utilisateur, de l'App et de l'installation.
- `Enterprise` : uniquement si les offres, permissions et installations réelles le permettent.
- Opérations destructrices, `Administration`, `Security`, secrets, règles de protection, déploiement de production : approbation gouvernée / séparation des responsabilités et récupération possible.

## 5. Pipeline d'ingénierie autonome cible — 20 passages à prouver

**Cette chaîne appartient au programme de plateforme, non aux API natives de GitHub**. Source : § 7 du plan V5, `docs/archive/PLAN_DIRECTEUR_UNIFIE_V5_20261021.md`.

| Passage | Action | Preuve attendue |
| ---: | --- | --- |
| 01 | Réception de demande, issue ou webhook | Source et `event_id` |
| 02 | Résolution du projet, agent et mission | Identités et droits vérifiés |
| 03 | Lecture des autorités du dépôt et du HEAD courant | Baseline et policies |
| 04 | Décomposition et dépendances | DAG et critères |
| 05 | Analyse d'architecture et impacts | Décisions/risques, ADR si approuvées |
| 06 | Affectation et réservation de tâche | Lease + mandat |
| 07 | Préparation du workspace/branche | SHA initial et branche autorisée |
| 08 | Construction code/doc/config | Commits traçables |
| 09 | Tests logiciels | Logs et résultats |
| 10 | Déclenchement et suivi CI | Run ID/HEAD |
| 11 | Ingestion résultats/artefacts CI | État terminal prouvé |
| 12 | Correction d'échecs et nouveaux tests | Diffs et nouveaux runs |
| 13 | Revue indépendante | Avis distinct |
| 14 | Sécurité | Résultats/alertes |
| 15 | Publication de la Pull Request | PR et SHA |
| 16 | Contrôle des protections/permissions | Décision gouvernée |
| 17 | Fusion admissible | Merge SHA autorisé |
| 18 | Déploiement autorisé si prévu | Cible et version |
| 19 | Vérification post-déploiement | Santé réelle/rollback possible |
| 20 | Checkpoint canonique | Historique + `NEXT_ACTION` ou `COMPLETED` |

## 6. Critères de réussite de la future GitHub App complète

- **Couverture inventoriée** : catalogue des catégories, des permissions officielles, des endpoints/API, de leurs besoins de jetons, installations, offres, événements et statuts *actualisé depuis les sources GitHub*.
- **Couverture attestée** : chaque opération nécessaire effectivement testée sur un LAB sous une installation appropriée, avec preuve et politique ; toute fonction non accessible marquée `NOT_GRANTED`, `NOT_APPLICABLE` ou `BLOCKED`.
- **Fonctionnement sécurisé** : broker et webhook durable, coffre, HMAC/replay, refus par défaut, scopes réduits, procédures de restauration et audit des modifications.
- **Automatisation réelle** : cycle LAB `issue → événement → tâche → branche → PR → tests/CI → review → checkpoint`, reprise après crash sans doublon.
- **Multi-agents réels** : continuité entre deux fournisseurs IA compatibles depuis le même `agent_id`, sans copie d'identité ni transfert implicite de droits.
- **Gouvernance intacte** : règles GitHub, droits personnels/organisations et politiques des projets jamais contournés.
- **Go-live attesté** : aucun statut `GATEWAY_RELEASE_ACCEPTED` sans gates `GA-00…GA-08` et avis de qualité indépendant.

## 7. Feuille de route d'implémentation — propriétaires existants

- **Source de vérité des 46 lots / critères :** `docs/roadmap/ROADMAP_V5.json`.
- **Ordre du programme :** `docs/roadmap/PROGRAMME_CHRONOLOGIQUE_V5.md`, 10 vagues.
- **138 fiches de travail proposées :** `docs/roadmap/REGISTRE_TACHES_V5.md` ; ce sont des *propositions*, pas des issues/tâches runtime créées.
- **Gates spécifiques GA-00–GA-08 et statut vérifié de l'App :** `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` ; **ce document n'est pas le propriétaire des exigences**.
- **Présent cahier des charges :** propriétaire unique de la **cible fonctionnelle détaillée** de la GitHub App, à enrichir dans ce même fichier sans copies concurrentes.
- **État courant / NEXT_ACTION :** `state/CURRENT_STATE.json` et `SUIVI.md`, à réconcilier avec GitHub live.
- **Preuves GitHub :** issues, PR, commentaires, SHA et checks ; **pas** de valeurs secrètes.

## 8. Sources à conserver et hiérarchie des preuves

**Sources de l'intention utilisateur (non réécrites) :**
1. `docs/archive/TEXTE_COMPLEMENTAIRE_ORIGINAL_20261021.txt` — 20 sections, couverture maximale souhaitée, autonomie, multi-IA et limites GitHub.
2. `docs/archive/PLAN_DIRECTEUR_UNIFIE_V5_20261021.md` — §§ 0–19, spécifications des permissions (§5), domaines (§6), pipeline (§7), dépendances (§11), tests (§12) et runbook (§13).
3. `docs/roadmap/CATALOGUE_30_DOMAINES_V5.json` — 30 domaines source et `verified_runtime:false`.
4. `docs/roadmap/ROADMAP_V5.json` — 46 lots, notamment D00–D14, et leurs états documentaires.
5. `docs/DECISIONS_LOG.md` — décisions DEC-001 à DEC-012 et suivante.
6. Échanges utilisateur d'octobre 2026 — confirmation explicite « App avec tous les droits », i.e. couverture maximale sous gouvernance ; cela **n'est pas** une permission accordée.

**Documentation externe de comparaison, non substitutive à la décision utilisateur :**
- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
- https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
- https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app

**Méthode de réconciliation** : `UTILISATEUR CONFIRMÉ` pour l'objectif ; `HISTORIQUE V5` pour les exigences déjà consignées ; `GITHUB LIVE` pour les permissions/implémentations ; `PROPOSÉ` pour les mécanismes futurs ; `NOT_VERIFIED` lorsque la preuve manque. Ne jamais remplacer un statut incertain par `DONE` sur la foi d'un document.

---

**Conclusion du cahier des charges :** l'App souhaitée devait viser la couverture GitHub la plus complète techniquement et contractuellement réalisable, fonctionner sur plusieurs comptes avec des identités et jetons séparés, automatiser l'ingénierie gouvernée, recevoir les événements et servir les agents et la plateforme persistante, tout en refusant les demandes qui ne sont pas autorisées. Sa livraison réelle nécessite un audit de permissions et un backend qui n'existent pas encore au niveau d'acceptation final.
