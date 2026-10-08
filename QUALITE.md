# Grille qualité du site Cœur Artichaut

Grille de référence pour chaque vérification du site. Les critères et les points ne changent pas d'un audit à l'autre, pour que les notes restent comparables.

Contrôle automatique : `hugo --destination <dossier>` puis `python scripts/audit-seo.py <dossier>`.

## Référencement (sur 100)

| Critère | Points | Ce qui est vérifié |
|---|---|---|
| Titres de page | 15 | Uniques, 30 à 65 caractères, mot-clé + lieu, sans émoji |
| Meta descriptions | 10 | Présentes, uniques, 120 à 190 caractères |
| Structure des titres | 10 | Un seul H1 par page, H2/H3 logiques |
| Contenu | 10 | ≥ 300 mots sur les pages de service, mots-clés locaux (Saint-Maximin, Var) |
| Maillage interne | 10 | Aucune page orpheline, aucun lien cassé |
| Images | 10 | Texte alternatif, chargement différé, poids raisonnable |
| Données structurées | 10 | JSON-LD valide et conforme au contenu visible (horaires, FAQ, livres) |
| Technique | 10 | Canonical, sitemap, robots.txt, page 404, favicon |
| Partage social | 5 | Titre, description, URL et image propres à chaque page, image existante |
| Mobile et rapidité | 10 | Pas de débordement à 375 px, pages légères |

## Cohérence (sur 100)

| Critère | Points | Ce qui est vérifié |
|---|---|---|
| Infos pratiques | 25 | Tarifs, horaires, lieux, téléphone, e-mail identiques partout |
| Méthode et discours | 15 | Même description de la méthode Cœur Artichaut™ sur toutes les pages |
| Publics | 10 | Mêmes publics annoncés partout (adultes, ados, enfants, familles) |
| Charte graphique | 15 | Même en-tête, pied de page, couleurs, polices, boutons sur toutes les pages |
| Ton éditorial | 10 | Doux, humour adulte, pas d'enfantin ; Arti & Chou dosés |
| Appels à l'action | 10 | E-mails préremplis, pas de doublon de bloc rendez-vous |
| Livres et offres | 10 | Les deux livres à jour partout, offres (land art, ateliers) à jour |
| Mentions légales | 5 | Exactes par rapport au fonctionnement réel du site |

## Historique des notes

| Date | Référencement | Cohérence | Commentaire |
|---|---|---|---|
| 2026-10-08 | 88 | 82 | Première mesure, version 2.0 avant publication |
| 2026-10-08 | 95 | 97 | Lieux (cabinet, domicile, extérieur, visio), horaires Google, méthode en 3 temps, titres de page, émojis retirés |
| 2026-10-08 | 95 | 99 | Déroulé de séance distinct des objectifs de la méthode, répliques d'Arti & Chou validées, répétitions allégées |
| 2026-10-08 | 95 | 100 | Tarif à domicile confirmé (60 €, comme au cabinet) |
| 2026-10-08 | 100 | 100 | Test mobile 375 px sur les 13 pages (débordements corrigés, menu non fixe sur mobile), images en WebP (jusqu'à −95 %), titre « Qu'est-ce que l'art-thérapie » localisé, page Contact enrichie (460 mots) |
