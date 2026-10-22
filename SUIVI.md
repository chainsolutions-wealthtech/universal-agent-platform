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

## NEXT_ACTION
`RESTORE_REQUIRED_GITHUB_ACTIONS_VALIDATE_ON_PR_1_HEAD`

Gates de fusion : règles GitHub actives ; `validate` sur HEAD courant ; **tous les fils de revue ouverts résolus** ; validation gouvernée admissible attestée ; aucun bypass. **Aucun merge automatique depuis ce checkpoint.**

Les projets `Patricked-code/MCP` et `chainsolutions-wealthtech/Governed-Repository-Template` conservent leurs identités, gouvernances et autorisations distinctes.
