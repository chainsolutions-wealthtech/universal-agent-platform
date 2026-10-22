# Registre de tâches V5 — décomposition chronologique des 46 lots

**Version :** proposition 22 octobre 2026, enregistrée sur la branche PR #1.  
**Statut :** `TASK_SPECIFICATIONS_DRAFT` — ce document n'est **ni un ticket GitHub ouvert**, ni un agent, ni une session, ni une tâche runtime admise.  
**Source canonique des identifiants et acceptations :** `docs/roadmap/ROADMAP_V5.json`.  
**Source canonique de l'ordre proposé :** `docs/roadmap/PROGRAMME_CHRONOLOGIQUE_V5.md`. Ce document possède uniquement la **décomposition de chaque lot en tâches proposées**, pas leur état courant.

## Mode de consommation

1. Lire `00_START_HERE.md`, puis `state/CURRENT_STATE.json`, `SUIVI.md`, `PROGRAMME_CHRONOLOGIQUE_V5.md` et `ROADMAP_V5.json`.
2. Vérifier l'autorité GitHub live, les dépendances de chaque lot, le mandat et les issues **existantes** avant d'admettre une tâche ; une fiche ci-dessous **n'autorise rien**.
3. Traiter les tâches `LOT-01`, `LOT-02`, `LOT-03` comme des **spécifications provisoires de 3 tranches**. Elles peuvent devenir des issues dans une future vague gouvernée, après déduplication et revue, **sans créer les 138 issues aujourd'hui**.
4. Pour chaque tâche admise : définir l'identité opérateur, l'autorité par projet, le SHA de départ, critères d'acceptation, tests, PR, état de review, preuves `proof_refs`, checkpoint/handoff et `NEXT_ACTION`.
5. Distinguer `PLANNED`, `ADMITTED`, `IN_PROGRESS`, `BLOCKED`, `VERIFIED`, `DONE`, `SUPERSEDED` dans le futur moteur d'exécution, sans écraser le `PLANNED` historique de la roadmap faute de preuves.
6. `B19` sécurité et `B23` documentation sont **transversaux en continu** depuis la première vague ; leur position de clôture n'est pas une permission d'attendre la fin pour sécuriser/documenter.

## Gate préalable hors lots

**`BOOTSTRAP-PR1-G0`** — rétablir le check `validate` sur la révision courante de PR #1, examiner les neuf fils de revue, corriger et obtenir contre-revue, puis intégrer via les protections GitHub applicables. Ce gate doit être satisfait **avant d'engager l'usine autonome sur main** ; les lectures et la préparation documentaire non destructives restent permises.

## Détails de tâches par vague et par lot

### P00 — B00

#### B00 — Inventaire GitHub/MCP/GRT/projets, états, outils, archives disponibles

**Préconditions source :** Autorisation lecture.  
**Critère d'acceptation V5 :** Carte des autorités et preuves.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B00-01` — INVENTORIER / SPÉCIFIER :** Recenser les sources et autorités explicitement accessibles en lecture seule, avec limites de mandat.
- **`B00-02` — CONSTRUIRE / INTÉGRER :** Établir la matrice composants/projets/états/risques sans écritures MCP ou GRT.
- **`B00-03` — VÉRIFIER / ATTESTER :** Faire contrôler les références HEAD et les écarts d'inventaire.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

### P01 — B01 · B02 · D00 · F00 · B23

#### B01 — Exigences et architecture de référence

**Préconditions source :** B00.  
**Critère d'acceptation V5 :** Architecture + décisions + matrice de traçabilité.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B01-01` — INVENTORIER / SPÉCIFIER :** Extraire les exigences des plans A/B/C/D et du programme AGSREF sans inventer de décision.
- **`B01-02` — CONSTRUIRE / INTÉGRER :** Comparer architectures B/E et contrats, enregistrer alternatives et arbitrages à approuver.
- **`B01-03` — VÉRIFIER / ATTESTER :** Vérifier la traçabilité exigences→conceptions→tests avant toute ADR définitive.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B02 — Schémas canoniques

**Préconditions source :** B01.  
**Critère d'acceptation V5 :** JSON Schema/OpenAPI, validation.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B02-01` — INVENTORIER / SPÉCIFIER :** Définir les entités et identifiants distincts (agent, session, mandat, mission, tâche).
- **`B02-02` — CONSTRUIRE / INTÉGRER :** Écrire JSON Schema/OpenAPI et contrats d'événements versionnés.
- **`B02-03` — VÉRIFIER / ATTESTER :** Tester schémas, cardinalités, cas invalides et évolutions compatibles.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D00 — Inventaire complet GitHub App et capacités

