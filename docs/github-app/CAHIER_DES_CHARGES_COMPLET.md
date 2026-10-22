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


## 9. Empreinte de l'ambition « tous les droits » — 100 permissions candidates archivées

**Source primaire :** archive utilisateur `REGISTER_UNIVERSAL_GITHUB_APP_V5.zip`, fichier `permissions-requested.json` (100 entrées), **SHA-256 `0de91cb024ba419f995897b18654ca93583b10cacb578804e598962e0ca6ec10`** sur les octets du fichier préparatoire. La même archive comporte `permissions-audit.csv` et `registration-settings.json` ; 72 candidats y ont été préremplis dans une URL d'inscription. **La sélection réelle GitHub ne peut pas être inférée d'une URL préremplie.**

**Statut du tableau : `HISTORICAL_REQUESTED_CANDIDATES_ONLY`**. Les noms techniques et niveaux ci-dessous sont reproduits depuis le paquet historique, **sans garantir** leur compatibilité avec la version actuelle des formulaires GitHub, leur disponibilité selon l'offre, ni leur inclusion effective parmi les permissions de l'App enregistrée. Certains champs peuvent avoir été ignorés, retirés, renommés ou exiger un consentement spécifique. Le tableau ne remplace **ni** la liste officielle actuelle des permissions **ni** l'audit `GET /app`. Les permissions liées à Copilot ont été envisagées comme candidats facultatifs et **ne sont pas des dépendances** de la plateforme.

| Famille d'origine | Nombre candidat | Traitement attendu |
| --- | ---: | --- |
| Repository | 41 | Confronter aux permissions GitHub actuelles, à l'installation et à chaque endpoint |
| Organization | 38 | Confronter à l'organisation cible, à l'offre et à l'installation |
| Account | 20 | Confronter à GitHub et au consentement OAuth propre à l'utilisateur |
| Enterprise | 1 | Confronter à l'éligibilité réelle ; `NOT_APPLICABLE` si aucune installation Enterprise |
| **TOTAL** | **100** | **Candidats historiques**, pas droits `GRANTED` ni `READY` |

