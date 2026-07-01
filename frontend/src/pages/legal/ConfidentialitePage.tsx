/** Politique de confidentialité — EduTutor IA (complétée J3-bis). */
import LegalScaffold, { type LegalSection } from './LegalScaffold';

const SECTIONS: LegalSection[] = [
  {
    title: 'Responsable du traitement',
    hint: 'qui décide pourquoi et comment les données sont traitées.',
    content: (
      <>
        <p>
          <strong>EduTutor IA — Équipe 16 IPSSI</strong>, 15 rue des Gobelins, 75013 Paris.
        </p>
        <p className="mt-1">
          DPO : <a href="mailto:dpo@edututor.fr" className="text-indigo-700 underline">dpo@edututor.fr</a>
        </p>
      </>
    ),
  },
  {
    title: 'Données personnelles collectées',
    hint: 'email, nom, prénom, documents envoyés, historique de quiz…',
    content: (
      <ul className="list-disc list-inside space-y-1">
        <li><strong>Identité</strong> : email (obligatoire), prénom et nom (optionnels)</li>
        <li><strong>Authentification</strong> : mot de passe (haché bcrypt, jamais stocké en clair)</li>
        <li><strong>Contenus pédagogiques</strong> : textes et PDFs uploadés pour générer des quiz (stockés en base de données)</li>
        <li><strong>Résultats</strong> : quiz générés, réponses données, scores /10</li>
        <li><strong>Journaux techniques</strong> : date d'inscription, date de connexion, adresse IP (logs serveur, 90 jours)</li>
        <li><strong>Demandes RGPD</strong> : journal des demandes d'accès SAR (Art. 15), conservé 5 ans</li>
      </ul>
    ),
  },
  {
    title: 'Finalités du traitement',
    hint: 'pourquoi vous collectez ces données (créer un compte, générer des quiz…).',
    content: (
      <ul className="list-disc list-inside space-y-1">
        <li>Authentification et gestion du compte utilisateur</li>
        <li>Génération de quiz personnalisés à partir de vos cours</li>
        <li>Affichage de votre historique et de votre progression pédagogique</li>
        <li>Sécurité et prévention des abus (rate limiting, détection d'injections)</li>
        <li>Conformité légale (réponses aux demandes RGPD, audit trail)</li>
      </ul>
    ),
  },
  {
    title: 'Base légale',
    hint: 'consentement, contrat, intérêt légitime… (RGPD art. 6).',
    content: (
      <ul className="list-disc list-inside space-y-1">
        <li><strong>Art. 6(1)(b)</strong> — Exécution du contrat : compte, quiz, historique (fonctionnement du service)</li>
        <li><strong>Art. 6(1)(c)</strong> — Obligation légale : journal SAR, audit trail CNIL</li>
        <li><strong>Art. 6(1)(f)</strong> — Intérêt légitime : sécurité applicative, débogage, amélioration du service</li>
      </ul>
    ),
  },
  {
    title: 'Durée de conservation',
    hint: 'combien de temps les données sont gardées, puis supprimées/anonymisées.',
    content: (
      <>
        <ul className="list-disc list-inside space-y-1">
          <li>Compte utilisateur : durée de vie du compte + 1 an après inactivité</li>
          <li>Quiz et réponses : 3 ans à compter de la date de création</li>
          <li>Journal SAR : 5 ans (obligation légale)</li>
          <li>Logs serveur : 90 jours maximum (rotation automatique)</li>
        </ul>
        <p className="mt-2">
          Détail complet :{' '}
          <a href="/legal/confidentialite" className="text-indigo-700 underline">
            Politique de rétention complète
          </a>
        </p>
      </>
    ),
  },
  {
    title: 'Destinataires des données',
    hint: 'qui y a accès (équipe, sous-traitants, fournisseurs LLM…).',
    content: (
      <>
        <ul className="list-disc list-inside space-y-1">
          <li><strong>Équipe 16 IPSSI</strong> : accès via l'interface d'administration (admin Django, accès restreint)</li>
          <li><strong>Fournisseur LLM actif</strong> : le texte de votre cours est envoyé au fournisseur LLM sélectionné (Ollama local, Groq, OpenAI…) pour générer les questions — voir ADR-01 pour le choix du fournisseur</li>
          <li><strong>Aucun tiers commercial</strong> : vos données ne sont pas vendues ni partagées à des fins publicitaires</li>
        </ul>
        <p className="mt-2 text-amber-800 bg-amber-50 p-2 rounded border-l-2 border-amber-400 text-xs">
          ⚠️ Si le fournisseur LLM est un service cloud (Groq, OpenAI), votre contenu de cours est traité sur leurs serveurs. Consultez leurs politiques de confidentialité respectives.
        </p>
      </>
    ),
  },
  {
    title: 'Transferts hors UE',
    hint: 'si un fournisseur cloud héberge les données hors Union européenne.',
    content: (
      <>
        <p>
          <strong>Ollama (mode par défaut)</strong> : traitement 100% local — aucun transfert hors UE.
        </p>
        <p className="mt-1">
          <strong>Fournisseurs cloud (Groq, OpenAI, Mistral…)</strong> : le contenu soumis est traité sur des serveurs situés aux États-Unis ou dans d'autres pays tiers. Ces transferts sont couverts par les clauses contractuelles types (CCT) de la Commission européenne ou les certifications Data Privacy Framework (DPF) des fournisseurs.
        </p>
        <p className="mt-1">
          Le fournisseur actif est documenté dans l'ADR-01 accessible à l'équipe.
        </p>
      </>
    ),
  },
  {
    title: 'Vos droits',
    hint: 'accès, rectification, suppression, portabilité, opposition, et comment les exercer.',
    content: (
      <>
        <ul className="list-disc list-inside space-y-1">
          <li><strong>Accès (Art. 15)</strong> : téléchargez vos données sur <a href="/profile" className="text-indigo-700 underline">/profile</a> → « Exporter mes données »</li>
          <li><strong>Rectification (Art. 16)</strong> : modifiez vos informations sur <a href="/profile" className="text-indigo-700 underline">/profile</a></li>
          <li><strong>Effacement (Art. 17)</strong> : supprimez votre compte sur /profile → zone « Danger » (suppression immédiate et irréversible)</li>
          <li><strong>Portabilité (Art. 20)</strong> : l'export JSON/CSV répond à ce droit</li>
          <li><strong>Limitation et opposition (Art. 18/21)</strong> : contactez le DPO</li>
        </ul>
        <p className="mt-2">
          Contact DPO :{' '}
          <a href="mailto:dpo@edututor.fr" className="text-indigo-700 underline">dpo@edututor.fr</a>{' '}
          — réponse sous 48h ouvrables.
        </p>
      </>
    ),
  },
  {
    title: 'Cookies',
    hint: 'renvoi vers la politique de cookies du site.',
    content: (
      <p>
        Voir notre{' '}
        <a href="/legal/cookies" className="text-indigo-700 underline">
          Politique de gestion des cookies
        </a>{' '}
        pour le détail des technologies de stockage utilisées.
      </p>
    ),
  },
  {
    title: 'Contact & réclamation',
    hint: 'email du référent données + droit de réclamation auprès de la CNIL.',
    content: (
      <>
        <p>
          DPO EduTutor IA :{' '}
          <a href="mailto:dpo@edututor.fr" className="text-indigo-700 underline">dpo@edututor.fr</a>
        </p>
        <p className="mt-1">
          Vous avez le droit d'introduire une réclamation auprès de la{' '}
          <a
            href="https://www.cnil.fr/fr/plaintes"
            target="_blank"
            rel="noopener noreferrer"
            className="text-indigo-700 underline"
          >
            CNIL
          </a>{' '}
          (Commission Nationale de l'Informatique et des Libertés).
        </p>
      </>
    ),
  },
];

export default function ConfidentialitePage() {
  return (
    <LegalScaffold
      title="Politique de confidentialité"
      intro="Comment les données personnelles des utilisateurs sont collectées, utilisées et protégées — RGPD (Règlement UE 2016/679). Dernière mise à jour : 1er juillet 2026."
      sections={SECTIONS}
    />
  );
}