**Préconditions source :** B00.  
**Critère d'acceptation V5 :** Catalogue doc → endpoint → token → test.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D00-01` — INVENTORIER / SPÉCIFIER :** Inventorier les permissions GitHub App, User, Org et Enterprise éligibles.
- **`D00-02` — CONSTRUIRE / INTÉGRER :** Lier permission→endpoint→type de token→installation→test autorisé.
- **`D00-03` — VÉRIFIER / ATTESTER :** Distinguer attesté, prévu, refusé et indisponible sans déclarer 100%.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### F00 — Bootstrap durable de l'usine d'ingénierie elle-même

**Préconditions source :** B00 + workspace autorisé.  
**Critère d'acceptation V5 :** Reprise après arrêt du moteur IA.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`F00-01` — INVENTORIER / SPÉCIFIER :** Définir le bootstrap persistant minimal, indépendant d'une conversation.
- **`F00-02` — CONSTRUIRE / INTÉGRER :** Implémenter la reprise d'un travail de construction dans un LAB, avec journal provisoire.
- **`F00-03` — VÉRIFIER / ATTESTER :** Démontrer crash/reprise sans déclarer prématurément B09 complet.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B23 — Documentation et migrations

**Préconditions source :** En continu.  
**Critère d'acceptation V5 :** Guides et runbooks complets.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B23-01` — INVENTORIER / SPÉCIFIER :** Définir documentation par rôle et point de reprise canonique unique.
- **`B23-02` — CONSTRUIRE / INTÉGRER :** Maintenir runbooks/migrations à chaque changement de lot.
- **`B23-03` — VÉRIFIER / ATTESTER :** Vérifier liens, README de reprise, provenance et version des contrats.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

### P02 — B03 · B04 · B05 · B10

#### B03 — Catalogue d'identités

**Préconditions source :** B02.  
**Critère d'acceptation V5 :** Resolver versionné + unicité.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B03-01` — INVENTORIER / SPÉCIFIER :** Relever les identités historiques sans en créer de nouvelles.
- **`B03-02` — CONSTRUIRE / INTÉGRER :** Développer RESOLVE/VERIFY/ALIAS avec unicité et namespaces.
- **`B03-03` — VÉRIFIER / ATTESTER :** Tester résolution répétée et rejets de collision.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B04 — Blueprints, compétences et affectations

**Préconditions source :** B02–03.  
**Critère d'acceptation V5 :** Contrat agent/projet/mission.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B04-01` — INVENTORIER / SPÉCIFIER :** Formaliser blueprints, compétences et affectations distincts des agents.
- **`B04-02` — CONSTRUIRE / INTÉGRER :** Implémenter registry versionné, références aux mandats et scopes.
- **`B04-03` — VÉRIFIER / ATTESTER :** Tester réaffectation sans changement d'identité ni élévation implicite.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B05 — Event ledger immuable logique

**Préconditions source :** B02.  
**Critère d'acceptation V5 :** Inbox/outbox et traçabilité.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B05-01` — INVENTORIER / SPÉCIFIER :** Définir l'enveloppe des événements, causalité, provenance et idempotence.
- **`B05-02` — CONSTRUIRE / INTÉGRER :** Implémenter append-only, inbox/outbox, signatures et projections préliminaires.
- **`B05-03` — VÉRIFIER / ATTESTER :** Tester duplications, crash durant publication et relecture intègre.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B10 — Gouvernance et moteur d'autorisation

**Préconditions source :** B02–05.  
**Critère d'acceptation V5 :** Decision API + refus explicites.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B10-01` — INVENTORIER / SPÉCIFIER :** Définir politique par projet, mandat, ressource, action et identité.
- **`B10-02` — CONSTRUIRE / INTÉGRER :** Implémenter décision d'autorisation vérifiable avec refus par défaut.
- **`B10-03` — VÉRIFIER / ATTESTER :** Tester refus, expiration, révocation, absence d'élévation par un document.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

### P03 — B06 · F01 · B07 · B08 · B09 · F02

#### B06 — Mémoire, références et snapshots

