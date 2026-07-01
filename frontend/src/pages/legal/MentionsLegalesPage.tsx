/** Mentions légales — EduTutor IA (complétées J3-bis). */
import LegalScaffold, { type LegalSection } from './LegalScaffold';

const SECTIONS: LegalSection[] = [
  {
    title: 'Éditeur du site',
    hint: "nom de l'organisation/équipe, statut, adresse, email de contact.",
    content: (
      <>
        <p>
          <strong>EduTutor IA</strong> — Projet pédagogique réalisé dans le cadre de la semaine
          immersive APOCAL'IPSSI 2026.
        </p>
        <p className="mt-1">
          Équipe 16 : Rania ZERAMDINI, Amani LAYOUNI, Badreddine CHEBBOUR, Taise de Thèse NGANGA
          YABIE, Noah MASSET, Awadi BEDJA MROINKODO SAID, Clément BASTIEN.
        </p>
        <p className="mt-1">
          Établissement : <strong>IPSSI Paris</strong> — 15 rue des Gobelins, 75013 Paris.
        </p>
        <p className="mt-1">
          Contact : <a href="mailto:equipe16@ipssi.fr" className="text-indigo-700 underline">equipe16@ipssi.fr</a>
        </p>
      </>
    ),
  },
  {
    title: 'Directeur de la publication',
    hint: 'nom de la personne responsable du contenu publié.',
    content: <p>Rania ZERAMDINI, Product Owner — équipe 16.</p>,
  },
  {
    title: 'Hébergeur',
    hint: "nom, adresse et téléphone de l'hébergeur du site.",
    content: (
      <>
        <p>
          <strong>Hébergement local (développement)</strong> : Docker Compose sur infrastructure
          IPSSI — localhost:3000 (frontend) / localhost:8000 (API).
        </p>
        <p className="mt-1">
          En production : infrastructure IPSSI Paris, 15 rue des Gobelins, 75013 Paris.
        </p>
      </>
    ),
  },
  {
    title: 'Propriété intellectuelle',
    hint: 'à qui appartiennent les textes, logos, code, contenus.',
    content: (
      <>
        <p>
          Le code source d'EduTutor IA est un travail collectif de l'équipe 16, réalisé dans un
          cadre pédagogique. Les contenus pédagogiques générés par l'IA appartiennent à
          l'utilisateur qui les a soumis.
        </p>
        <p className="mt-1">
          Les quiz générés à partir de documents uploadés par l'utilisateur restent la propriété
          intellectuelle de cet utilisateur. EduTutor IA ne revendique aucun droit sur ces
          contenus.
        </p>
        <p className="mt-1">
          Le code du kit pédagogique est fourni par Mohamed EL AFRIT (IPSSI) dans un cadre
          académique et ne peut être utilisé à des fins commerciales sans autorisation.
        </p>
      </>
    ),
  },
  {
    title: 'Contact',
    hint: 'comment vous joindre pour toute question juridique.',
    content: (
      <>
        <p>
          Pour toute question juridique ou relative à la protection des données :{' '}
          <a href="mailto:dpo@edututor.fr" className="text-indigo-700 underline">dpo@edututor.fr</a>
        </p>
        <p className="mt-1">Délai de réponse garanti : 48 heures ouvrables.</p>
      </>
    ),
  },
];

export default function MentionsLegalesPage() {
  return (
    <LegalScaffold
      title="Mentions légales"
      intro="Informations légales obligatoires identifiant l'éditeur et l'hébergeur du site (Loi pour la confiance dans l'économie numérique — LCEN)."
      sections={SECTIONS}
    />
  );
}
