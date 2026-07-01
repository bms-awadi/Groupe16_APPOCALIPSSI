/** Politique de gestion des cookies — EduTutor IA (complétée J3-bis). */
import LegalScaffold, { type LegalSection } from './LegalScaffold';

const SECTIONS: LegalSection[] = [
  {
    title: "Qu'est-ce qu'un cookie ?",
    hint: 'définition simple à destination des utilisateurs.',
    content: (
      <p>
        Un cookie est un petit fichier texte déposé sur votre appareil par un site web lors de
        votre visite. EduTutor IA n'utilise <strong>pas de cookies</strong> au sens strict — nous
        utilisons le <strong>stockage local du navigateur</strong> (<code className="bg-slate-100 px-1 rounded">localStorage</code>)
        pour stocker votre token d'authentification. Cette technologie est fonctionnellement
        similaire aux cookies mais ne peut pas être transmise automatiquement à chaque requête HTTP.
      </p>
    ),
  },
  {
    title: 'Cookies et stockage utilisés',
    hint: "lister ce que le site dépose (ex. token d'authentification en localStorage).",
    content: (
      <div className="overflow-x-auto">
        <table className="w-full text-sm border-collapse">
          <thead>
            <tr className="bg-slate-100">
              <th className="text-left p-2 border border-slate-200">Nom / Clé</th>
              <th className="text-left p-2 border border-slate-200">Type</th>
              <th className="text-left p-2 border border-slate-200">Valeur</th>
              <th className="text-left p-2 border border-slate-200">Durée</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td className="p-2 border border-slate-200 font-mono text-xs">token</td>
              <td className="p-2 border border-slate-200">localStorage</td>
              <td className="p-2 border border-slate-200">Token DRF (40 caractères alphanumériques)</td>
              <td className="p-2 border border-slate-200">Jusqu'à la déconnexion</td>
            </tr>
          </tbody>
        </table>
        <p className="mt-2 text-slate-500 text-xs">
          Aucun cookie tiers, aucun tracker publicitaire, aucune technologie de mesure d'audience.
        </p>
      </div>
    ),
  },
  {
    title: 'Finalité de chaque cookie',
    hint: "à quoi sert chaque cookie/stockage (technique, mesure d'audience…).",
    content: (
      <>
        <p>
          <strong>Token d'authentification</strong> (<code className="bg-slate-100 px-1 rounded">localStorage.token</code>) :
        </p>
        <ul className="list-disc list-inside mt-1 space-y-1">
          <li>Permet au frontend de s'authentifier auprès de l'API Django (header <code className="bg-slate-100 px-1 rounded">Authorization: Token ...</code>)</li>
          <li>Évite de redemander votre mot de passe à chaque page</li>
          <li>Classé « strictement nécessaire » — non soumis au consentement préalable (Directive ePrivacy Art. 5(3))</li>
        </ul>
      </>
    ),
  },
  {
    title: 'Consentement',
    hint: 'cookies nécessitant un consentement préalable et comment il est recueilli.',
    content: (
      <p>
        Le seul stockage utilisé (token d'authentification) est <strong>strictement nécessaire</strong>{' '}
        au fonctionnement du service. Il est exempté de consentement préalable conformément à la
        Directive ePrivacy (2002/58/CE Art. 5(3)) et aux recommandations CNIL. Aucun bandeau de
        consentement n'est donc requis pour EduTutor IA dans sa configuration actuelle.
      </p>
    ),
  },
  {
    title: 'Durée de conservation',
    hint: 'combien de temps chaque cookie est conservé.',
    content: (
      <p>
        Le token d'authentification est conservé dans le <code className="bg-slate-100 px-1 rounded">localStorage</code>{' '}
        jusqu'à votre déconnexion (clic sur « Se déconnecter »). Il est automatiquement supprimé
        en cas de suppression du compte. Contrairement aux cookies, le localStorage persiste
        entre les sessions jusqu'à suppression explicite — cela vous permet de rester connecté
        entre deux visites sans ressaisir votre mot de passe.
      </p>
    ),
  },
  {
    title: 'Gérer ou refuser les cookies',
    hint: 'comment paramétrer ou supprimer les cookies (navigateur, bannière).',
    content: (
      <>
        <p>Pour supprimer votre token d'authentification :</p>
        <ul className="list-disc list-inside mt-1 space-y-1">
          <li><strong>Via le site</strong> : cliquez sur « Se déconnecter » — le token est effacé immédiatement</li>
          <li><strong>Via votre navigateur</strong> : Outils développeurs (F12) → Application → Local Storage → supprimer la clé <code className="bg-slate-100 px-1 rounded">token</code></li>
          <li><strong>Via la page profil</strong> : la suppression de compte efface également le token côté serveur</li>
        </ul>
        <p className="mt-2">
          Supprimer le token vous déconnecte du service. Vous pourrez vous reconnecter à tout moment.
        </p>
      </>
    ),
  },
];

export default function CookiesPage() {
  return (
    <LegalScaffold
      title="Politique de gestion des cookies"
      intro="Les technologies de stockage utilisées par EduTutor IA et comment les gérer. Dernière mise à jour : 1er juillet 2026."
      sections={SECTIONS}
    />
  );
}