**Préconditions source :** B05.  
**Critère d'acceptation V5 :** Projections et restauration.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B06-01` — INVENTORIER / SPÉCIFIER :** Définir politiques d'archivage, références et frontières données publiques/privées.
- **`B06-02` — CONSTRUIRE / INTÉGRER :** Implémenter snapshots/projections, stockage privé des originaux et liens de provenance.
- **`B06-03` — VÉRIFIER / ATTESTER :** Tester restauration et détection d'incohérences de versions.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### F01 — Conversation Capture & Canonicalization Pipeline

**Préconditions source :** B02,B05.  
**Critère d'acceptation V5 :** Capture vérifiée depuis ≥1 source réellement accessible.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`F01-01` — INVENTORIER / SPÉCIFIER :** Identifier les sources de conversations effectivement accessibles et autorisées.
- **`F01-02` — CONSTRUIRE / INTÉGRER :** Capturer originaux dans un stockage privé et produire références/provenance.
- **`F01-03` — VÉRIFIER / ATTESTER :** Vérifier échantillon d'intégrité, droits d'accès et absence d'archive fictive.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B07 — Session rebinding / conversation binding

**Préconditions source :** B03–06.  
**Critère d'acceptation V5 :** Reprise nouvelle conversation.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B07-01` — INVENTORIER / SPÉCIFIER :** Définir les contrats conversation→session→agent et la politique de rebinding.
- **`B07-02` — CONSTRUIRE / INTÉGRER :** Implémenter recherche d'identité, rattachement de conversation et anti-collision.
- **`B07-03` — VÉRIFIER / ATTESTER :** Tester nouvelle conversation sur mandat existant, sans session concurrente fictive.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B08 — Moteur de continuité et checkpoints

**Préconditions source :** B05–07.  
**Critère d'acceptation V5 :** Handoffs et NEXT_ACTION attestés.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B08-01` — INVENTORIER / SPÉCIFIER :** Définir machines à états de continuité, handoff et NEXT_ACTION.
- **`B08-02` — CONSTRUIRE / INTÉGRER :** Implémenter checkpoint atomique et restauration/réconciliation des états.
- **`B08-03` — VÉRIFIER / ATTESTER :** Tester interruption/réentrée/rejeu et preuve du dernier checkpoint.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B09 — Missions, tâches et workflows durables

**Préconditions source :** B02,B05,B08.  
**Critère d'acceptation V5 :** DAG + leases + retries.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B09-01` — INVENTORIER / SPÉCIFIER :** Définir DAG, statuts, tâches, leases, retry et budgets sous B08.
- **`B09-02` — CONSTRUIRE / INTÉGRER :** Implémenter moteur durable et récupération d'actions réservées.
- **`B09-03` — VÉRIFIER / ATTESTER :** Tester crash/reprise sur une même tâche sans effets secondaires dupliqués.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### F02 — Canonical Memory Verifier Adapter

**Préconditions source :** B06,F01.  
**Critère d'acceptation V5 :** Bundles valides/invalides testés.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`F02-01` — INVENTORIER / SPÉCIFIER :** Formaliser bundles canoniques valides et invalides et invariants.
- **`F02-02` — CONSTRUIRE / INTÉGRER :** Implémenter vérificateur mémoire indépendant de la génération IA.
- **`F02-03` — VÉRIFIER / ATTESTER :** Tester rejets de corruption, doublons et provenance ambiguë.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

### P04 — D01 · D02 · D03 · D04 · D05 · D06 · D13

#### D01 — Authentification App/IAT/UAT multi-comptes

**Préconditions source :** D00,B10.  
**Critère d'acceptation V5 :** Trois installations et token mapping prouvé.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D01-01` — INVENTORIER / SPÉCIFIER :** Vérifier l'App 5417646, les trois installations, scopes réellement accordés et rotation.
- **`D01-02` — CONSTRUIRE / INTÉGRER :** Implémenter broker JWT→token installation et flux user OAuth séparé lorsque mandaté.
- **`D01-03` — VÉRIFIER / ATTESTER :** Tester expiry, scoping minimal et absence de secrets dans logs/dépôt.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D02 — Repositories/Git/code/branches/PR

