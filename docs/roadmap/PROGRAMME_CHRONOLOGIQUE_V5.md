# Programme directeur chronologique V5 — plan de construction et de reprise

**Date de consolidation :** 22 octobre 2026  
**Périmètre exclusif de publication :** `chainsolutions-wealthtech/universal-agent-platform`, branche `bootstrap/canonical-v5-foundation`, PR #1.  
**Statut :** `PROPOSED_EXECUTION_ORDER` — **proposition documentaire non fusionnée et non autorité runtime**, soumise à revue de gouvernance ; aucune création en masse d'issues ou de tâches runtime.  

## 0. Pourquoi ce document existe

Rendre l'exécution **reconstructible de bout en bout** par n'importe quelle conversation ou agent autorisé : où commencer, pourquoi, dans quel ordre, avec quelles dépendances, quelles preuves et quel `NEXT_ACTION`. La GitHub App est une infrastructure d'accès ; le produit final est une plateforme multi-agents **et** l'usine autonome qui la construit.

**Trois sources ayant chacune un propriétaire unique :**

1. **Source V5 historique immuable** : `docs/archive/PLAN_DIRECTEUR_UNIFIE_V5_20261021.md`, complément original `docs/archive/TEXTE_COMPLEMENTAIRE_ORIGINAL_20261021.txt` et `docs/archive/IMPORT_MANIFEST.json`. Ne jamais réécrire pour corriger une date historique.
2. **Définition canonique des 46 lots** : `docs/roadmap/ROADMAP_V5.json` (identifiants, objectifs, dépendances formulées, critères d'acceptation, statut documentaire `PLANNED`). **Ce document-ci ne remplace pas ces définitions** ; il possède uniquement l'ordre de construction proposé, les vagues et les gates.
3. **État de la PR et prochaine action** : `state/CURRENT_STATE.json` et `SUIVI.md` (instantanés documentaires à réconcilier avec GitHub live). L'état GitHub réel prime : PR, HEAD, ruleset, CI, reviews. Les événements d'exécution futurs seront stockés dans le ledger privé conçu plus tard.

Les plans **A (plateforme)**, **B (usine)**, **C (GitHub App/Bootstrap)** et **D (couverture GitHub)** restent distincts et complémentaires. L'architecture B « monolithe modulaire » vs E « Control Plane / Execution Plane » reste une **décision ouverte**, à instruire avec ADR avant verrouillage ; ce document ne tranche pas à sa place.

## 1. Chronologie historique attestée vs déclarée

| Moment | Événement | Nature de la preuve | Portée exacte |
| --- | --- | --- | --- |
| Jusqu'au 21 octobre 2026 | Travail conceptuel, plans A/B/C, programme AGSREF, études d'architecture, complément D et consolidation V5 | Documents historiques et discussions | Planification, **pas** exécution de 46 lots |
| 21 octobre 2026 | Création de GitHub App `ChainSolutions Universal Gateway` (App ID `5417646`) dans `chainsolutions-wealthtech` | Capture GitHub et sortie locale communiquées par le propriétaire | Enregistrement et identité de l'application |
| 21 octobre 2026 | Authentification locale sur trois installations : org `173915815`, `Wealthtechinnovations` `173916302`, `Patricked-code` `173916438` | Journal local transmis par le propriétaire | Accès observé au moment du test ; **pas** couverture exhaustive des permissions |
| 21 octobre 2026 | Création du dépôt public `chainsolutions-wealthtech/universal-agent-platform` | Dépôt GitHub et journal local | Premier bootstrap réel du dépôt |
| 22 octobre 2026 | PR #1 sur `bootstrap/canonical-v5-foundation`, archives V5, roadmap et règles ; `main` protégée par ruleset `25599154` | GitHub live, commits, PR, ruleset | Proposition documentaire non fusionnée |
| 22 octobre 2026 | Revue et remédiations de sécurité/documentation ; issue de revue #2 | Commentaires GitHub, tests et fichiers de suivi | Corrections committées ; revue finale encore attendue |
| 22 octobre 2026 — dernier contrôle de préparation | `main` HEAD `0b8b2e01e826b915a0c593d5d6545681e9316567`, PR #1 HEAD initial de cette rédaction `88e2a13928d95acc3bbec13dd235c2c2e3e48a9c` ; check `validate` sur cette révision non attesté, 9 discussions non résolues à la dernière vérification | GitHub live | **Blocage d'intégration**, pas blocage de la rédaction du plan |

Les valeurs de HEAD sont des **points de contrôle historiques**. Les vérifier de nouveau lors de chaque reprise ; ne jamais les traiter comme des références immuables vers le dernier état.

## 2. Gate de bootstrap avant exécution autonome

**G0 — `RESTORE_REQUIRED_GITHUB_ACTIONS_VALIDATE_ON_PR_1_HEAD` :** diagnostiquer l'absence de `validate` sur le dernier HEAD, faire tourner les tests, recevoir la contre-revue sur les 9 fils et les résoudre conformément à la gouvernance, puis demander la décision d'intégration de PR #1. Aucun contournement du ruleset, aucun force-push, aucune fusion en l'absence des preuves requises. La documentation et les audits en lecture seule peuvent progresser en parallèle.

**G1 — `BASELINE_V5_ADOPTED` :** seulement après fusion gouvernée, reconcilier `CURRENT_STATE` avec GitHub live, figer la référence de base et vérifier protections/CI sur `main`.

**G2 — `SAFE_ENGINEERING_WORKSPACE` :** périmètre LAB dédié, secrets protégés, politique d'autorisations et règle de non-régression avant toute exécution de code autonome.

## 3. Vagues chronologiques — graphe de dépendances V5

L'ordre ci-dessous est **topologique** pour les dépendances explicites de `ROADMAP_V5.json` ; les conditions transversales `En continu`, `Tous lots concernés` et les permissions effectives restent des gates **à tout moment**. Les lots sont listés une seule fois ; une même vague contient des travaux qui peuvent être parallèles seulement si leurs prérequis sont effectivement satisfaits.

| Vague | Chantier | Ordre interne de lots | Critère de sortie |
| --- | --- | --- | --- |
| P00 | Reconnaissance et périmètres d'autorité | `B00` | Inventaire traçable des sources, comptes, autorités, limites de lecture, zones non vérifiées et exclusions explicites. |
| P01 | Référentiel des exigences et fondation de l'usine | `B01 → B02 → D00 → F00 → B23` | Contrats initiaux, registre de risques et capacité de reprendre un travail de bootstrap minimal sans le présenter comme le lot B09 achevé. |
| P02 | Identités, modèles et preuve événementielle | `B03 → B04 → B05 → B10` | Schémas stables, résolution d'identité de test, ledger append-only et décisions de politique testables. |
| P03 | Mémoire, checkpoints et orchestrateur complet | `B06 → F01 → B07 → B08 → B09 → F02` | Capture d'une source réellement accessible, intégrité/snapshots, reprise après interruption sans identité ni tâche dupliquée. |
| P04 | Gateway GitHub industriel et CI | `D01 → D02 → D03 → D04 → D05 → D06 → D13` | Scopes App/IAT/UAT vérifiés séparément, opérations GitHub en dépôt LAB, CI réelle, sécurité et dérive de capacités. |
| P05 | Collaboration, bus, interfaces et multi-IA | `B11 → B12 → B13 → B15 → F03 → D07 → D08 → D09 → D10` | Messages corrélés/dédupliqués, autorisations respectées, webhook vérifié, reprise inter-fournisseurs démontrée ; options non éligibles déclarées N/A. |
| P06 | Infrastructure, monitoring et reprise en exploitation | `B14 → B16 → B17 → B18 → F04 → D11 → D12` | Audit et tableaux de bord, recovery/rollback testé en LAB, preuve de déploiement seulement si autorisé. |
| P07 | Durcissement, charges et pilotes | `B19 → B20 → B21 → B22` | Tests de sécurité, charge, chaos/reprise et pilotes admissibles ; règles MCP/GRT préservées. |
| P08 | Vérification indépendante et couverture finale | `B24 → D14` | Rapport indépendant avec preuves reproductibles, couverture des 30 domaines, écarts et exceptions documentés. |
| P09 | Livraison et exploitation gouvernée | `B25` | Release attestée, procédures RUN, budgets, alertes, sauvegardes et prochaine action validée. |

### Précision importante sur F00, B05, B09

Le chapitre 11.2 recommande très tôt une **première tranche de `F00 + B05 + B09`**, mais la définition **complète** de `B09` dépend explicitement de `B08` qui dépend des registres B03–B07. Il n'est donc **pas permis de marquer B09 DONE** lors d'une démonstration minimale précoce. En P01 on construit uniquement F00, avec journal et mécanisme de reprise *provisoires*, puis P02 établit B05 et P03 termine B09 après B08. Toute démonstration anticipée reste `PROTOTYPE` avec une traçabilité séparée.

### 3.1 Les 46 lots ordonnés, critères et dépendances originaux

| N° | Vague | Lot | Objet selon V5 | Dépendances déclarées | Preuve minimale / acceptation définie par V5 |
| ---: | --- | --- | --- | --- | --- |
| 1 | P00 | **`B00`** | Inventaire GitHub/MCP/GRT/projets, états, outils, archives disponibles | Autorisation lecture | Carte des autorités et preuves |
| 2 | P01 | **`B01`** | Exigences et architecture de référence | B00 | Architecture + décisions + matrice de traçabilité |
| 3 | P01 | **`B02`** | Schémas canoniques | B01 | JSON Schema/OpenAPI, validation |
| 4 | P01 | **`D00`** | Inventaire complet GitHub App et capacités | B00 | Catalogue doc → endpoint → token → test |
| 5 | P01 | **`F00`** | Bootstrap durable de l'usine d'ingénierie elle-même | B00 + workspace autorisé | Reprise après arrêt du moteur IA |
| 6 | P01 | **`B23`** | Documentation et migrations | En continu | Guides et runbooks complets |
| 7 | P02 | **`B03`** | Catalogue d'identités | B02 | Resolver versionné + unicité |
| 8 | P02 | **`B04`** | Blueprints, compétences et affectations | B02–03 | Contrat agent/projet/mission |
| 9 | P02 | **`B05`** | Event ledger immuable logique | B02 | Inbox/outbox et traçabilité |
| 10 | P02 | **`B10`** | Gouvernance et moteur d'autorisation | B02–05 | Decision API + refus explicites |
| 11 | P03 | **`B06`** | Mémoire, références et snapshots | B05 | Projections et restauration |
| 12 | P03 | **`F01`** | Conversation Capture & Canonicalization Pipeline | B02,B05 | Capture vérifiée depuis ≥1 source réellement accessible |
| 13 | P03 | **`B07`** | Session rebinding / conversation binding | B03–06 | Reprise nouvelle conversation |
| 14 | P03 | **`B08`** | Moteur de continuité et checkpoints | B05–07 | Handoffs et NEXT_ACTION attestés |
| 15 | P03 | **`B09`** | Missions, tâches et workflows durables | B02,B05,B08 | DAG + leases + retries |
| 16 | P03 | **`F02`** | Canonical Memory Verifier Adapter | B06,F01 | Bundles valides/invalides testés |
| 17 | P04 | **`D01`** | Authentification App/IAT/UAT multi-comptes | D00,B10 | Trois installations et token mapping prouvé |
| 18 | P04 | **`D02`** | Repositories/Git/code/branches/PR | D01 | Cycle repo→PR→checks en sandbox |
| 19 | P04 | **`D03`** | Issues et GitHub Projects | D01,B09 | GraphQL mutation contract test |
| 20 | P04 | **`D04`** | Actions/Checks/CI/CD | D02 | Workflow dispatch et suivi |
| 21 | P04 | **`D05`** | Sécurité/attestations/scanning | D02,D04 | Alertes et preuves fiables |
| 22 | P04 | **`D06`** | Administration/properties/org | D01,B10 | Drift detection + correction approuvée |
| 23 | P04 | **`D13`** | GitHub capability drift watch | D00,D01 | Détection des évolutions GitHub |
| 24 | P05 | **`B11`** | Communication interagents | B05,B09–10 | Messages, corrélation, DLQ |
| 25 | P05 | **`B12`** | Adaptateur MCP et outillage | B10–11 | Tools bridge avec droits vérifiés |
| 26 | P05 | **`B13`** | Intégration GitHub | B10,D01–D03 | App broker, API, webhooks |
| 27 | P05 | **`B15`** | Fédération agent-agent/A2A | B03,B11 | Interop optionnelle testée |
| 28 | P05 | **`F03`** | Multi-Provider Agent Gateway | B03,B08,B10 | Mission reprise par deux moteurs compatibles |
| 29 | P05 | **`D07`** | Webhook Receiver/Event Bus | D01,B05,B11 | HMAC, queue, replay, déduplication |
| 30 | P05 | **`D08`** | Packages/Pages/releases/discussions/etc. | D02,D04 | APIs choisies testées |
| 31 | P05 | **`D09`** | Account OAuth/delegation | D01,B10 | UAT dédié, accord utilisateur réel |
| 32 | P05 | **`D10`** | Enterprise adapters optionnels | D00,D01 | Seulement si plan et compte Enterprise validés |
| 33 | P06 | **`B14`** | Intégration serveurs | B10,B12–13 | Accès serveur sans bypass |
| 34 | P06 | **`B16`** | Observabilité et audit | B05,B09 | Traces et tableaux de bord |
| 35 | P06 | **`B17`** | Console de supervision | B03,B06,B09,B16 | Cockpit gouverné |
| 36 | P06 | **`B18`** | Recovery et disaster recovery | B05–09 | Scénarios de restauration |
| 37 | P06 | **`F04`** | Production readiness / rollback controller | B09,B14,B18 | Rollback vérifié en LAB |
| 38 | P06 | **`D11`** | Déploiements, infra externe et servers | D04,B14 | Version de prod attestée |
| 39 | P06 | **`D12`** | Multi-repo analytics et pilotage | D02–08,B16 | KPIs sourcés et contrôlables |
| 40 | P07 | **`B19`** | Security hardening | Tous lots concernés | Threat model et scans |
| 41 | P07 | **`B20`** | Performance et charge | B09,B13 | Tests et limites quantifiées |
| 42 | P07 | **`B21`** | Résilience et chaos tests | B18–20 | Pannes simulées et recovery |
| 43 | P07 | **`B22`** | Pilotes d'intégration | B10–21 | Pilotes MCP/GRT indépendants |
| 44 | P08 | **`B24`** | Vérification indépendante | B19–23 | Conformance report externe |
| 45 | P08 | **`D14`** | Audit couverture fonctionnelle finale | D00–13,B24 | Matrice 30 domaines et anomalies ouvertes |
| 46 | P09 | **`B25`** | Livraison, état final, exploitation | B24 | Release attestée, mode RUNNING |

**Lecture des statuts :** aucun de ces lots ne devient `DONE` du seul fait de la création de la GitHub App ou de cette roadmap. Les succès de bootstrap se rapportent à leurs opérations ponctuelles ; les critères de sortie de D00, D01, D02 et F00 restent à vérifier sur leur périmètre **industriel complet**.

## 4. Comment découper un lot en tâches exécutables

**Hiérarchie unique** : `PROGRAMME → VAGUE → LOT (ID stable) → TÂCHE (ID stable) → OPÉRATION (idempotency_key) → PREUVE → CHECKPOINT/NEXT_ACTION`.

Pour chaque lot `XXX`, préparer **trois tranches documentaires** synchronisées avec `REGISTRE_TACHES_V5.md` : `XXX-01 DISCOVER + CONTRACT` (lecture des autorités, baseline, exigences et interfaces) → `XXX-02 IMPLEMENT` (conception approuvée, réalisation admissible, branche/PR et tests) → `XXX-03 VERIFY + ACCEPT` (CI au dernier HEAD, sécurité, revue distincte, preuves et handoff). Selon le lot, subdiviser ensuite une tranche en tâches plus petites **uniquement après admission gouvernée**. Pour un lot purement documentaire, la réalisation prend la forme de documents vérifiables, jamais d'une implémentation fictive.

**Aucune génération automatique de 138 issues** à partir des 3 sous-tâches proposées : d'abord qualifier chaque lot, vérifier les issues existantes, résoudre l'identité et les mandats, établir un registre anti-doublon, puis ne créer que les tâches immédiatement admissibles sous autorisation.

Une fiche de lot ne doit pas revendiquer de résultat sans `proof_refs` vérifiés et un HEAD/horodatage. Chaque transition documente `requested_by`, `operator`, `project_scope`, `authorization_source`, `checkpoint`, `next_action` ; ces champs documentaires **ne valent pas permission runtime**.

## 5. Gates transversaux non négociables

- **Conservation** : aucune suppression ou écrasement silencieux de la source V5, des décisions et des historiques ; éviter les canons concurrents.
- **Autorité** : MCP (`Patricked-code/MCP`) et GRT (`chainsolutions-wealthtech/Governed-Repository-Template`) sont des projets séparés, non modifiés depuis cette feuille de route. L'inventaire de leurs mécanismes nécessite le périmètre de lecture réellement autorisé.
- **Confidentialité** : la plateforme est publique ; aucune clé PEM, token, conversation privée brute ou donnée personnelle sensible dans Git. Une mémoire confidentielle nécessitera un stockage protégé externe.
- **Identités** : `agent_id ≠ blueprint_id ≠ assignment_id ≠ mandate_id ≠ mission_id ≠ task_id ≠ session_id ≠ continuity_id`. Reprise avant création ; aucun identifiant documentaire ne confère un droit runtime.
- **Architecture** : conserver les options ouvertes tant que contrats et preuves comparatives ne tranchent pas ; pas de seconde gouvernance ou bus concurrent.
- **Qualité** : `PR → CI au dernier HEAD → revue indépendante admissible → politique → fusion autorisée`. Aucun contournement des protections, y compris par agent automatisé.
- **Autonomie** : le fonctionnement durable n'est prouvé qu'après crash/reprise, absence de doublon et vérification des external side effects.
- **Parallélisation** : ne lancer une tâche d'une vague ultérieure que si tous ses vrais prérequis sont attestés, son environnement et son mandat indépendants et ses ressources réservées.
- **Ressources** : quotas API, budget IA, temps, sécurité et limites fournisseurs sont suivis explicitement sans extrapolation.

## 6. Scénario bout en bout — démonstration obligatoire

`Issue LAB` → `webhook signé` → `intake durable` → `resolve_identity` → `load_authorities` → `policy decision` → `task lease` → `branche` → `commit` → `CI` → `review indépendante` → `PR` → `checkpoint` → `NEXT_ACTION` → `reprise après interruption`.

Acceptation : le même `continuity_id` reprend l'exécution sans agent/tâche/communication en doublon, chaque side effect externe est idempotent ou réconcilié, la provenance complète est récupérable, aucune permission n'est inférée du document.

## 7. Vue de priorité après fondation

1. **Immédiat :** `G0` sur PR #1 (CI au HEAD et contre-revue des 9 discussions), sans merge prématuré.
2. **Conception exécutable :** `B00 → B01 → B02` (autorités, exigences, schémas), `D00` (inventaire permissions effectives), `F00` (bootstrap minimal gouverné) ; contribuer sur une branche/PR gouvernée après la fondation.
3. **Noyau durable :** `B03/B04/B05/B10 → B06/F01/B07/B08/B09/F02`.
4. **Connectivité :** `D01–D13` selon dépendances réelles (pas "toutes les permissions" par simple consentement conversationnel).
5. **Transversal :** `B19` sécurité et `B23` documentation continuellement, même si leurs jalons de clôture sont situés plus tard.
6. **Sortie :** `B24` avis indépendant → `D14` couverture → `B25` release.

## 8. Reprise par un autre agent/une autre conversation

Lire `00_START_HERE.md`, puis `state/CURRENT_STATE.json`, `SUIVI.md`, ce programme et `ROADMAP_V5.json`, puis `docs/DECISIONS_LOG.md` et `docs/SECURITY_GOVERNANCE.md`. Vérifier dans GitHub live : dépôt, HEAD, PR/issue, ruleset, workflow/check au dernier commit et commentaires non résolus. Résoudre l'identité et le mandat existants avant toute attribution nouvelle. Produire un différentiel entre **observé** et **documenté**, puis exécuter uniquement la première action admissible. Mettre à jour le propriétaire de la vérité modifiée et relire l'état persistant après toute écriture.

## 9. Références et statut de cette rédaction

- Source historique principale : `docs/archive/PLAN_DIRECTEUR_UNIFIE_V5_20261021.md`, en particulier §§ 0–19, Annexes A/B, § 11.2 et § 13.
- Lot registry : `docs/roadmap/ROADMAP_V5.json`, 46 entrées ; aucun ID ajouté ou supprimé.
- Complément de 20 sections : `docs/archive/TEXTE_COMPLEMENTAIRE_ORIGINAL_20261021.txt`.
- Point d'entrée et suivi : `00_START_HERE.md`, `SUIVI.md`, `state/CURRENT_STATE.json`.
- Revue : PR #1 / issue #2 ; pas d'auto-approbation.
- Méthodologies **utilisées comme disciplines** : Better Plans (objectifs, risques, dépendances), Memory Keeper (propriétaire canonique, provenance, non-duplication), Matt Pocock Skills (modèle de domaine/interface/tests), AI Software Architect (comparaison architecturale et décisions/ADR **sous approbation**). Aucune de ces méthodes n'est par elle-même un service runtime installé dans le dépôt.
- **Statut de ce document :** nouvel ordre proposé, pas adoption définitive des variantes architecturales ni implémentation des 46 lots.
