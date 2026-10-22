# SUIVI — Universal Agent Platform / Bootstrap V5

> Instantané documentaire : la source de vérité pour les états GitHub est l'API live. Aucune autorité runtime d'agent n'est créée ici.

## Acquis et preuves
- Dépôt public `chainsolutions-wealthtech/universal-agent-platform`, branche `main` initialement au SHA `0b8b2e01e826b915a0c593d5d6545681e9316567`, protection ruleset dépôt `25599154` active, sans bypass.
- GitHub App `ChainSolutions Universal Gateway` (App ID `5417646`) et trois installations déclarées testées dans la sortie locale fournie par le propriétaire. Le fichier PEM n'est pas hébergé dans ce dépôt.
- Une unique branche `bootstrap/canonical-v5-foundation`, PR #1 **ouverte et prête pour revue**, sans fusion. CI `validate` requise par ruleset.
- Plan V5 complet, texte original de 20 sections, roadmap 46 lots, catalogue de 30 domaines, correspondance 20 sections et manifeste SHA-256 présents sur cette branche.
- Issue #2 créée pour revue. Une **session Claude Code distincte** a rendu un avis documentaire favorable avec réserves au HEAD `5b624efe56a5c7f4722b5532bd6fd037d6522271` ; commentaire GitHub `6328770309`. La revue GitHub correspondante porte l'état `COMMENTED` et ne vaut pas approbation formelle.

## Revue P1/P2 du bot GitHub déjà présent
- Un contrôle automatisé préexistant a formulé cinq remarques sur une ancienne version (1 P1 : clés privées ; 4 P2 : gouvernance, index, chemin historique de source et manifeste).
- Les cinq corrections ont été **publiées sur cette même branche**, sans toucher les fichiers archives V5 ni leur manifeste canonique.
- Dossier : `docs/reviews/PR_1_REMEDIATION_LOG_20261022.md`.
- Un chemin de référence historique `sources/TEXTE_COMPLEMENTAIRE_ORIGINAL_20261021.txt` est maintenant disponible, avec le **même blob Git** que le fichier canonique de `docs/archive/`.
- Validation renforcée des en-têtes de clés, extensions sensibles et tokens GitHub ; comparaison de tous les champs des deux index avec les annexes V5 ; liste exhaustive des 3 sources canoniques.
- Douze tests de régression négatifs/positifs sont présents dans `tests/test_canonical_bootstrap.py`, désormais exécutés par le workflow CI avant la validation documentaire.

## Programme directeur chronologique — proposition sur PR #1

- `docs/roadmap/PROGRAMME_CHRONOLOGIQUE_V5.md` : ordre prospectif documenté de **46 lots dans 10 vagues**, construit à partir du registre historique `ROADMAP_V5.json`, avec dépendances, critères de sortie, jalons et références.
- `docs/roadmap/REGISTRE_TACHES_V5.md` : **138 fiches de sous-tâches proposées** (3 par lot), non admises ni créées comme issues GitHub ; ne remplace pas la source canonique ni la mémoire runtime.
- La distinction `historique attesté / roadmap prévue / travaux réellement admis` est obligatoire. Le problème CI au dernier HEAD et les fils de revue restent bloquants pour la fusion ; **aucun lot industriel n'est déclaré DONE par cette publication**.

## Contrôles restant indispensables
- Constater le statut `SUCCESS` du dernier HEAD de la PR #1 **après** les corrections et les mises à jour de suivi.
- Faire revérifier les neuf corrections par un intervenant admissible distinct ; répondre et résoudre les neuf discussions GitHub selon leurs résultats.
- Recontrôler l'absence de secrets, les registres, le ruleset et la politique avant toute fusion ; une CI verte ne vaut pas avis indépendant.
- Maintenir l'exigence de confidentialité d'un dépôt public, ajouter à terme un scanner dédié et des approbations formelles configurées.
- La mémoire canonique runtime, la capture automatique des conversations, les identités/mandats vérifiés et l'orchestrateur **ne sont pas encore développés**.


