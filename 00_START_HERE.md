# Point d'entrée — Universal Agent Platform

**Statut :** fondation documentaire proposée en Pull Request, **non encore fusionnée ou déclarée autorité runtime**.

## Mission
Construire une plateforme universelle multi-agents, multi-projets, multi-comptes GitHub et multi-fournisseurs IA. Conserver identité, mémoire canonique, continuité, plans, autorisations, communications, preuves, orchestration et reprise durable sans dépendance obligatoire à Copilot, Codex ou une conversation particulière.

## Lecture recommandée à chaque reprise
1. `00_START_HERE.md` — périmètre et point d'entrée proposé.
2. `state/CURRENT_STATE.json` — instantané documentaire daté, à réconcilier avec GitHub live.
3. `docs/PLAN_DIRECTEUR_UNIFIE_V5_BASELINE.md` — plans A/B/C/D et invariants.
4. `docs/DECISIONS_LOG.md` — décisions et statut de leur preuve.
5. `docs/SECURITY_GOVERNANCE.md` — règles de confidentialité, de séparation et d'autorisation.
6. `SUIVI.md` — travail réalisé / non réalisé et NEXT_ACTION.
7. `docs/SOURCE_PROVENANCE.md` — origines, limites et conservation documentaire.

## Invariants
- **Identité d'agent ≠ blueprint ≠ affectation ≠ mandat ≠ session ≠ conversation ≠ permission.**
- Un identifiant ou document historique **ne vaut jamais autorisation runtime**.
- Aucun transfert implicite de droits entre projets, comptes GitHub, installations ou fournisseurs IA.
- `Patricked-code/MCP` et `chainsolutions-wealthtech/Governed-Repository-Template` restent des projets autonomes avec leurs gouvernances existantes ; aucune modification n'est autorisée implicitement par ce dépôt.
- Aucune clé, token, conversation privée ou donnée sensible ne doit être publiée dans ce dépôt **public**.
- Lire HEAD, branches, règles, docs et état actuel **avant** une opération ; privilégier une branche/PR et les contrôles anti-régression.
- Les sources observées, confirmations de l'utilisateur, hypothèses, propositions et opérations effectivement exécutées doivent être marquées différemment.
- Le futur registre canonique et l'orchestrateur **restent à développer** ; GitHub seul ne les implémente pas.

## Autorité
Ces documents sont un **bootstrap proposé**, pas une modification des autorités des systèmes déjà existants. La mémoire canonique runtime devra s'appuyer sur une base externe protégée et sur des preuves indépendantes. Toute adoption du plan doit être traçable et révisable.
