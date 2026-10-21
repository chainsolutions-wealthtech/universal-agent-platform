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
- Dix tests de régression négatifs/positifs ont été ajoutés dans `tests/test_canonical_bootstrap.py`, désormais exécutés par le workflow CI avant la validation documentaire.

## Contrôles restant indispensables
- Constater le statut `SUCCESS` du dernier HEAD de la PR #1 **après** les corrections et les mises à jour de suivi.
- Faire revérifier les cinq corrections par un intervenant admissible distinct ; répondre et résoudre les cinq discussions GitHub selon leurs résultats.
- Recontrôler l'absence de secrets, les registres, le ruleset et la politique avant toute fusion ; une CI verte ne vaut pas avis indépendant.
- Maintenir l'exigence de confidentialité d'un dépôt public, ajouter à terme un scanner dédié et des approbations formelles configurées.
- La mémoire canonique runtime, la capture automatique des conversations, les identités/mandats vérifiés et l'orchestrateur **ne sont pas encore développés**.

## NEXT_ACTION
`VERIFY_REMEDIATION_CI_AND_REQUEST_INDEPENDENT_RE_REVIEW_PR_1`

Gates de fusion : règles GitHub actives ; `validate` sur HEAD courant ; cinq discussions résolues ; validation gouvernée admissible attestée ; aucun bypass. **Aucun merge automatique depuis ce checkpoint.**

Les projets `Patricked-code/MCP` et `chainsolutions-wealthtech/Governed-Repository-Template` conservent leurs identités, gouvernances et autorisations distinctes.
