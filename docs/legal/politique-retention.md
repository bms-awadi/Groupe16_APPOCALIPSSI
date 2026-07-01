# Politique de rétention des données — EduTutor IA

**Équipe 16 · APOCAL'IPSSI 2026**
Version 1.0 · Rédigée le 1er juillet 2026 · Conformité RGPD — Art. 5(1)(e), Art. 13

---

## 1. Durées de rétention par catégorie de données

| Catégorie | Données concernées | Base légale (Art. 6) | Durée de conservation | Déclencheur de suppression |
|-----------|-------------------|----------------------|-----------------------|---------------------------|
| **Compte utilisateur** | Email, nom, prénom, mot de passe (haché), date d'inscription | Art. 6(1)(b) — exécution du contrat | Durée de vie du compte + **1 an** après inactivité | Suppression du compte (Art. 17) ou 1 an d'inactivité complète |
| **Quiz et questions** | Titre du quiz, texte source extrait, 10 questions générées | Art. 6(1)(b) — exécution du contrat | **3 ans** à compter de la date de création | Suppression du compte ou expiration de la période |
| **Réponses et scores** | `selected_index` par question, score `/10`, date de passage | Art. 6(1)(b) — suivi pédagogique + Art. 6(1)(f) — amélioration du service | **3 ans** à compter de la date de passage | Suppression du compte ou expiration de la période |
| **Journal SAR** | Demandes d'accès RGPD (requester, timestamp, statut, hash) | Art. 6(1)(c) — obligation légale CNIL | **5 ans** (preuve de conformité en cas de contrôle) | Automatique après 5 ans (cron mensuel à implémenter) |
| **Tokens d'authentification** | Token DRF (hash SHA-256) | Art. 6(1)(b) — sécurité du compte | Invalidé à chaque déconnexion ou reset de mot de passe | Logout / reset / suppression du compte |
| **Emails de vérification** | Token de confirmation d'email (UUID) | Art. 6(1)(b) — validation d'identité | **24 heures** (expiration automatique) | Expiration ou confirmation |
| **Logs applicatifs** | Adresses IP (si activés dans Gunicorn/Caddy), user-agent | Art. 6(1)(f) — sécurité + débogage | **90 jours** maximum | Rotation automatique des logs |

---

## 2. Bases légales et droits associés

| Base légale | Article | Application dans EduTutor IA |
|-------------|---------|------------------------------|
| Exécution du contrat | Art. 6(1)(b) | Compte, quiz, réponses — nécessaires à l'utilisation du service |
| Obligation légale | Art. 6(1)(c) | Journal SAR — preuve de conformité CNIL/RGPD |
| Intérêt légitime | Art. 6(1)(f) | Amélioration de la pertinence des quiz, sécurité applicative |

### Droits de la personne concernée

- **Art. 15** — Droit d'accès : exercé via `GET /api/accounts/me/export/` (JSON ou CSV, téléchargement immédiat)
- **Art. 16** — Droit de rectification : via la page `/profile` (modification prénom/nom/email)
- **Art. 17** — Droit à l'effacement : via la zone « Danger » de `/profile` — suppression immédiate et définitive de toutes les données (cascade DB)
- **Art. 18** — Droit à la limitation : contacter le DPO (voir ci-dessous)
- **Art. 20** — Droit à la portabilité : l'export Art. 15 répond à ce droit (format JSON lisible par machine)

### Contact DPO

**dpo@edututor.fr** · Délai de réponse garanti : 48 heures ouvrables
Courrier : EduTutor IA — DPO, 15 rue des Gobelins, 75013 Paris

---

## 3. Procédures de suppression (Art. 17 — droit à l'effacement)

### Suppression à la demande de l'utilisateur

1. L'utilisateur accède à `/profile` → zone « Danger »
2. Saisit son mot de passe + coche la case de confirmation
3. `DELETE /api/accounts/me/delete/` est appelé
4. Django supprime l'utilisateur (`User.delete()`) : toutes les données liées (Quiz, Question, DataRequest, Profile, Token) sont supprimées en cascade (`on_delete=CASCADE`)
5. La session est invalidée, le token DRF détruit

**Délai effectif : immédiat** (synchrone, même requête HTTP)

### Suppression automatique par expiration

| Déclencheur | Action | Implémentation actuelle |
|-------------|--------|------------------------|
| Inactivité > 1 an | Suppression du compte | À implémenter — cron Django management command `purge_inactive_accounts` |
| Quiz > 3 ans | Suppression des Quiz et Questions | À implémenter — cron `purge_old_quizzes` |
| SAR > 5 ans | Suppression des DataRequest | À implémenter — cron `purge_old_sar` |
| Logs > 90 jours | Rotation Caddy/Gunicorn | Via logrotate (infrastructure) |

> **Note technique** : les suppressions automatiques par expiration sont planifiées pour la Release 2. Elles seront implémentées via des `management commands` Django exécutées par un cron Kubernetes (ou cron Docker en développement).

### Preuve de conformité

Chaque suppression à la demande génère une entrée dans le journal SAR (`DataRequest`) avec `status=completed` et `responded_at` horodaté. Ce journal est conservé 5 ans conformément à l'Art. 6(1)(c).
