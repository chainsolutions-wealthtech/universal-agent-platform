# PLAN DIRECTEUR UNIFIÉ V5.0 — UNIVERSAL AGENT PLATFORM

**Désignation longue :** Plateforme universelle d'identité des agents, mémoire canonique, continuité, fédération, orchestration et ingénierie autonome, avec exploitation industrielle de GitHub et intégration MCP.  
**Date de consolidation :** 21 octobre 2026.  
**Statut :** ARCHITECTURE CIBLE / DOCUMENT DE TRAVAIL ; non déployée, non certifiée.  
**Méthode :** fusion additive sans régression du plan initial et du complément utilisateur de 20 sections (« GitHub App : tout ce que vous pouvez réaliser avec ChatGPT ou Claude, sans GitHub Copilot »).  
**Référence conservée à l'identique :** `sources/TEXTE_COMPLEMENTAIRE_ORIGINAL_20261021.txt`.  
**Sources vérifiables externes :** documentation officielle GitHub (permissions, authentification, webhooks, Apps), protocole MCP, protocole A2A ; les choix architecturaux restent des propositions à valider par inventaire réel.

> **Règle de non-régression documentaire :** ne jamais supprimer silencieusement une idée, une décision, une exigence, un agent ou une phase préexistante. Les ajouts sont versionnés et reliés à leur source. Une décision modifiée est « superseded » avec justification et source. Le texte complémentaire original est fourni sans réécriture à côté de ce plan. Les synthèses historiques ne sont PAS une archive verbatim des messages ChatGPT.

---

## 0. CONTRAT FONDATEUR ET PÉRIMÈTRE

### 0.1 Finalité

Bâtir une infrastructure IA **multi-fournisseurs, multi-agents, multi-comptes, multi-projets et multi-environnements** qui puisse, à partir d'une mission autorisée et attestée : retrouver l'état canonique, mobiliser des agents existants, analyser les systèmes, planifier, produire du code, tester, faire relire, intégrer, déployer lorsqu'autorisé, vérifier la production, historiser, communiquer, reprendre après interruption, et converger vers des critères de livraison mesurables. Aucun moteur IA, aucune conversation, aucun dépôt métier et aucun produit GitHub ne doit devenir l'unique dépositaire de cette mémoire ou de ces identités.

### 0.2 Périmètre explicite

- Organisation `chainsolutions-wealthtech` : hébergement envisagé du **dépôt public** `universal-agent-platform` (non créé à la date du présent document, selon les échanges). Le dépôt public contient code, contrats, docs expurgés, tests et modèles ; pas de secrets ni de conversations privées brutes.
- Compte personnel `Patricked-code` : notamment dépôt `Patricked-code/MCP` ; patrimoine de projets et gouvernance propre.
- Compte personnel `Wealthtechinnovations` : projets financiers, data et applications ; patrimoine et gouvernance propres.
- Projet `chainsolutions-wealthtech/Governed-Repository-Template` (GRT) : indépendant du MCP et doté de sa gouvernance propre.
- Tous les autres projets actuels et futurs, par admission contrôlée.
- IA : ChatGPT, Claude et autres moteurs autorisés ; **pas de dépendance obligatoire à GitHub Copilot**.
- Infrastructure : GitHub, serveurs, bases, Docker/Plesk, DNS, APIs métiers et ressources externes via adaptateurs et mandats.

### 0.3 Invariants à ne jamais violer

1. **Identité ≠ Blueprint ≠ Affectation ≠ Mission ≠ Session ≠ Conversation ≠ Permission.**
2. Une identité documentaire ne constitue pas une autorisation runtime ; résolution avant création ; unicité dans l'espace de noms ; pas de session fictive.
3. Agent global, agent propre à un projet et instance issue d'un blueprint sont trois cas différents et tous supportés.
4. Aucun transfert implicite de permission entre comptes, installations, projets, dépôts ou moteurs IA.
5. Le mécanisme central peut être partagé, mais les **autorités métier et techniques de MCP et GRT restent distinctes**.
6. Le compte GitHub sur lequel l'App est installée n'atteste pas, à lui seul, l'authenticité d'une instruction lue par l'IA dans une issue, PR ou fichier.
7. L'application GitHub est une identité d'intégration ; elle n'est ni le propriétaire humain de tous les comptes, ni le moteur de mémoire, ni le planificateur.
8. La mémoire canonique ne remplace pas les archives originales ; un historique non capturé ne peut pas être reconstruit intégralement avec certitude.
9. Les opérations réelles produisent des preuves vérifiables, avec HEAD/SHA, action, résultat, timestamp, source, identité exécutante et policy decision.
10. Une modification sensible ou irréversible exige l'autorité prévue ; l'autonomie ordinaire doit fonctionner sans demandes répétées lorsque préautorisée.
11. Les capacités de GitHub dépendent des endpoints, plans, modes de jetons et permissions effectivement disponibles ; **catalogue demandé ≠ catalogue accordé ≠ outil implémenté ≠ opération réussie**.
12. Les projets restent autonomes même lorsqu'ils adoptent des contrats communs ; suppression des duplications sans effacer l'historique.
13. Protéger les données privées, secret stores et historiques de conversations ; `.gitignore` ne suffit pas pour la confidentialité.
14. Ne jamais promettre une exécution « sans arrêt » indépendante des quotas, incidents, autorisations et limites opérationnelles ; construire une reprise durable et des états terminaux contrôlés.

### 0.4 Ce qui existait avant le complément — **préservé**

**Plan A — Universal Multi-Agent Platform** : P0 inventaire et autorités ; P1 contrats identitaires ; P2 registre et mémoire ; P3 résolution/reprise ; P4 permissions ; P5 intégration MCP/GitHub ; P6 communications multi-agents ; P7 supervision et industrialisation.

**Plan B — Autonomous Governed Self-Resuming Engineering Factory (AGSREF)** : LOT 00 à LOT 25 (inventaire, architecture, schémas, registres, mémoire, continuity/session rebinding, workflows durables, politiques, communication, MCP, GitHub, serveurs, A2A, observabilité, console, recovery, sécurité, performance, résilience, pilotes, docs, vérification indépendante, livraison/exploitation). Les 26 lots ne sont pas supprimés ; ils sont détaillés et complétés ci-dessous.

**Plan C — GitHub App & Bootstrap** : paramétrage d'une App propriétaire sous `chainsolutions-wealthtech`, installable « Any account » sur les trois espaces, accès `All repositories` lorsque explicitement choisi, quatre catégories de permissions, broker d'authentification, repository public, intégration MCP, webhooks et contrôles. Les versions précédentes du bootstrap V1–V4 restent historiques ; elles ne valent pas certificat de permissions valides.

**Plan D — NOUVEAU / GitHub Full-Capability Automation** : référentiel des capacités, couverture API REST/GraphQL/Git, intégration Projects/Actions/Issues/PR, pilotage inter-dépôts, sécurité, déploiements, produits GitHub additionnels, comptes utilisateur, organisations, Enterprise lorsque disponible, mesure, audit et découverte continue. Les 20 sections et 30 domaines du complément sont conservés, cartographiés et intégrés en annexe.

---

## 1. DÉCOMPOSITION DE LA PLATEFORME (CIBLES LOGIQUES)

### 1.1 Couche expérience et accès

Clients ChatGPT, Claude, autres LLM, CLI, console web, agents hébergés et API externes se connectent à un **AI Provider Gateway** et à un **Entry/Resume API**. Chaque appel possède une identité initiatrice prouvée, une source, un projet, une mission, une trace et un contexte de conformité. Aucun client IA n'accède directement aux clés maîtres de la GitHub App.

### 1.2 Global Identity & Capability Control Plane

- Organisation, espaces de confiance, projets, dépôts, agents, alias, blueprints, compétences, affectations, mandats, politiques, installations et outils.
- Résolveur d'identité avec recherche par ID canonique, alias, projet et source ancre ; rejet des ambiguïtés et interdiction des doublons concurrents.
- Catalogue des capabilities avec `capability_id`, catégorie, endpoint/protocole, scopes vérifiés, type de jeton, plan, feature-flag, entitlements et tests de conformance.
- Politique contextuelle de délégation : acteur, agent, mission, compte GitHub, dépôt, branche, action, intervalle temporel, état du workflow et ressources disponibles.

### 1.3 Canonical Memory & Conversation Capture Plane