| Portée | Paramètre du paquet historique | Niveau demandé historiquement | Octroi actuel |
| --- | --- | --- | --- |
| `repository` | `actions` | `write` | `NOT_VERIFIED` |
| `repository` | `administration` | `write` | `NOT_VERIFIED` |
| `repository` | `agent_secrets` | `write` | `NOT_VERIFIED` |
| `repository` | `agent_tasks` | `write` | `NOT_VERIFIED` |
| `repository` | `agent_variables` | `write` | `NOT_VERIFIED` |
| `repository` | `artifact_metadata` | `write` | `NOT_VERIFIED` |
| `repository` | `attestations` | `write` | `NOT_VERIFIED` |
| `repository` | `checks` | `write` | `NOT_VERIFIED` |
| `repository` | `code_quality` | `read` | `NOT_VERIFIED` |
| `repository` | `code_scanning_alerts` | `write` | `NOT_VERIFIED` |
| `repository` | `codespaces` | `write` | `NOT_VERIFIED` |
| `repository` | `codespaces_lifecycle_admin` | `write` | `NOT_VERIFIED` |
| `repository` | `codespaces_metadata` | `read` | `NOT_VERIFIED` |
| `repository` | `codespaces_secrets` | `write` | `NOT_VERIFIED` |
| `repository` | `statuses` | `write` | `NOT_VERIFIED` |
| `repository` | `contents` | `write` | `NOT_VERIFIED` |
| `repository` | `copilot_agent_settings` | `read` | `NOT_VERIFIED` |
| `repository` | `custom_properties` | `write` | `NOT_VERIFIED` |
| `repository` | `dependabot_alerts` | `write` | `NOT_VERIFIED` |
| `repository` | `dependabot_secrets` | `write` | `NOT_VERIFIED` |
| `repository` | `deployments` | `write` | `NOT_VERIFIED` |
| `repository` | `discussions` | `write` | `NOT_VERIFIED` |
| `repository` | `environments` | `write` | `NOT_VERIFIED` |
| `repository` | `github_app_installation_repository_access` | `write` | `NOT_VERIFIED` |
| `repository` | `issues` | `write` | `NOT_VERIFIED` |
| `repository` | `license_compliance_alerts` | `read` | `NOT_VERIFIED` |
| `repository` | `merge_queues` | `write` | `NOT_VERIFIED` |
| `repository` | `packages` | `write` | `NOT_VERIFIED` |
| `repository` | `pages` | `write` | `NOT_VERIFIED` |
| `repository` | `repository_projects` | `write` | `NOT_VERIFIED` |
| `repository` | `pull_requests` | `write` | `NOT_VERIFIED` |
| `repository` | `repository_creation` | `write` | `NOT_VERIFIED` |
| `repository` | `repository_license_policy` | `read` | `NOT_VERIFIED` |
| `repository` | `repository_security_advisories` | `write` | `NOT_VERIFIED` |
| `repository` | `secret_scanning_alert_dismissal_requests` | `write` | `NOT_VERIFIED` |
| `repository` | `secret_scanning_alerts` | `write` | `NOT_VERIFIED` |
| `repository` | `secret_scanning_push_protection_bypass_requests` | `write` | `NOT_VERIFIED` |
| `repository` | `secrets` | `write` | `NOT_VERIFIED` |
| `repository` | `variables` | `write` | `NOT_VERIFIED` |
| `repository` | `webhooks` | `write` | `NOT_VERIFIED` |
| `repository` | `workflows` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_api_insights` | `read` | `NOT_VERIFIED` |
| `organization` | `organization_administration` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_agent_secrets` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_agent_variables` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_user_blocking` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_campaigns` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_copilot_requests` | `read` | `NOT_VERIFIED` |
| `organization` | `organization_copilot_spaces` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_copilot_agent_settings` | `read` | `NOT_VERIFIED` |
| `organization` | `organization_copilot_content_exclusion` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_custom_org_roles` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_custom_properties` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_custom_roles` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_events` | `read` | `NOT_VERIFIED` |
| `organization` | `organization_external_properties_for_repos` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_copilot_seat_management` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_hosted_runner_custom_images` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_issue_fields` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_issue_types` | `write` | `NOT_VERIFIED` |
| `organization` | `members` | `read` | `NOT_VERIFIED` |
| `organization` | `organization_models` | `read` | `NOT_VERIFIED` |
| `organization` | `organization_network_configurations` | `read` | `NOT_VERIFIED` |
| `organization` | `organization_copilot_metrics` | `read` | `NOT_VERIFIED` |
| `organization` | `organization_announcement_banners` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_codespaces` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_codespaces_secrets` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_codespaces_settings` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_credentials` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_dependabot_secrets` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_private_registries` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_personal_access_token_requests` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_personal_access_tokens` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_plan` | `read` | `NOT_VERIFIED` |
| `organization` | `organization_projects` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_secrets` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_self_hosted_runners` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_actions_variables` | `write` | `NOT_VERIFIED` |
| `organization` | `organization_hooks` | `write` | `NOT_VERIFIED` |
| `account` | `blocking` | `write` | `NOT_VERIFIED` |
| `account` | `codespaces_user_secrets` | `write` | `NOT_VERIFIED` |
| `account` | `copilot_chat` | `read` | `NOT_VERIFIED` |
| `account` | `copilot_editor_context` | `read` | `NOT_VERIFIED` |
| `account` | `email_addresses` | `read` | `NOT_VERIFIED` |
| `account` | `user_events` | `read` | `NOT_VERIFIED` |
| `account` | `followers` | `read` | `NOT_VERIFIED` |
| `account` | `gpg_keys` | `write` | `NOT_VERIFIED` |
| `account` | `gists` | `write` | `NOT_VERIFIED` |
| `account` | `git_ssh_keys` | `write` | `NOT_VERIFIED` |
| `account` | `interaction_limits` | `write` | `NOT_VERIFIED` |
| `account` | `user_issue_fields` | `write` | `NOT_VERIFIED` |
| `account` | `user_issue_types` | `write` | `NOT_VERIFIED` |
| `account` | `models` | `read` | `NOT_VERIFIED` |
| `account` | `plan` | `read` | `NOT_VERIFIED` |
| `account` | `plugin_gateway_connections` | `write` | `NOT_VERIFIED` |
| `account` | `profile` | `write` | `NOT_VERIFIED` |
| `account` | `ssh_signing_keys` | `write` | `NOT_VERIFIED` |
| `account` | `starring` | `write` | `NOT_VERIFIED` |
| `account` | `watching` | `write` | `NOT_VERIFIED` |
| `enterprise` | `enterprise_copilot_metrics` | `read` | `NOT_VERIFIED` |

**Pour chaque ligne, audit GA-00 obligatoire :** `historical_parameter` → `official_current_permission` (ou `INVALID/RENAMED/NOT_APPLICABLE`) → `requested_current` → `granted_installation` → `endpoint_supported` → `runtime_probed` → `policy_allowed` → `proof_ref`. Ne pas activer automatiquement les 100 ; examiner d'abord les besoins, possibilités et risques, puis demander l'accord requis pour chaque augmentation effective des privilèges.

### 9.1 Les quatre constats distincts

1. **Intention :** demander une couverture fonctionnelle maximale et conserver toutes les permissions candidates du paquet préparatoire.
2. **Enregistrement :** l'App #5417646 a été créée et testée localement ; cela ne valide pas l'import de toutes les permissions candidates.
3. **État réel :** la liste exacte de `GET /app` et les accords par installation sont **non attestés** à cette étape.
4. **Droit d'usage des agents :** même si l'App possède une permission, un agent ne peut s'en servir que sous mandat, politique, périmètre et preuve d'autorisation.



## 10. Confrontation officielle 2026 — index des permissions dans la référence REST GitHub

**Vérification documentaire : 22 octobre 2026.** Source GitHub officielle : https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps (rubrique **In this article**). Source de politique : https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app .

Cette page officielle indexe les **familles de permissions pour lesquelles elle décrit les endpoints REST**. **Ce n'est pas une preuve qu'il n'existe que 80 permissions possibles dans le formulaire d'une GitHub App** : certains droits concernent d'autres API/produits, certaines dénominations ont changé et la documentation évolue. Il ne faut donc ni déduire « 20 permissions historiques supprimées » ni présenter cette liste comme exhaustive de toutes les permissions d'installation. C'est un **index de correspondance externe** pour le rapprochement des 100 candidats historiques.

| Famille de rubrique REST | Rubriques présentes dans la page GitHub | Signification |
| --- | ---: | --- |
| Enterprise | 1 | En fonction de l'offre/installation et de l'API |
| Organization | 32 | Endpoints et permissions d'organisation |
| Repository | 33 | Endpoints et permissions de repository |
| User (= famille Account dans l'interface générale) | 14 | Endpoints utilisant les autorisations d'utilisateur |
| **Total rubriques REST indexées** | **80** | **Pas** un total certifié des permissions configurables d'une GitHub App |

| Famille | Intitulé officiel de rubrique REST (source au 22 octobre 2026) | Statut de l'audit de notre App |
| --- | --- | --- |
| enterprise | Enterprise Copilot metrics | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | API Insights | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Administration | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Agent secrets | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Agent variables | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Blocking users | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Campaigns | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Copilot Spaces | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Copilot agent settings | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Copilot content exclusion | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Custom organization roles | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Custom properties | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Events | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | External custom properties for repositories | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | GitHub Copilot Business | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Hosted runner custom images | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Issue Fields | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Issue Types | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Members | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Network configurations | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Organization Copilot metrics | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Organization codespaces secrets | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Organization codespaces settings | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Organization codespaces | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Organization dependabot secrets | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Organization private registries | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Personal access token requests | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Personal access tokens | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Projects | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Secrets | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Self-hosted runners | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Variables | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| organization | Webhooks | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Actions | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Administration | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Agent secrets | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Agent variables | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Artifact metadata | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Attestations | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Checks | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Code quality | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Code scanning alerts | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Codespaces lifecycle admin | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Codespaces metadata | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Codespaces secrets | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Codespaces | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Commit statuses | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Contents | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Copilot agent settings | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Custom properties | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Dependabot alerts | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Dependabot secrets | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Deployments | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Environments | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | GitHub App installation repository access | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Issues | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Metadata | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Pages | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Pull requests | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Repository creation | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Repository security advisories | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Secret scanning alerts | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Secrets | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Variables | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Webhooks | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| repository | Workflows | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Block another user | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Codespaces user secrets | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Email addresses | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Followers | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | GPG keys | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Gists | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Git SSH keys | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Interaction limits | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Plan | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Private repository invitations | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Profile | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | SSH signing keys | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Starring | `NOT_PROBED_IN_CHAIN_GATEWAY` |
| account | Watching | `NOT_PROBED_IN_CHAIN_GATEWAY` |

### 10.1 Réconciliation ligne à ligne sans régression

1. Réconcilier les 100 paramètres historiques du § 9 avec les rubriques REST officielles du § 10 (noms/alias) et les permissions actuelles de l'interface GitHub App. Une correspondance absente de cette **référence REST** n'est **pas** une preuve de permission invalide.
2. Vérifier l'état réel de l'App avec un JWT issu de sa clé privée **conservée localement**, puis celui des trois installations, sans transmettre de secrets.
3. Classer chaque permission : `OFFICIAL_AND_GRANTED`, `OFFICIAL_BUT_NOT_GRANTED`, `RENAMED_OR_ALIAS`, `NON_REST_SCOPE`, `NOT_AVAILABLE`, `ENTERPRISE_ONLY`, `REQUIRES_USER_AUTHORIZATION`, `UNKNOWN_NEEDS_VERIFICATION`.
4. Exiger un endpoint/GraphQL operation, type de jeton, compte, niveau `read/write/admin` **lorsque réellement applicable**, test réversible et preuve avant de la marquer `RUNTIME_PROBED`.
5. Soumettre toute élévation de droits au processus officiel GitHub et aux approbations propres à chaque installation/utilisateur, en conservant la possibilité de capacités sensibles isolées dans des identités séparées.

### 10.2 Modifications de permissions : réalité opérationnelle

- GitHub signale que l'App n'obtient pas de droits par défaut. Les droits sont demandés et validés par les installations et utilisateurs.
- L'ajout de permissions Repository ou Organization déclenche une **nouvelle approbation par chaque propriétaire d'installation** ; les permissions Account/User passent par le consentement utilisateur.
- Jusqu'à cette approbation, l'installation garde **ses anciennes permissions** ; une suppression de permission peut s'appliquer immédiatement.
- Les événements webhook disponibles dépendent des permissions sélectionnées ; l'authentification JWT/IAT/UAT et les politiques métier restent des couches distinctes.
- Une installation Enterprise n'est possible que si les conditions de visibilité, de propriétaire et de produit sont réunies ; certaines permissions Enterprise d'installation sont soumises à des restrictions supplémentaires.

**Conclusion de réconciliation :** couverture exhaustive = `historique 100 candidats + référence REST actuelle + formulaire réel et paramètres App + permissions réellement accordées sur 3 installations + événements + probes API + contrôle de mandat`. Aucune de ces listes, prise isolément, n'établit que notre App possède tous les droits.


## 11. Deuxième référence officielle 2026 — schéma de paramètres des jetons d'installation

**Référence officielle :** https://docs.github.com/en/rest/apps/apps, section **Create an installation access token for an app**, paramètres `permissions` du corps de requête (rubrique consultée le 22 octobre 2026, version API `2026-03-10`, environs des lignes 315–372). GitHub expose des noms techniques de champs qui n'apparaissent pas nécessairement dans l'index des rubriques REST du §10 ; la présence d'un champ dans ce schéma apporte une **deuxième preuve documentaire de son vocabulaire GitHub**, pas une preuve qu'il est octroyé, utilisable avec chaque jeton, ni proposé dans toutes les éditions/organisations.

**Ce schéma de requête n'est pas une liste exhaustive de tous les droits GitHub**, et ne couvre pas à lui seul toutes les permissions Account/OAuth/Enterprise. La **classe de rapprochement** ci-dessous est une classification de comparaison avec notre historique ; la documentation présente les champs dans un objet JSON commun sans garantir qu'ils seront admissibles pour chaque type de jeton ou installation.

| Classe de rapprochement (indicative) | Champ technique documenté GitHub | Octroi effectif ChainSolutions Universal Gateway |
| --- | --- | --- |
| repository | `actions` | `NOT_VERIFIED` |
| repository | `administration` | `NOT_VERIFIED` |
| repository | `artifact_metadata` | `NOT_VERIFIED` |
| repository | `attestations` | `NOT_VERIFIED` |
| repository | `checks` | `NOT_VERIFIED` |
| repository | `code_quality` | `NOT_VERIFIED` |
| repository | `codespaces` | `NOT_VERIFIED` |
| repository | `contents` | `NOT_VERIFIED` |
| repository | `dependabot_secrets` | `NOT_VERIFIED` |
| repository | `deployments` | `NOT_VERIFIED` |
| repository | `discussions` | `NOT_VERIFIED` |
| repository | `environments` | `NOT_VERIFIED` |
| repository | `issues` | `NOT_VERIFIED` |
| repository | `merge_queues` | `NOT_VERIFIED` |
| repository | `metadata` | `NOT_VERIFIED` |
| repository | `packages` | `NOT_VERIFIED` |
| repository | `pages` | `NOT_VERIFIED` |
| repository | `pull_requests` | `NOT_VERIFIED` |
| repository | `repository_custom_properties` | `NOT_VERIFIED` |
| repository | `repository_hooks` | `NOT_VERIFIED` |
| repository | `repository_projects` | `NOT_VERIFIED` |
| repository | `secret_scanning_alerts` | `NOT_VERIFIED` |
| repository | `secrets` | `NOT_VERIFIED` |
| repository | `security_events` | `NOT_VERIFIED` |
| repository | `single_file` | `NOT_VERIFIED` |
| repository | `statuses` | `NOT_VERIFIED` |
| repository | `vulnerability_alerts` | `NOT_VERIFIED` |
| repository | `workflows` | `NOT_VERIFIED` |
| organization | `custom_properties_for_organizations` | `NOT_VERIFIED` |
| organization | `members` | `NOT_VERIFIED` |
| organization | `organization_administration` | `NOT_VERIFIED` |
| organization | `organization_custom_roles` | `NOT_VERIFIED` |
| organization | `organization_custom_org_roles` | `NOT_VERIFIED` |
| organization | `organization_custom_properties` | `NOT_VERIFIED` |
| organization | `organization_copilot_seat_management` | `NOT_VERIFIED` |
| organization | `organization_copilot_agent_settings` | `NOT_VERIFIED` |
| organization | `organization_copilot_requests` | `NOT_VERIFIED` |
| organization | `organization_external_properties_for_repos` | `NOT_VERIFIED` |
| organization | `organization_announcement_banners` | `NOT_VERIFIED` |
| organization | `organization_events` | `NOT_VERIFIED` |
| organization | `organization_hooks` | `NOT_VERIFIED` |
| organization | `organization_personal_access_tokens` | `NOT_VERIFIED` |
| organization | `organization_personal_access_token_requests` | `NOT_VERIFIED` |
| organization | `organization_plan` | `NOT_VERIFIED` |
| organization | `organization_projects` | `NOT_VERIFIED` |
| organization | `organization_packages` | `NOT_VERIFIED` |
| organization | `organization_secrets` | `NOT_VERIFIED` |
| organization | `organization_self_hosted_runners` | `NOT_VERIFIED` |
| organization | `organization_user_blocking` | `NOT_VERIFIED` |
| account | `email_addresses` | `NOT_VERIFIED` |
| account | `followers` | `NOT_VERIFIED` |
| account | `git_ssh_keys` | `NOT_VERIFIED` |
| account | `gpg_keys` | `NOT_VERIFIED` |
| account | `interaction_limits` | `NOT_VERIFIED` |
| account | `profile` | `NOT_VERIFIED` |
| account | `starring` | `NOT_VERIFIED` |
| enterprise | `enterprise_custom_properties_for_organizations` | `NOT_VERIFIED` |

**Contrôle du double catalogue :** conserver `100 candidats historiques` + `80 rubriques REST` + `57 champs de schéma d'émission de jetons` séparément ; une correspondance d'intitulé ou de champ technique est **documentation**, pas `GRANTED`. Le nombre des références distinctes ne représente pas le nombre officiel total de permissions qu'il serait possible d'activer.