## Revue complémentaire et CI — checkpoint du 22 octobre 2026
- Une seconde revue automatique GitHub a ajouté **quatre observations** après les cinq remarques initiales : jetons `ghr_` et jetons avec `_`, chemin `sources/SOURCE_MANIFEST.json`, contrôle de sécurité avant les tests PR et fichiers placés sous `__pycache__`.
- Ces quatre corrections ont été apportées **sur la même branche** ; 12 tests unitaires sont désormais présents (dont les tests des nouveaux formats et sous-répertoires). Le workflow contrôle le checkout avant et après l'exécution des tests.
- Les neuf remarques ont reçu une réponse explicative ; leurs fils sont **laissés ouverts** en attente de contre-revue.
- **Blocage restant :** GitHub Actions ne montre aucun `validate: success` sur le dernier HEAD corrigé. Ancien run attesté `39693813473`, commit `fbf4c81f50396f157d69c8d668b3c19262d8ad20` seulement. Aucune ancienne réussite n'est attribuée au dernier HEAD.
- Diagnostic détaillé : `docs/reviews/CI_TRIGGER_DIAGNOSTIC_20261022.md`. Cause racine non attestée ; contrôle des paramètres GitHub Actions et des éventuelles demandes d'approbation requis. Le fichier workflow n'est pas encore sur `main`.
- La revue distincte précédente est antérieure à ces correctifs ; pas de nouvelle approbation formelle, pas de permission runtime nouvelle, pas de fusion.

## Actualisation après revue automatique supplémentaire — 22 octobre 2026
- Le contrôle live de PR #1 a révélé **13 fils ouverts**, contre 9 lors du checkpoint précédent. Quatre remarques nouvelles concernent : bytecode Python généré et faux positifs au second scan CI ; exigence de preuves pour un lot `DONE` ; décompte périmé des fils de revue ; ancrage indépendant des empreintes d'archives.
- Les corrections précédemment consignées couvrent les neuf premières remarques ; les **quatre nouvelles ne sont pas encore remédiées ni contre-vérifiées**. Les précédentes réussites CI sont historiques et ne valident pas la révision actuelle.
- Le programme de construction proposé et le registre de tâches restent documentaires, prêts pour revue, **sans ouverture d'issues ni démarrage des lots**.

## Finalisation de la passerelle GitHub App — nouveau contrat documentaire
- `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` documente les faits réellement vérifiés, le périmètre de l'App #5417646, ses trois installations, les gates GA-00–GA-08 et leurs correspondances aux lots D00–D14.
- L'authentification locale et la création du dépôt ont fonctionné ; **ni la matrice finale des permissions réellement accordées, ni le broker durable, ni les webhooks signés, ni OAuth utilisateur, ni la couverture D00–D14 ne sont attestés**.
- Un audit local read-only `UNIVERSAL_GATEWAY_AUDIT_V1_1.zip` (V1 superseded pour exécution ; mapping API corrigé) est fourni en artefact de conversation et testé hors réseau (3 tests passés). L'audit des configurations privées exige une exécution locale avec la clé PEM **sans partage de secret**.
- Le validateur a reçu des durcissements supplémentaires : vérification des six colonnes des 46 lots chronologiques, refus d'IDs de sous-tâches supplémentaires, preuve requise pour `DONE`, états mémoire cohérents et environnement CI sans génération de bytecode. Les 16 tests sur branche **ne constituent pas** une CI verte au HEAD.
- **17 fils de revue étaient ouverts lors du dernier audit avant ce checkpoint**, dont un P1 sur l'absence de validation de sécurité depuis une source de confiance. Le contrôle CI de la PR au HEAD courant reste non attesté ; ne pas confondre tests ajoutés et tests exécutés.

## Exigences « tous les droits » et audit GA-00 — checkpoint documentaire du 22 octobre 2026

- `docs/github-app/CAHIER_DES_CHARGES_COMPLET.md` conserve **53 exigences cibles**, les **30 domaines V5** et les **20 passages du pipeline autonome**. Les droits maximaux sont un **objectif de couverture**, jamais une preuve de droits accordés à l'App ou aux agents.
- Le paquet d'inscription initial fournit **100 permissions candidates** (41 Repository, 38 Organization, 20 Account, 1 Enterprise) et **72 paramètres préremplis**. Noms/niveaux recopiés dans le cahier des charges avec empreinte de provenance ; **aucun octroi actuel n'est déduit de la liste**.
- `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` reste le propriétaire du **statut vérifié** ; son § 6 publie l'**audit partiel GA-00**, qui sépare sources historiques, preuves GitHub live sur notre dépôt et configuration App privée non attestée.
- `DEC-013` formalise l'instruction de consigner toute l'intention avant l'audit ; aucun token/PEM, permission, installation ou dépôt tiers n'a été modifié pour cette consignation.
- À contrôler en lecture seule depuis l'App réelle : `GET /app`, ses permissions, événements, trois installations et périmètres, config webhook expurgée et paramètres Actions ; sans preuve, le statut reste `NOT_VERIFIED`.
- La PR #1 reste **ouverte et non fusionnée**, ruleset actif, échec de preuve CI sur le dernier HEAD, revue indépendante et **tous** les fils ouverts à traiter. Ne pas confondre publication documentaire et réalisation GA-00–GA-08.

