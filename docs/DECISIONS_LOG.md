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

| DEC-011 | Documenter de bout en bout et dans l'ordre chronologique le programme universel avant d'admettre et de construire les lots pas à pas ; préserver le propriétaire canonique de chaque information et éviter les lots/tickets doublons. | Décision utilisateur du 22 octobre 2026 ; exécution documentaire proposée sur PR #1 : `docs/roadmap/PROGRAMME_CHRONOLOGIQUE_V5.md` et `docs/roadmap/REGISTRE_TACHES_V5.md`. |

| DEC-012 | Finaliser en priorité la GitHub App existante et conserver un programme V5 intégralement chronologique et découpé en tâches, sans recréer l'application, les 46 lots ni les identités et sans modifier MCP/GRT. | Instruction explicite utilisateur du 22 octobre 2026 ; complément d'acceptation `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` ; livraison complète soumise à preuves GA-00–GA-08. |


| DEC-013 | Conserver intégralement la vision souhaitée pour `ChainSolutions Universal Gateway` : couverture GitHub maximale (quatre familles de permissions et toutes fonctions pertinentes), sur les trois espaces, exploitable par les agents IA, avec droits effectivement accordés et mandats distincts ; consigner d'abord le cahier des charges puis auditer les droits et écarts existants sans recréer l'App. | Instruction explicite du 22 octobre 2026 ; cible détaillée dans `docs/github-app/CAHIER_DES_CHARGES_COMPLET.md` ; observations et gates dans `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` ; aucune permission nouvelle activée. |

| DEC-014 | Priorité opérationnelle immédiate exclusive : achever la GitHub App existante `ChainSolutions Universal Gateway` avec couverture maximale des permissions **réellement configurables et approuvées** ; comparer tous les candidats historiques aux droits officiels actuels, auditer les trois installations, puis prévoir activation gouvernée et tests runtime, avant les autres chantiers de plateforme. | Instruction explicite utilisateur du 22 octobre 2026 ; registre focalisé `GH-MAX-01` à `GH-MAX-10` dans `docs/github-app/GATEWAY_IMPLEMENTATION_GATES.md` ; aucune permission modifiée par cette décision. |

**À valider :** publication intégrale du plan V5, inventaire actualisé des 46 lots, matrice des permissions *effectives* et protocole de mémorisation canonique persistant. Toute modification future doit ajouter une entrée et indiquer ce qui est superseded, pourquoi et sur quelle source.