## 12. Sources spécialisées GitHub — permissions absentes des deux index généraux

**État documentaire :** `OFFICIAL_SPECIALIZED_REFERENCE_NOT_GRANT` (22 octobre 2026). Ces cinq candidats historiques n'avaient de correspondance littérale ni au § 10 (80 rubriques REST générales) ni au § 11 (57 paramètres de jeton). Une recherche dans **la documentation des fonctionnalités spécialisées** permet toutefois d'identifier leur intitulé officiel, avec les restrictions propres à leur API ou abonnement.

| Portée | Candidat historique | Source GitHub officielle | Condition d'exploitation constatée |
| --- | --- | --- | --- |
| `repository` | `agent_tasks` | https://docs.github.com/en/rest/agent-tasks/agent-tasks | `UAT_ONLY_COPILOT_BUSINESS_OR_ENTERPRISE_SUBSCRIPTION` |
| `repository` | `license_compliance_alerts` | https://docs.github.com/en/webhooks/webhook-events-and-payloads | `WEBHOOK_SUBSCRIPTION_REQUIRES_PERMISSION` |
| `repository` | `repository_license_policy` | https://docs.github.com/en/enterprise-cloud@latest/rest/authentication/permissions-required-for-github-apps | `ENTERPRISE_CLOUD_API_AVAILABILITY_REQUIRES_CHECK` |
| `repository` | `secret_scanning_alert_dismissal_requests` | https://docs.github.com/en/enterprise-cloud@latest/rest/secret-scanning/alert-dismissal-requests | `SEPARATE_CONTENTS_ALERT_AND_REVIEW_AUTHORITY_REQUIREMENTS` |
| `repository` | `secret_scanning_push_protection_bypass_requests` | https://docs.github.com/en/enterprise-cloud@latest/rest/secret-scanning/delegated-bypass | `DELEGATED_BYPASS_PERMISSION_AND_REVIEW_ROLE_REQUIRED` |