**Préconditions source :** D01.  
**Critère d'acceptation V5 :** Cycle repo→PR→checks en sandbox.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D02-01` — INVENTORIER / SPÉCIFIER :** Spécifier Git/REST/GraphQL repos, branches, commits et PR sur LAB.
- **`D02-02` — CONSTRUIRE / INTÉGRER :** Implémenter opérations testables avec idempotence et politique par installation.
- **`D02-03` — VÉRIFIER / ATTESTER :** Tester cycle complet repo→branche→PR et règles de protection.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D03 — Issues et GitHub Projects

**Préconditions source :** D01,B09.  
**Critère d'acceptation V5 :** GraphQL mutation contract test.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D03-01` — INVENTORIER / SPÉCIFIER :** Spécifier Issues, dépendances, champs et GitHub Projects.
- **`D03-02` — CONSTRUIRE / INTÉGRER :** Implémenter lecture puis mutations sous scopes précis.
- **`D03-03` — VÉRIFIER / ATTESTER :** Tester absence de tickets doublons et contrats GraphQL réels.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D04 — Actions/Checks/CI/CD

**Préconditions source :** D02.  
**Critère d'acceptation V5 :** Workflow dispatch et suivi.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D04-01` — INVENTORIER / SPÉCIFIER :** Inventorier Actions/Checks, droits et politique du dernier HEAD.
- **`D04-02` — CONSTRUIRE / INTÉGRER :** Implémenter suivi/dispatch/retry autorisé et provenance des runs.
- **`D04-03` — VÉRIFIER / ATTESTER :** Tester workflow réel du LAB, succès/échec/timeout et gates de PR.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D05 — Sécurité/attestations/scanning

**Préconditions source :** D02,D04.  
**Critère d'acceptation V5 :** Alertes et preuves fiables.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D05-01` — INVENTORIER / SPÉCIFIER :** Distinguer secret scanning, Dependabot, CodeQL, attestations et entitlements.
- **`D05-02` — CONSTRUIRE / INTÉGRER :** Intégrer scanners réellement disponibles et alertes gouvernées.
- **`D05-03` — VÉRIFIER / ATTESTER :** Tester détection/triage/traitement sans inventer un produit souscrit.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D06 — Administration/properties/org

**Préconditions source :** D01,B10.  
**Critère d'acceptation V5 :** Drift detection + correction approuvée.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D06-01` — INVENTORIER / SPÉCIFIER :** Définir comparaison live↔policy des règles repo/org et propriétés.
- **`D06-02` — CONSTRUIRE / INTÉGRER :** Implémenter observation de drift et correction seulement après autorisation.
- **`D06-03` — VÉRIFIER / ATTESTER :** Tester protection main sans bypass et restauration de configuration.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D13 — GitHub capability drift watch

**Préconditions source :** D00,D01.  
**Critère d'acceptation V5 :** Détection des évolutions GitHub.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D13-01` — INVENTORIER / SPÉCIFIER :** Définir snapshot versionné des permissions/capacités GitHub.
- **`D13-02` — CONSTRUIRE / INTÉGRER :** Détecter dérive API/permissions et entitlements sans write automatique.
- **`D13-03` — VÉRIFIER / ATTESTER :** Tester alertes et rejets des capacités retirées.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

### P05 — B11 · B12 · B13 · B15 · F03 · D07 · D08 · D09 · D10

#### B11 — Communication interagents

**Préconditions source :** B05,B09–10.  
**Critère d'acceptation V5 :** Messages, corrélation, DLQ.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B11-01` — INVENTORIER / SPÉCIFIER :** Inventorier les bus et flux existants pour éviter tout canal concurrent.
- **`B11-02` — CONSTRUIRE / INTÉGRER :** Implémenter messages corrélés, ACK, retry, dead letter et déduplication.
- **`B11-03` — VÉRIFIER / ATTESTER :** Tester répétitions, pannes et absence de collision interagents.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B12 — Adaptateur MCP et outillage

**Préconditions source :** B10–11.  
**Critère d'acceptation V5 :** Tools bridge avec droits vérifiés.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B12-01` — INVENTORIER / SPÉCIFIER :** Inventorier contrats des outils MCP autorisés sans reprendre leur gouvernance.
- **`B12-02` — CONSTRUIRE / INTÉGRER :** Implémenter adaptateur d'outils avec vérification de scopes et preuves.
- **`B12-03` — VÉRIFIER / ATTESTER :** Tester rejet hors mandat, erreurs, timeouts et audit.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B13 — Intégration GitHub