- Archive immuable ou à intégrité vérifiable des conversations **effectivement capturées** ; métadonnées (source, conversation_id, message_id, ordre, horodatage d'origine si connu, pièces jointes référencées, empreintes).
- Extracteur des idées, exigences, contraintes, décisions, objections, hypothèses, travaux, checkpoints, preuves, risques et NEXT_ACTION.
- Canonical memory ledger avec `claim_id`, provenance, état, confiance, supersession/ancestry, projection courante et politiques de rétention.
- `canonical-memory-verifier` = vérificateur en lecture seule de bundles sélectionnés ; **pas** collecteur universel ni validateur automatique de véracité des faits.
- Sémantique de mémoire par niveau : global identitaire, compétences approuvées, projet, mission, session, archive brute protégée.

### 1.4 Orchestration, communication et exécution

- Orchestrateur durable : DAG de lots/tâches, réservations, leases, retries plafonnés, files durables, idempotence, compensations, deadlines, budgets, priorités, états terminal/blocked.
- Agent Communication Bus : messages corrélés, routage, accusés, déduplication, dead-letter queues, reprise, transports internes et adaptateur A2A si utile ; ne pas déplacer le bus existant MCP sans audit.
- GitHub Capability Gateway : App API, broker JWT/installation/user tokens, REST, GraphQL, Git, webhooks signés, observabilité et orchestration des capacités.
- Infrastructure Gateway : MCP existant, adaptateurs serveurs, Docker, Plesk, API, données, DNS, déploiements; séparation de l'autorisation GitHub et de l'accès serveur.

### 1.5 Quality/Policy/Audit Planes

- Qualité, sécurité, CI, tests, contrôles de HEAD, anti-régression, évaluations multi-IA, replay d'incidents et preuves.
- Un contrôleur indépendant vérifie les livrables ; les validations déterministes sont prioritaires aux auto-évaluations d'un modèle.
- Observabilité transverse : CloudEvents pour événements structurés (si adopté), OpenTelemetry pour corrélation de traces, coût LLM, occupation workers, latences, intégrité, conformité et incidents.

### 1.6 Stockages séparés

| Objet | Stockage cible | Raison |
|---|---|---|
| Code, contrats, docs publics, ADR expurgés | GitHub public `chainsolutions-wealthtech/universal-agent-platform` | Transparence, révision et CI |
| Registres d'état / projections | PostgreSQL ou autre base transactionnelle | Transactions et concurrence |
| Événements, inbox/outbox, idempotency keys | Base durable append-only / queue | Reprise et livraison fiable |
| Conversations brutes, artefacts sensibles | Chiffrement + object store privé | Confidentialité et volumes |
| Secrets, clés privées, tokens | Secret manager / KMS | Rotation et révocation |
| Index de recherche sémantique | Service indexé avec ACL | Retrieval par autorisation |
| Attestations / manifestes de preuves publics | GitHub, selon classification | Audit et provenance |
| Archives réglementées / données personnelles | Stockage à rétention et effacement contrôlés | Gouvernance des données |

---

## 2. MODÈLE CANONIQUE ET RELATIONS

### 2.1 Schéma d'identifiants et cardinalités

- `organization_id` → possède 0..N `project_id` ; chaque projet a 0..N `repository_binding` (un dépôt peut être partagé par plusieurs projets selon règle).
- `agent_id` → 1..N versions d'`agent_blueprint_id` compatibles ; un agent a 0..N `assignment_id`.
- `assignment_id` → lie agent, projet, périmètre, rôles et autorités ; permissions non héritées d'une autre affectation.
- `mandate_id` → objectifs, limites et délégation ; 1..N `mission_id`, 0..N `policy_grant_id`.
- `mission_id` → 0..N `task_id`, 0..N `continuity_id` ; les tâches forment un DAG versionné.
- `continuity_id` → 0..N `session_id`, `conversation_binding_id`, `checkpoint_id`, `handoff_id`, `event_id`.
- `execution_id` → 1 tâche et 1 agent exécutant ; peut contenir sous-appels outils, status, attestation, budget et coût.
- `source_ref` → URI/commit SHA/issue/PR/message/artifact + empreinte, provenance et autorité ; jamais un texte libre censé prouver une approbation.
- `installation_id` → compte GitHub précis, ensemble de dépôts, permissions effectives, dernière vérification et révocations connues.
- `api_capability_id` → endpoint REST/GraphQL/transport Git, types de jetons et états d'accès testés.

### 2.2 Identités et rôles

Une GitHub App peut faire une requête comme App (JWT), comme installation (IAT) ou comme utilisateur (UAT/OAuth). Ces modes ne sont pas substituables. Une organisation GitHub ne devient pas copropriétaire de l'enregistrement d'une App simplement en l'installant ; elle administre son installation selon les règles GitHub. Un agent conversationnel ne devient pas propriétaire humain du compte par sa connexion.

Un agent logique peut survivre à son moteur IA : une mission commencée sous Claude peut être poursuivie par ChatGPT après résolution et vérification, avec nouvelle session d'exécution, mais la même identité logique et la même continuité.

### 2.3 Machines à états proposées

Agent: `DRAFT → DISCOVERED → ADMITTED → ACTIVE → SUSPENDED → ARCHIVED → REVOKED` (transitions gouvernées).  
Mandate: `PROPOSED → VERIFIED → GRANTED → ACTIVE → EXPIRED/REVOKED`.  
Task: `PLANNED → READY → CLAIMED → RUNNING → VERIFYING → DONE`, et branches `RETRY_WAIT`, `BLOCKED_AUTHORITY`, `BLOCKED_EXTERNAL`, `FAILED_RECOVERABLE`, `FAILED_TERMINAL`, `CANCELLED`.  
Memory claim: `CAPTURED → EXTRACTED → REVIEWABLE → VERIFIED/SUPERSEDED/REJECTED`, la vérité factuelle restant distincte de la conformité du bundle.  
GitHub capability: `DESCRIBED → DOCUMENTED → CONFIGURED → AUTHORIZED → PROBED → VERIFIED_AVAILABLE → ENROLLED`, avec `UNAVAILABLE`, `REVOKED`, `DEPRECATED`.

### 2.4 Événements essentiels

`agent.registered`, `agent.resolved`, `assignment.changed`, `mandate.granted/revoked`, `task.claimed/started/completed/failed`, `checkpoint.created`, `continuity.resumed`, `message.received/acknowledged`, `github.installation.changed`, `github.permission.changed`, `github.workflow.completed`, `github.pr.merged`, `deploy.verified`, `memory.claim.superseded`, `incident.opened/resolved`. Chaque événement = ID stable + timestamp origine et ingestion + source + correlation_id + actor + payload versionné + signature/empreinte lorsque requis.

---

## 3. MÉMOIRE, CAPTURE ET CONTINUITÉ DEPUIS N'IMPORTE QUELLE IA

### 3.1 Architecture de capture

**Connecteur source → réception signée/authentifiée → normalisation → déduplication → chiffrement et archivage brut → extraction de propositions → résolution des références → projection canonique → vérification → indexation gouvernée → checkpoint.**

Chaque connecteur doit déclarer sa couverture : historique complet, messages futurs, exports manuels, pièces jointes, timestamp exact, auteur, tool calls, streaming, rétention, limites fournisseur. Aucun connecteur ne peut prétendre capturer une donnée non exposée par l'API ou le produit. Import historique et capture live sont deux voies distinctes.

### 3.2 Préservation de la chronologie

- La capture brute est append-only au niveau logique et hashée ; rectifications en événements successeurs ; effacement réglementaire géré avec tombstones appropriés.
- Les décisions reçoivent `decision_id`, source, autorité, statut `proposed/accepted/superseded/rejected`, liens parents/enfants, date observée et justification.
- Un plan n'écrase jamais l'ancien : versionnement, diff, change log, supersession et identifiant stable des exigences.
- Les idées non retenues restent retrouvables comme hypothèses/propositions et non décisions.
- Une date ou un auteur absent est indiqué `unknown`, pas reconstitué par supposition.

### 3.3 Contrat de reprise canonique

`RESOLVE_PROJECT → RESOLVE_AGENT → VERIFY_ASSIGNMENT → LOAD_CANONICAL_STATE → RECONCILE_RUNTIME → VERIFY_LIVE_PERMISSIONS → BIND_CONVERSATION → CLAIM_NEXT_TASK → RESUME_OR_BLOCK → WRITE_CHECKPOINT`.

Une nouvelle conversation fournit un `conversation_binding` ; elle n'usurpe pas l'ID d'une session de processus et ne crée pas automatiquement une identité. Les états enregistrés sont confrontés au HEAD courant des dépôts, aux PR/issues et aux autorisations actuelles ; aucun checkpoint historique n'octroie le droit d'exécuter quoi que ce soit.

### 3.4 Mémoire et confidentialité

- Programme public : architecture et exigences publiables, décisions expurgées.
- Conversations ChatGPT/Claude : données privées par défaut, exportables selon consentement, ACL et contraintes d'usage.
- Données de projets : cloisonnées et régies par gouvernance locale.
- Promotion de compétences transverses uniquement après revue, anonymisation et autorisation.
- Pas de clé, token, secret, fichier `.env` ou données personnelles dans l'historique Git public ; scanning de secrets avant commit et en CI.

### 3.5 Vérificateur canonique

Le plugin `canonical-memory-verifier` vérifie un bundle explicitement désigné en lecture seule, sa structure, ses sources déclarées, les remplacements et ambiguïtés ; il ne capture pas de conversations, ne fournit pas d'approbations live et ne confirme pas par lui-même la véracité de tous les faits. Prévoir adaptateur de format, tests de bundle valide/invalide et politique de non-consommation des bundles invalides.

---

## 4. PLATEFORME MULTI-IA ET COMMUNICATION INTERAGENTS

### 4.1 Abstraction de fournisseur IA

Contrat commun `ProviderAdapter`: `discover_capabilities`, `create_execution`, `resume_execution` si supporté, `call_model`, `stream_events`, `invoke_tool`, `get_usage`, `cancel`, `health`. Les capacités réellement exposées par ChatGPT/Claude/autres doivent être inventoriées ; certaines ne permettent pas un contrôle programmatique complet ou un accès à tout l'historique.

Ne pas copier les secrets entre agents ; réserver les appels GitHub au broker; injecter données documentaires comme données non fiables, jamais comme instructions propriétaires. Séparer prompt de mission, instructions du système, contenus de dépôts et commentaires externes.

### 4.2 Interopérabilité

- **MCP** : couche d'outils et ressources ; votre projet `Patricked-code/MCP` pourra être un fournisseur d'outils, sans devenir source de vérité globale par défaut.
- **A2A** : interopérabilité agent-agent entre services indépendants, via adaptateur et authentification ; ne l'installer que si elle apporte des capacités pertinentes, sans doubler votre bus existant.
- Bus interne : enveloppe `message_id`, `source_actor`, `destination_actor`, `project_id`, `mandate_id`, `correlation_id`, `causation_id`, `expires_at`, `payload_ref`, `ack`, `retry_count`, politique de déduplication et de priorité.

### 4.3 Collaboration et concurrence

Des agents de moteurs différents peuvent travailler sur la même mission à des étapes séparées, avec révisions indépendantes. Un `task_claim` doit être exclusif si la ressource est mutable, expirer, et être réconcilié à chaque changement de session. Les branches et PR doivent porter des références de mission sans prétendre représenter l'identité runtime d'un fournisseur.

### 4.4 Agent reuse

Un blueprint générique `CODE_ENGINEER` peut produire plusieurs agents distincts pour différents projets, ou un même `agent_id` peut posséder plusieurs affectations ; ces deux stratégies ne doivent pas être fusionnées automatiquement. Les agents historiques ATLAS, FORGE, AUTO-INTAKE/BUS et AUDIT_SUPERVISOR sont des **cas d'intégration pilotes** : ne pas reconstruire leurs identités ni déplacer leur mémoire avant une réconciliation probante de leurs autorités.

---

## 5. GITHUB APP : MODÈLE D'ACCÈS, PERMISSIONS ET MODES D'AUTHENTIFICATION

### 5.1 Modèle d'application

Nom provisoire `ChainSolutions Universal Gateway`, App appartenant à `chainsolutions-wealthtech`, installable `Any account` ; installations distinctes sur les trois espaces. Sélection `All repositories` envisagée pour couvrir les projets futurs, sous réserve d'acceptation ; cela n'étend pas les permissions de l'App au-delà des niveaux approuvés. La création de la GitHub App ne crée pas le repository `universal-agent-platform`.

**Les droits disponibles doivent être définis en quatre états :** `REQUESTED`, `GRANTED_BY_INSTALLATION/USER`, `RUNTIME_PROBED`, `POLICY_ALLOWED`. Une capacité ne devient `READY` que si tous ces tests réussissent.

### 5.2 Trois modes d'authentification

| Mode | Preuve | Usage | Limitations |
|---|---|---|---|
| App-level JWT | Clé privée et App ID | Gestion de l'app / création de jetons d'installation | Pas un accès générique au code d'un dépôt |
| Installation Access Token (IAT) | Installation sur un compte | Repos, organisation et automatisations sans intervention utilisateur pour endpoints compatibles | Permissions plafonnées par App et installation |
| User Access Token (UAT/OAuth) | Autorisation d'un utilisateur | Fonctions de compte et endpoints agissant au nom d'un utilisateur | Permissions intersectées avec celles du compte utilisateur |

Les jetons et clés sont hébergés dans un secret manager, jamais fournis aux modèles ni stockés dans Git. Émission de jetons de portée réduite quand l'API le permet, rotation, traces et révocation. Ne pas supposer la possibilité de créer un GitHub Project avec n'importe quel type de jeton sans test GraphQL spécifique.

### 5.3 Quatre familles de permissions

| Famille | Ressources | Conditions |
|---|---|---|
| Repository | Contents, Issues, PR, Actions, Workflows, Checks, Security, Packages, Pages, Deployments, administration, agent tasks, etc. | App installée avec repos accessibles |
| Organization | Projects v2, membres, runners, properties, issues types/fields, config, sécurité, etc. | Installation sur une organisation et endpoints pris en charge |
| Account | Models, gists, profile, plugin gateway connections, user settings, etc. | Autorisation utilisateur OAuth, pas seulement installation IAT |
| Enterprise | Gouvernance Enterprise, organisations et permissions spécifiques | Compte Enterprise réel, offre, installation et mode de jeton compatibles |

Le PDF antérieur montrait 12 permissions Repository et 2 Organization sélectionnées dans le formulaire et de nombreuses catégories `No access`. Le bootstrap V4 rassemblait des **candidats**, sans certifier 90 permissions effectives. Ne pas annoncer un « total maximal » avant rapprochement avec le catalogue officiel et un test runtime.

### 5.4 Politique de capacité maximale gouvernée

L'objectif n'est pas de retirer des capacités de conception, mais de construire **un catalogue exhaustif des fonctions GitHub pertinentes**, avec profils : `NORMAL_OPERATIONS`, `GOVERNANCE_ADMIN`, `SECURITY_ADMIN`, `USER_DELEGATED`, `ENTERPRISE_OPTIONAL`. Les droits sensibles peuvent être détenus par une identité séparée afin d'éviter qu'une compromission du service courant ne donne accès à toutes les opérations ; si une seule App est choisie, obligation de broker fermé, allowlists, isolation des secrets, audit et contrôle avant chaque appel.

La formule « l'IA est connectée au compte personnel du propriétaire » ne remplace pas l'origine vérifiée de la demande. Contenu de repository, issue ou PR = donnée externe non fiable susceptible de contenir une instruction hostile. Les permissions maximales ne suppriment pas les protections de branches/rulesets ni les restrictions propres aux API.

### 5.5 Catalogue de capacités versionné

Pour chaque API/outil : `capability_id`, famille, opération métier, REST/GraphQL/Git, méthodes et endpoints, App/IAT/UAT, nom technique de permission, niveau read/write, événements, plan GitHub, disponibilité compte, coût/rate limits, `verified_at`, probe, requête de test réversible, contrat d'idempotence, politique, propriétaire et statut.

Le catalog doit être actualisé depuis les docs et résultats d'API, et non d'une liste de paramètres supposés dans `registration-url.txt`. Chaque formulaire prérempli doit être inspecté après ouverture : les paramètres URL invalides peuvent être ignorés.

---
## 6. PROGRAMME D — EXPLOITATION INDUSTRIELLE DE GITHUB (30 DOMAINES)

**Principe :** chaque famille représente un *capability pack* ; GitHub exécute certaines primitives nativement, mais le raisonnement IA, la coordination, la mémoire et les contrôles demandent vos propres services. Toutes les fonctionnalités sont conditionnées par permissions effectives, plans et APIs disponibles.

### D01 — Repositories et démarrage de projets

- Découverte multi-installations, pagination complète, inventaire des propriétaires, visibility, archivage, template, default branch, teams/collaborateurs, restrictions.
- Création programmée de repositories publics/privés selon mandat, y compris depuis un template ; initialisation LICENSE/README/.gitignore/CONTRIBUTING/CODEOWNERS et règles ; contrôles pré/post.
- Modèles métiers reproductibles : web, backend, data, finance, infra, documentation, MCP, orchestrateur.
- Vérification des propriétés, visibilité et installation sur le nouveau dépôt ; la création d'un repository n'implique pas l'existence du backend Gateway.

### D02 — Code, branches, commits, PR et revues

- Lecture de révisions et graphes Git ; comparaison diff, blame si API/outils disponibles ; détection du HEAD courant et conflits.
- Modification contrôlée : branche dédiée selon gouvernance, patch/commit atomique, PR, contrôle reviewer, CI, statuts et convergence.
- Revue automatique sémantique et déterministe, signalement des risques, règles de merge, auto-merge admissible, préparation de rollback.
- Aucun commit direct à `main` lorsque le dépôt l'interdit ; pas de suppression ou de reset forcé sans mandat précis.

### D03 — Issues, sous-issues, dépendances, GitHub Projects

- Intake événementiel, dédoublonnage d'issues, classification, labels, priorisation, assignation, hiérarchies et liens vers PR/commits.
- Projects nouvelle génération : création/lecture/mutations GraphQL testées, status, custom fields, views selon capacités disponibles, roadmap et synchronisation.
- GitHub stocke la représentation visible des tâches ; le moteur durable possède les leases, collisions, idempotency keys et la vérité d'exécution.

### D04 — GitHub Actions, Checks, statuts et CI/CD

- Lire/créer workflows YAML via permissions Contents+Workflows, `workflow_dispatch`, rerun/cancel, runs, jobs, logs et artefacts suivant endpoints autorisés.
- Scripts runner/CI et vérifications par matrice de versions ; détecter flakiness, lenteur, régressions, dépendances obsolètes et permissions surdimensionnées.
- Générer checks et statuts corrélés à `task_id` et `trace_id` ; échec CI → incident/diagnostic → correctif en PR → re-test.
- Réduire le risque supply-chain : pin d'actions, validation des workflows modifiés et sandbox des PR non fiables.

### D05 — Sécurité, conformité et supply chain

- SAST/code scanning, Dependabot alerts, secret scanning, security advisories, attestations, provenance, code quality, SBOM, dépendances et permissions.
- Séparer capacité d'observer les alertes de capacité de les fermer, ignorer ou contourner : audit visible, approbations adaptées, suppression des secrets réellement exposés.
- Un secret Actions peut être géré avec API compatible, mais sa valeur existante ne peut pas être récupérée en clair.
- Scanner les commits, PR, images Docker, packages et scripts d'infrastructure ; expliquer toute exception.

### D06 — Administration GitHub et conformité configuration

- Inventaire et comparaison de repository settings, rulesets, branch protection, CODEOWNERS, merge policies, environments, pages, visibilité, webhooks et restrictions.
- Détection des écarts de configuration ; correction gouvernée et réversible avec snapshots ; ne pas désactiver une protection pour faciliter la CI.
- Organization : Teams/Members, projects, properties, issues taxonomy, runners, variables/secrets selon endpoints et types de jetons ; pas de pouvoir organisationnel implicite sur deux comptes personnels.

### D07 — Déploiements, Infrastructure et publications

- Releases, tags, changelogs, packages, Pages et environnements GitHub ; intégration actions/runners à Docker, VPS, Plesk, DNS, DB et monitoring externe.
- GitHub n'accorde aucun droit SSH/DB/serveur par lui-même : recours à `Patricked-code/MCP` et adaptateurs supplémentaires avec mandats techniques distincts.
- Contrôle des versions déployées, HEAD et SHA, health HTTP, rollback testé, prévention double-déploiement et vérification post-deploy.

### D08 — Webhooks et architecture événementielle

- Récepteur HTTPS + signature HMAC GitHub + secret stocké hors Git + journal de delivery, déduplication `X-GitHub-Delivery`, classification event/action.
- ACK rapide, outbox/inbox transactionnelles, queue durable, retries avec backoff, dead-letter queue, corrélation, replay autorisé, contrôle du traitement non fiable.
- Flux : issue ouverte → intake ; PR ouverte → revue ; workflow failed → analyse ; PR merged → release ; security alert → incident ; installation changed → permission revalidation.
- Observer seulement les événements utiles ; le catalogue d'événements doit être audité selon l'installation réelle.

### D09 — Produits et espaces GitHub additionnels

- `Codespaces`, `Packages`, `Pages`, `Gists`, `Discussions`, `GitHub Models`, `Agent tasks`, `Agent variables`, `Agent secrets`, `Copilot` et fonctions de sécurité suivant disponibilité.
- **Sans Copilot obligatoire** : les fonctionnalités d'Agent Apps/Copilot sont facultatives ; aucun agent ChatGPT/Claude n'en dépend pour exister.
- Account-scoped features utilisent un jeton utilisateur autorisé lorsque nécessaire ; ne pas essayer d'utiliser un IAT pour tout.
- Enterprise uniquement si un compte Enterprise approprié est réellement détecté et installé ; pas de droits fictifs.

### D10 — Portefeuille multi-repositories et analytics

- KPIs : incidents, PR, lead time, cycle time, failed builds, pass rate, bug recurrence, tests flakiness, couverture, cadence, livraisons, supply chain, risque et coût IA.
- Analyse transversale avec sources attestées et fraîcheur, tableaux de bord par installation/projet/agent, historique et piste d'audit.
- Nombre d'agents actifs = sessions prouvées par heartbeats, pas simple observation de commits.

### D11 — Migration et transformation des projets

- Détection/plan de migration d'architecture, bibliothèques, conventions et dépendances ; contrôles de compatibilité et non-régression.
- Distinguer migration d'identités/mémoire et migration de code/repositories ; préserver les SHAs historiques et points de reprise.
- Ne jamais déplacer MCP ou GRT dans la plateforme universelle : les intégrer par adaptateurs et contrats.

### D12 — Universal Control Center

- Console globale : installations comptes, permissions effectives, outils, agents, mandats, tâches, messages, checkpoints, PR, CI, security, déploiements, incidents et versions.
- Profils d'accès opérateur, propriétaire, reviewer, auditor ; logs et justification des décisions ; simulation de permissions et mode dry-run.
- Déclenchement d'une nouvelle mission, recherche d'agents et reprise depuis une conversation, intervention human-in-the-loop uniquement lorsqu'une autorité l'exige.

### D13 — Découverte continuelle des capacités GitHub

- Surveillance des changelogs GitHub, permissions nouvelles, endpoints, versions API et changements de plans ; classification des nouveautés et création d'une issue d'intégration.
- Test de conformance isolé, vérification du type de jeton et de la permission ; publication dans le capability registry et versionnement.
- N'augmenter les permissions de l'App qu'après réconciliation des besoins et approbation des installations concernées.

---

## 7. PIPELINE COMPLET D'INGÉNIERIE AUTONOME — 20 ÉTAPES

Cette chaîne complète le programme AGSREF initial et reprend les opérations développées dans le complément utilisateur ; elle ne présume pas que toutes les étapes sont déjà automatisées :

| N° | Opération | Acteur responsable | Preuve de passage |
|---:|---|---|---|
| 01 | Intake demande/issue/webhook | Gateway / Bus | event_id validé, source et hash |
| 02 | Résolution du projet/dépôt/mission | Registry | IDs uniques et permissions vérifiées |
| 03 | Lecture gouvernance et état | Discovery | HEAD, sources, documents d'autorité |
| 04 | Décomposition des travaux | Planner | DAG, dépendances et critères |
| 05 | Analyse d'architecture / impact | Architect | ADR et liste de risques |
| 06 | Attribution de tâche | Governance Engine | lease, assignment, mandate |
| 07 | Préparation workspace/branche | GitHub Gateway | Branche autorisée, SHA initial |
| 08 | Production code/doc/config | Engineer | Commits ou artefacts signés/référencés |
| 09 | Production et exécution des tests | Test Engineer | Suite/version, résultats et logs |
| 10 | Déclenchement des Actions | GitHub Gateway | workflow_run_id et HEAD |
| 11 | Ingestion des CI artefacts | Event Engine | Run final, logs/attestations |
| 12 | Correction des échecs | Engineer | Diff correctif et nouveaux tests |
| 13 | Revue indépendante | Reviewer | Review, anomalies, absence d'auto-approbation |
| 14 | Scan de sécurité | Security Engine | Résultats et traitement des alertes |
| 15 | Publication PR | GitHub Gateway | PR ID, branche, SHA |
| 16 | Contrôles de gouvernance | Governor/CI | Rulesets, check statuses, autorisations |
| 17 | Fusion autorisée | GitHub App | Merge SHA et décision de policy |
| 18 | Déploiement autorisé | Release/Infra Gateway | Run, cible, version, autorisation |
| 19 | Santé post-déploiement | Validator | HTTP/DB/metrics & état réel |
| 20 | Canonical checkpoint et suite | Memory + Orchestrator | Memory refs, task state, NEXT_ACTION |

**Anti-boucle :** la dernière étape se termine par `COMPLETED` lorsque les critères globaux sont satisfaits ; la plateforme ne génère pas indéfiniment du travail nouveau juste pour rester active. `BLOCKED_AUTHORITY` exige un mandat additionnel, jamais un bypass silencieux.

---

## 8. RÉSILIENCE, REPRISE ET CONCURRENCE

### 8.1 Continuité durable, hors processus conversationnel

Le programme fonctionne via un **service orchestrateur persistant indépendant des sessions modèles** : workers relançables, scheduler durable, watchdog externe, jobs versionnés, outbox/inbox et journaux. Les callbacks provider ne sont que des moyens d'exécution temporaires. Toute étape a un point d'arrêt persistant. Il n'est pas honnête de présenter une simple conversation ChatGPT/Claude comme un runtime permanent.

### 8.2 Idempotence et external side effects

Chaque action reçoit un `idempotency_key` et un enregistrement de tentative. Avant retry d'une mutation GitHub, réconcilier l'objet cible (branche, fichier SHA, issue, PR, workflow, déploiement). Les APIs externes ne garantissent pas toutes exactement-une-fois ; viser traitement effectif sans duplication par réconciliation transactionnelle et compensation.

### 8.3 Conflits et concurrence

- `optimistic_lock` sur projections et HEAD Git ; leases renouvelables sur tâches et ressources critiques ; fencing token/sequence pour empêcher les anciens workers de committer.
- Plusieurs agents peuvent analyser ; un seul détenteur d'une réservation peut muter la même unité critique à la fois.
- Changements inter-dépôts = opérations coordonnées et compensables, sans prétendre à transaction atomique GitHub + DB + serveur.

### 8.4 Gestion d'incidents

`TRANSIENT` → retry plafonné. `API_RATE_LIMIT` → backoff/rate budget. `DEPENDENCY_FAILURE` → tâches indépendantes. `AUTHORITY_MISSING` → blocage du périmètre. `SCHEMA_DRIFT` → migration/test. `HEAD_MOVED` → rebase/reconciliation après contrôle. `REGRESSION` → rollback/revert autorisé. `CREDENTIAL_EXPIRED` → renouvellement via broker. `PROVIDER_UNAVAILABLE` → failover contrôlé compatible. `CRITICAL_SECURITY` → isolation et journal d'audit.

### 8.5 Disaster recovery

Snapshots vérifiables, restauration périodiquement testée, RPO/RTO à définir, clés en vault, backups chiffrés, restauration DB et object store, journal des migrations, vérification d'intégrité entre DB/archives GitHub et système de fichiers. Préparer runbooks de conflit, corruption, perte de webhook, expiration de lease, token révoqué et compromission de clé.

---

## 9. SÉCURITÉ ET GOUVERNANCE AUTOMATISABLE

1. Appartenance à `Patricked-code` ou `Wealthtechinnovations` = identité propriétaire des ressources, pas preuve universelle de toute instruction introduite dans un fichier tiers.
2. Authentifier le demandeur effectif et prouver la délégation ; label `OWNER_DELEGATED` seulement si mandat valide et source vérifiée.
3. Classer les entrées de repositories, issues, commentaires, logs, webhooks, réponses LLM et pages web comme **données non fiables** face aux instructions système.
4. Maintenir politiques `project_scope`, `allowed_operations`, `sensitive_actions`, `branch/ruleset`, `budget`, `approval_requirements`, `time_window` ; autoriser sans demandes répétées les opérations ordinaires préapprouvées.
5. Administration (modification rulesets, secret policies, delete/transfer, changement de visibilité) via service privilégié, contrôles deterministes et journal d'audit ; absence de permission = blocage, pas escalade par prompt.
6. Chiffrement et classement public/interne/confidentiel/sensible ; DLP/secret scanning avant publication ; politique de rétention et effacement autorisé.
7. Protéger CI : événements de PR issues de forks, jetons GitHub Actions restreints, exécuteurs isolés, validation de workflows modifiés.
8. Procéder à des évaluations de prompt injection et d'exfiltration, y compris simulation de commentaires malveillants et documents compromettants.
9. Prévoir limites de coûts, rate-limits, quotas IA, consommation Actions, création massive de projets et rollback.
10. Tracer identités humaines, applications GitHub, agents logiques, sessions et exécutants sans les confondre.

---

## 10. STRATÉGIE D'INTÉGRATION NON RÉGRESSIVE MCP/GRT/PROJETS MÉTIERS

### 10.1 Gouvernance par projet

Chaque projet choisit `READ_ONLY`, `PLANNING_ONLY`, `PR_ONLY`, `DEPLOY_GOVERNED`, `FULL_DELEGATION_AS_ALLOWED`. Le mode global ne doit pas effacer les fichiers `.md`, protections et processus locaux.

### 10.2 Audit avant réutilisation

Pour chaque dépôt admis : lire README, CLAUDE.md, SUIVI.md, CONTRIBUTING, DECISIONS_LOG, CURRENT_STATE, policy, branches, PR, checks, issues, checkpoints ; établir autorité/actualité/contradictions. Les exemples du projet MCP (AUTO-INTAKE/BUS, AUDIT_SUPERVISOR) et GRT (ATLAS/FORGE) restent documentaires tant qu'une identité runtime et une session n'ont pas été établies par des sources actuelles.

### 10.3 Adaptateurs et migration progressive

Construire adaptateurs plutôt que recopier le bus ou les registres. Garantir compatibilité read-only au début ; tests de bout en bout en LAB/sandbox ; migration avec dual-read et projection si nécessaire ; écriture autorisée uniquement après validation. Conserver `old_id → canonical_id` avec preuve pour préserver la chronologie.

### 10.4 Déploiement multi-environnement

GitHub n'est pas SSH. Les accès serveurs passent par le MCP ou une infrastructure Gateway, authentifiée séparément et capable d'observer l'état avant et après les déploiements. Aucune écriture serveur directe ne peut violer une politique GitHub→S1 existante.

---
## 11. FEUILLE DE ROUTE CONSOLIDÉE — CONSERVATION LOT 00–25 ET EXTENSIONS

**Quatre programmes, mais un seul graphe global de dépendances.** Ne pas créer quatre systèmes de pilotage parallèles. Les lots B00 à B25 préservent leur identité d'origine ; extensions Dxx et Fxx sont additives. Les durées, coûts et responsables physiques sont à estimer après l'inventaire, jamais inventés.

| Lot | Contenu, sans suppression de phase historique | Dépendance essentielle | Sortie exigée |
|---|---|---|---|
| B00 | Inventaire GitHub/MCP/GRT/projets, états, outils, archives disponibles | Autorisation lecture | Carte des autorités et preuves |
| B01 | Exigences et architecture de référence | B00 | Architecture + décisions + matrice de traçabilité |
| B02 | Schémas canoniques | B01 | JSON Schema/OpenAPI, validation |
| B03 | Catalogue d'identités | B02 | Resolver versionné + unicité |
| B04 | Blueprints, compétences et affectations | B02–03 | Contrat agent/projet/mission |
| B05 | Event ledger immuable logique | B02 | Inbox/outbox et traçabilité |
| B06 | Mémoire, références et snapshots | B05 | Projections et restauration |
| B07 | Session rebinding / conversation binding | B03–06 | Reprise nouvelle conversation |
| B08 | Moteur de continuité et checkpoints | B05–07 | Handoffs et NEXT_ACTION attestés |
| B09 | Missions, tâches et workflows durables | B02,B05,B08 | DAG + leases + retries |
| B10 | Gouvernance et moteur d'autorisation | B02–05 | Decision API + refus explicites |
| B11 | Communication interagents | B05,B09–10 | Messages, corrélation, DLQ |
| B12 | Adaptateur MCP et outillage | B10–11 | Tools bridge avec droits vérifiés |
| B13 | Intégration GitHub | B10,D01–D03 | App broker, API, webhooks |
| B14 | Intégration serveurs | B10,B12–13 | Accès serveur sans bypass |
| B15 | Fédération agent-agent/A2A | B03,B11 | Interop optionnelle testée |
| B16 | Observabilité et audit | B05,B09 | Traces et tableaux de bord |
| B17 | Console de supervision | B03,B06,B09,B16 | Cockpit gouverné |
| B18 | Recovery et disaster recovery | B05–09 | Scénarios de restauration |
| B19 | Security hardening | Tous lots concernés | Threat model et scans |
| B20 | Performance et charge | B09,B13 | Tests et limites quantifiées |
| B21 | Résilience et chaos tests | B18–20 | Pannes simulées et recovery |
| B22 | Pilotes d'intégration | B10–21 | Pilotes MCP/GRT indépendants |
| B23 | Documentation et migrations | En continu | Guides et runbooks complets |
| B24 | Vérification indépendante | B19–23 | Conformance report externe |
| B25 | Livraison, état final, exploitation | B24 | Release attestée, mode RUNNING |

### 11.1 Extensions additives prioritaires

| Extension | Définition | Dépendances | Validation |
|---|---|---|---|
| F00 | Bootstrap durable de l'usine d'ingénierie elle-même | B00 + workspace autorisé | Reprise après arrêt du moteur IA |
| F01 | Conversation Capture & Canonicalization Pipeline | B02,B05 | Capture vérifiée depuis ≥1 source réellement accessible |
| F02 | Canonical Memory Verifier Adapter | B06,F01 | Bundles valides/invalides testés |
| F03 | Multi-Provider Agent Gateway | B03,B08,B10 | Mission reprise par deux moteurs compatibles |
| F04 | Production readiness / rollback controller | B09,B14,B18 | Rollback vérifié en LAB |
| D00 | Inventaire complet GitHub App et capacités | B00 | Catalogue doc → endpoint → token → test |
| D01 | Authentification App/IAT/UAT multi-comptes | D00,B10 | Trois installations et token mapping prouvé |
| D02 | Repositories/Git/code/branches/PR | D01 | Cycle repo→PR→checks en sandbox |
| D03 | Issues et GitHub Projects | D01,B09 | GraphQL mutation contract test |
| D04 | Actions/Checks/CI/CD | D02 | Workflow dispatch et suivi |
| D05 | Sécurité/attestations/scanning | D02,D04 | Alertes et preuves fiables |
| D06 | Administration/properties/org | D01,B10 | Drift detection + correction approuvée |
| D07 | Webhook Receiver/Event Bus | D01,B05,B11 | HMAC, queue, replay, déduplication |
| D08 | Packages/Pages/releases/discussions/etc. | D02,D04 | APIs choisies testées |
| D09 | Account OAuth/delegation | D01,B10 | UAT dédié, accord utilisateur réel |
| D10 | Enterprise adapters optionnels | D00,D01 | Seulement si plan et compte Enterprise validés |
| D11 | Déploiements, infra externe et servers | D04,B14 | Version de prod attestée |
| D12 | Multi-repo analytics et pilotage | D02–08,B16 | KPIs sourcés et contrôlables |
| D13 | GitHub capability drift watch | D00,D01 | Détection des évolutions GitHub |
| D14 | Audit couverture fonctionnelle finale | D00–13,B24 | Matrice 30 domaines et anomalies ouvertes |

### 11.2 Ordre de travail réellement recommandé (chemin critique)

1. **Inventaire lecture seule (B00)** : vérifier les trois comptes, les dépôts, la propriété de la nouvelle App et l'état de la configuration en cours ; ne pas présumer de l'existence du repository universel.
2. **Base documentaire canonique (B01+B02, F01 sous forme d'import initial)** : figer décisions V5, archive source, schémas de capture, planning et NEXT_ACTION.
3. **Bootstrap de la GitHub App (D00→D01)** : génération vérifiée des permissions et installation, puis premier token broker, sans exposer les secrets.
4. **Créer et initialiser le repository public (D02)** après validation d'App et droits de création ; branch protection et CI sur `main`.
5. **Mettre en service l'orchestrateur durable minimal (F00+B05+B09)**, capable de reprendre un seul job après redémarrage.
6. **Déployer mémoire canonique et résolveur (B03–08, F01–02)** ; premier import de conversation compatible et test d'intégrité.
7. **Déployer moteur de politiques et outils GitHub/MCP (B10–14, D02–08)**.
8. **Multi-IA, communications et pilotes (F03, B11, B15, B22)** ; reprise Claude↔ChatGPT sans identité concurrente.
9. **Sécurité, restauration, charge, audit et release (B16–25)** ; industrialisation et exploitation.

### 11.3 Dépendances structurantes non déplaçables

- Capture continue réelle dépend des accès aux interfaces sources ; peut commencer par import manuel des archives accessibles sans prétendre à une capture automatique.
- Permissions Account dépendent d'une autorisation utilisateur, pas d'un simple IAT d'installation.
- Webhooks live dépendent d'un endpoint HTTPS sécurisé ; peuvent être préparés désactivés jusqu'à déploiement du récepteur.
- Déploiement réel dépend d'une identité d'infrastructure distincte ; GitHub App ne donne pas SSH automatiquement.
- Une autorisation de création de repository ne donne pas automatiquement la possibilité de modifier toutes les protections sur les repositories d'autres propriétaires.

---

## 12. CRITÈRES D'ACCEPTATION ET TESTS DE NON-RÉGRESSION

### T01–T12 : identité et mémoire

T01 — Résoudre un agent à partir d'un alias connu sans doublon.  
T02 — Rejeter deux identités prétendument canoniques pour le même agent.  
T03 — Séparer agent, blueprint, assignment, task et session dans les traces.  
T04 — Reprendre une continuité depuis une nouvelle conversation sans simuler une session runtime.  
T05 — Modifier le fournisseur IA sans changer `agent_id` ni `continuity_id`.  
T06 — Refuser la mémoire sans source lorsque l'opération exige une preuve.  
T07 — Projeter une décision superseded sans effacer son histoire.  
T08 — Vérifier bundles valides/invalides avec canonical-memory-verifier.  
T09 — Restaurer un checkpoint et détecter un HEAD Git déplacé.  
T10 — Garantir isolation des mémoires BRVM/BVMAC/MCP/GRT.  
T11 — Importer un échange et conserver son SHA-256, ordre et source.  
T12 — Documenter explicitement les conversations non capturées.

### T13–T24 : GitHub et autonomie

T13 — Installer l'App sur les trois espaces autorisés, avec installation IDs effectivement vérifiés.  
T14 — Démontrer une création de dépôt de test, ou consigner un blocage précis si permission non reconnue.  
T15 — Lire, modifier et PR via token d'installation sans disposer de clé privée côté agent.  
T16 — Tester GraphQL Projects avec type de jeton et permission réellement compatibles.  
T17 — Déclencher, suivre et attester un workflow Actions.  
T18 — Rejeter une permission Account testée avec un IAT si le endpoint exige UAT.  
T19 — Accepter un webhook valide, refuser HMAC invalide, dédupliquer retry.  
T20 — Relancer un job après crash sans deuxième PR/issue/déploiement.  
T21 — Échouer proprement avec `403`, token expiré et `rate limit exceeded`.  
T22 — Ne pas franchir la protection de branche ou l'autorité d'un dépôt.  
T23 — Préserver les fonctionnalités existantes des pilotes MCP/GRT (smoke + CI).  
T24 — Produire preuves d'attribution GitHub App vs agent logique vs initiateur humain.

### T25–T36 : qualité, sécurité et exploitation

T25 — Injection malveillante dans une issue GitHub ne devient pas instruction propriétaire.  
T26 — Secrets supprimés des artefacts publics et jamais imprimés dans les logs.  
T27 — SAST/Dependabot/secret scanning consommés selon permissions et offres.  
T28 — Rollback autorisé en lab après échec post-déploiement.  
T29 — Contrôler les races de deux agents mutateurs sur même branche.  
T30 — Tester un backup/restore de DB+archives+snapshot.  
T31 — Stopper les retries à budget maximal et ouvrir l'incident.  
T32 — Agent supervisor n'auto-certifie pas ses propres modifications sans preuves déterministes.  
T33 — Vérifier le catalog des 30 domaines (supported / unsupported / deferred / blocked).  
T34 — Ajouter un projet entièrement nouveau par schéma standard sans modifier les noyaux centraux.  
T35 — Ajouter un modèle IA compatible sans réenregistrer tous les agents.  
T36 — Livraison seulement si tous les gates obligatoires et les preuves sont satisfaits.

**Définition de « sans régression » :** aucune régression détectée par les suites et critères déclarés, avec baseline, environnements, limites de couverture et preuve de vérification ; impossible de garantir mathématiquement l'absence de toute régression non testée.

---

## 13. RUNBOOK INITIAL : DE LA CONVERSATION AU PREMIER SYSTÈME OPÉRATIONNEL

### Étape 0 : protection de la mémoire présente

Conserver ce plan V5, le complément original exact et leurs empreintes ; les rattacher au dépôt lorsqu'il existe. Ne pas affirmer que tous les échanges antérieurs ont été capturés. Référencer l'historique ChatGPT disponible comme source partielle et compléter par exports explicites quand accessibles.

### Étape 1 : état GitHub actuel

Vérifier live via connecteur : organisation, comptes installés, GitHub App `ChainSolutions Universal Gateway` existante ou non, configuration et permissions, repositories actuels. L'absence de preuve d'une App créée implique `NOT_VERIFIED`, pas `CREATED`. Ne pas toucher `ChatGPT Codex Connector` ni `Wealthtechfunds` sans audit et mandat explicites.

### Étape 2 : configuration maximale documentaire

Étendre le catalogue de permissions à toutes les catégories GitHub pertinentes, en distinguant `parameter_name_confirmed`, `value_confirmed`, `present_in_form`, `granted`, `runtime_tested`. Réviser les URL de préremplissage. Le manifeste officiel GitHub App peut servir à la reproductibilité ; aucun paramètre approximatif ne doit être déclaré accepté automatiquement.

### Étape 3 : enregistrement de l'App et installations

Sous `chainsolutions-wealthtech`, enregistrer App si autorité, installer sur les 3 espaces avec comptes propriétaires, choisir `Any account` et couverture dépôts appropriée. Conserver app_id et installation_ids non secrets, clés et secrets dans vault ; activer OAuth Device Flow/webhook lorsque services correspondants sont disponibles, pas par simple désir de cocher « tout ».

### Étape 4 : repository public

Création de `chainsolutions-wealthtech/universal-agent-platform` en mode public, avec policy, copyright/licence décidée, tests, .gitignore, secret scanning, branch rules, CODEOWNERS, architecture/roadmap, rapport baseline. Toute archive brute ou mémoire privée reste hors de Git.

### Étape 5 : first vertical slice

`mission issue → webhook → intake → agent resolve → policy → task lease → branch → commit → CI → review → PR → checkpoint → NEXT_ACTION`, sur un dépôt de test sans données sensibles. Reprendre au milieu après crash et démontrer pas de doublon. Ensuite projets pilotes existants en lecture seule, puis ouverture graduée des écritures.

---

## 14. EXPLOITATION ET MESURES

### 14.1 KPI gouvernance et continuité

- `agent_identity_resolution_success_rate`, `duplicate_agent_prevention_count`, `checkpoint_restore_success_rate`, `time_to_resume`, `source_trace_coverage`, `memory_claim_ambiguity_rate`, `blocked_authority_count`, `unauthorized_operation_rejected_count`.
- `webhook_dedup_rate`, `unhandled_delivery_count`, `task_replay_without_duplication_rate`, `task_lease_collision_count`, `recovery_RTO`, `disaster_recovery_RPO`.

### 14.2 KPI GitHub/ingénierie

- Build success/failure, PR throughput/lead time, CI flaky test rate, merge conflicts, opened security alerts, vulnerability aging, deploy pass, rollback pass, median time to repair, GitHub API quota/429/403, cost per task et per fournisseur IA.
- Chaque indicateur porte provenance, fenêtre, frais/quotas et périmètre ; un indicateur sans données fiables n'est pas présenté comme calculé.

### 14.3 Coûts et limites

Budget IA, GitHub Actions/runners, stockage privé, webhook delivery, retry, projets et agents concurrents ; contrôle d'admission des tâches selon capacités. Mesurer avant extrapoler. Ce programme n'affirme ni continuité infinie sans coût ni exécution garantie en cas d'autorité manquante.

---

## 15. DÉCISIONS STRUCTURANTES VERSION V5 (AJOUTS, NON REMPLACEMENTS)

| ID | Décision ou exigence | Statut | Provenance |
|---|---|---|---|
| ARCH-001 | Plateforme indépendante de tous les fournisseurs IA et repos métier | Retenue conceptuellement | Conversations précédentes |
| ARCH-002 | MCP et GRT distincts ; mémoires et permissions locales | Retenue | Conversations précédentes |
| ARCH-003 | Identités durables, résolveur avant création, session rebinding vérifié | Retenue | Conversations précédentes |
| ARCH-004 | Capture des conversations + canonicalisation + mémoire attestable | Retenue / à implémenter | Conversations précédentes |
| ARCH-005 | Autonomous Engineering Factory et contrôleur durable externe | Retenue / à implémenter | Conversations précédentes |
| ARCH-006 | GitHub App propre, sous org, installable sur trois espaces | Retenue conceptuellement | Conversations précédentes |
| ARCH-007 | Repository `universal-agent-platform` public ; secrets et archives privés | Retenue conceptuellement | Conversations précédentes |
| ARCH-008 | Quatre familles de permissions avec registres des permissions effectives | Retenue / vérification nécessaire | Conversations précédentes |
| ARCH-009 | Programme D / 30 domaines GitHub exhaustifs comme backlog capability-driven | **AJOUT V5** | Texte utilisateur 20 sections |
| ARCH-010 | Flux de développement autonome 20 étapes, avec preuves et CI | **AJOUT V5** | Texte utilisateur section 5 |
| ARCH-011 | Webhook/event-driven avec HMAC, redelivery et déduplication | **AJOUT V5** | Texte utilisateur section 14 |
| ARCH-012 | Analytics multi-projets et centre de contrôle global | **AJOUT V5** | Texte utilisateur sections 13 et 17 |
| ARCH-013 | Intégration GitHub complète (REST/GraphQL/Git, produits optionnels) | **AJOUT V5** | Texte utilisateur sections 2,6–7,10,12 |
| ARCH-014 | Catalogue évolutif des capacités, plans, endpoints et permissions | **AJOUT V5** | Texte utilisateur sections 17–20 |
| ARCH-015 | Interop A2A éventuelle, sans forcer Copilot ni dupliquer MCP BUS | Confirmée et approfondie | Historique + section 4 |
| ARCH-016 | Distinction « demandé/accordé/disponible/opérationnel » par permission | **AJOUT V5** | Contrôle de faisabilité |
| ARCH-017 | Politique multi-projets de migration sans régression et sans fusion d'autorités | Confirmée | Historique + sections 11–12 |

Ces décisions sont des **préférences architecturales documentées**, pas des approvals d'exécution autonomes ; l'état runtime ne peut être déduit de ce tableau.

---

## 16. SOURCES ET VALIDATION DOCUMENTAIRE

### 16.1 Source interne transmise par l'utilisateur

`sources/TEXTE_COMPLEMENTAIRE_ORIGINAL_20261021.txt` — 20 sections, 30 domaines, matrice des possibilités GitHub, plan de workflow 20 étapes, risques, priorités ; conservée intégralement dans ce paquet, sans réécriture ni effacement. `sources/SOURCE_MANIFEST.json` contient son empreinte SHA-256 et sa taille.

### 16.2 Références officielles externes à contrôler périodiquement

- GitHub permissions : https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
- GitHub endpoint/permissions : https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps
- GitHub App authentication : https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app
- GitHub webhook best practices : https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks
- GitHub manifest registration : https://docs.github.com/en/apps/sharing-github-apps/registering-a-github-app-from-a-manifest
- Model Context Protocol : https://modelcontextprotocol.io/
- Agent2Agent : https://a2a-protocol.org/latest/

### 16.3 Non-confusion entre constat, proposition et exécution

- **CONSTATÉ DANS LA PIÈCE** : un contenu décrit comme possible et son périmètre théorique.
- **DOCUMENTÉ OFFICIELLEMENT** : API/capacité publiée par un fournisseur et vérifiée dans sa doc à une date.
- **RUNTIME VERIFIED** : opération testée réellement avec l'installation, la permission et le type de jeton correspondants.
- **IMPLEMENTED** : code présent, CI et tests réussis, livrable vérifié.
- **DEPLOYED** : service actif sur la cible, tests post-déploiement et preuve.

Ces statuts ne doivent jamais être interchangeables.

---

## 17. CURRENT STATE ET NEXT_ACTION (DOCUMENTAIRES, NON RUNTIME)

**État au moment de cette consolidation :** réflexion et conception consolidées en V5 ; une GitHub App `ChainSolutions Universal Gateway` a été préparée sous forme de formulaires/bootstraps historiques mais sa création effective n'a pas été attestée ici. L'existence effective d'un dépôt public `chainsolutions-wealthtech/universal-agent-platform` n'a pas été attestée dans cette étape. Aucun audit actuel et exhaustif des permissions des trois comptes ni déploiement du pipeline de capture n'est présenté comme réalisé.

**NEXT_ACTION_V5 = `VERIFY_GITHUB_APP_AND_REPO_LIVE_STATE_THEN_CANONICAL_BOOTSTRAP`**

Séquence atomique recommandée :
1. Lecture seule GitHub de l'organisation, du compte propriétaire et de l'éventuelle nouvelle App.
2. Vérification des paramètres du formulaire (toutes catégories et leurs identifiants acceptés), sans confondre URL candidate et permission accordée.
3. Confirmation de la propriété et de l'existence de l'App/dépôt ; création initiale seulement par moyen techniquement disponible et mandat explicite.
4. Mise sous version du présent plan et de la source originale, dans un emplacement autorisé après contrôle de classification.
5. Développement d'un premier slice de `Conversation Capture & Canonicalization Pipeline` avec chaîne de preuves, puis GitHub Gateway et reprise autonome minimale.

**Ne pas poursuivre automatiquement des opérations d'écriture uniquement parce que ce document contient un plan de livraison.** Le mandat et les autorités live doivent être résolus en début d'exécution.

---

## 18. DÉFINITION DE LIVRAISON FINALE

Un programme terminé doit livrer : code versionné, API/documentation, schema registry, policy engine, adapters ChatGPT/Claude/autres selon capacités, GitHub broker, MCP bridge, event ledger, conversation capture, mémoire vérifiée, orchestration persistante, console de supervision, intégrations pilotes, sauvegardes, observabilité, conformité tests T01–T36, contrôles de sécurité, runbooks, migration plan, release SHA et rapport indépendant. L'acceptation exige les preuves et l'absence de blocants selon le périmètre formel, pas une simple auto-déclaration de complétude.

Le programme passe ensuite de `BUILD_COMPLETE` à `OPERATING` selon le plan d'exploitation autorisé, et non à une boucle de développement infinie.

---

## 19. LÉGENDE DE CONTRÔLE DE CHANGEMENT

- `UNCHANGED`: principe fondateur conservé.
- `EXPANDED`: détail enrichi sans changement de portée ni de responsabilité.
- `ADDED`: nouveau domaine ou fonctionnalité, relié à sa source.
- `DEFERRED`: possible mais non pertinent/autorisé à l'instant.
- `NEEDS_VERIFICATION`: existence de permission/API ou autorité runtime non attestée.
- `SUPERSEDED`: décision remplacée explicitement avec justification et lien de provenance ; aucune suppression historique.

**Version documentaire V5.0 ne signifie pas version produit V5.0.** La plateforme reste à implémenter et valider.

## ANNEXE A — CORRESPONDANCE EXHAUSTIVE DES 20 SECTIONS DE LA PIÈCE UTILISATEUR

| Section d’origine | Titre original | Chapitres de consolidation V5 | Traitement |
|---:|---|---|---|
| 1 | Ce qu'est réellement une GitHub App et jusqu'où elle peut aller | 0.1, 1, 4, 5 | Conservé et étendu |
| 2 | Les grands domaines que vous pouvez exploiter | 6, 6.D01–D13 | Conservé et étendu |
| 3 | Développer et modifier automatiquement des logiciels entiers | 6.D02, 7, 12 | Conservé et étendu |
| 4 | Utiliser ChatGPT et Claude simultanément sur un même projet | 2.2, 4, 7 | Conservé et étendu |
| 5 | Construire une usine logicielle automatisée | 7, 8, 11 | Conservé et étendu |
| 6 | Piloter tout GitHub Actions et les automatisations CI/CD | 6.D04, 7, 12 | Conservé et étendu |
| 7 | Administrer et gouverner les dépôts GitHub | 5, 6.D06, 9 | Conservé et étendu |
| 8 | Créer une mémoire canonique et une continuité entre ChatGPT et Claude | 2, 3, 12 | Conservé et étendu |
| 9 | Transformer GitHub en système de gestion de projet multi-agents | 6.D03, 7, 11 | Conservé et étendu |
| 10 | Gérer la sécurité de l'ensemble des projets | 6.D05, 9, 12 | Conservé et étendu |
| 11 | Déployer automatiquement des applications et administrer des serveurs | 6.D07, 10, 13 | Conservé et étendu |
| 12 | Créer automatiquement de nouveaux projets | 6.D01, 11, 13 | Conservé et étendu |
| 13 | Superviser l'activité et produire des rapports | 6.D10, 14 | Conservé et étendu |
| 14 | Aller encore plus loin avec une architecture événementielle | 6.D08, 8 | Conservé et étendu |
| 15 | Ce qu'une GitHub App ne peut pas faire seule | 0.3, 5, 13 | Conservé et étendu |
| 16 | Faut-il une seule GitHub App ou plusieurs ? | 5.4, 9 | Conservé et étendu |
| 17 | Ce que je construirais en priorité pour votre plateforme ChatGPT + Claude | 11, 13, 17 | Conservé et étendu |
| 18 | Les possibilités les plus avancées | 6.D11–D13, 8, 14 | Conservé et étendu |
| 19 | Les documents officiels utiles | 16 | Conservé et étendu |
| 20 | Le véritable potentiel pour votre objectif | 0, 18 | Conservé et étendu |

## ANNEXE B — LES 30 DOMAINES FONCTIONNELS DE LA PIÈCE INITIALE

| # | Domaine | Réalisation décrite par la pièce | Statut V5 |
|---:|---|---|---|
| 1 | Dépôts Git | Natif | À vérifier sur l’installation/API réelle |
| 2 | Code source | Natif + IA | À vérifier sur l’installation/API réelle |
| 3 | Branches | Natif | À vérifier sur l’installation/API réelle |
| 4 | Commits | Natif | À vérifier sur l’installation/API réelle |
| 5 | Pull requests | Natif | À vérifier sur l’installation/API réelle |
| 6 | Issues | Natif | À vérifier sur l’installation/API réelle |
| 7 | GitHub Projects | Natif | À vérifier sur l’installation/API réelle |
| 8 | GitHub Actions | Natif | À vérifier sur l’installation/API réelle |
| 9 | Tests logiciels | GitHub Actions + outils | À vérifier sur l’installation/API réelle |
| 10 | Sécurité | Natif + outils | À vérifier sur l’installation/API réelle |
| 11 | Administration | Natif | À vérifier sur l’installation/API réelle |
| 12 | Déploiement | Natif + infrastructure | À vérifier sur l’installation/API réelle |
| 13 | Documentation | Natif + IA | À vérifier sur l’installation/API réelle |
| 14 | GitHub Pages | Natif | À vérifier sur l’installation/API réelle |
| 15 | Releases | Natif | À vérifier sur l’installation/API réelle |
| 16 | Packages | Natif, selon registre | À vérifier sur l’installation/API réelle |
| 17 | Webhooks | Natif + récepteur | À vérifier sur l’installation/API réelle |
| 18 | Comptes utilisateurs | Autorisation utilisateur | À vérifier sur l’installation/API réelle |
| 19 | Organisations | Natif | À vérifier sur l’installation/API réelle |
| 20 | Enterprise | Selon offre et accès | À vérifier sur l’installation/API réelle |
| 21 | Agents IA | À développer | À vérifier sur l’installation/API réelle |
| 22 | Mémoire des agents | À développer | À vérifier sur l’installation/API réelle |
| 23 | Communication entre agents | À développer | À vérifier sur l’installation/API réelle |
| 24 | Gouvernance des agents | À développer | À vérifier sur l’installation/API réelle |
| 25 | Audit continu | Natif + service | À vérifier sur l’installation/API réelle |
| 26 | Automatisation inter-dépôts | Natif + orchestration | À vérifier sur l’installation/API réelle |
| 27 | Migration de projets | Natif + outils | À vérifier sur l’installation/API réelle |
| 28 | Gestion d'infrastructure | Intégrations externes | À vérifier sur l’installation/API réelle |
| 29 | Analyse de portefeuille logiciel | API + analyse | À vérifier sur l’installation/API réelle |
| 30 | Supervision autonome | À développer | À vérifier sur l’installation/API réelle |

**Note de provenance :** l’original complet des 20 sections est conservé en fichier séparé et fait foi ; les tableaux ci-dessus sont des index pour retrouver tous ses domaines.