**Points techniques à ne pas confondre :**

- `agent_tasks` concerne la **tâche de l'agent cloud Copilot**, en aperçu public selon la documentation ; `UAT` est admissible mais **`IAT` n'est pas pris en charge** pour les endpoints indiqués, et certaines opérations exigent un abonnement Copilot Business/Enterprise. Cette permission est **optionnelle** et ne rend **pas** Codex/Copilot obligatoire pour ChainSolutions Universal Gateway.
- `license_compliance_alerts` apparaît notamment dans les conditions d'abonnement au webhook `dismissal_request_license_compliance` ; cela ne prouve pas que notre installation est abonnée ou éligible.
- `repository_license_policy` figure dans les références GitHub Enterprise Cloud pour les contrôles de licences ; vérifier produit, plan et ressource.
- Les demandes de rejet d'alertes ou de contournement de protection de secrets exigent des combinaisons de permissions/roles et des paramètres de délégation ; **aucune demande n'est approuvée par le seul fait d'avoir le droit de la consulter**.

**Statut des cinq candidats :** présence dans une documentation GitHub spécialisée, **pas** preuve de permission configurée, accordée, disponible sur nos trois espaces, exercée via notre App ou politiquement autorisée. Le niveau historique `write` n'est pas nécessairement applicable aux API en lecture seule.