**Préconditions source :** B10,D01–D03.  
**Critère d'acceptation V5 :** App broker, API, webhooks.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B13-01` — INVENTORIER / SPÉCIFIER :** Définir les contrats de l'adaptateur GitHub sur les capacités D01–D03.
- **`B13-02` — CONSTRUIRE / INTÉGRER :** Implémenter résolveur de capacités et opérations sous installation appropriée.
- **`B13-03` — VÉRIFIER / ATTESTER :** Tester repo/PR/issues sur LAB sans dépassement de scopes.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B15 — Fédération agent-agent/A2A

**Préconditions source :** B03,B11.  
**Critère d'acceptation V5 :** Interop optionnelle testée.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B15-01` — INVENTORIER / SPÉCIFIER :** Formaliser découverte A2A et restrictions entre agents/fournisseurs.
- **`B15-02` — CONSTRUIRE / INTÉGRER :** Implémenter adaptateur fédéré optionnel aux interfaces vérifiées.
- **`B15-03` — VÉRIFIER / ATTESTER :** Tester délégation tracée et refus de fédération non autorisée.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### F03 — Multi-Provider Agent Gateway

**Préconditions source :** B03,B08,B10.  
**Critère d'acceptation V5 :** Mission reprise par deux moteurs compatibles.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`F03-01` — INVENTORIER / SPÉCIFIER :** Définir interface fournisseur IA et gestion des contextes.
- **`F03-02` — CONSTRUIRE / INTÉGRER :** Intégrer au moins deux moteurs autorisés via adaptateurs interchangeables.
- **`F03-03` — VÉRIFIER / ATTESTER :** Tester reprise du même agent/mission entre fournisseurs, scopes inchangés.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D07 — Webhook Receiver/Event Bus

**Préconditions source :** D01,B05,B11.  
**Critère d'acceptation V5 :** HMAC, queue, replay, déduplication.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D07-01` — INVENTORIER / SPÉCIFIER :** Définir schémas webhooks, HMAC, corrélation et rejeu.
- **`D07-02` — CONSTRUIRE / INTÉGRER :** Implémenter receiver sûr relié au bus commun sans bus concurrent.
- **`D07-03` — VÉRIFIER / ATTESTER :** Tester replay, déduplication, panne et rotation du secret.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D08 — Packages/Pages/releases/discussions/etc.

**Préconditions source :** D02,D04.  
**Critère d'acceptation V5 :** APIs choisies testées.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D08-01` — INVENTORIER / SPÉCIFIER :** Sélectionner APIs Packages, Pages, Releases et Discussions réellement utilisables.
- **`D08-02` — CONSTRUIRE / INTÉGRER :** Construire adaptateurs progressifs plutôt qu'activer toutes les permissions.
- **`D08-03` — VÉRIFIER / ATTESTER :** Tester opérations représentatives par domaine et scopes.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D09 — Account OAuth/delegation

**Préconditions source :** D01,B10.  
**Critère d'acceptation V5 :** UAT dédié, accord utilisateur réel.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D09-01` — INVENTORIER / SPÉCIFIER :** Définir besoins UAT, consentement, Device Flow/OAuth et révocation.
- **`D09-02` — CONSTRUIRE / INTÉGRER :** Implémenter authentification utilisateur distincte du token d'installation.
- **`D09-03` — VÉRIFIER / ATTESTER :** Tester consentement explicite, expiration, rotation et déconnexion.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D10 — Enterprise adapters optionnels

**Préconditions source :** D00,D01.  
**Critère d'acceptation V5 :** Seulement si plan et compte Enterprise validés.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D10-01` — INVENTORIER / SPÉCIFIER :** Vérifier existence effective d'un compte/abonnement Enterprise admissible.
- **`D10-02` — CONSTRUIRE / INTÉGRER :** Définir adaptateur optionnel ou documenter NOT_APPLICABLE sans imiter des droits.
- **`D10-03` — VÉRIFIER / ATTESTER :** Tester entitlements ou attester blocage sans forcer la fonctionnalité.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

### P06 — B14 · B16 · B17 · B18 · F04 · D11 · D12

#### B14 — Intégration serveurs

