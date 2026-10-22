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