## 13. Alias fonctionnels GitHub App prouvés par leurs endpoints — hors libellés exacts

**Date :** 22 octobre 2026. **Statut :** `OFFICIAL_GITHUB_APP_ENDPOINT_ALIGNED_HISTORICAL_PARAMETER_NOT_GRANT`.

Les candidats ci-dessous n'avaient pas de correspondance **littérale** dans les 80 rubriques REST ni parmi les 57 noms de paramètres de jeton. Ils correspondent néanmoins à des **capacités GitHub App documentées** par les endpoints officiels et le nom historique issu du paquet d'inscription. Pour ces entrées, `documentation_app_endpoint=true` n'implique **pas** `permission_parameter_exact_name_currently_confirmed`, `configured`, `granted` ou `runtime_probed`.

| Portée | Paramètre candidat historique | Libellé officiel de capacité | Type de jeton pris en charge | Source GitHub |
| --- | --- | --- | --- | --- |
| `account` | `blocking` | Block another user | `UAT` uniquement sur les endpoints utilisateur | https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps |
| `organization` | `organization_actions_variables` | Variables | `UAT` ou `IAT` avec permission d'organisation `Variables` | https://docs.github.com/en/rest/actions/variables |

**Preuve complémentaire :** la documentation officielle sur l'URL d'enregistrement d'une GitHub App illustre explicitement `blocking=read` (https://docs.github.com/en/apps/sharing-github-apps/registering-a-github-app-using-url-parameters). Le nom historique `organization_actions_variables` apparaît également dans le tableau des permissions fines GitHub, mais ce tableau concerne les PAT et **ne suffit pas seul** à prouver un paramètre configurable d'une GitHub App ; le rapprochement retenu concerne la capacité **Variables** dont les endpoints confirment l'utilisation par IAT/UAT.

**Contrat d'exploitation :** aucune de ces deux opérations ne peut être appelée par un agent sans la preuve d'autorisation et de permission effective ; `blocking` est de plus une opération personnelle sensible, jamais déclenchée depuis une instruction issue d'un commentaire non fiable.