**Préconditions source :** B10,B12–13.  
**Critère d'acceptation V5 :** Accès serveur sans bypass.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B14-01` — INVENTORIER / SPÉCIFIER :** Définir les accès serveur/mcp/déploiements distincts de GitHub.
- **`B14-02` — CONSTRUIRE / INTÉGRER :** Implémenter adaptateur d'infrastructure sous mandat explicite.
- **`B14-03` — VÉRIFIER / ATTESTER :** Tester lecture et opérations LAB, refus d'accès production hors mandat.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B16 — Observabilité et audit

**Préconditions source :** B05,B09.  
**Critère d'acceptation V5 :** Traces et tableaux de bord.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B16-01` — INVENTORIER / SPÉCIFIER :** Définir logs/metrics/traces corrélés à agents/tâches/PR.
- **`B16-02` — CONSTRUIRE / INTÉGRER :** Implémenter observabilité et registre de preuves sans secrets.
- **`B16-03` — VÉRIFIER / ATTESTER :** Tester complétude des traces et restitution d'incident.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B17 — Console de supervision

**Préconditions source :** B03,B06,B09,B16.  
**Critère d'acceptation V5 :** Cockpit gouverné.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B17-01` — INVENTORIER / SPÉCIFIER :** Définir vues supervisées (agents, missions, droits, budgets, incidents).
- **`B17-02` — CONSTRUIRE / INTÉGRER :** Construire console limitée aux données autorisées par rôle.
- **`B17-03` — VÉRIFIER / ATTESTER :** Tester navigation, RBAC, données absentes et cohérence d'état.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B18 — Recovery et disaster recovery

**Préconditions source :** B05–09.  
**Critère d'acceptation V5 :** Scénarios de restauration.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B18-01` — INVENTORIER / SPÉCIFIER :** Établir scénarios de panne, sauvegarde et RPO/RTO cibles.
- **`B18-02` — CONSTRUIRE / INTÉGRER :** Implémenter restauration ledger/snapshots/leases et reprise contrôlée.
- **`B18-03` — VÉRIFIER / ATTESTER :** Tester recovery après interruption et absence de doubles effets.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### F04 — Production readiness / rollback controller

**Préconditions source :** B09,B14,B18.  
**Critère d'acceptation V5 :** Rollback vérifié en LAB.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`F04-01` — INVENTORIER / SPÉCIFIER :** Définir gates de préparation production, rollback et état d'incident.
- **`F04-02` — CONSTRUIRE / INTÉGRER :** Implémenter contrôleur de déploiement réversible avec arrêt sûr.
- **`F04-03` — VÉRIFIER / ATTESTER :** Tester rollback en LAB et preuves d'intégrité après restauration.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D11 — Déploiements, infra externe et servers

**Préconditions source :** D04,B14.  
**Critère d'acceptation V5 :** Version de prod attestée.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D11-01` — INVENTORIER / SPÉCIFIER :** Définir contrats de déploiement GitHub et infrastructures sous mandat.
- **`D11-02` — CONSTRUIRE / INTÉGRER :** Intégrer pipelines LAB, rollback et contrôle de production.
- **`D11-03` — VÉRIFIER / ATTESTER :** Tester release et rollback observables avant élargissement.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D12 — Multi-repo analytics et pilotage

**Préconditions source :** D02–08,B16.  
**Critère d'acceptation V5 :** KPIs sourcés et contrôlables.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D12-01` — INVENTORIER / SPÉCIFIER :** Définir KPI GitHub multi-comptes avec source et périmètre.
- **`D12-02` — CONSTRUIRE / INTÉGRER :** Construire indicateurs versionnés (commits, CI, issues, coûts, incidents).
- **`D12-03` — VÉRIFIER / ATTESTER :** Vérifier données, écarts, latences et permissions par compte.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

### P07 — B19 · B20 · B21 · B22

#### B19 — Security hardening

**Préconditions source :** Tous lots concernés.  
**Critère d'acceptation V5 :** Threat model et scans.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B19-01` — INVENTORIER / SPÉCIFIER :** Modéliser menaces par frontière de confiance, secrets et supply chain.
- **`B19-02` — CONSTRUIRE / INTÉGRER :** Appliquer durcissements aux lots réellement construits, sans permissions globales implicites.
- **`B19-03` — VÉRIFIER / ATTESTER :** Vérifier scans, séparation des comptes, tests adversariaux et exceptions.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B20 — Performance et charge

