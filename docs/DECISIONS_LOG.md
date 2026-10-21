# Journal des décisions — fondation proposée

Ce journal sépare **décision utilisateur**, **proposition technique** et **état vérifié**. Les entrées ne donnent aucune permission supplémentaire à un agent.

| Référence | Énoncé | Statut / preuve |
| --- | --- | --- |
| DEC-001 | Plateforme globale réutilisable sur tous les projets, et pas uniquement MCP ou GRT. | Objectif confirmé en conversation |
| DEC-002 | Préserver l'identité stable des agents, sans identité, session ou tâche concurrente inventée. | Objectif confirmé |
| DEC-003 | Capturer les conversations accessibles, préserver verbatim les sources et dériver une mémoire canonique traçable. | Objectif confirmé ; service non construit |
| DEC-004 | Plateforme indépendante de Copilot, Codex et du fournisseur IA. | Objectif confirmé |
| DEC-005 | Plans A, B et C maintenus ; plan D Full-Capability GitHub ajouté sans suppression. | Décision architecturale retenue |
| DEC-006 | `Patricked-code/MCP` et GRT sont deux projets, autorités et historiques distincts. | Invariant retenu |
| DEC-007 | Code et documentation publique sur `chainsolutions-wealthtech/universal-agent-platform`, sans secrets ni archives privées. | Objectif retenu ; dépôt public désormais observé |
| DEC-008 | GitHub App unique `ChainSolutions Universal Gateway`, App ID `5417646`, installations sur trois comptes. | Création, installations et authentification rapportées par l'utilisateur ; repo public directement observé par connecteur |
| DEC-009 | Couverture fonctionnelle maximale de GitHub avec isolation des jetons, du périmètre et des opérations à risque. | Principe d'architecture ; audit complet des permissions non réalisé |
| DEC-010 | Sur le nouveau dépôt, proposer d'abord la fondation dans une branche/PR ; ne pas modifier directement `main`. | Méthode de bootstrap |

**À valider :** publication intégrale du plan V5, inventaire actualisé des 46 lots, matrice des permissions *effectives* et protocole de mémorisation canonique persistant. Toute modification future doit ajouter une entrée et indiquer ce qui est superseded, pourquoi et sur quelle source.
