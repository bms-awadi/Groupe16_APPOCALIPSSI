# Spécification — Bouton "Exporter mes données"

## Localisation

Page profil de l'utilisateur connecté (`/profile` ou menu utilisateur déroulant).

## Composant

```
[Bouton] "Exporter mes données personnelles"
```

## Comportement

1. **Clic sur le bouton** → ouverture d'une modale ou menu avec choix du format :
   - JSON (recommandé, machine-readable)
   - CSV (optionnel, lisible tableur)

2. **Sélection du format** → appel API :
   ```
   GET /api/accounts/me/export/?format=json
   ```
   avec header `Authorization: Token <token>`.

3. **Téléchargement automatique** du fichier reçu (header `Content-Disposition: attachment`).

4. **Notification** :
   - Succès : "Vos données ont été exportées. Le fichier a été téléchargé."
   - Erreur : "L'export est temporairement indisponible. Veuillez réessayer plus tard."

## Accessibilité

- Visible uniquement si l'utilisateur est authentifié.
- Masqué ou désactivé si l'email n'est pas vérifié (selon configuration admin).

## Sécurité UX

- Aucune donnée affichée à l'écran (pas de prévisualisation) : téléchargement direct uniquement.
- Pas de bouton "Partager" : l'export est personnel et non transférable.

## Statut d'implémentation

**À implémenter** — maquette et spécification prêtes, développement planifié post-MVP (dépend de l'endpoint backend).
