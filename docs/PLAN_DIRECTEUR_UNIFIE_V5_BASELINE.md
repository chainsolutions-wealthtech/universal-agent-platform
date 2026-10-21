# Plan directeur unifié V5 — Baseline de bootstrap

**Nature :** synthèse de travail additive, sans remplacement du dossier complet V5 conservé comme artefact séparé.  
**Source temporelle :** consolidation du 21 octobre 2026 ; mise à jour du statut de création du dépôt après le journal GitHub du 21 octobre.  
**Statut :** proposition documentaire à relire avant fusion. **Ce fichier ne reproduit pas encore intégralement les 67 Ko du plan V5 ni le texte original de 20 sections.**

## Objectif fondateur
Un agent déjà constitué doit pouvoir être **résolu, identifié, vérifié, repris** et chargé d'une mission existante depuis toute conversation ou moteur IA autorisé, avec rôles, mandats, checkpoints, historique, NEXT_ACTION et permissions **effectivement attestées**, sans identité concurrente. Les fournisseurs d'IA sont interchangeables ; la plateforme conserve les registres et les sources d'autorité.

## Plans conservés
- **A — Universal Multi-Agent Platform :** identités, blueprints, affectations, missions, sessions, registres, mémoire, politiques, communication et observabilité ; séparation des gouvernances des projets.
- **B — Autonomous Governed Self-Resuming Engineering Factory :** lots historiques 00–25 ; inventaire, comparaison d'architectures, conception, code, tests, revue indépendante, CI, récupération, livraison, budgets et reprise après interruption.
- **C — GitHub App & Bootstrap :** GitHub App `ChainSolutions Universal Gateway`, installations par compte, auth broker sécurisé, registre des permissions réellement vérifiées, dépôt public, fondation documentaire et intégration MCP.
- **D — GitHub Full-Capability Automation :** inventaire de toutes les grandes fonctionnalités GitHub et intégration progressive des endpoints REST/GraphQL/Git, GitHub Projects, Issues, PR, Actions, packages, Pages, sécurité, déploiements, Account/Organization/Enterprise et webhooks.

La version consolidée prévoit **46 lots planifiés** (26 historiques, 5 extensions de fondation et 15 extensions GitHub) : ce chiffre est une cible de planification, non des travaux exécutés. Le détail exhaustif reste dans l'artefact V5 à importer et auditer.

## Architecture logique
1. **AI Provider Gateway** : ChatGPT, Claude et autres moteurs indépendants ; aucun moteur n'est source unique de vérité.
2. **Global Identity & Capability Registry** : identités, blueprints, affectations, mandats, périmètres et permissions contextuelles.
3. **Canonical Memory & Capture** : sources originales réellement capturées, ledger d'événements append-only, provenance, décision/supersession, projection CURRENT_STATE.
4. **Continuity/Resume** : résolution d'identité, session rebinding, checkpoints, handoffs, vérification d'autorité live et NEXT_ACTION.
5. **Durable Orchestration Engine** : DAG, réservations, leases, concurrence, retry bornés, idempotence, compensation et états terminaux.
6. **Communication Bus** : événements corrélés, déduplication, ACK, dead letter, routage, audit ; intégrer aux systèmes existants sans créer de bus concurrent non autorisé.
7. **GitHub Capability & Authentication Gateway** : identités d'app, JWT, installations, jetons temporaires, OAuth utilisateur, webhooks signés, catalogue de capacités.
8. **MCP/Infrastructure Gateway** : serveurs, Docker, Plesk, bases, DNS, GitHub Actions et déploiements uniquement sous autorisations distinctes.
9. **Independent Quality, Security & Audit** : tests, statuts, contrôles anti-régression, journaux, traces, coûts, alertes et preuves.
10. **Universal Control Center** : état des agents, projets, missions, droits, incidents, coûts et opérations.

## Couverture GitHub attendue
L'objectif est la couverture maximale **effective**, pas l'activation aveugle de permissions. Domaines : repositories, code, branches, commits, PR, issues, Projects, Actions, tests, sécurité, administration, déploiements, documentation, Pages, releases, packages, webhooks, comptes utilisateur, organisations, enterprise éligible, agents, mémoire, communication, gouvernance, audit, inter-dépôts, migration, infrastructure, portefeuille logiciel et supervision autonome.

Chaque capacité aura : identifiant, endpoint, type de jeton, permission, installation, éventuel entitlement, test runtime, politique, statut implémenté et preuve. Les permissions `Account` nécessitant un jeton utilisateur ne sont pas assimilées aux jetons d'installation. Les autorisations Enterprise sont conditionnelles aux produits souscrits.

## Ingénierie autonome
Cycle : intake → contexte → architecture → décomposition → réservation → branche → code → tests → CI → correction → review indépendante → sécurité → PR → approbations → fusion autorisée → déploiement autorisé → vérifications → preuves → checkpoint → prochaine action.

Aucun agent ne peut se déclarer auto-approuvé ou contourner les règles de protection ; une IA ne peut pas garantir zéro régression, seulement renforcer ses tests et contrôles.

## Non-régression et données
- Ne jamais fusionner automatiquement la gouvernance de `Patricked-code/MCP` avec celle de `chainsolutions-wealthtech/Governed-Repository-Template`.
- Ne pas copier les conversations brutes privées dans un dépôt public.
- Ne pas confondre la GitHub App avec une mémoire autonome, un processus 24/7 ni un droit universel d'administration.
- Ne pas présenter les 46 lots comme réalisés : ils sont planifiés.
- Préserver les textes sources complets, sous contrôle de confidentialité, et faire correspondre chaque décision à une provenance.
