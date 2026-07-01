# Réponse à Hugo Petit — Demande d'accès RGPD Art. 15

**Objet :** Réponse à votre demande d'accès à vos données personnelles — Art. 15 RGPD

Bonjour Monsieur Petit,

Nous accusons réception de votre demande d'accès à vos données personnelles, formulée au titre de l'article 15 du Règlement Général sur la Protection des Données (RGPD), concernant votre compte EduTutor IA associé à l'adresse `hugo.petit@test.local`.

Votre demande a été enregistrée le mercredi à 10h30. Conformément au RGPD, le délai légal maximal de réponse est de 30 jours. Dans le cadre de notre POC et conformément à l'engagement pris auprès du sponsor, nous visons une réponse sous 48 heures.

## Données concernées

L'export qui sera préparé couvre les catégories suivantes, sous réserve qu'elles existent effectivement pour votre compte :

- données de compte : adresse email, dates de création et informations de profil ;
- cours ou textes que vous avez importés dans la plateforme ;
- quiz générés à partir de vos contenus ;
- questions, réponses sélectionnées et scores associés.

Les signalements et traces d'audit sont à implémenter dans la plateforme. Ils seront intégrés à l'export dès leur activation.

Les données seront préparées dans un format structuré, couramment utilisé et lisible par machine, prioritairement JSON, avec possibilité d'un format CSV.

## Modalité de transmission

Dans la version MVP actuelle, l'équipe privilégie une transmission contrôlée afin d'éviter tout risque de fuite de données entre utilisateurs. L'export sera vérifié manuellement pour garantir qu'il contient uniquement les données rattachées à votre compte.

Lorsque l'endpoint d'export automatisé sera activé, il sera accessible depuis un compte authentifié via :

`GET /api/accounts/me/export/`

Un téléchargement au format JSON ou CSV sera alors disponible directement depuis votre espace personnel.

## Garanties de sécurité

Nous nous engageons à appliquer les principes suivants :

- filtrage strict des données par utilisateur ;
- absence d'export global non filtré ;
- vérification que les données d'autres utilisateurs ne sont pas incluses ;
- traçabilité de la demande dans un audit trail SAR (à implémenter) ;
- conservation limitée des exports temporaires.

## Rappel de vos droits

Vous disposez également des droits suivants :

- droit de rectification — Art. 16 RGPD ;
- droit à l'effacement — Art. 17 RGPD ;
- droit à la limitation du traitement — Art. 18 RGPD ;
- droit à la portabilité — Art. 20 RGPD ;
- droit d'opposition lorsque applicable — Art. 21 RGPD.

Pour exercer ces droits ou poser une question complémentaire, vous pouvez contacter notre référent protection des données fictif :

**DPO EduTutor IA**  
`dpo@edututor-ia.local`

Cordialement,

L'équipe EduTutor IA — Équipe 16