## Focus prioritaire GH-MAX — GitHub App seule, toutes permissions admissibles

- Instruction utilisateur `DEC-014` : **priorité à la finalisation complète** de `ChainSolutions Universal Gateway`, avec toutes les permissions GitHub éligibles, pas au lancement d'autres lots.
- Le cahier des charges conserve **100 permissions candidates historiques** (41 Repository, 38 Organization, 20 Account, 1 Enterprise). La référence REST GitHub consultée le 22 octobre 2026 indexe **80 rubriques de permissions** (33 Repository, 32 Organization, 14 User/Account, 1 Enterprise), répertoriées au § 10 du même cahier. Ces deux référentiels **ne sont pas directement comparables** et **80 n'est pas** un total de droits GitHub disponibles.
- Le contrat d'audit `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` § 7 détaille `GH-MAX-01 → GH-MAX-10`, de la confrontation officielle à la livraison auditable ; l'état courant de `GH-MAX-02/03` reste `NOT_VERIFIED`.
- Prochaine opération App : lecture seule de l'App ID `5417646` via `GET /app`, puis des **trois installations** et de leurs permissions réellement accordées. **Ne pas confondre le connecteur GitHub de ChatGPT avec notre propre App.**
- Aucune permission, installation, identité ou dépôt tiers modifié ; `main` ne doit pas être contournée. La CI manquante sur PR #1 reste bloquante pour fusionner, même si l'audit App peut progresser en parallèle.

## Projection exécutable GH-MAX — registre machine en préparation

- `docs/github-app/GH_MAX_EXECUTION_PLAN.json` est une **projection technique** (pas une seconde source de vérité) des dix actions déjà décrites au § 7.2 du contrat d'audit : dépendances, vérifications, garde-fous, preuves, blocages et champs de checkpoint. **Aucun état d'exécution réel n'y est affirmé**.
- `scripts/check_gateway_execution_plan.py` fournit validation documentaire et aperçu `--next` **sans effet sur GitHub** ; `tests/test_gateway_execution_plan.py` ajoute **8 tests** de sécurité de contrat.
- Les deux interrupteurs `execution_enabled` et `mutations_enabled` sont **désactivés** ; les dix tâches restent `PLANNED` non admises. Le futur moteur ne pourra exécuter qu'après autorisation et vérification d'état live.
- La CI du dernier HEAD PR #1 demeure non attestée ; les tests ajoutés et la vérification structurelle ponctuelle **ne sont pas** une preuve de GitHub Actions vert ou de production opérationnelle.

## GH-MAX-01 — rapprochement documentaire exécutable

- Script ajouté : `scripts/reconcile_gateway_permissions.py` — analyse en lecture seule les **100 permissions candidates historiques** et les **80 intitulés REST** présents dans le propriétaire documentaire `docs/github-app/CAHIER_DES_CHARGES_COMPLET.md`. Aucun jeton, aucun endpoint privé, aucune écriture ni approbation simulée.
- Résultat du rapprochement strict des intitulés par famille : **70 libellés normalisés correspondants**, **30 cas à rechercher dans GraphQL, Git, autres API ou alias** (10 Repository, 12 Organization, 8 Account ; 0 Enterprise). Les 30 cas **ne sont pas des droits supprimés** et les 70 correspondances ne sont **pas des droits accordés**.
- Contrôles ajoutés : `tests/test_gateway_permission_reconciliation.py` (**9 tests déclarés**) et étapes documentaires dans `.github/workflows/canonical-documentation.yml` avant la suite de régression. Avec les huit tests précédents `test_gateway_execution_plan.py`, cela fait **17 tests spécifiques Gateway déclarés** sur la branche.
- Le détail et le statut exacts restent dans `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` § 7.6, propriétaire de l'audit. **`GH-MAX-01 = DOCUMENTARY_PARTIAL`** et **`GA-00 = PARTIAL_EVIDENCE`**.
- **Les scripts ne sont pas encore attestés comme exécutés par GitHub Actions sur le HEAD de PR #1** ; les tests déclarés ne sont pas des tests réussis. Le blocage des contrôles au HEAD et la revue indépendante persistent.
- **Prochaine action App :** observation de `GET /app` et des trois installations sous l'identité réelle de l'App, sans export de PEM, puis poursuite du rapprochement des 30 cas restants.

## GH-MAX-01 — deuxième source officielle et périmètre restant

