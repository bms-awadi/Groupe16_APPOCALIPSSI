/** Conditions Générales d'Utilisation — EduTutor IA (complétées J3-bis). */
import LegalScaffold, { type LegalSection } from './LegalScaffold';

const SECTIONS: LegalSection[] = [
  {
    title: 'Objet',
    hint: 'ce que régissent ces CGU et le service concerné (EduTutor IA).',
    content: (
      <p>
        Les présentes Conditions Générales d'Utilisation (CGU) régissent l'accès et l'utilisation
        du service <strong>EduTutor IA</strong>, plateforme de révision assistée par intelligence
        artificielle développée par l'équipe 16 IPSSI dans le cadre de la semaine immersive
        APOCAL'IPSSI 2026. En utilisant EduTutor IA, vous acceptez les présentes conditions.
      </p>
    ),
  },
  {
    title: 'Acceptation des conditions',
    hint: "comment l'utilisateur accepte les CGU (inscription, usage…).",
    content: (
      <p>
        L'utilisation du service vaut acceptation pleine et entière des présentes CGU. En créant
        un compte sur EduTutor IA, vous déclarez avoir pris connaissance des CGU et les accepter
        sans réserve. Si vous n'acceptez pas ces conditions, vous devez vous abstenir d'utiliser
        le service.
      </p>
    ),
  },
  {
    title: 'Accès au service',
    hint: "conditions d'accès, disponibilité, prérequis techniques.",
    content: (
      <>
        <p>Le service est accessible :</p>
        <ul className="list-disc list-inside mt-1 space-y-1">
          <li>Sur inscription préalable (email + mot de passe)</li>
          <li>Depuis tout navigateur moderne (Chrome 90+, Firefox 90+, Safari 14+, Edge 90+)</li>
          <li>Dans la limite des capacités de l'infrastructure (service fourni « en l'état »)</li>
        </ul>
        <p className="mt-1">
          EduTutor IA est un projet académique. Aucune garantie de disponibilité continue n'est
          offerte. Des interruptions de service peuvent survenir sans préavis.
        </p>
      </>
    ),
  },
  {
    title: 'Compte utilisateur',
    hint: 'création, responsabilité du mot de passe, exactitude des informations.',
    content: (
      <>
        <ul className="list-disc list-inside space-y-1">
          <li>Vous êtes responsable de la confidentialité de vos identifiants</li>
          <li>Vous vous engagez à renseigner des informations exactes lors de l'inscription</li>
          <li>Tout accès frauduleux à votre compte doit être signalé immédiatement à <a href="mailto:equipe16@ipssi.fr" className="text-indigo-700 underline">equipe16@ipssi.fr</a></li>
          <li>Un seul compte par personne physique est autorisé</li>
          <li>Vous pouvez supprimer votre compte à tout moment depuis votre profil</li>
        </ul>
      </>
    ),
  },
  {
    title: 'Comportements interdits',
    hint: 'usages abusifs, contenus illicites, atteinte à la sécurité.',
    content: (
      <>
        <p>Sont strictement interdits :</p>
        <ul className="list-disc list-inside mt-1 space-y-1">
          <li>L'injection de contenu malveillant dans les cours uploadés (prompt injection, scripts, contenus illicites)</li>
          <li>L'utilisation du service à des fins autres que la révision pédagogique personnelle</li>
          <li>Toute tentative de contournement des limites de taux (rate limiting) ou des mécanismes de sécurité</li>
          <li>L'upload de contenus protégés par droit d'auteur sans autorisation</li>
          <li>L'utilisation automatisée (bots, scrapers) sans accord préalable</li>
          <li>Toute action susceptible de compromettre la sécurité ou la disponibilité du service</li>
        </ul>
      </>
    ),
  },
  {
    title: 'Contenu généré par IA',
    hint: "limites des quiz générés (peuvent contenir des erreurs), responsabilité de l'utilisateur.",
    content: (
      <>
        <p>
          EduTutor IA utilise des modèles de langage (LLM) pour générer des quiz. Ces modèles
          peuvent produire des erreurs, des inexactitudes ou des « hallucinations ».
        </p>
        <ul className="list-disc list-inside mt-1 space-y-1">
          <li>Les quiz générés sont des <strong>aides pédagogiques</strong>, non des ressources certifiées</li>
          <li>L'utilisateur est seul responsable de la vérification des contenus générés</li>
          <li>EduTutor IA ne garantit pas l'exactitude ou l'exhaustivité des questions générées</li>
          <li>En cas de contenu manifestement erroné, utilisez le bouton « Signaler » (disponible prochainement)</li>
        </ul>
      </>
    ),
  },
  {
    title: 'Responsabilité',
    hint: "limites de responsabilité de l'éditeur.",
    content: (
      <p>
        EduTutor IA est un projet pédagogique académique. Dans les limites autorisées par la loi,
        l'équipe 16 IPSSI ne saurait être tenue responsable de dommages directs ou indirects
        résultant de l'utilisation du service, d'erreurs dans les quiz générés, ou d'interruptions
        de service. La responsabilité est expressément limitée au cadre pédagogique de l'événement
        APOCAL'IPSSI 2026.
      </p>
    ),
  },
  {
    title: 'Propriété intellectuelle',
    hint: "droits sur le service et sur les contenus déposés par l'utilisateur.",
    content: (
      <>
        <p>
          Le code, le design et les fonctionnalités d'EduTutor IA sont la propriété de l'équipe 16
          et de l'IPSSI dans un cadre académique.
        </p>
        <p className="mt-1">
          Les documents que vous uploadez restent votre propriété. En les soumettant, vous accordez
          à EduTutor IA une licence non-exclusive, limitée à la génération de votre quiz et au
          stockage dans votre espace personnel.
        </p>
      </>
    ),
  },
  {
    title: 'Modification des CGU',
    hint: 'comment et quand les CGU peuvent évoluer.',
    content: (
      <p>
        Ces CGU peuvent être modifiées à tout moment. Les utilisateurs seront informés par email
        de toute modification substantielle. L'utilisation du service après notification vaut
        acceptation des nouvelles conditions.
      </p>
    ),
  },
  {
    title: 'Droit applicable et litiges',
    hint: 'droit applicable et juridiction compétente.',
    content: (
      <p>
        Les présentes CGU sont soumises au <strong>droit français</strong>. En cas de litige, les
        parties s'efforceront de trouver une solution amiable. À défaut, le tribunal compétent
        sera celui de <strong>Paris (75013)</strong>, nonobstant pluralité de défendeurs ou appel en
        garantie.
      </p>
    ),
  },
];

export default function CGUPage() {
  return (
    <LegalScaffold
      title="Conditions Générales d'Utilisation"
      intro="Les règles d'utilisation du service EduTutor IA — acceptées lors de l'inscription. Dernière mise à jour : 1er juillet 2026."
      sections={SECTIONS}
    />
  );
}