**Préconditions source :** B09,B13.  
**Critère d'acceptation V5 :** Tests et limites quantifiées.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B20-01` — INVENTORIER / SPÉCIFIER :** Mesurer les chemins critiques des tâches, GitHub API et mémoire.
- **`B20-02` — CONSTRUIRE / INTÉGRER :** Définir limites et optimiser goulots prouvés, pas des hypothèses.
- **`B20-03` — VÉRIFIER / ATTESTER :** Tester charge, quotas, saturation et coûts par scénario.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B21 — Résilience et chaos tests

**Préconditions source :** B18–20.  
**Critère d'acceptation V5 :** Pannes simulées et recovery.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B21-01` — INVENTORIER / SPÉCIFIER :** Définir scénarios de chaos : panne DB, réseau, broker, worker.
- **`B21-02` — CONSTRUIRE / INTÉGRER :** Exécuter incidents contrôlés en LAB, puis restaurer.
- **`B21-03` — VÉRIFIER / ATTESTER :** Prouver idempotence, cohérence finale et traçabilité.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### B22 — Pilotes d'intégration

**Préconditions source :** B10–21.  
**Critère d'acceptation V5 :** Pilotes MCP/GRT indépendants.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B22-01` — INVENTORIER / SPÉCIFIER :** Sélectionner des pilotes strictement autorisés, commencer en lecture seule.
- **`B22-02` — CONSTRUIRE / INTÉGRER :** Intégrer graduellement un projet sans déplacer son autorité.
- **`B22-03` — VÉRIFIER / ATTESTER :** Auditer les pilotes, annulations, non-régression et consentements.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

### P08 — B24 · D14

#### B24 — Vérification indépendante

**Préconditions source :** B19–23.  
**Critère d'acceptation V5 :** Conformance report externe.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B24-01` — INVENTORIER / SPÉCIFIER :** Constituer un dossier indépendant : sources, CI, tests, décisions.
- **`B24-02` — CONSTRUIRE / INTÉGRER :** Faire examiner par réviseur distinct et gérer changements demandés.
- **`B24-03` — VÉRIFIER / ATTESTER :** Publier un rapport de conformité traçable et borné.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

#### D14 — Audit couverture fonctionnelle finale

**Préconditions source :** D00–13,B24.  
**Critère d'acceptation V5 :** Matrice 30 domaines et anomalies ouvertes.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`D14-01` — INVENTORIER / SPÉCIFIER :** Consolider matrice finale de 30 domaines et 15 lots D.
- **`D14-02` — CONSTRUIRE / INTÉGRER :** Faire auditer fonctionnalités, trous de couverture et exceptions justifiées.
- **`D14-03` — VÉRIFIER / ATTESTER :** Produire verdict de couverture sans pourcentage non attesté.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).

### P09 — B25

#### B25 — Livraison, état final, exploitation

**Préconditions source :** B24.  
**Critère d'acceptation V5 :** Release attestée, mode RUNNING.  
**État source au 22 octobre :** `PLANNED` (**à qualifier**, ne pas déduire `DONE` de preuves de bootstrap).

- **`B25-01` — INVENTORIER / SPÉCIFIER :** Préparer la release, critères de prod, restauration et exploitation.
- **`B25-02` — CONSTRUIRE / INTÉGRER :** Effectuer livraison uniquement après gates et approbation applicables.
- **`B25-03` — VÉRIFIER / ATTESTER :** Attester état RUNNING réel, monitoring, runbooks et NEXT_ACTION.

**Gate de sortie :** sources et décisions citées, périmètre d'autorité valide, tests/CI pertinents, revue proportionnée, aucune régression non traitée, `proof_refs` vérifiés, handoff et `NEXT_ACTION` (ou statut `BLOCKED/N/A` justifié).


## Garde-fous de planification

- Les sous-tâches sont des **propositions de travail**, non des identités, affectations ou permissions.
- Ne pas créer de queues ou de bus de communication concurrents à l'existant.
- Le premier scenario LAB de bout en bout devra se terminer par une reprise après crash sans doublon.
- La CI d'une ancienne révision ne justifie jamais un état `DONE` pour le HEAD courant.
- Tous les originaux confidentiels restent dans un stockage privé protégé et hors Git public.
- Les décisions d'architecture non approuvées (notamment B vs E) restent ouvertes ; ne pas créer les ADR comme déjà adoptées.
- À chaque acceptation d'un lot, mettre à jour **son propriétaire canonique** après observation des preuves, puis seulement le routage global / prochain gate.