- Le cahier des charges `docs/github-app/CAHIER_DES_CHARGES_COMPLET.md` (§ 11) conserve **57 champs d'API officiels** du schéma d'émission des jetons GitHub App, catégorie documentaire distincte des 80 rubriques REST et des 100 candidats historiques.
- Le script `scripts/reconcile_gateway_permissions.py` compare ces deux références : **34 candidats dans les deux**, **36 REST uniquement**, **14 schéma de jeton uniquement**, **16 sans correspondance littérale** dans ces deux documents, toujours à investiguer.
- Détail/provenance des 16 cas et limite du rapprochement : `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` § 7.7. **84/100 = présence dans les références documentaires**, **pas** permissions accordées ou fonctionnelles. GH-MAX-01 reste `DOCUMENTARY_PARTIAL`.
- `tests/test_gateway_permission_reconciliation.py` déclare désormais **11 tests** (soit 19 tests Gateway nouveaux avec les 8 du DAG), mais aucun résultat Actions du dernier HEAD n'est encore disponible.
- GH-MAX-02 et GH-MAX-03 nécessitent toujours l'audit privé en lecture seule de l'App #5417646 et de ses trois installations depuis l'environnement où la clé est stockée. Ne transmettre que les résultats expurgés ; ne pas publier les secrets.

## GH-MAX-01 — cinq cas spécialisés documentés, onze restant à étudier

- Sources GitHub spécialisées trouvées pour cinq candidats historiques supplémentaires : `agent_tasks`, `license_compliance_alerts`, `repository_license_policy`, `secret_scanning_alert_dismissal_requests`, `secret_scanning_push_protection_bypass_requests`.
- La comparaison dans `scripts/reconcile_gateway_permissions.py` couvre à présent **trois familles de documentation** : 80 intitulés REST, 57 champs d'émission de jeton, cinq sources spécialisées. **89/100 candidats possèdent au moins une correspondance documentaire** ; **11 restent ouverts** (3 Organization, 8 Account).
- `agent_tasks` peut impliquer Copilot Business/Enterprise et un UAT, **pas un IAT** : facultatif, aucune dépendance imposée à Codex/Copilot.
- `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` § 7.8 est propriétaire du résultat, toujours `GH-MAX-01 DOCUMENTARY_PARTIAL`. Les 89 cas ne constituent **pas** 89 permissions activées.
- `tests/test_gateway_permission_reconciliation.py` possède désormais **13 tests déclarés** (21 tests Gateway ajoutés avec les huit du DAG) ; pas encore de réussite GitHub Actions attestée au HEAD de PR #1.
- Les permissions privées de l'App et des trois installations restent `NOT_VERIFIED`, `GH-MAX-02/03` et `GA-00` incomplets.

## GH-MAX-01 — alias officiels documentés, neuf cas restant à qualifier

- Deux correspondances fonctionnelles supplémentaires ont été établies à partir des API GitHub App officielles : `account/blocking` → `Block another user` (`UAT`) et `organization/organization_actions_variables` → capacité `Variables` organisation (`UAT/IAT`).
- **91/100** candidats historiques ont maintenant une correspondance documentaire au moins ; **9** restent à examiner (2 Organization, 7 Account). Les paramètres techniques historiques ne sont pas automatiquement les noms configurables aujourd'hui.
- Le tableau canonique de preuves et des restrictions est dans `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` § 7.9 ; les deux nouveaux alias sont sourcés au §13 de `docs/github-app/CAHIER_DES_CHARGES_COMPLET.md`.
- Les permissions mentionnées dans un guide de **PAT fine-grained** ne constituent pas une preuve des permissions disponibles pour une **GitHub App**. Aucun droit App ou utilisateur n'est déduit du simple libellé.
- `scripts/reconcile_gateway_permissions.py` inclut la quatrième famille de preuves et `tests/test_gateway_permission_reconciliation.py` déclare **15 tests** (23 tests spécifiques Gateway avec les huit du DAG) ; l'exécution Actions au dernier HEAD reste non attestée.
- Prochain blocage : `GH-MAX-02/03` audit de l'App #5417646 avec clé gardée localement, puis droits effectivement octroyés et approbations. **Aucun nouveau droit activé**, aucune action sur MCP ou GRT.

## NEXT_ACTION
`RESTORE_REQUIRED_GITHUB_ACTIONS_VALIDATE_ON_PR_1_HEAD`

Gates de fusion : règles GitHub actives ; `validate` sur HEAD courant ; **tous les fils de revue ouverts résolus** ; validation gouvernée admissible attestée ; aucun bypass. **Aucun merge automatique depuis ce checkpoint.**

Les projets `Patricked-code/MCP` et `chainsolutions-wealthtech/Governed-Repository-Template` conservent leurs identités, gouvernances et autorisations distinctes.
