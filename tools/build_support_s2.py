from __future__ import annotations

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "support-technique-seance-02.html"
INDEX_OUT = ROOT / "index.html"

DOCS = {
    "codex_quickstart": "https://developers.openai.com/codex/quickstart",
    "codex_pricing": "https://developers.openai.com/codex/pricing",
    "codex_cli": "https://developers.openai.com/codex/cli",
    "codex_features": "https://developers.openai.com/codex/cli/features",
    "codex_agents": "https://developers.openai.com/codex/guides/agents-md",
    "codex_help": "https://help.openai.com/en/articles/11369540-getting-started-with-codex",
    "codex_product": "https://openai.com/codex/",
    "codex_app_article": "https://openai.com/index/introducing-the-codex-app/",
    "codex_app": "https://developers.openai.com/codex/app",
    "codex_app_automations": "https://developers.openai.com/codex/app/automations",
    "codex_plugins": "https://developers.openai.com/codex/plugins",
    "codex_use_cases": "https://developers.openai.com/codex/use-cases",
    "codex_permissions": "https://developers.openai.com/codex/permissions",
    "codex_cli_features": "https://developers.openai.com/codex/cli/features",
    "chatgpt_pricing": "https://chatgpt.com/pricing/",
    "claude_quickstart": "https://code.claude.com/docs/en/quickstart",
    "claude_pro_max": "https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan",
    "claude_limits": "https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code",
    "claude_plan": "https://support.claude.com/en/articles/11049762-choose-a-claude-plan",
    "claude_extend": "https://code.claude.com/docs/en/features-overview",
    "github_pages": "https://docs.github.com/en/pages",
}


IMAGES = [
    "hero-codex-claude.png",
    "codex-home-screen.png",
    "codex-plugiciels-screen.png",
    "codex-automatisations-screen.png",
    "codex-install.png",
    "codex-login.png",
    "claude-install.png",
    "same-folder.png",
    "same-brief.png",
    "agents-md.png",
    "claude-md.png",
    "first-comparison.png",
    "codex-plan.png",
    "claude-plan.png",
    "diff-codex.png",
    "diff-claude.png",
    "browser-preview.png",
    "mobile-check.png",
    "git-status.png",
    "approval-modes.png",
    "pricing-comparison.png",
    "local-vs-cloud.png",
    "business-task.png",
    "prompt-bad-good.png",
    "debug-flow.png",
    "review-other-agent.png",
    "parallel-workflow.png",
    "daily-routine.png",
    "decision-matrix.png",
    "risk-table.png",
    "source-check.png",
    "handoff-summary.png",
    "easter-egg.png",
    "codex-app.png",
    "claude-web.png",
    "final-map.png",
]


CHAPTERS = [
    (
        "Acte 1 - Le terrain commun",
        "Avant de comparer deux agents, le projet doit être clair. Le fil rouge reste Le Comptoir Bleu, une page business simple que l’on peut regarder, corriger et publier.",
        "Comprendre",
        "blue",
        [
            ("Le point de départ après la séance 1", "La première séance a posé une base : un dossier, une page simple et l’habitude de vérifier dans le navigateur. La séance 2 ne recommence pas à zéro. Elle reprend ce même terrain pour poser une question plus utile au quotidien : quand faut-il utiliser Codex, quand faut-il utiliser Claude Code, et quand faut-il les faire travailler ensemble ?", "Ouvrez le dossier du Comptoir Bleu ou créez un dossier test avec une page `index.html`. Le but n’est pas d’avoir un projet parfait, mais d’avoir une base visible.", "La page s’ouvre dans le navigateur et vous savez expliquer en une phrase ce qu’elle contient.", "Codex va servir de regard OpenAI sur le même projet, avec ses surfaces local, app, CLI et cloud.", "Claude Code reste l’agent terminal déjà vu, utile pour travailler dans le dossier et suivre une action pas à pas.", "À quoi sert une comparaison si les deux outils ne regardent pas le même projet ? Commencez toujours par ce point.", "hero-codex-claude.png"),
            ("La mission du Comptoir Bleu", "Le propriétaire fictif veut une amélioration concrète : rendre la formule midi plus visible, garder le bouton Réserver au bon endroit et vérifier le rendu mobile. C’est volontairement simple. Une tâche simple permet de voir le comportement réel de chaque agent sans se noyer dans une architecture compliquée.", "Écrivez la mission en une phrase : `Ajouter une formule midi claire sur la page du Comptoir Bleu et vérifier que le bouton Réserver mène au contact.`", "La mission tient sur une seule ligne et ne mélange pas dix objectifs.", "Codex sera testé sur une demande courte, puis sur une relecture de diff.", "Claude Code sera testé sur la même demande et sur la correction guidée dans le terminal.", "Un bon comparatif commence avec une tâche de commerce réel, pas avec une question abstraite.", "business-task.png"),
            ("Codex en phrase simple", "Codex est l’agent de code d’OpenAI. Il aide à écrire, relire et livrer du code. Les docs officielles indiquent qu’il peut être utilisé dans plusieurs surfaces : application, CLI, extension IDE, web ou cloud. Pour cette séance, retenez seulement ceci : Codex peut travailler avec votre projet et vous aider à comprendre ou modifier des fichiers.", "Ouvrez la page officielle Codex et repérez les surfaces disponibles : app, CLI, IDE, cloud. Ne choisissez pas encore. Observez seulement les options.", "Vous savez dire que Codex n’est pas juste une réponse de chat : c’est un agent de travail autour du code.", "Codex est intéressant quand vous voulez un second avis, une relecture, un plan ou une tâche locale/cloud selon le contexte.", "Claude Code a une logique très proche côté terminal, mais avec les conventions Anthropic et le fichier `CLAUDE.md`.", "Ne retenez pas tous les noms de modèles. Retenez plutôt la question : où l’agent travaille-t-il et que va-t-il modifier ?", "codex-app.png"),
            ("Claude Code en phrase simple", "Claude Code est l’outil de ligne de commande d’Anthropic pour accéder à Claude dans un dossier de travail. Le Help Center explique qu’il permet de déléguer des tâches de code tout en gardant de la transparence et du contrôle. En clair : vous lancez `claude`, vous expliquez l’objectif, vous lisez ce qu’il propose, puis vous vérifiez.", "Relisez la définition officielle de Claude Code et reformulez-la avec vos mots : `Claude Code travaille dans mon terminal, dans mon dossier, avec mon accord.`", "La définition est comprise sans jargon et sans phrase longue.", "Codex et Claude Code ont une zone commune : aider sur un vrai projet de code.", "Claude Code se distingue par son usage terminal très direct et ses commandes de session comme `/login`, `/clear`, `/compact` ou `/model`.", "Si la définition ne tient pas en une phrase, la pratique sera floue. Simplifiez avant d’aller plus loin.", "claude-install.png"),
            ("La comparaison honnête", "Comparer ne veut pas dire choisir un vainqueur définitif. Sur le terrain, le bon outil dépend du moment : installation, création, relecture, correction, publication, budget, habitudes. Une personne peut préférer Codex pour relire et Claude Code pour exécuter, ou l’inverse. Le support montre une méthode de décision.", "Créez trois colonnes dans vos notes : `Situation`, `Codex`, `Claude Code`. Vous les remplirez au fil de la séance.", "La comparaison porte sur une situation réelle, pas sur une préférence personnelle.", "Codex sera jugé sur clarté, contrôle, installation, diff, review et surfaces disponibles.", "Claude Code sera jugé sur terminal, permissions, contexte, commandes, limites et continuité de travail.", "La bonne question n’est pas `lequel est le meilleur ?` mais `lequel m’aide le plus maintenant ?`", "first-comparison.png"),
            ("Le même dossier pour les deux", "Si Codex travaille dans un dossier et Claude Code dans un autre, le résultat ne veut plus rien dire. Les deux doivent voir la même page, les mêmes images, les mêmes règles et le même état Git. Cette discipline paraît basique, mais elle évite une grosse partie des confusions.", "Placez-vous dans le dossier `restaurant-comptoir-bleu`. Vérifiez le chemin avec `pwd` sur Mac/Linux/WSL ou avec le chemin affiché dans le terminal Windows.", "Les deux agents pointent vers le même dossier et vous voyez les mêmes fichiers.", "Codex travaille depuis le dossier sélectionné dans l’app ou depuis le terminal avec `codex`.", "Claude Code travaille depuis le terminal avec `claude` dans le dossier courant.", "Avant de parler à l’agent, demandez-vous : est-ce que je suis vraiment au bon endroit ?", "same-folder.png"),
            ("Le même brief pour les deux", "Une comparaison propre impose la même consigne. Si vous donnez à Codex une demande claire et à Claude Code une demande vague, vous comparez surtout votre prompt. Le brief commun doit dire le contexte, le résultat attendu, les limites et la vérification.", "Préparez le brief commun : `Dans la page du Comptoir Bleu, ajoute une formule midi. Garde fond blanc, accents bleu/violet, bouton Réserver visible, version mobile propre. À la fin, résume les fichiers modifiés.`", "Le même texte peut être envoyé aux deux outils.", "Codex reçoit le brief pour proposer un plan ou modifier le fichier selon le mode choisi.", "Claude Code reçoit le même brief et doit rester dans le même cadre.", "Un bon brief est comme une commande de terrain : court, précis, vérifiable.", "same-brief.png"),
            ("Les critères de décision", "Avant de lancer les agents, fixez les critères. On va observer cinq points : la clarté du plan, la prudence avant modification, la qualité du texte produit, la facilité à vérifier le résultat et le risque de changements inutiles. Ces critères empêchent de juger au feeling.", "Écrivez ces cinq critères au-dessus de votre tableau de comparaison.", "Chaque résultat sera noté avec les mêmes critères.", "Codex peut être très utile pour structurer les risques et relire un diff.", "Claude Code peut être très utile pour dérouler une correction guidée et expliquer le terminal.", "Sans critères, une interface plus agréable peut vous donner l’impression d’être plus fiable. Ce n’est pas toujours vrai.", "decision-matrix.png"),
            ("La règle du résultat visible", "Le test final n’est jamais la phrase de l’agent. Le test final est la page ouverte, le bouton testé, le mobile regardé et le diff compris. Une réponse peut être polie et pourtant laisser une page cassée. À l’inverse, une réponse courte peut produire un résultat propre.", "Après chaque modification, ouvrez la page et regardez la zone touchée. Le navigateur est votre juge principal.", "Le résultat se voit dans la page, pas seulement dans le terminal.", "Codex doit produire ou relire quelque chose de visible : diff, page, checklist, message de livraison.", "Claude Code doit produire la même preuve visible.", "À quoi sert une belle explication si le bouton Réserver ne clique nulle part ?", "browser-preview.png"),
            ("Le plan de travail", "Dans cette séance, le but est de comprendre comment bien utiliser Codex. On va voir ce que Codex fait, comment l’installer, comment lui parler, comment lire ses modifications et surtout comment savoir s’il faut choisir Codex ou Claude Code pour une tâche précise.", "Gardez ce plan ouvert pendant la lecture. Il sert de carte, pas de texte à apprendre par cœur.", "Vous savez ce que la séance va vous apprendre et pourquoi c’est utile.", "Codex sera introduit progressivement, sans supposer que vous connaissez déjà l’outil.", "Claude Code sera replacé en face de Codex pour montrer les vraies différences dans un travail concret.", "Si une étape vous semble trop rapide, revenez à la preuve : dossier, brief, fichier, navigateur.", "final-map.png"),
        ],
    ),
    (
        "Acte 2 - Installer et accéder",
        "Une comparaison sérieuse commence par les accès. On vérifie les commandes officielles, les comptes, les plans et les limites avant de demander une modification.",
        "Accès",
        "violet",
        [
            ("Les surfaces Codex à connaître", "Les docs OpenAI présentent Codex dans plusieurs surfaces : application locale, extension IDE, CLI, web et cloud. Cela peut sembler beaucoup, mais le choix reste simple : si vous voulez travailler depuis un dossier local, l’app ou le CLI suffisent. Si vous voulez déléguer une tâche liée à un dépôt, le cloud peut devenir utile.", "Ouvrez la documentation Codex Quickstart et repérez les options `App`, `IDE`, `CLI`, `Cloud`.", "Vous savez qu’il existe plusieurs portes d’entrée, sans les mélanger.", "Codex propose une app macOS/Windows, un CLI, une extension IDE et des tâches cloud selon l’accès.", "Claude Code propose terminal, web, desktop et intégrations selon le plan et la configuration.", "Ne choisissez pas l’outil parce que l’interface paraît plus moderne. Choisissez-le selon votre façon de travailler.", "local-vs-cloud.png"),
            ("Installation Codex CLI", "Le Quickstart officiel indique l’installation du CLI avec un installateur autonome sur macOS/Linux, une commande PowerShell sur Windows, et aussi des options npm ou Homebrew. Pour une première prise en main, copiez la commande officielle du jour plutôt qu’une commande vue dans une ancienne vidéo.", "Sur macOS/Linux : `curl -fsSL https://chatgpt.com/codex/install.sh | sh`. Sur Windows : utilisez la commande PowerShell officielle. Alternative : `npm install -g @openai/codex` ou `brew install --cask codex`.", "La commande `codex` répond dans le terminal.", "Codex peut ensuite se lancer avec `codex` depuis le dossier du projet.", "Claude Code utilise une commande différente, donc ne mélangez pas les installations.", "Tip terrain : gardez une note avec la date de vérification des commandes.", "codex-install.png"),
            ("Connexion Codex", "Codex demande une connexion avec un compte ChatGPT ou une clé API selon le mode. Les pages officielles indiquent que les plans ChatGPT incluent Codex avec des limites variables. Pour cette séance, partez avec votre compte ChatGPT, sauf cas précis où une clé API est demandée.", "Lancez `codex` dans le dossier test, puis suivez le flux de connexion. Ne collez pas de clé API dans un fichier du projet.", "La session Codex démarre et reconnaît votre dossier.", "Codex peut fonctionner avec ChatGPT ou API selon le contexte, mais les fonctionnalités peuvent varier.", "Claude Code peut utiliser un abonnement Claude ou une clé API selon la connexion.", "Une clé API est un secret. Si elle apparaît dans une capture ou un dépôt public, c’est une erreur.", "codex-login.png"),
            ("Installation Claude Code", "La documentation Claude Code indique une installation native. Sur macOS/Linux/WSL, la commande officielle actuelle passe par `https://claude.ai/install.sh`. Sur Windows PowerShell, elle passe par `https://claude.ai/install.ps1`. Le terminal utilisé compte beaucoup.", "Installez Claude Code avec la commande officielle adaptée à votre système. Lancez ensuite `claude` depuis le dossier.", "La session Claude Code s’ouvre dans le terminal.", "Codex et Claude Code ne partagent pas la même commande. Gardez deux lignes distinctes dans vos notes.", "Claude Code démarre avec `claude` et peut demander `/login` au premier usage ou pour changer de compte.", "Si vous êtes sous Windows, notez si vous utilisez PowerShell, CMD, Git Bash ou WSL. Ce détail évite beaucoup d’erreurs.", "claude-install.png"),
            ("Compte Claude et abonnement", "Le Help Center Anthropic explique que Claude Code peut être relié aux plans Pro ou Max avec les mêmes identifiants que Claude. Il précise aussi que Pro et Max partagent les limites entre Claude et Claude Code. Donc une grosse session de code peut compter dans le même budget d’usage que vos autres demandes Claude.", "Connectez-vous avec le bon compte Claude. Si vous êtes déjà connecté via un autre mode, utilisez `/login` pour vérifier.", "Le compte affiché est celui que vous voulez utiliser pour cette séance.", "Codex dépend de l’accès ChatGPT ou API choisi.", "Claude Code dépend du compte Claude, du plan et du mode de connexion.", "La question simple : est-ce que je teste l’outil, ou est-ce que je pars déjà sur un usage quotidien intensif ?", "pricing-comparison.png"),
            ("Prix à lire avec prudence", "Les prix changent. Au 3 juin 2026, la page Codex Pricing affiche Free à 0 $, Go à 8 $/mois, Plus à 20 $/mois et Pro à partir de 100 $/mois côté Codex. La page Claude Help Center affiche Free à 0 $, Pro à 20 $/mois, Max 5x à 100 $/mois et Max 20x à 200 $/mois. Vérifiez toujours les pages officielles avant de payer.", "Ouvrez les deux pages de pricing et notez le plan qui correspond à votre usage réel, pas au plan qui paraît le plus impressionnant.", "Vous savez où vérifier les prix et vous ne décidez pas sur une capture ancienne.", "Codex est rattaché aux plans ChatGPT/Codex avec des limites selon plan et usage.", "Claude Code est rattaché aux plans Claude ou à une facturation API selon le mode.", "Payez plus seulement si la limite bloque votre travail quotidien. Sinon, testez d’abord.", "pricing-comparison.png"),
            ("API ou abonnement", "L’abonnement sert à utiliser l’outil avec votre compte. L’API sert quand une application, un script ou une automatisation appelle le modèle. Les deux peuvent mener à des coûts, mais ce ne sont pas les mêmes habitudes. Le Help Center Claude avertit aussi qu’une variable `ANTHROPIC_API_KEY` peut faire utiliser l’API au lieu du plan.", "Vérifiez si vous avez une clé API dans votre environnement seulement si vous savez pourquoi elle est là. Sinon, restez sur la connexion par compte.", "Vous savez si vous utilisez un abonnement ou une facturation API.", "Codex peut accepter une clé API pour certains usages, avec des fonctionnalités cloud parfois différentes.", "Claude Code peut utiliser Pro/Max ou API selon la connexion et les variables d’environnement.", "Si le budget vous surprend, cherchez d’abord le mode de connexion utilisé.", "source-check.png"),
            ("La première commande Codex", "Une fois installé, Codex se lance avec `codex`. Le CLI officiel indique qu’il ouvre une interface terminale capable de lire le dépôt, proposer un plan, éditer et exécuter des commandes avec validation selon les modes. Pour la séance, on commence sans demander de modification.", "Dans le dossier, tapez `codex`, puis demandez : `Explique ce projet sans modifier les fichiers.`", "Codex répond sans toucher au projet.", "Codex doit vous montrer qu’il comprend le dossier avant d’agir.", "Claude Code fera exactement la même étape plus tard pour comparer.", "Le premier message ne doit pas être `améliore tout`. Il doit être `regarde et explique`.", "codex-plan.png"),
            ("La première commande Claude Code", "Claude Code se lance avec `claude`. Le Quickstart explique qu’il peut analyser les fichiers du projet et répondre sur la structure avant de faire un changement. Comme pour Codex, on commence avec une demande sans modification.", "Dans le même dossier, tapez `claude`, puis demandez : `Explique ce projet sans modifier les fichiers.`", "Claude Code décrit le dossier et ne crée rien.", "Codex et Claude Code ont reçu une première demande équivalente.", "Claude Code doit rester transparent sur les fichiers qu’il lit.", "Si un agent modifie avant que vous l’ayez demandé, stoppez et revenez à une demande plus stricte.", "claude-plan.png"),
            ("Le diagnostic avant la pratique", "Avant de comparer, vérifiez trois preuves : `codex` répond, `claude` répond, et la page s’ouvre localement. Sans ces trois preuves, la séance va se transformer en dépannage. Le dépannage est utile, mais il ne doit pas remplacer la comparaison.", "Faites une mini-checklist : commande Codex, commande Claude Code, page ouverte, bon dossier, compte attendu.", "Les deux outils sont prêts à recevoir le même brief.", "Codex est prêt côté installation et accès.", "Claude Code est prêt côté installation et accès.", "Quand tout bloque, copiez le message exact. Une erreur exacte vaut mieux que dix suppositions.", "risk-table.png"),
        ],
    ),
    (
        "Acte 3 - Préparer le dossier",
        "Le dossier devient le contrat commun. Les règles, le brief et l’état Git donnent aux deux agents le même terrain de travail.",
        "Cadre",
        "cyan",
        [
            ("Le dossier propre", "Le dossier `restaurant-comptoir-bleu` doit contenir seulement le projet de test. Si vous laissez des anciens essais, des captures privées ou des fichiers d’un autre client, les agents peuvent les lire ou les prendre en compte. Une comparaison propre commence par un dossier propre.", "Rangez le dossier. Gardez `index.html`, les images utiles, un README et les fichiers de règles. Supprimez les brouillons inutiles si vous savez qu’ils ne servent pas.", "Chaque fichier du dossier a un rôle clair.", "Codex travaille mieux quand le dossier ne contient pas de bruit inutile.", "Claude Code aussi, car le contexte lu influence ses propositions.", "Un dossier propre fait gagner plus de temps qu’un prompt compliqué.", "same-folder.png"),
            ("README comme carte simple", "Le README n’est pas réservé aux gros projets. Dans cette séance, il explique le but : page fictive du Comptoir Bleu, formule midi à ajouter, test mobile à vérifier. Quand vous revenez le lendemain, cette carte évite de tout redemander.", "Créez ou mettez à jour `README.md` avec trois lignes : objectif, fichier principal, vérifications attendues.", "Vous pouvez rouvrir le projet et comprendre le but sans la conversation.", "Codex peut lire ce README pour comprendre l’intention.", "Claude Code peut aussi s’appuyer dessus comme contexte de projet.", "Écrivez le README pour vous, pas pour impressionner. Simple et utile.", "handoff-summary.png"),
            ("AGENTS.md pour Codex", "Les docs OpenAI expliquent que Codex lit les fichiers `AGENTS.md` avant de travailler. Ce fichier sert à donner des attentes : commandes à lancer, style de code, limites, préférences. Pour notre page, il doit rester court, parce qu’un fichier de règles trop long devient lui-même un problème.", "Ajoutez `AGENTS.md` avec : fond blanc, accents bleu/violet, pas de dépendance sans accord, vérifier mobile, résumer les fichiers modifiés.", "Codex peut citer ou appliquer ces règles dans ses réponses.", "Codex a un cadre projet explicite.", "Claude Code n’utilise pas ce fichier comme source principale, mais le dossier reste compréhensible.", "Si Codex répète une erreur deux fois, ajoutez une règle courte dans `AGENTS.md`.", "agents-md.png"),
            ("CLAUDE.md pour Claude Code", "Claude Code utilise `CLAUDE.md` pour garder des conventions de projet. Les docs Anthropic recommandent de commencer par ce fichier quand vous avez des règles persistantes. Dans notre cas, il sert à rappeler le ton, le style, la contrainte mobile et la sécurité.", "Ajoutez `CLAUDE.md` avec les mêmes règles que `AGENTS.md`, adaptées à Claude Code.", "Claude Code comprend le cadre sans que vous recopiiez tout à chaque prompt.", "Codex reste cadré par `AGENTS.md`.", "Claude Code est cadré par `CLAUDE.md`.", "Gardez ces fichiers maigres. Ils sont faits pour guider, pas pour remplacer une demande claire.", "claude-md.png"),
            ("Même règle, deux fichiers", "Il peut sembler répétitif d’avoir `AGENTS.md` et `CLAUDE.md`, mais cette duplication est utile pour une séance de comparaison. Chaque agent reçoit son fichier naturel, avec les mêmes règles de fond. On réduit ainsi les écarts qui viennent du cadre.", "Copiez les règles essentielles dans les deux fichiers, avec le même sens et des phrases courtes.", "Les deux agents reçoivent la même intention de projet.", "Codex lit ses instructions projet.", "Claude Code lit ses conventions projet.", "Si une règle est importante, elle doit exister là où l’agent va vraiment la lire.", "first-comparison.png"),
            ("État Git avant le test", "Git n’est pas obligatoire pour comprendre, mais il rend la comparaison beaucoup plus nette. Avant le test, il faut savoir ce qui est déjà modifié. Sinon, vous ne saurez pas si une ligne vient de Codex, de Claude Code ou d’un ancien essai.", "Lancez `git status --short` si le projet est dans Git. Sinon, notez les fichiers présents avant de commencer.", "Vous connaissez l’état de départ.", "Codex pourra être jugé sur les fichiers réellement touchés.", "Claude Code pourra être jugé sur la même base.", "Ne comparez jamais deux agents avec un dossier déjà confus.", "git-status.png"),
            ("Branche ou copie de sécurité", "Pour tester deux outils, il faut pouvoir revenir en arrière. Une branche Git, un commit de départ ou une copie du dossier évite de perdre du temps si un agent change trop de choses. Cette sécurité rend la pratique plus calme.", "Créez un commit de départ ou une branche `comparaison-codex-claude` si Git est prêt.", "Vous pouvez revenir au point de départ.", "Codex peut travailler sans peur de casser définitivement la page.", "Claude Code aussi, parce que le retour arrière est prévu.", "La sécurité n’est pas une perte de temps. C’est ce qui permet d’oser tester.", "git-status.png"),
            ("Le brief maître", "Le brief maître est la consigne que l’on donnera aux deux agents. Il doit rester assez précis pour empêcher les écarts et assez court pour être copiable. Il doit aussi demander un résumé final, parce qu’un agent qui ne résume pas ses changements vous laisse faire le tri seul.", "Écrivez le brief maître dans `README.md` sous le titre `Mission séance 2`.", "Le brief peut être copié dans Codex et Claude Code sans modification.", "Codex reçoit exactement la mission prévue.", "Claude Code reçoit exactement la même mission.", "Un brief qui ne dit pas comment vérifier crée souvent un résultat difficile à juger.", "same-brief.png"),
            ("Les données fictives", "Le Comptoir Bleu est fictif. Les prix, horaires, plats et coordonnées doivent rester fictifs aussi. Cela permet de publier, partager et corriger sans risque. Le support technique doit donner une méthode, pas exposer une vraie donnée privée.", "Vérifiez que la page ne contient pas de vrai numéro, vraie adresse personnelle, clé API ou information sensible.", "Le projet peut être consulté sans dévoiler d’information privée.", "Codex ne doit pas inventer ou conserver de secret.", "Claude Code ne doit pas non plus ajouter de données réelles.", "Un projet de formation doit être publiable sans nettoyage stressant.", "risk-table.png"),
            ("Le feu vert de départ", "Le cadre est prêt quand cinq preuves sont là : les deux commandes répondent, le dossier est propre, les règles existent, l’état de départ est connu et le brief maître est écrit. À partir de là, la comparaison peut commencer sans partir dans tous les sens.", "Lisez la checklist à voix haute ou dans vos notes. Si un point manque, corrigez-le avant de lancer le duel.", "Le dossier est prêt pour un test juste.", "Codex va recevoir un contexte propre.", "Claude Code va recevoir le même contexte propre.", "La méthode paraît lente au début. Elle devient rapide quand vous la refaites tous les jours.", "final-map.png"),
        ],
    ),
    (
        "Acte 4 - Premier passage Codex",
        "Codex reçoit le brief en premier. On observe son plan, son niveau de prudence, le diff proposé et les preuves de vérification.",
        "Codex",
        "blue",
        [
            ("Lecture du projet par Codex", "Avant de lui demander d’ajouter la formule, Codex doit lire le projet et expliquer ce qu’il voit. Cette étape montre s’il comprend la page existante. Elle montre aussi s’il respecte la demande de ne rien modifier pour l’instant.", "Dans Codex : `Explique ce projet en 6 lignes. Ne modifie aucun fichier.`", "La réponse décrit `index.html`, les règles et le but du Comptoir Bleu.", "Codex commence par comprendre avant d’agir.", "Claude Code fera la même lecture ensuite pour comparer.", "Si la réponse parle d’un fichier qui n’existe pas, le dossier ou le contexte est mauvais.", "codex-plan.png"),
            ("Plan Codex avant modification", "Un bon agent ne saute pas tout de suite sur le fichier quand la tâche touche le rendu. Il propose un plan court : repérer le menu, ajouter une section formule midi, vérifier le bouton, tester mobile, résumer le diff. Le plan doit tenir en quelques étapes.", "Demandez : `Avant de modifier, propose un plan en 5 étapes maximum pour ajouter la formule midi.`", "Le plan est court, concret et adapté à la page.", "Codex montre comment il va procéder.", "Claude Code devra proposer un plan comparable.", "Un plan long peut cacher une demande mal cadrée. Gardez cinq étapes.", "codex-plan.png"),
            ("Autorisation de changer", "Après le plan, vous pouvez autoriser la modification. L’important est de garder la demande étroite. Codex ne doit pas refaire tout le site, changer la palette, renommer toutes les sections ou ajouter une dépendance inutile.", "Dites : `Applique seulement l’ajout de la formule midi et le lien du bouton si nécessaire. Ne refais pas tout le design.`", "Les changements restent limités à la mission.", "Codex modifie peu de fichiers, idéalement `index.html` seulement.", "Claude Code sera évalué sur la même retenue.", "La maîtrise vient souvent du mot `seulement` dans le prompt.", "diff-codex.png"),
            ("Diff Codex à lire", "Le diff raconte la vérité du travail. Même si vous ne comprenez pas chaque ligne, vous pouvez repérer les titres ajoutés, les textes, les liens et les classes modifiées. Si le diff touche une zone sans rapport, demandez pourquoi.", "Lisez le diff ou demandez : `Résume le diff fichier par fichier, sans vendre le résultat.`", "Vous savez ce qui a changé et pourquoi.", "Codex doit être capable d’expliquer ses changements simplement.", "Claude Code devra produire le même niveau de lisibilité.", "Un diff lu calmement vaut mieux qu’une confiance rapide.", "diff-codex.png"),
            ("Aperçu Codex dans le navigateur", "Après le diff, ouvrez la page. Le navigateur permet de voir les problèmes que le terminal ne montre pas : titre trop grand, bouton trop bas, section mal alignée, texte qui déborde. Ce test donne une preuve visuelle.", "Ouvrez `index.html` et regardez le haut de page, la nouvelle formule et le bouton Réserver.", "La formule midi apparaît et la page reste lisible.", "Codex est jugé sur le résultat visible.", "Claude Code sera jugé avec le même navigateur.", "Ne dites pas `c’est bon` tant que vous n’avez pas ouvert la page.", "browser-preview.png"),
            ("Test mobile après Codex", "Un restaurant se consulte souvent sur mobile. La formule midi doit rester lisible sur une largeur étroite. Les cartes ne doivent pas déborder, le bouton doit rester cliquable et le texte ne doit pas écraser la section suivante.", "Réduisez la fenêtre ou utilisez un aperçu mobile, puis notez deux points : lisibilité et bouton.", "La page fonctionne sur téléphone sans zoom.", "Codex doit corriger si le mobile casse.", "Claude Code devra passer le même test.", "Le mobile révèle vite les corrections de façade.", "mobile-check.png"),
            ("Question à Codex", "Une bonne comparaison inclut une question de recul. Demandez à Codex ce qu’il changerait s’il avait plus de temps, mais interdisez-lui de modifier. Vous verrez s’il distingue amélioration future et tâche actuelle.", "Demandez : `Sans modifier, quelles seraient les 3 prochaines améliorations utiles pour ce restaurant ?`", "Codex propose des pistes, pas de nouveau diff.", "Codex sert ici de conseiller.", "Claude Code sera aussi interrogé sans modifier.", "Un agent utile sait aussi ne pas agir.", "review-other-agent.png"),
            ("Codex et les images", "Codex peut aider à lire un screenshot ou une maquette selon la surface utilisée. Pour la séance, l’idée est simple : une image sert à montrer un problème visuel, pas à décorer la demande. Si vous envoyez une capture, expliquez ce que vous voulez vérifier.", "Si vous avez une capture de la page, demandez : `Regarde ce screenshot et dis seulement si la formule midi se repère vite.`", "La réponse se concentre sur le problème visuel.", "Codex peut utiliser le visuel comme contexte de design.", "Claude Code peut aussi travailler avec des éléments visuels selon l’environnement disponible.", "Une capture sans question claire devient vite une discussion floue.", "browser-preview.png"),
            ("Résumé Codex", "À la fin de son passage, Codex doit laisser une trace claire : fichiers touchés, changements faits, tests recommandés, limites. Ce résumé vous prépare à comparer avec Claude Code sans tout relire.", "Demandez : `Résume ton passage en 6 lignes : fichiers, changements, vérifications, limites.`", "Vous avez un résumé comparable au futur résumé Claude Code.", "Codex livre une trace exploitable.", "Claude Code devra produire une trace du même format.", "Le résumé final doit être court, factuel, et utile pour reprendre le travail.", "handoff-summary.png"),
            ("Note provisoire Codex", "Ne décidez pas encore. Notez seulement ce que Codex a bien fait et ce qui manque. Par exemple : plan clair, diff court, mobile à corriger, résumé précis. Cette note provisoire évite de mélanger les souvenirs quand Claude Code passera après.", "Remplissez la colonne Codex du tableau de comparaison avec faits observés, pas avec impressions vagues.", "La colonne Codex contient des preuves.", "Codex a été évalué sur le même projet.", "Claude Code va maintenant passer sur le même cadre.", "Écrire `rapide` ne suffit pas. Écrivez `rapide à quel moment et avec quelle preuve`.", "decision-matrix.png"),
        ],
    ),
    (
        "Acte 5 - Même passage avec Claude Code",
        "Claude Code reçoit le même brief. Le but n’est pas de refaire l’exercice au hasard, mais de comparer plan, diff, prudence et vérification.",
        "Claude Code",
        "violet",
        [
            ("Retour au point de départ", "Pour comparer honnêtement, il faut repartir du même état. Si Codex a déjà modifié la page, vous devez soit revenir au commit de départ, soit créer une copie avant Claude Code. Sinon Claude Code travaille sur le résultat de Codex, ce qui fausse le test.", "Revenez au point de départ avec Git ou une copie du dossier, puis relancez `claude` dans ce dossier.", "Claude Code voit la même base que Codex.", "Codex a eu son passage isolé.", "Claude Code démarre sans hériter d’un diff déjà appliqué.", "Si vous comparez deux cuisiniers, donnez-leur la même recette de départ.", "git-status.png"),
            ("Lecture par Claude Code", "Comme avec Codex, la première demande ne modifie rien. Claude Code doit expliquer la structure du projet, la page principale et les règles. Cette étape permet de repérer s’il lit bien `CLAUDE.md` et s’il comprend le Comptoir Bleu.", "Demandez : `Explique ce projet en 6 lignes. Ne modifie aucun fichier.`", "Claude Code décrit correctement le projet et ne crée rien.", "Codex avait déjà fait cette lecture.", "Claude Code montre sa compréhension avant action.", "La symétrie des étapes rend la comparaison plus juste.", "claude-plan.png"),
            ("Plan Claude Code", "Demandez ensuite un plan en cinq étapes. Observez s’il demande une validation, s’il repère le bouton, s’il garde le style et s’il propose une vérification mobile. Un plan utile n’est pas spectaculaire. Il rend l’action prévisible.", "Demandez : `Avant de modifier, propose un plan en 5 étapes maximum pour ajouter la formule midi.`", "Le plan de Claude Code peut être comparé au plan Codex.", "Codex a donné un plan que vous avez noté.", "Claude Code doit donner un plan aussi exploitable.", "Un plan prévisible rassure plus qu’un plan brillant mais vague.", "claude-plan.png"),
            ("Modification Claude Code", "Autorisez maintenant la même modification, avec les mêmes limites. Claude Code doit ajouter la formule midi, garder la page blanche avec accents bleu/violet et vérifier que le bouton Réserver garde son rôle. Il ne doit pas transformer toute la page.", "Dites : `Applique seulement l’ajout de la formule midi et le lien du bouton si nécessaire. Ne refais pas tout le design.`", "Le diff reste limité à la mission.", "Codex a été limité de la même manière.", "Claude Code montre s’il sait rester cadré.", "Si l’agent veut tout améliorer, ramenez-le à la mission du jour.", "diff-claude.png"),
            ("Diff Claude Code", "Lisez le diff comme avec Codex. Comparez la quantité de changements, la clarté des noms, la lisibilité du texte et les risques. Un diff plus long n’est pas forcément meilleur. Un diff très court n’est pas forcément suffisant.", "Demandez : `Résume le diff fichier par fichier, sans vendre le résultat.`", "Vous pouvez expliquer ce qui a changé.", "Codex a déjà donné un diff comparable.", "Claude Code doit expliquer ses lignes de manière simple.", "La question terrain : est-ce que je peux relire ce diff sans me perdre ?", "diff-claude.png"),
            ("Aperçu Claude Code", "Ouvrez la page après le passage Claude Code. Regardez la même zone : haut de page, formule midi, bouton, contact. Ne changez pas les critères en cours de route. Sinon la comparaison devient injuste.", "Ouvrez `index.html` et vérifiez exactement les mêmes points qu’après Codex.", "La formule midi apparaît et reste lisible.", "Codex a été testé dans le navigateur.", "Claude Code est testé dans le même navigateur.", "La méthode tient parce que les critères restent fixes.", "browser-preview.png"),
            ("Mobile après Claude Code", "Passez au mobile avec la même largeur que pour Codex. Regardez si le titre coupe mal, si le bouton se voit, si la nouvelle section prend trop de place. Le mobile est un bon juge parce qu’il force la simplicité.", "Testez la largeur mobile et notez les problèmes précis.", "La page reste lisible sur téléphone.", "Codex a une note mobile.", "Claude Code obtient une note mobile comparable.", "Ne notez pas `mobile OK` trop vite. Cliquez et lisez vraiment.", "mobile-check.png"),
            ("Question à Claude Code", "Comme pour Codex, demandez les trois prochaines améliorations sans modifier. On observe si Claude Code propose des pistes utiles ou s’il repart dans un chantier trop large. Un agent mature sait proposer sans envahir.", "Demandez : `Sans modifier, quelles seraient les 3 prochaines améliorations utiles pour ce restaurant ?`", "La réponse reste une liste de conseils, sans action cachée.", "Codex a déjà donné ses pistes.", "Claude Code donne ses pistes dans le même format.", "Le conseil est utile seulement s’il respecte la priorité actuelle.", "review-other-agent.png"),
            ("Résumé Claude Code", "À la fin, demandez le même résumé que pour Codex : fichiers, changements, vérifications, limites. Le format identique permet de comparer vite. Vous n’avez pas besoin de relire toute la conversation pour décider.", "Demandez : `Résume ton passage en 6 lignes : fichiers, changements, vérifications, limites.`", "Le résumé Claude Code est comparable au résumé Codex.", "Codex a laissé une trace.", "Claude Code laisse la même trace.", "Un bon résumé réduit la charge mentale après une session longue.", "handoff-summary.png"),
            ("Note provisoire Claude Code", "Remplissez maintenant la colonne Claude Code du tableau. Notez des faits : plan clair ou non, diff court ou large, mobile propre ou non, résumé utile ou non. À ce stade, vous avez deux passages comparables.", "Complétez la colonne Claude Code avec les mêmes critères que la colonne Codex.", "Le tableau contient deux séries de preuves.", "Codex est évalué sans être idéalisé.", "Claude Code est évalué sans être favorisé.", "La comparaison devient un outil de décision, pas un débat.", "decision-matrix.png"),
        ],
    ),
    (
        "Acte 6 - Comparer les preuves",
        "La comparaison devient concrète : on regarde les plans, les diffs, le mobile, les explications, le budget et les risques de terrain.",
        "Comparer",
        "green",
        [
            ("Plan contre plan", "Comparez les deux plans. Le meilleur plan n’est pas le plus long. C’est celui qui permet de savoir ce qui va être touché et comment le vérifier. Si un agent propose de tout refaire, il sort du cadre. Si l’autre oublie le mobile, il manque une contrainte importante.", "Dans votre tableau, notez `plan clair`, `plan trop large` ou `plan incomplet` pour chaque agent.", "Vous savez quel plan était le plus facile à suivre.", "Codex peut briller dans la structuration rapide d’un plan.", "Claude Code peut briller dans la progression étape par étape.", "La clarté du plan compte plus que le style de la réponse.", "first-comparison.png"),
            ("Diff contre diff", "Comparez maintenant les diffs. Regardez le nombre de fichiers touchés, la cohérence des noms, la simplicité du HTML/CSS, et les changements hors mission. Un outil qui touche moins de fichiers est souvent plus facile à contrôler, mais seulement si le résultat est complet.", "Placez les deux résumés de diff côte à côte.", "Vous savez quel diff est le plus facile à relire.", "Codex peut proposer un diff net, surtout si le brief est précis.", "Claude Code peut proposer un diff accompagné d’explications terminal.", "Le meilleur diff est celui que vous acceptez en comprenant pourquoi.", "diff-codex.png"),
            ("Texte contre texte", "Le contenu business compte. La formule midi doit parler simplement : ce que la personne obtient, à quel moment, et comment réserver. Si un agent écrit un texte trop marketing ou trop vague, demandez une correction. Le support doit rester humain et direct.", "Comparez les phrases proposées pour la formule midi. Gardez celle qui se comprend le plus vite.", "La section formule midi est claire et naturelle.", "Codex peut proposer plusieurs variantes de texte rapidement.", "Claude Code peut ajuster le texte dans le fichier et vérifier le rendu.", "Un texte simple bat presque toujours un texte trop décoratif.", "prompt-bad-good.png"),
            ("Mobile contre mobile", "Le mobile départage souvent les outils. L’un peut produire une section jolie sur desktop mais trop longue sur téléphone. L’autre peut rester plus simple mais plus lisible. Pour un usage business, la lisibilité mobile compte beaucoup.", "Comparez les captures ou vos notes mobile pour les deux passages.", "Vous savez quel résultat est le plus utilisable sur téléphone.", "Codex peut relire un screenshot et proposer une correction ciblée.", "Claude Code peut appliquer la correction dans le fichier local.", "Le mobile ne ment pas : si vous devez zoomer, il faut corriger.", "mobile-check.png"),
            ("Bouton Réserver", "Le bouton principal doit rester visible et mener à une zone utile. Si l’un des agents ajoute une section mais casse l’ancre du bouton, la page paraît avancée mais perd son action principale. C’est un bon test de sérieux.", "Cliquez le bouton Réserver dans les deux versions.", "Le bouton mène au contact ou à la réservation prévue.", "Codex doit repérer le lien ou l’ancre dans son analyse.", "Claude Code doit corriger le lien dans le fichier si besoin.", "Une page business sans action claire perd vite sa valeur.", "debug-flow.png"),
            ("Gestion des limites", "Les deux outils ont des limites d’usage et de contexte. Les pages officielles expliquent que les messages, la taille du projet, la durée de session et le mode local/cloud influencent la consommation. Ce n’est pas un détail : un projet trop large peut vider votre quota plus vite.", "Notez la durée de la session et la taille de la demande. Si vous approchez une limite, réduisez la tâche.", "Vous reliez les limites à votre manière de travailler.", "Codex compte selon plan, modèle, surface et usage agentique.", "Claude Code compte selon connexion, modèle, contexte et plan/API.", "Quand ça devient cher ou lent, découpez. Ce n’est pas un échec, c’est une méthode.", "pricing-comparison.png"),
            ("Commandes et permissions", "Comparez la manière dont chaque outil demande l’autorisation. Les permissions ne sont pas là pour ralentir. Elles protègent contre les commandes opaques, les modifications trop larges et les actions hors dossier. Au début, gardez un niveau de contrôle élevé.", "Notez quand l’outil demande une validation et ce qu’il explique avant d’agir.", "Vous savez quel agent vous laisse le plus de contrôle dans cette tâche.", "Codex propose des modes d’approbation et une TUI avec validation des étapes.", "Claude Code propose aussi des permissions et des modes de travail selon l’environnement.", "Une commande que vous ne comprenez pas doit être expliquée avant d’être lancée.", "approval-modes.png"),
            ("Mémoire de projet", "Codex a `AGENTS.md`, Claude Code a `CLAUDE.md`. Les deux fichiers servent à éviter de répéter les règles à chaque prompt. Mais ils ne remplacent pas votre demande du moment. Une règle permanente dit le style général ; le brief dit la mission précise.", "Vérifiez que les deux agents ont respecté les règles sans que vous les recopiiez entièrement.", "Les règles de projet ont été utiles sans devenir lourdes.", "Codex applique les instructions projet découvertes dans `AGENTS.md`.", "Claude Code applique les conventions lues dans `CLAUDE.md`.", "Si une règle ne sert qu’une fois, mettez-la dans le prompt, pas dans le fichier permanent.", "agents-md.png"),
            ("Second avis croisé", "La vraie force peut venir du duo. Après le passage Claude Code, demandez à Codex de relire le diff. Après le passage Codex, demandez à Claude Code de proposer une correction limitée. Cette revue croisée transforme la comparaison en méthode de travail.", "Demandez à un agent de relire le travail de l’autre en listant uniquement les risques réels.", "Vous obtenez une relecture sans relancer tout le chantier.", "Codex peut servir de reviewer clair.", "Claude Code peut servir de correcteur local après review.", "Le meilleur duo : un agent fait, l’autre relit, vous décidez.", "review-other-agent.png"),
            ("Conclusion provisoire", "À ce stade, vous n’avez pas besoin d’un verdict universel. Vous avez un verdict pour cette tâche : formule midi, page simple, mobile, bouton. Cette nuance est importante. Un outil peut gagner ici et être moins adapté demain.", "Écrivez une conclusion en trois lignes : `Pour cette tâche, je choisis... parce que... La prochaine fois, je vérifierai...`", "La décision repose sur des preuves observées.", "Codex garde sa place dans la méthode.", "Claude Code garde sa place dans la méthode.", "Une décision claire aujourd’hui n’empêche pas de changer demain.", "decision-matrix.png"),
        ],
    ),
    (
        "Acte 7 - Choisir au quotidien",
        "La séance devient une méthode de travail. On apprend dans quelles situations lancer Codex, Claude Code, ou les deux sur un vrai besoin business.",
        "Décider",
        "orange",
        [
            ("Quand lancer Codex d’abord", "Lancez Codex d’abord quand vous voulez un regard structuré, une revue, une explication rapide du projet, un plan avant correction ou une comparaison de pistes. Il est utile quand vous ne voulez pas forcément modifier tout de suite, mais comprendre les options.", "Pour une tâche inconnue, commencez par : `Explique le risque et propose un plan sans modifier.`", "Vous obtenez une direction avant d’ouvrir un chantier.", "Codex devient votre premier regard ou votre reviewer.", "Claude Code pourra ensuite exécuter une correction validée.", "Le bon premier geste peut être de réfléchir, pas de modifier.", "codex-plan.png"),
            ("Quand lancer Claude Code d’abord", "Lancez Claude Code d’abord quand vous voulez travailler directement dans le terminal, modifier un fichier précis, suivre une correction pas à pas, relancer des commandes et garder une relation forte avec le dossier local. C’est très pratique pour dérouler une tâche concrète.", "Pour une correction simple, demandez : `Modifie seulement ce fichier et explique le diff.`", "La correction avance dans le dossier local.", "Codex peut intervenir après pour relire.", "Claude Code porte l’exécution guidée.", "Quand la tâche est claire, l’exécution peut venir vite. Quand elle est floue, revenez au plan.", "claude-plan.png"),
            ("Quand utiliser les deux", "Utilisez les deux quand le résultat compte vraiment : page client, bug pénible, refonte visible, livraison publique. Un agent peut produire, l’autre peut relire. Cela évite de laisser une seule réponse décider de tout. Le duo doit rester cadré pour ne pas doubler le chaos.", "Faites produire par un outil, puis demandez à l’autre : `Relis seulement le diff et liste les risques réels.`", "La relecture ajoute de la valeur sans refaire tout le travail.", "Codex peut relire et proposer des risques.", "Claude Code peut appliquer une correction locale limitée.", "Deux agents mal cadrés font deux fois plus de bruit. Deux agents cadrés font un meilleur contrôle.", "parallel-workflow.png"),
            ("Routine de 15 minutes", "Chaque jour, choisissez une petite tâche business : corriger un bouton, ajouter une section, relire une page, préparer un résumé de livraison. Le but n’est pas de faire une grosse refonte. Le but est d’intégrer l’outil dans une routine utile.", "Lancez une tâche de 15 minutes : brief court, agent choisi, diff lu, navigateur ouvert, note finale.", "La tâche a un résultat visible avant la fin du quart d’heure.", "Codex peut être le point de départ ou le reviewer.", "Claude Code peut faire la modification locale.", "La régularité vient de petites tâches bien fermées.", "daily-routine.png"),
            ("Choix selon le budget", "Si vous atteignez souvent les limites, ne payez pas plus par réflexe. Regardez d’abord la cause : sessions trop longues, demandes trop larges, contexte énorme, modèle trop coûteux, agents lancés sans objectif. Le bon budget commence avec une bonne méthode.", "Notez pendant une semaine les moments où la limite vous bloque vraiment.", "Le plan choisi répond à un usage observé.", "Codex a des limites et crédits selon plan, surface et usage.", "Claude Code partage certaines limites avec Claude selon plan ou API.", "Un plan plus cher ne corrige pas un prompt trop large.", "pricing-comparison.png"),
            ("Choix selon le risque", "Sur un projet sensible, choisissez le mode qui vous laisse le plus de contrôle. Lisez les commandes, refusez les changements hors mission, gardez un commit de départ. Les outils savent aller vite, mais la sécurité vient de votre cadre.", "Avant une tâche sensible, créez un checkpoint Git et demandez un plan sans modification.", "Vous pouvez revenir en arrière si le changement dérape.", "Codex peut fonctionner avec approbations et review.", "Claude Code peut demander des validations avant édition.", "Plus le risque est haut, plus la demande doit être petite.", "approval-modes.png"),
            ("Choix selon la clarté", "Quand vous ne comprenez pas une réponse, ne continuez pas. Demandez une reformulation en français simple, puis réduisez la tâche. Un agent qui donne beaucoup de détails n’est pas forcément plus clair. La clarté se mesure à votre capacité de faire l’action suivante.", "Demandez : `Explique-moi l’étape suivante en 3 lignes et dis quel fichier sera touché.`", "Vous savez quoi faire juste après.", "Codex peut être très utile pour reformuler le plan.", "Claude Code peut expliquer le fichier ou la commande dans le contexte.", "Si la prochaine action n’est pas claire, la session doit ralentir.", "prompt-bad-good.png"),
            ("Choix selon le type de tâche", "Pour une revue, Codex peut être très pratique. Pour une correction locale dans le terminal, Claude Code peut être plus naturel. Pour une tâche cloud liée à GitHub, regardez les surfaces disponibles et les accès. Le choix dépend du type de travail, pas d’une fidélité à un outil.", "Classez votre tâche : comprendre, modifier, relire, publier, automatiser.", "Le type de tâche guide le choix de l’agent.", "Codex couvre app, CLI, IDE, web et cloud selon accès.", "Claude Code couvre terminal, web et autres surfaces selon plan et configuration.", "Le choix devient plus simple quand la tâche est nommée.", "local-vs-cloud.png"),
            ("Erreurs fréquentes", "Les erreurs reviennent souvent : mauvais dossier, mauvais compte, clé API exposée, brief trop vague, test mobile oublié, validation sans lecture, trop de changements en une demande. La séance sert aussi à reconnaître ces pièges avant qu’ils coûtent du temps.", "Relisez la liste avant chaque livraison importante.", "Vous repérez les erreurs avant de les subir.", "Codex n’empêchera pas toutes les erreurs de cadre.", "Claude Code non plus. Le cadre vient de vous.", "Un bon outil dans un mauvais dossier reste dangereux.", "risk-table.png"),
            ("Décision finale du jour", "Pour Le Comptoir Bleu, choisissez l’organisation qui vous paraît la plus efficace. Exemple : Claude Code pour modifier localement, Codex pour relire le diff et challenger le mobile. Ou l’inverse si Codex vous semble plus fluide dans votre environnement.", "Écrivez votre décision finale : outil principal, outil de relecture, règle de sécurité.", "Vous repartez avec une méthode personnelle et vérifiable.", "Codex trouve sa place concrète.", "Claude Code trouve sa place concrète.", "La meilleure méthode est celle que vous referez demain sans vous perdre.", "decision-matrix.png"),
        ],
    ),
    (
        "Acte 8 - Livrer et retenir",
        "La séance se termine avec une page consultable, un résumé clair, des sources officielles et une méthode simple à réutiliser.",
        "Livrer",
        "green",
        [
            ("Dernière version du Comptoir Bleu", "Choisissez la meilleure version issue du test ou combinez prudemment les points forts. Le résultat final doit rester simple : formule midi visible, bouton Réserver utile, mobile propre, texte naturel, pas de dépendance inutile.", "Gardez une seule version finale et supprimez les brouillons de comparaison si vous n’en avez plus besoin.", "La page finale est claire et consultable.", "Codex peut aider à relire la version finale.", "Claude Code peut appliquer les dernières corrections locales.", "Ne gardez pas deux versions si vous ne savez plus laquelle livrer.", "browser-preview.png"),
            ("Checklist avant publication", "Avant de publier, vérifiez le nom du restaurant, la formule midi, les horaires fictifs, le contact, le bouton, le mobile, le diff Git et l’absence de secret. Cette checklist est courte, mais elle couvre les erreurs les plus visibles.", "Créez une checklist dans le README ou cochez-la dans vos notes.", "Tous les points importants sont contrôlés.", "Codex peut générer la checklist ou la relire.", "Claude Code peut l’ajouter au README.", "Une livraison sans checklist finit souvent avec un oubli simple.", "daily-routine.png"),
            ("Résumé de livraison", "Le résumé final doit être compréhensible sans ouvrir la conversation. Il dit l’objectif, les fichiers modifiés, les vérifications faites, le lien final et la prochaine action. C’est utile pour vous, pour un client, ou pour reprendre le projet plus tard.", "Rédigez un résumé de 6 lignes : objectif, outils utilisés, fichiers, tests, limites, prochaine étape.", "Quelqu’un comprend le travail sans relire toute la séance.", "Codex peut proposer une version du résumé.", "Claude Code peut écrire le résumé dans le README.", "Un bon résumé évite la phrase `je ne sais plus ce que j’ai fait`.", "handoff-summary.png"),
            ("Publication GitHub Pages", "Une page simple peut être publiée avec GitHub Pages. Le point important est de pousser les bons fichiers, pas les vidéos lourdes, les fichiers système ou les secrets. Le lien public doit être ouvert après publication pour vérifier le rendu réel.", "Poussez seulement les fichiers utiles : `index.html`, CSS, images, scripts de génération si vous voulez garder la source.", "Le lien public s’ouvre et affiche la page attendue.", "Codex peut aider à relire le dépôt avant push.", "Claude Code peut aider à préparer la commande Git et le résumé.", "Un push réussi ne garantit pas une page correcte. Ouvrez l’URL.", "source-check.png"),
            ("Sources officielles à garder", "Les commandes d’installation, les prix, les limites et les surfaces changent. Gardez les liens officiels dans le support : OpenAI Codex Quickstart, Codex Pricing, AGENTS.md, Claude Code Quickstart, Pro/Max, limites et CLAUDE.md. La date de vérification doit rester visible.", "Ajoutez une section sources dans vos notes ou dans le support final.", "Vous savez où vérifier avant de répéter l’installation.", "Codex doit être vérifié côté docs OpenAI.", "Claude Code doit être vérifié côté docs Anthropic.", "Quand une info coûte de l’argent ou bloque une installation, vérifiez la source officielle.", "source-check.png"),
            ("Ce que la comparaison a appris", "La séance montre surtout une méthode. Codex et Claude Code peuvent tous les deux aider à coder. Le vrai niveau se voit dans votre façon de cadrer : même dossier, même brief, même test, même vérification, décision finale humaine.", "Relisez votre tableau et gardez les trois règles qui vous ont le plus aidé.", "Vous repartez avec une méthode, pas seulement une opinion.", "Codex reste un outil de travail, pas une réponse magique.", "Claude Code aussi. Les deux demandent un cadre.", "Une méthode simple bat un comparatif sans preuve.", "final-map.png"),
            ("Méthode à réutiliser demain", "Demain, vous pouvez refaire la même méthode sur une page artisan, un mini-outil interne, une landing page ou une correction de bug. Il suffit de remplacer le Comptoir Bleu par le vrai projet et de garder les étapes : préparer, demander, comparer, vérifier, livrer.", "Créez un modèle de brief réutilisable en quatre lignes : contexte, action, contraintes, vérification.", "Le modèle peut servir sur un autre projet.", "Codex reçoit un brief propre dès le départ.", "Claude Code reçoit le même niveau de contexte.", "Ce que vous répétez devient votre vrai système de travail.", "prompt-bad-good.png"),
            ("Petit test final", "Pour vérifier que la séance est comprise, posez-vous une question : si demain le bouton Réserver ne marche plus, quel outil lancez-vous, quelle demande écrivez-vous, et quelle preuve attendez-vous ? Si la réponse est claire, la séance a fait son travail.", "Écrivez la réponse en trois lignes dans vos notes.", "Vous savez transformer un problème en demande vérifiable.", "Codex peut analyser le risque et proposer le plan.", "Claude Code peut corriger le lien localement.", "La bonne réponse contient toujours une preuve finale.", "debug-flow.png"),
            ("Le détail qui montre le sérieux", "Un support bien fait ne se contente pas d’être joli. Il aide à ne pas se perdre. Les micro-interactions, les boutons copier, les ancres de section et la progression de lecture sont là pour rendre le parcours plus fluide, pas pour décorer.", "Utilisez les blocs copiables et les ancres pour retrouver vite une étape.", "La page reste utile pendant la pratique.", "Codex peut aider à améliorer ce support plus tard.", "Claude Code peut aussi modifier la page support avec le même cadre.", "Un détail utile est mieux qu’un effet qui distrait.", "easter-egg.png"),
            ("Dernière phrase de méthode", "La comparaison tient en une phrase : même projet, même brief, même contrôle, puis choix selon la situation. Si vous gardez cette phrase, vous pouvez utiliser Codex et Claude Code sans les opposer inutilement. Le but est d’avancer proprement sur un vrai travail.", "Gardez la phrase finale dans votre README ou dans vos notes de séance.", "Vous pouvez refaire le parcours sans relire les 80 sections.", "Codex a une place claire.", "Claude Code a une place claire.", "Le bon outil est celui qui vous aide à produire, vérifier et livrer sans perdre le contrôle.", "final-map.png"),
        ],
    ),
]


def _codex_item(
    title: str,
    story: str,
    action: str,
    check: str,
    image: str,
    codex: str | None = None,
    claude: str | None = None,
    tip: str | None = None,
) -> tuple[str, str, str, str, str, str, str, str]:
    return (
        title,
        story,
        action,
        check,
        codex or "Codex est l’outil principal de cette étape. Il sert à comprendre, organiser, modifier ou relire un projet selon le contexte.",
        claude or "Claude Code sert ici de repère de comparaison. Il a déjà été vu avant, donc on ne refait pas son installation.",
        tip or "Gardez une preuve simple avant de continuer : un écran, un fichier, un diff, une commande ou un résumé clair.",
        image,
    )


def _build_codex_chapters() -> list[tuple[str, str, str, str, list[tuple[str, str, str, str, str, str, str, str]]]]:
    return [
        (
            "Acte 1 - Comprendre Codex",
            "Cette première partie pose les bases : ce qu’est Codex, à quoi il sert, et pourquoi on ne l’utilise pas exactement comme Claude Code.",
            "Comprendre",
            "blue",
            [
                _codex_item("C’est quoi Codex ?", "Codex est l’agent de code d’OpenAI. Il sert à travailler sur des projets : comprendre un dossier, proposer un plan, modifier des fichiers, relire un diff, préparer une livraison ou lancer une tâche depuis plusieurs surfaces.", "Retenez une définition simple : `Codex m’aide à faire avancer un projet de code avec des actions vérifiables.`", "Vous savez expliquer Codex en une phrase sans parler de magie ou d’outil vague.", "web-captures/codex-product-official.png", tip="Si la définition ne parle pas de projet, de fichiers ou de vérification, elle reste trop floue."),
                _codex_item("À quoi ça sert dans un vrai travail", "Codex devient utile quand une tâche doit produire quelque chose : corriger une page, relire un bug, créer une branche, préparer une checklist, analyser une erreur ou organiser un plan d’action. Il ne sert pas seulement à discuter.", "Prenez un exemple concret : `corriger le bouton Réserver`, `relire un fichier`, `préparer une PR`, `expliquer un bug`.", "L’exemple contient une action et un résultat observable.", "web-captures/codex-use-cases-official.png", tip="Une demande utile commence souvent par un verbe : lire, corriger, créer, relire, vérifier."),
                _codex_item("Différence entre ChatGPT et Codex", "ChatGPT aide surtout à réfléchir et écrire. Codex va plus loin dans un contexte de travail : il peut se connecter à un projet, suivre des règles, lire des fichiers, proposer des changements et travailler avec des outils selon les accès activés.", "Écrivez deux colonnes : `ChatGPT = expliquer`, `Codex = agir dans un projet`.", "Vous ne demandez pas à ChatGPT seul de faire ce que Codex doit faire avec un dossier.", "codex-home-screen.png", tip="Quand il faut modifier un fichier ou relire un diff, pensez Codex plutôt qu’un simple chat."),
                _codex_item("Différence entre app et terminal", "Codex existe dans l’interface et dans le terminal. L’app est pratique pour piloter des projets, plugiciels, automatisations et tâches visuelles. Le terminal est pratique quand vous êtes déjà dans un dossier local et que vous voulez une commande directe.", "Associez chaque surface à un usage : app pour organiser et piloter, terminal pour travailler vite dans un dossier.", "Vous savez pourquoi les deux surfaces existent au lieu de les confondre.", "web-captures/codex-app-docs-official.png", tip="Le bon choix dépend surtout d’où vous travaillez déjà : navigateur/app ou terminal."),
                _codex_item("Ce que Codex peut faire", "Codex peut lire un dossier, proposer un plan, modifier des fichiers, expliquer une erreur, relire un changement, utiliser des plugiciels, lancer des automatisations et travailler avec un dépôt selon la configuration.", "Listez trois choses que vous voulez vraiment lui demander cette semaine.", "Chaque demande est reliée à un fichier, un projet ou une tâche de travail.", "web-captures/codex-app-article-official.png", tip="Plus la tâche est concrète, plus Codex a de chances de vous aider proprement."),
                _codex_item("Ce que Codex ne doit pas décider seul", "Codex peut aller vite, mais il ne doit pas décider seul d’un changement large, d’un accès sensible, d’une publication ou d’une suppression. Le contrôle reste humain : vous lisez, vous vérifiez, puis vous acceptez.", "Ajoutez une règle personnelle : `pas de gros changement sans plan court avant action`.", "Vous savez refuser ou réduire une proposition trop large.", "web-captures/codex-permissions-official.png", tip="Un agent rapide sans limite peut faire perdre du temps. La limite fait partie du travail."),
                _codex_item("Pourquoi Codex aide sur un projet", "Un projet contient du contexte : fichiers, règles, erreurs, historique et objectifs. Codex est utile parce qu’il peut travailler avec ce contexte au lieu de répondre seulement à une question isolée.", "Choisissez un projet simple pour la séance : une page existante, un mini-site ou un dossier de test.", "Le projet est assez petit pour être compris et assez concret pour être vérifié.", "same-folder.png", tip="Un petit projet propre vaut mieux qu’un gros dossier confus pour apprendre."),
                _codex_item("Claude Code comme repère", "Claude Code a déjà été vu avant. Dans cette séance, il ne sert pas à refaire l’installation. Il sert seulement de repère : même famille d’outils, mais surface, habitudes et intégrations différentes.", "Gardez une phrase simple : `Claude Code = terminal Anthropic ; Codex = agent OpenAI avec app, CLI, cloud et plugiciels`.", "La comparaison reste courte et ne remplace pas l’apprentissage de Codex.", "claude-install.png", tip="Ne transformez pas la séance Codex en deuxième séance Claude Code."),
                _codex_item("Le fil rouge de la séance", "Le fil rouge est simple : apprendre Codex assez bien pour savoir quelle surface utiliser. On part de l’interface, on passe par le terminal, puis on voit les plugiciels, les automatisations et la comparaison finale.", "Gardez le plan sous les yeux. Chaque acte répond à une question précise.", "Vous savez pourquoi chaque partie arrive dans cet ordre.", "final-map.png", tip="Si une section semble abstraite, rattachez-la à cette question : où est-ce que Codex travaille ?"),
                _codex_item("La méthode à suivre", "La méthode restera toujours la même : comprendre la surface, cadrer la demande, vérifier les accès, lire la proposition, contrôler le résultat, puis résumer. Cette boucle évite de partir dans tous les sens.", "Écrivez la boucle : `surface -> demande -> accès -> diff -> vérification -> résumé`.", "La boucle est claire avant de passer à l’interface.", "daily-routine.png", tip="Une bonne méthode simple bat une longue liste de fonctionnalités apprises sans ordre."),
            ],
        ),
        (
            "Acte 2 - Découvrir l’interface Codex",
            "Cette partie explique l’écran Codex : accueil, message, projet, modèle, accès, mode de raisonnement, historique et paramètres.",
            "Interface",
            "violet",
            [
                _codex_item("L’écran d’accueil", "L’accueil Codex sert à démarrer une demande. On y trouve la zone de message, le choix de projet, le niveau d’accès et le modèle. C’est le point de départ pour comprendre comment Codex va travailler.", "Repérez les quatre zones : message, accès, modèle, projet.", "Vous savez où poser une demande et où regarder le contexte actif.", "codex-home-screen.png", tip="Avant d’écrire, regardez toujours si un projet est sélectionné ou non."),
                _codex_item("La zone de message", "La zone de message reçoit votre demande. Une bonne demande ne dit pas seulement `fais mieux`. Elle donne le contexte, l’objectif, les limites et la preuve attendue.", "Préparez une demande courte : `Lis ce projet et explique ce qu’il contient. Ne modifie rien.`", "Codex répond sans partir directement dans une modification.", "codex-home-screen.png", tip="La première demande doit souvent être une lecture, pas une action."),
                _codex_item("Le choix du modèle", "Le modèle indique le niveau de raisonnement utilisé. Un modèle plus approfondi peut être utile pour une tâche complexe, mais il peut aussi être plus lent. Le choix doit suivre la difficulté de la tâche.", "Pour une demande simple, gardez un mode normal. Pour une analyse large, utilisez un mode plus approfondi.", "Le modèle choisi correspond au niveau de difficulté réel.", "codex-home-screen.png", tip="Ne mettez pas le mode le plus lourd par réflexe. Commencez simple quand la tâche est simple."),
                _codex_item("Le mode très approfondi", "Le mode très approfondi sert quand il faut réfléchir longtemps : architecture, bug difficile, refonte risquée, comparaison de solutions. Il n’est pas nécessaire pour renommer un bouton ou relire un petit texte.", "Posez-vous la question : `est-ce que cette tâche demande une vraie réflexion ou seulement une exécution propre ?`", "Le mode choisi ne ralentit pas inutilement le travail.", "codex-home-screen.png", tip="Le bon mode est celui qui répond au risque, pas celui qui paraît plus sérieux."),
                _codex_item("Le mode Fast", "Le mode Fast vise la vitesse. Il peut aider pour des tâches courtes, mais il ne remplace pas la vérification. Plus la tâche est sensible, plus vous devez lire le résultat avant d’accepter.", "Utilisez Fast seulement sur une action claire et peu risquée.", "Vous savez quand aller vite et quand ralentir.", "codex-home-screen.png", tip="Fast sert à gagner du temps, pas à sauter la relecture."),
                _codex_item("Le niveau d’accès", "Le niveau d’accès dit ce que Codex peut faire. C’est une partie très importante : lire, modifier, utiliser des outils, accéder à des données ou lancer des actions. Un accès trop large sans cadre peut créer des surprises.", "Avant de lancer une tâche, vérifiez le niveau d’accès affiché.", "Vous savez ce que Codex est autorisé à faire dans cette session.", "web-captures/codex-permissions-official.png", tip="Si vous ne comprenez pas un accès, baissez le niveau ou demandez une explication."),
                _codex_item("Travailler sur un projet", "Le bouton de projet rattache Codex à un contexte. Sans projet, Codex peut répondre de manière générale. Avec un projet, il peut travailler avec des fichiers, des règles et un historique.", "Sélectionnez un projet seulement si vous voulez que Codex tienne compte de ce dossier.", "Le projet affiché correspond bien au travail en cours.", "codex-home-screen.png", tip="Le mauvais projet est une source classique d’erreurs."),
                _codex_item("Les projets dans la sidebar", "La barre latérale montre des projets et des conversations précédentes. Elle sert à retrouver le bon contexte. Mais attention : un ancien projet peut garder une intention qui ne correspond plus à la tâche actuelle.", "Lisez le nom du projet avant de reprendre une conversation.", "Vous ne reprenez pas une ancienne session par accident.", "codex-home-screen.png", tip="Si la session est confuse, ouvrez une nouvelle conversation dans le bon projet."),
                _codex_item("Les clavardages précédents", "Les anciens clavardages peuvent servir d’historique, mais ils peuvent aussi vous enfermer dans un vieux contexte. Pour une nouvelle tâche importante, il vaut mieux repartir proprement avec une demande claire.", "Décidez si vous reprenez un ancien clavardage ou si vous partez d’un nouveau.", "La conversation utilisée correspond vraiment à la tâche du moment.", "codex-home-screen.png", tip="Un ancien fil n’est utile que si son contexte est encore bon."),
                _codex_item("Les paramètres Codex", "Les paramètres servent à gérer les préférences, les plugiciels, les accès et les habitudes de travail. On ne change pas tout dès le début. On observe d’abord ce qui est activé.", "Ouvrez les paramètres et repérez les zones liées aux accès, plugiciels et projets.", "Vous savez où revenir quand un comportement Codex vous surprend.", "web-captures/codex-app-docs-official.png", tip="Un réglage doit répondre à un problème réel, pas à une curiosité."),
            ],
        ),
        (
            "Acte 3 - Installer Codex en terminal",
            "Cette partie explique pourquoi et comment utiliser Codex CLI dans un dossier local, avec les commandes officielles et les bons contrôles.",
            "Terminal",
            "cyan",
            [
                _codex_item("Pourquoi utiliser le terminal", "Le terminal est utile quand vous travaillez déjà dans un dossier local. Vous pouvez lancer Codex depuis le projet, lui demander de lire les fichiers, proposer un diff et exécuter certaines commandes avec validation.", "Retenez : app pour piloter, terminal pour agir vite dans un dossier local.", "Vous savez pourquoi le CLI existe même si l’app Codex existe aussi.", "web-captures/codex-cli-docs-official.png", tip="Le terminal n’est pas obligatoire pour tout, mais il est très efficace dans un dossier de code."),
                _codex_item("Préparer les prérequis", "Avant d’installer, il faut savoir sur quel système vous travaillez : macOS, Windows ou Linux. Le Quickstart officiel indique que le CLI est supporté sur ces trois environnements.", "Notez votre système et ouvrez le terminal adapté.", "Vous choisissez la bonne commande pour votre système.", "web-captures/codex-cli-install-official.png", tip="Beaucoup d’erreurs viennent d’une commande copiée pour le mauvais système."),
                _codex_item("Installer Codex CLI", "La documentation officielle donne plusieurs routes : installateur autonome, PowerShell Windows, npm ou Homebrew. La commande à utiliser dépend de votre machine et de votre préférence.", "macOS/Linux : `curl -fsSL https://chatgpt.com/codex/install.sh | sh`. Windows : commande PowerShell officielle. Alternatives : `npm install -g @openai/codex` ou `brew install --cask codex`.", "La commande d’installation vient de la page officielle, pas d’une vieille capture.", "web-captures/codex-cli-install-official.png", tip="Vérifiez toujours la commande officielle avant une nouvelle installation."),
                _codex_item("Vérifier que codex répond", "Une installation n’est pas validée parce que la commande a semblé se terminer. Elle est validée quand `codex` répond dans le terminal. C’est la preuve minimale.", "Tapez `codex --help` ou lancez simplement `codex` selon votre cas.", "Le terminal reconnaît la commande Codex.", "codex-install.png", tip="Si `codex` ne répond pas, ne passez pas à la suite. Corrigez d’abord l’installation."),
                _codex_item("Se connecter au compte", "Au premier lancement, Codex demande une connexion avec un compte ChatGPT ou une clé API selon le mode. Pour la plupart des usages de cette séance, la connexion ChatGPT est le chemin le plus simple.", "Lancez `codex` puis suivez la connexion proposée.", "La session indique que vous êtes connecté et prêt à travailler.", "codex-login.png", tip="Ne collez jamais une clé API dans un fichier public ou dans une capture destinée à être partagée."),
                _codex_item("Compte ChatGPT ou API", "Compte ChatGPT et API ne sont pas la même chose. Le compte sert à utiliser Codex avec votre abonnement. L’API sert plutôt quand un script ou un système appelle OpenAI avec une clé.", "Notez quel mode vous utilisez : compte ChatGPT ou clé API.", "Vous savez d’où viendra l’usage et le coût éventuel.", "web-captures/codex-pricing-official.png", tip="Si un coût vous surprend, vérifiez d’abord le mode de connexion."),
                _codex_item("Ouvrir le bon dossier", "Codex CLI travaille dans le dossier courant. Si vous lancez Codex au mauvais endroit, il peut analyser ou modifier les mauvais fichiers. Le chemin du terminal passe donc avant le prompt.", "Dans le terminal : `cd chemin/vers/votre-projet`, puis vérifiez avec `pwd`.", "Le dossier affiché est bien celui du projet.", "same-folder.png", tip="Avant chaque session terminal, vérifiez le nom du dossier."),
                _codex_item("Lancer Codex dans un projet", "Une fois dans le bon dossier, `codex` démarre la session. La première demande doit être prudente : comprendre sans modifier. Cela confirme que Codex voit le bon contexte.", "Demandez : `Explique ce projet en 6 lignes. Ne modifie aucun fichier.`", "Codex décrit le projet sans créer ni modifier.", "web-captures/codex-cli-docs-official.png", tip="Première demande : observer. Deuxième demande : agir."),
                _codex_item("Premier diagnostic si ça bloque", "Si Codex ne se lance pas, ne multipliez pas les commandes. Regardez le message exact, le système, le mode d’installation et le chemin du terminal. Une erreur exacte permet d’aller plus vite.", "Copiez le message d’erreur complet et cherchez la cause : installation, connexion, permissions ou chemin.", "Vous avez une piste claire au lieu d’un dépannage au hasard.", "risk-table.png", tip="Un message d’erreur complet vaut mieux qu’une phrase approximative."),
                _codex_item("Checkpoint Git avant action", "Codex peut modifier des fichiers. La doc recommande de créer des checkpoints Git pour revenir en arrière. Même sur un petit projet, ce réflexe protège votre travail.", "Avant une vraie modification : `git status`, puis commit ou branche de test si besoin.", "Vous pouvez revenir à l’état initial si Codex change trop de choses.", "git-status.png", tip="Le retour arrière prévu rend l’expérimentation beaucoup plus calme."),
            ],
        ),
        (
            "Acte 4 - Bien utiliser Codex CLI",
            "Cette partie montre comment parler au CLI : plan, lecture, mission précise, diff, commandes, tests, Git et résumé.",
            "CLI",
            "cyan",
            [
                _codex_item("Demander un plan avant action", "Quand la tâche peut toucher plusieurs fichiers, demandez un plan avant modification. Le plan vous permet de refuser une direction trop large avant que le diff existe.", "Demandez : `Propose un plan en 5 étapes. Ne modifie rien pour l’instant.`", "Le plan annonce les fichiers et les contrôles prévus.", "codex-plan.png", tip="Plan court d’abord, modification ensuite."),
                _codex_item("Demander une lecture du dossier", "Une lecture du dossier sert à vérifier que Codex comprend le projet. Cette étape est utile au début, après une longue pause ou quand le dossier vient d’être récupéré.", "Demandez : `Liste les fichiers importants et explique leur rôle en une phrase.`", "Vous savez ce que Codex a compris du projet.", "same-folder.png", tip="Si Codex oublie un fichier important, donnez-lui le chemin explicitement."),
                _codex_item("Donner une mission précise", "Une mission précise contient l’action, la zone, les limites et la preuve. Exemple : `corrige le bouton Réserver dans index.html, sans toucher au reste, puis résume le diff`.", "Transformez une demande vague en demande précise avant de l’envoyer.", "La demande peut être vérifiée sans interprétation.", "prompt-bad-good.png", tip="Une phrase précise évite dix corrections derrière."),
                _codex_item("Limiter les fichiers touchés", "Codex peut parfois proposer plus que nécessaire. Si la tâche est petite, limitez les fichiers ou les zones. Cela rend le diff plus facile à relire.", "Ajoutez : `Ne touche qu’à index.html sauf si tu expliques pourquoi.`", "Le diff reste dans la zone attendue.", "diff-codex.png", tip="Limiter n’empêche pas Codex de travailler ; ça l’aide à rester utile."),
                _codex_item("Lire les changements proposés", "Lire un diff ne demande pas de tout comprendre. Regardez les fichiers touchés, les titres ajoutés, les suppressions et les zones hors mission. C’est déjà un bon contrôle.", "Demandez : `Résume le diff fichier par fichier, sans phrase marketing.`", "Vous savez ce qui a changé et pourquoi.", "diff-codex.png", tip="Un diff que vous ne comprenez pas doit être expliqué avant validation."),
                _codex_item("Comprendre les permissions", "Les permissions servent à contrôler les actions : lecture, édition, commandes, réseau ou accès sensible. Plus une action est risquée, plus la permission doit être lue calmement.", "Si Codex demande une permission, lisez l’action exacte avant d’accepter.", "Vous savez ce que vous autorisez.", "web-captures/codex-permissions-official.png", tip="Une permission n’est pas une gêne. C’est un garde-fou."),
                _codex_item("Lancer une commande de test", "Codex peut proposer une commande pour vérifier : build, test, lint ou ouverture locale. La commande doit être comprise avant d’être lancée.", "Demandez : `Explique cette commande en français simple avant de la lancer.`", "La commande a un rôle clair et un résultat attendu.", "web-captures/codex-cli-features-official.png", tip="Une commande inconnue ne doit pas être lancée par automatisme."),
                _codex_item("Vérifier avec Git", "Git donne une vue fiable des changements. `git status` montre les fichiers modifiés ; `git diff` montre le détail. Ces deux commandes complètent la réponse Codex.", "Après action : `git status --short`, puis relisez le diff important.", "Les fichiers modifiés correspondent à la mission.", "git-status.png", tip="Si un fichier inattendu apparaît, demandez une explication avant de continuer."),
                _codex_item("Refuser une action risquée", "Un bon usage de Codex inclut le refus. Si la proposition touche trop de fichiers, installe une dépendance inutile ou change le style global, réduisez la mission.", "Écrivez : `Stop. Reviens à une correction limitée. Ne touche pas aux autres fichiers.`", "La session revient à une action contrôlable.", "approval-modes.png", tip="Refuser tôt coûte moins cher que corriger tard."),
                _codex_item("Résumer la session", "À la fin d’une session terminal, demandez un résumé. Il doit dire ce qui a été demandé, ce qui a changé, ce qui a été vérifié et ce qui reste à faire.", "Demandez : `Résumé final en 6 lignes : objectif, fichiers, diff, tests, limite, prochaine étape.`", "Vous pouvez reprendre la session sans relire toute la conversation.", "handoff-summary.png", tip="Un résumé clair transforme une session longue en trace utile."),
            ],
        ),
        (
            "Acte 5 - Travailler sur un projet",
            "Cette partie met Codex dans un vrai dossier : règles, AGENTS.md, petite modification, vérification, revue et livraison.",
            "Projet",
            "green",
            [
                _codex_item("Choisir un dossier propre", "Un dossier propre aide Codex à répondre juste. Si le dossier contient de vieux tests, des secrets ou des fichiers sans rapport, le contexte devient mauvais.", "Gardez seulement les fichiers utiles au projet de test.", "Chaque fichier a un rôle compréhensible.", "same-folder.png", tip="Plus le dossier est clair, moins le prompt doit compenser."),
                _codex_item("Expliquer le projet", "Codex travaille mieux quand le projet a une intention claire. Un README simple suffit : objectif, fichier principal, commande de test, règles visuelles et limite de sécurité.", "Ajoutez ou relisez `README.md` avant de demander une action.", "Codex peut comprendre le projet sans deviner.", "handoff-summary.png", tip="Un README court peut éviter de répéter le même contexte à chaque session."),
                _codex_item("Créer AGENTS.md", "AGENTS.md est le fichier de consignes projet pour Codex. Il peut contenir le style attendu, les commandes utiles, les fichiers à éviter et les règles de livraison.", "Créez un `AGENTS.md` court avec 5 règles maximum.", "Codex peut s’appuyer sur des règles stables.", "web-captures/codex-agents-md-official.png", tip="Un bon AGENTS.md est utile, court et orienté action."),
                _codex_item("Donner les règles du projet", "Les règles doivent être concrètes : fond blanc, accents bleu/violet, pas de dépendance sans demande, vérifier mobile, résumer les fichiers modifiés. Des règles vagues aident peu.", "Transformez une préférence en règle vérifiable.", "Codex sait quoi respecter pendant les modifications.", "agents-md.png", tip="Une règle vérifiable commence souvent par `faire`, `éviter` ou `vérifier`."),
                _codex_item("Demander une petite modification", "La première modification doit être petite. C’est comme un test : Codex comprend-il le dossier, respecte-t-il AGENTS.md et produit-il un diff lisible ?", "Demandez une correction limitée : texte, bouton, section courte ou bug simple.", "La modification est visible et facile à contrôler.", "business-task.png", tip="Petite action, preuve visible, puis seulement ensuite tâche plus large."),
                _codex_item("Vérifier le rendu", "Un projet web doit être ouvert. Le terminal peut dire que tout va bien, mais le navigateur montre les vrais problèmes : espace, débordement, bouton invisible, texte trop long.", "Ouvrez la page locale ou la preview après modification.", "Le résultat visuel correspond à la demande.", "browser-preview.png", tip="Le rendu réel a toujours le dernier mot."),
                _codex_item("Corriger une erreur", "Quand une erreur apparaît, copiez le texte exact et gardez la correction petite. Codex peut diagnostiquer, mais il faut lui donner le symptôme réel.", "Envoyez : `Voici l’erreur exacte... Explique puis propose une seule correction.`", "La correction cible le problème sans refaire tout le projet.", "debug-flow.png", tip="Une erreur exacte donne une réponse plus fiable qu’une description floue."),
                _codex_item("Demander une revue", "Codex peut servir de reviewer. Il peut relire un diff, chercher les risques, proposer des tests ou signaler une incohérence. La revue ne doit pas recréer tout le travail.", "Demandez : `Relis ce diff et liste seulement les risques réels.`", "La revue produit une liste courte et actionnable.", "review-other-agent.png", tip="Une bonne revue sépare risque réel et préférence personnelle."),
                _codex_item("Préparer une livraison", "Avant de livrer, Codex peut préparer un résumé : fichiers, changements, vérifications, limites. Ce résumé aide à expliquer le travail sans rouvrir toute la session.", "Demandez un résumé de livraison simple.", "La livraison se comprend sans relire tout le projet.", "handoff-summary.png", tip="Le résumé doit parler de preuves, pas seulement d’intention."),
                _codex_item("Garder une trace claire", "Une bonne séance Codex finit avec une trace : commit, résumé, checklist ou note de décision. Sans trace, le travail se perd vite.", "Ajoutez une note finale dans README ou dans votre historique de projet.", "Vous savez ce qui a été fait et ce qui reste à faire.", "git-status.png", tip="Une trace courte aujourd’hui évite une reprise confuse demain."),
            ],
        ),
        (
            "Acte 6 - Plugiciels Codex",
            "Cette partie explique les plugiciels : à quoi ils servent, comment les choisir, et quand les éviter.",
            "Plugiciels",
            "orange",
            [
                _codex_item("C’est quoi un plugiciel", "Un plugiciel connecte Codex à un outil ou une compétence. Il peut aider avec GitHub, Gmail, Notion, Linear, Slack, spreadsheets, présentations ou autres usages selon ce qui est disponible.", "Ouvrez la zone Plugiciels et regardez ce qui est activé.", "Vous savez quels outils Codex peut utiliser dans votre espace.", "codex-plugiciels-screen.png", tip="Un plugiciel activé doit servir un besoin réel."),
                _codex_item("Pourquoi les plugiciels changent l’usage", "Sans plugiciel, Codex travaille surtout avec la demande et le projet. Avec plugiciel, il peut accéder à un outil métier. Cela augmente l’utilité, mais aussi la responsabilité.", "Pour chaque plugiciel, demandez : `quelles données peut-il lire ou modifier ?`", "Vous comprenez le lien entre utilité et accès.", "web-captures/codex-plugins-docs-official.png", tip="Plus un plugiciel est puissant, plus le cadre doit être clair."),
                _codex_item("GitHub", "GitHub est utile pour relire une PR, comprendre une issue, suivre un diff, préparer un résumé ou vérifier une branche. C’est souvent l’un des plugiciels les plus utiles pour un projet code.", "Testez une demande de revue ou de résumé de PR si GitHub est connecté.", "Codex parle du dépôt réel, pas d’un projet imaginé.", "web-captures/codex-plugins-docs-official.png", tip="Sur GitHub, demandez des risques et des fichiers précis."),
                _codex_item("Gmail", "Gmail peut servir pour lire ou rédiger des réponses liées au travail. Ce plugiciel est sensible : il touche à des messages personnels ou professionnels. Il faut donc être très clair sur le périmètre.", "Avant d’utiliser Gmail, définissez le type de mails autorisé et le résultat attendu.", "Codex ne mélange pas une tâche code avec des messages privés.", "codex-plugiciels-screen.png", tip="Un accès mail doit être cadré avant d’être utilisé."),
                _codex_item("Notion", "Notion peut aider à retrouver une note, résumer une spec, transformer une décision en checklist ou préparer un document de projet. C’est utile si votre organisation vit déjà dans Notion.", "Demandez une recherche précise : page, sujet, période ou projet.", "La réponse cite le bon contexte et ne mélange pas les espaces.", "web-captures/codex-plugins-docs-official.png", tip="Une recherche Notion trop large produit souvent une réponse trop large."),
                _codex_item("Linear", "Linear sert au suivi produit : tickets, priorités, bugs, projets. Codex peut aider à transformer une demande en tâche, relire un ticket ou préparer un résumé d’avancement.", "Demandez à Codex de résumer un ticket ou de proposer une checklist de résolution.", "La tâche Linear devient plus claire et actionnable.", "codex-plugiciels-screen.png", tip="Un ticket doit finir avec une prochaine action claire."),
                _codex_item("Slack", "Slack peut aider à retrouver un contexte d’équipe ou préparer une réponse. Comme Gmail, c’est sensible : il faut éviter de mélanger conversations internes et génération sans contrôle.", "Limitez la demande à un canal, une période ou un sujet précis.", "La réponse ne sort pas du contexte demandé.", "web-captures/codex-plugins-docs-official.png", tip="Ne demandez jamais un résumé général de tout un espace sans raison précise."),
                _codex_item("Spreadsheets", "Le plugiciel spreadsheets aide à créer, lire ou structurer des tableaux. Pour un travail business, il peut servir à organiser une liste de bugs, une checklist, un budget ou un suivi de tâches.", "Demandez une table simple : colonnes, lignes attendues, format final.", "Le tableau produit peut être relu et utilisé.", "codex-plugiciels-screen.png", tip="Un tableau utile commence par des colonnes bien nommées."),
                _codex_item("Presentations", "Le plugiciel presentations aide à créer ou structurer un support. Codex peut transformer un résumé technique en plan de slides ou en contenu plus clair.", "Donnez le public, le nombre de slides et le niveau de détail attendu.", "La présentation répond à un objectif clair.", "codex-plugiciels-screen.png", tip="Une bonne slide explique une idée, pas cinq."),
                _codex_item("Activer ou éviter un plugiciel", "Activez un plugiciel quand il aide directement la tâche. Évitez-le quand il ajoute du bruit, touche des données sensibles ou donne à Codex un accès inutile.", "Pour chaque plugiciel, notez : besoin, accès, risque, preuve attendue.", "Le plugiciel utilisé a une vraie raison.", "web-captures/codex-plugins-docs-official.png", tip="Le meilleur plugiciel est parfois celui qu’on laisse désactivé."),
            ],
        ),
        (
            "Acte 7 - Automatisations Codex",
            "Cette partie explique les automatisations : quand elles servent, comment les cadrer et pourquoi il faut les vérifier avant de les laisser tourner.",
            "Automatiser",
            "violet",
            [
                _codex_item("C’est quoi une automatisation", "Une automatisation Codex lance un travail de façon programmée ou récurrente. Elle peut gérer un bilan, une revue, une surveillance ou une tâche répétitive sans tout relancer à la main.", "Repérez l’écran Automatisations et les options de création.", "Vous savez distinguer une demande ponctuelle d’une tâche répétée.", "codex-automatisations-screen.png", tip="Automatiser trop tôt répète parfois une mauvaise méthode."),
                _codex_item("Demande simple ou automatisation", "Une demande simple sert une fois. Une automatisation revient selon un rythme. Si la tâche n’est pas encore claire à la main, elle n’est pas prête à être automatisée.", "Avant d’automatiser, faites la tâche une fois manuellement avec Codex.", "La tâche est stable avant d’être programmée.", "web-captures/codex-app-automations-docs-official.png", tip="D’abord manuel, ensuite automatique."),
                _codex_item("Bilan quotidien", "Un bilan quotidien peut résumer des changements, tickets, messages ou actions du jour. C’est utile si le même point de suivi revient souvent.", "Définissez ce que le bilan doit lire et ce qu’il doit ignorer.", "Le bilan ne raconte pas tout, il met en avant l’utile.", "codex-automatisations-screen.png", tip="Un bon bilan a peu de rubriques et des actions claires."),
                _codex_item("Revue hebdomadaire", "Une revue hebdomadaire aide à prendre du recul : avancement, blocages, décisions et prochaine priorité. Codex peut préparer ce résumé si les sources sont bien cadrées.", "Donnez les sources autorisées et le format final.", "La revue aide à décider la suite.", "web-captures/codex-automations-official.png", tip="Une revue doit finir avec une prochaine priorité."),
                _codex_item("Suivi de projet", "Le suivi de projet peut surveiller une branche, des tickets, une PR ou une liste de tâches. Codex peut signaler ce qui demande attention.", "Choisissez un seul projet et une fréquence raisonnable.", "Le suivi ne génère pas trop de bruit.", "codex-automatisations-screen.png", tip="Une automatisation bruyante sera vite ignorée."),
                _codex_item("Créer par clavardage", "Créer par clavardage signifie décrire l’automatisation en langage simple. Mais la phrase doit rester précise : objectif, fréquence, sources, sortie et limites.", "Écrivez : `Chaque lundi, résume les tickets ouverts de ce projet et propose 3 priorités.`", "La demande contient fréquence, source et format.", "codex-automatisations-screen.png", tip="Un bon prompt d’automatisation ressemble à une mini-procédure."),
                _codex_item("Voir les modèles", "Les modèles servent de point de départ. Ils aident à comprendre les usages courants : bilan, revue, suivi. Ils ne doivent pas être copiés sans adaptation.", "Ouvrez un modèle et remplacez les éléments vagues par votre contexte.", "Le modèle devient adapté à votre travail.", "codex-automatisations-screen.png", tip="Un modèle est une base, pas une solution finale."),
                _codex_item("Cadrer l’automatisation", "Le cadrage doit préciser ce que Codex peut lire, ce qu’il peut faire, ce qu’il ne doit pas toucher et comment vous serez averti du résultat. Sans ça, l’automatisation peut dériver.", "Ajoutez une section `limites` dans la consigne.", "Les limites sont visibles avant activation.", "web-captures/codex-app-automations-docs-official.png", tip="Une automatisation sans limite finit souvent par produire trop ou mal."),
                _codex_item("Vérifier avant de laisser tourner", "Avant d’activer une automatisation durable, lancez un test. L’objectif est de voir si le résultat est utile, court, fiable et sans accès inutile.", "Faites une exécution de test et relisez le résultat comme une livraison.", "Le premier résultat donne confiance ou montre quoi corriger.", "web-captures/codex-automations-official.png", tip="Ne laissez pas tourner ce que vous n’avez pas relu au moins une fois."),
                _codex_item("Les erreurs à éviter", "Les erreurs classiques : source trop large, fréquence trop élevée, sortie trop longue, action non validée, accès sensible inutile. Une automatisation doit alléger le travail, pas créer une deuxième surveillance.", "Avant activation, vérifiez source, fréquence, sortie, accès et validation.", "L’automatisation a un périmètre raisonnable.", "risk-table.png", tip="Automatiser, c’est répéter une bonne règle. Pas compenser une règle floue."),
            ],
        ),
        (
            "Acte 8 - Codex vs Claude Code",
            "Cette dernière partie compare sans répéter : app Codex, terminal Codex, Claude Code, usage combiné et routine finale.",
            "Comparer",
            "green",
            [
                _codex_item("Différence simple", "Codex est l’agent OpenAI avec app, terminal, cloud, plugiciels et automatisations. Claude Code est l’agent Anthropic déjà vu, très orienté terminal et travail dans un dossier. La différence se voit surtout dans la surface et les habitudes.", "Écrivez une phrase de comparaison avec vos mots.", "La différence est claire sans refaire l’installation Claude Code.", "decision-matrix.png", tip="Comparer n’est pas choisir pour toujours. C’est choisir pour la tâche."),
                _codex_item("Codex app : quand l’utiliser", "Utilisez l’app Codex quand vous voulez piloter un projet, voir des conversations, gérer des plugiciels, lancer une automatisation, suivre plusieurs tâches ou travailler avec une interface plus visuelle.", "Classez votre tâche : pilotage, plugiciel, automatisation, suivi ou projet.", "L’app est choisie pour une raison précise.", "web-captures/codex-app-docs-official.png", tip="L’app est pratique quand il faut superviser plutôt que seulement taper une commande."),
                _codex_item("Codex terminal : quand l’utiliser", "Utilisez Codex CLI quand vous êtes déjà dans un dossier local et que vous voulez lire, modifier, tester ou résumer sans quitter le terminal.", "Si le dossier est ouvert dans le terminal, lancez `codex` depuis ce dossier.", "Le terminal pointe vers le bon projet.", "web-captures/codex-cli-docs-official.png", tip="Terminal = contexte local immédiat."),
                _codex_item("Claude Code : quand le garder", "Gardez Claude Code quand vous voulez continuer un flux Anthropic déjà installé, travailler avec ses conventions, ses commandes et sa manière de guider les changements. La séance ne le réexplique pas : elle le place en comparaison.", "Pour chaque tâche, demandez : `est-ce que je veux l’écosystème Codex ou continuer avec Claude Code ?`", "Le choix vient de la tâche, pas de l’habitude seule.", "claude-plan.png", tip="Un outil déjà maîtrisé reste utile, mais il ne doit pas empêcher de comprendre Codex."),
                _codex_item("Codex pour relire", "Codex peut très bien servir de reviewer : relire un diff, lister les risques, proposer des tests ou vérifier une logique. C’est utile même si la modification a été faite ailleurs.", "Demandez : `Relis ce diff et signale seulement les risques réels.`", "La revue produit des points courts et vérifiables.", "review-other-agent.png", tip="Une revue utile ne réécrit pas tout."),
                _codex_item("Codex pour organiser", "Codex peut aussi organiser un travail : transformer une demande floue en plan, séparer les étapes, écrire une checklist ou préparer une automatisation. C’est souvent plus utile que de lui demander directement d’agir.", "Demandez un plan avant action sur une tâche inconnue.", "Le plan rend le travail plus simple à lancer.", "codex-plan.png", tip="Organiser avant d’agir évite les gros retours arrière."),
                _codex_item("Claude Code pour agir dans le terminal", "Claude Code reste très naturel dans un terminal local si vous l’avez déjà vu et installé. La vraie question n’est pas de le remplacer, mais de savoir quand Codex apporte une surface ou un accès plus utile.", "Comparez sur une petite tâche : même dossier, même objectif, même vérification.", "Vous voyez la différence dans la pratique, pas dans une opinion.", "parallel-workflow.png", tip="La comparaison doit rester petite et mesurable."),
                _codex_item("Utiliser les deux sans doublon", "Les deux outils peuvent travailler ensemble si les rôles sont séparés : l’un produit, l’autre relit ; l’un organise, l’autre applique ; l’un travaille dans l’app, l’autre dans le terminal.", "Définissez les rôles avant de lancer les deux.", "Les deux outils ne modifient pas la même chose en même temps.", "parallel-workflow.png", tip="Deux agents sans rôle clair ajoutent du bruit."),
                _codex_item("Tableau de décision simple", "La décision finale doit rester simple : app Codex pour piloter, terminal Codex pour agir localement, plugiciels pour connecter des outils, automatisations pour répéter, Claude Code pour continuer le flux terminal Anthropic déjà connu.", "Créez un tableau `situation -> outil -> preuve attendue`.", "Vous savez choisir sans hésiter pendant une vraie tâche.", "decision-matrix.png", tip="La preuve attendue est plus importante que le nom de l’outil."),
                _codex_item("Routine finale à garder", "La routine quotidienne tient en peu d’étapes : choisir la surface, écrire une demande précise, demander un plan si besoin, lire le diff, vérifier le résultat, résumer. Cette routine rend Codex utile au lieu de le rendre confus.", "Gardez cette routine dans vos notes de séance.", "Vous pouvez utiliser Codex demain sur une vraie tâche sans repartir de zéro.", "daily-routine.png", tip="Codex devient utile quand il entre dans une méthode simple."),
            ],
        ),
    ]


CHAPTERS = _build_codex_chapters()


def e(text: str) -> str:
    return escape(text, quote=True)


def clean_public_copy(html: str) -> str:
    replacements = {
        "élèves": "vous",
        "élève": "vous",
        "Eleves": "Vous",
        "Élèves": "Vous",
        "tu": "vous",
        "Tu": "Vous",
        "toi": "vous",
        "Toi": "Vous",
        "ton": "votre",
        "Ton": "Votre",
        "ta": "votre",
        "Ta": "Votre",
        "tes": "vos",
        "Tes": "Vos",
    }
    for old, new in replacements.items():
        html = re.sub(rf"\b{re.escape(old)}\b", new, html)
    return html


def all_sections() -> list[dict[str, str]]:
    sections = []
    for chapter, summary, tag, color, items in CHAPTERS:
        for title, story, action, check, codex, claude, tip, image in items:
            sections.append(
                {
                    "chapter": chapter,
                    "summary": summary,
                    "tag": tag,
                    "color": color,
                    "title": title,
                    "story": story,
                    "action": action,
                    "check": check,
                    "codex": codex,
                    "claude": claude,
                    "tip": tip,
                    "image": image,
                }
            )
    return sections


def badge(text: str, color: str) -> str:
    colors = {
        "blue": "bg-blue-600 text-white",
        "violet": "bg-violet-600 text-white",
        "cyan": "bg-cyan-100 text-slate-950",
        "green": "bg-emerald-100 text-slate-950",
        "orange": "bg-orange-100 text-slate-950",
    }
    return f'<span class="{colors[color]} border-2 border-slate-950 px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] shadow-neo-sm">{e(text)}</span>'


def code_block(lines: list[str], label: str = "Bloc pratique") -> str:
    return f"""
      <div class="code-panel max-w-full overflow-hidden border-2 border-slate-950 bg-slate-950 text-white shadow-neo">
        <div class="flex items-center justify-between border-b-2 border-white/20 bg-slate-900 px-4 py-2">
          <span class="font-mono text-[11px] font-black uppercase tracking-[.16em] text-cyan-200">{e(label)}</span>
          <button type="button" class="copy-btn border-2 border-white bg-white px-3 py-1 text-xs font-black text-slate-950 transition hover:-translate-y-0.5">Copier</button>
        </div>
        <pre class="max-w-full whitespace-pre-wrap break-words p-5 text-sm leading-7"><code>{e(chr(10).join(lines))}</code></pre>
      </div>
    """


def image_card(item: dict[str, str], index: int) -> str:
    if item["image"].startswith("web-captures/"):
        src = f"img/{item['image']}"
    else:
        src = f"img/interface-s2/{item['image']}"
    return f"""
      <figure class="group min-w-0 overflow-hidden border-2 border-slate-950 bg-white shadow-neo">
        <img class="aspect-[16/10] w-full bg-white object-contain transition duration-300 group-hover:scale-[1.015]" src="{src}" alt="{e(item['title'])}" loading="lazy">
        <figcaption class="border-t-2 border-slate-950 bg-white px-4 py-3 text-sm font-semibold leading-6 text-slate-700">
          Visuel {index:02d} · {e(item['tag'])} · {e(item['title'])}
        </figcaption>
      </figure>
    """


def mini_table(rows: list[tuple[str, str]]) -> str:
    body = ""
    for label, value in rows:
        body += f"""
          <tr>
            <th class="w-[210px] border-2 border-slate-950 bg-blue-50 px-4 py-3 text-left font-mono text-[11px] font-black uppercase tracking-[.14em] text-slate-700">{e(label)}</th>
            <td class="border-2 border-slate-950 bg-white px-4 py-3 text-sm leading-7 text-slate-700">{e(value)}</td>
          </tr>
        """
    return f'<div class="max-w-full overflow-x-auto border-2 border-slate-950 bg-white shadow-neo"><table class="w-full min-w-[720px] border-collapse">{body}</table></div>'


def section_header(item: dict[str, str], n: int) -> str:
    return f"""
      <div class="mb-6 flex flex-wrap items-center gap-3">
        {badge(f"{n:02d}", item["color"])}
        {badge(item["tag"], item["color"])}
        <span class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] text-slate-700 shadow-neo-sm">{e(item["chapter"])}</span>
      </div>
    """


def detail_grid(item: dict[str, str]) -> str:
    cards = [
        ("Ce qui se passe", item["story"], "bg-white"),
        ("Action terrain", item["action"], "bg-violet-50"),
        ("Preuve attendue", item["check"], "bg-blue-50"),
        ("Tip simple", item["tip"], "bg-cyan-50"),
    ]
    html = ""
    for title, body, tone in cards:
        html += f"""
          <article class="{tone} min-w-0 border-2 border-slate-950 p-5 transition duration-200 hover:-translate-y-1 hover:shadow-neo-sm">
            <h3 class="text-lg font-black leading-6 text-slate-950">{e(title)}</h3>
            <p class="mt-3 text-[15px] leading-7 text-slate-700">{e(body)}</p>
          </article>
        """
    return f'<div class="mt-7 grid gap-4 md:grid-cols-2">{html}</div>'


def compare_block(item: dict[str, str]) -> str:
    return f"""
      <div class="grid gap-4 md:grid-cols-2">
        <article class="border-2 border-slate-950 bg-blue-50 p-5 shadow-neo-sm">
          <p class="font-mono text-[11px] font-black uppercase tracking-[.16em] text-blue-700">Côté Codex</p>
          <p class="mt-3 text-[15px] leading-7 text-slate-700">{e(item['codex'])}</p>
        </article>
        <article class="border-2 border-slate-950 bg-violet-50 p-5 shadow-neo-sm">
          <p class="font-mono text-[11px] font-black uppercase tracking-[.16em] text-violet-700">Côté Claude Code</p>
          <p class="mt-3 text-[15px] leading-7 text-slate-700">{e(item['claude'])}</p>
        </article>
      </div>
    """


def layout_a(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-8 lg:grid-cols-[1.05fr_.95fr] lg:items-start">
        <article class="min-w-0 border-2 border-slate-950 bg-white p-6 shadow-neo sm:p-8">
          <h2 class="font-display text-3xl font-black leading-tight text-slate-950 sm:text-5xl">{e(item['title'])}</h2>
          <p class="mt-5 text-lg leading-8 text-slate-700">{e(item['summary'])}</p>
          {detail_grid(item)}
        </article>
        {image_card(item, n)}
      </div>
    </section>
    """


def layout_b(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-8 lg:grid-cols-[.9fr_1.1fr]">
        {image_card(item, n)}
        <article class="min-w-0 border-2 border-slate-950 bg-white p-6 shadow-neo sm:p-8">
          <h2 class="font-display text-3xl font-black leading-tight text-slate-950 sm:text-5xl">{e(item['title'])}</h2>
          <p class="mt-5 text-lg leading-8 text-slate-700">{e(item['story'])}</p>
          <div class="mt-6 border-l-4 border-blue-600 bg-blue-50 p-5">
            <p class="font-black text-slate-950">Le geste à faire</p>
            <p class="mt-2 leading-7 text-slate-700">{e(item['action'])}</p>
          </div>
          <div class="mt-6">{compare_block(item)}</div>
          <p class="mt-6 border-2 border-slate-950 bg-cyan-50 p-5 font-semibold leading-7 text-slate-800">{e(item['check'])}</p>
        </article>
      </div>
    </section>
    """


def layout_c(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="overflow-hidden border-2 border-slate-950 bg-white shadow-neo">
        <div class="border-b-2 border-slate-950 bg-violet-600 px-5 py-3 font-mono text-xs font-black uppercase tracking-[.16em] text-white">Bloc pratique à copier</div>
        <div class="grid gap-0 lg:grid-cols-[minmax(0,.95fr)_minmax(0,1.05fr)]">
          <article class="min-w-0 p-6 sm:p-8">
            <h2 class="font-display text-3xl font-black leading-tight text-slate-950 sm:text-5xl">{e(item['title'])}</h2>
            <p class="mt-5 text-lg leading-8 text-slate-700">{e(item['story'])}</p>
            <div class="mt-6">{compare_block(item)}</div>
          </article>
          <div class="min-w-0 border-t-2 border-slate-950 p-6 sm:p-8 lg:border-l-2 lg:border-t-0">
            {code_block([item['action'], '', 'Vérification :', item['check'], '', 'Tip :', item['tip']])}
          </div>
        </div>
        <div class="border-t-2 border-slate-950 p-6 sm:p-8">
          {image_card(item, n)}
        </div>
      </div>
    </section>
    """


def layout_d(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-8 lg:grid-cols-[.75fr_1.25fr] lg:items-start">
        <div class="border-2 border-slate-950 bg-blue-600 p-6 text-white shadow-neo sm:p-8">
          <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-blue-100">{e(item['tag'])}</p>
          <h2 class="mt-4 font-display text-3xl font-black leading-tight sm:text-5xl">{e(item['title'])}</h2>
          <p class="mt-5 text-lg leading-8 text-blue-50">{e(item['story'])}</p>
        </div>
        <div class="min-w-0 space-y-6">
          {mini_table([("Action", item['action']), ("Preuve", item['check']), ("Codex", item['codex']), ("Claude Code", item['claude']), ("Tip", item['tip'])])}
          {image_card(item, n)}
        </div>
      </div>
    </section>
    """


def layout_e(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-8 lg:grid-cols-[1fr_1fr]">
        <article class="min-w-0 border-2 border-slate-950 bg-white p-6 shadow-neo sm:p-8">
          <h2 class="font-display text-3xl font-black leading-tight text-slate-950 sm:text-5xl">{e(item['title'])}</h2>
          <p class="mt-5 text-lg leading-8 text-slate-700">{e(item['story'])}</p>
          <div class="mt-6 grid gap-4">
            <div class="border-2 border-slate-950 bg-violet-50 p-5">
              <p class="font-black">Action terrain</p>
              <p class="mt-2 leading-7 text-slate-700">{e(item['action'])}</p>
            </div>
            <div class="border-2 border-slate-950 bg-cyan-50 p-5">
              <p class="font-black">À vérifier</p>
              <p class="mt-2 leading-7 text-slate-700">{e(item['check'])}</p>
            </div>
          </div>
        </article>
        <div class="min-w-0 space-y-6">
          {image_card(item, n)}
          {compare_block(item)}
          <p class="border-2 border-slate-950 bg-white p-5 font-semibold leading-7 text-slate-800 shadow-neo-sm">{e(item['tip'])}</p>
        </div>
      </div>
    </section>
    """


def layout_f(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="border-2 border-slate-950 bg-white shadow-neo">
        <div class="grid lg:grid-cols-[minmax(0,1fr)_minmax(0,1fr)]">
          <div class="min-w-0 p-6 sm:p-8">
            <h2 class="font-display text-3xl font-black leading-tight text-slate-950 sm:text-5xl">{e(item['title'])}</h2>
            <p class="mt-5 text-lg leading-8 text-slate-700">{e(item['story'])}</p>
            <div class="mt-6">{code_block([item['action'], item['check']], 'Action + preuve')}</div>
          </div>
          <div class="min-w-0 border-t-2 border-slate-950 p-6 sm:p-8 lg:border-l-2 lg:border-t-0">
            {image_card(item, n)}
          </div>
        </div>
        <div class="grid gap-4 border-t-2 border-slate-950 p-6 sm:grid-cols-3 sm:p-8">
          <article class="border-2 border-slate-950 bg-blue-50 p-5"><p class="font-black">Codex</p><p class="mt-2 text-sm leading-7 text-slate-700">{e(item['codex'])}</p></article>
          <article class="border-2 border-slate-950 bg-violet-50 p-5"><p class="font-black">Claude Code</p><p class="mt-2 text-sm leading-7 text-slate-700">{e(item['claude'])}</p></article>
          <article class="border-2 border-slate-950 bg-cyan-50 p-5"><p class="font-black">Tip terrain</p><p class="mt-2 text-sm leading-7 text-slate-700">{e(item['tip'])}</p></article>
        </div>
      </div>
    </section>
    """


LAYOUTS = [layout_a, layout_b, layout_c, layout_d, layout_e, layout_f]


def render_section(item: dict[str, str], n: int) -> str:
    return LAYOUTS[(n - 1) % len(LAYOUTS)](item, n)


def nav() -> str:
    links = [
        ("Comprendre", "#section-01"),
        ("Accès", "#section-11"),
        ("Cadre", "#section-21"),
        ("Codex", "#section-31"),
        ("Claude Code", "#section-41"),
        ("Comparer", "#section-51"),
        ("Décider", "#section-61"),
        ("Livrer", "#section-71"),
    ]
    return "".join(
        f'<a class="nav-chip border-2 border-slate-950 bg-white px-3 py-2 text-xs font-black uppercase tracking-[.12em] text-slate-950 no-underline shadow-neo-sm transition hover:-translate-y-0.5 hover:bg-blue-600 hover:text-white" href="{href}">{e(label)}</a>'
        for label, href in links
    )


def intro(sections: list[dict[str, str]]) -> str:
    plan_cards = ""
    for i, (chapter, summary, tag, color, _items) in enumerate(CHAPTERS, 1):
        plan_cards += f"""
          <a href="#section-{(i - 1) * 10 + 1:02d}" class="group border-2 border-slate-950 bg-white p-5 no-underline shadow-neo-sm transition hover:-translate-y-1 hover:bg-{ 'blue' if color == 'blue' else 'violet' if color == 'violet' else 'cyan' if color == 'cyan' else 'emerald' if color == 'green' else 'orange' }-50">
            <p class="font-mono text-[11px] font-black uppercase tracking-[.16em] text-slate-500">Acte {i:02d} · {e(tag)}</p>
            <h3 class="mt-3 text-xl font-black leading-7 text-slate-950">{e(chapter.replace('Acte ' + str(i) + ' - ', ''))}</h3>
            <p class="mt-3 text-sm leading-6 text-slate-700">{e(summary)}</p>
          </a>
        """
    return f"""
    <header class="relative overflow-hidden bg-white">
      <div class="absolute inset-0 pointer-events-none bg-[linear-gradient(#dbeafe_1px,transparent_1px),linear-gradient(90deg,#ede9fe_1px,transparent_1px)] bg-[size:32px_32px] opacity-55"></div>
      <div class="relative mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <nav class="flex flex-wrap items-center justify-between gap-4">
          <a href="#top" class="flex items-center gap-3 no-underline">
            <img class="h-12 w-12 border-2 border-slate-950 object-cover shadow-neo-sm" src="logo-denem.jpeg" alt="Logo Denem Academy">
            <span class="border-2 border-slate-950 bg-white px-3 py-2 font-mono text-xs font-black uppercase tracking-[.16em] text-slate-950 shadow-neo-sm">Denem Academy · Séance 2</span>
          </a>
          <div class="flex flex-wrap gap-2">{nav()}</div>
        </nav>
        <div class="grid gap-10 py-14 lg:grid-cols-[1.05fr_.95fr] lg:items-center">
          <div>
            <div class="mb-5 inline-flex border-2 border-slate-950 bg-violet-600 px-4 py-2 font-mono text-xs font-black uppercase tracking-[.18em] text-white shadow-neo-sm">Comparaison terrain</div>
            <h1 class="font-display text-5xl font-black leading-[.95] text-slate-950 sm:text-7xl lg:text-8xl">Codex ou Claude Code ?</h1>
            <p class="mt-6 max-w-3xl text-xl leading-9 text-slate-700">Dans cette séance, on va voir comment bien utiliser Codex. On va comprendre à quoi il sert, comment l’installer, comment lui demander un travail propre, puis quelle est la vraie différence avec Claude Code. Le but est simple : savoir quel outil lancer quand il faut créer, corriger, relire ou livrer un projet.</p>
            <div class="mt-8 grid gap-4 sm:grid-cols-3">
              <div class="border-2 border-slate-950 bg-blue-600 p-4 text-white shadow-neo-sm"><p class="font-mono text-xs font-black uppercase tracking-[.16em]">80</p><p class="mt-2 font-black">sections guidées</p></div>
              <div class="border-2 border-slate-950 bg-white p-4 shadow-neo-sm"><p class="font-mono text-xs font-black uppercase tracking-[.16em] text-violet-700">33+</p><p class="mt-2 font-black">visuels d’interface</p></div>
              <div class="border-2 border-slate-950 bg-cyan-50 p-4 shadow-neo-sm"><p class="font-mono text-xs font-black uppercase tracking-[.16em] text-slate-600">1</p><p class="mt-2 font-black">exemple qui se suit</p></div>
            </div>
          </div>
          <figure class="overflow-hidden border-2 border-slate-950 bg-white shadow-neo">
            <img class="aspect-[16/10] w-full object-contain" src="img/interface-s2/hero-codex-claude.png" alt="Comparaison Codex et Claude Code" loading="eager">
            <figcaption class="border-t-2 border-slate-950 bg-white px-4 py-3 text-sm font-semibold text-slate-700">Même projet, même brief, même contrôle.</figcaption>
          </figure>
        </div>
      </div>
    </header>

    <section class="mx-auto max-w-7xl bg-white px-4 py-12 sm:px-6 lg:px-8">
      <div class="grid gap-8 lg:grid-cols-[.9fr_1.1fr]">
        <div class="border-2 border-slate-950 bg-white p-6 shadow-neo sm:p-8">
          <h2 class="font-display text-4xl font-black text-slate-950 sm:text-6xl">Le parcours de la séance</h2>
          <p class="mt-5 text-lg leading-8 text-slate-700">On commence par les bases : c’est quoi Codex, ce qu’il peut faire dans un dossier, et pourquoi ce n’est pas exactement la même chose que Claude Code. Ensuite, on utilise le même exemple pour comparer les deux outils sans théorie inutile.</p>
          {code_block(['Brief maître :', 'Dans la page du Comptoir Bleu, ajoute une formule midi.', 'Garde fond blanc, accents bleu/violet, bouton Réserver visible.', 'Vérifie mobile et résume les fichiers modifiés.'], 'Brief commun')}
        </div>
        <div class="grid gap-4 md:grid-cols-2">{plan_cards}</div>
      </div>
    </section>
    """


def sources_block() -> str:
    rows = [
        ("OpenAI Codex Quickstart", DOCS["codex_quickstart"], "Surfaces Codex, installation app/CLI/cloud et premiers messages."),
        ("OpenAI Codex Pricing", DOCS["codex_pricing"], "Plans Codex, prix et limites à vérifier au moment de l’achat."),
        ("OpenAI AGENTS.md", DOCS["codex_agents"], "Instructions projet lues par Codex."),
        ("Codex CLI Features", DOCS["codex_features"], "Mode interactif, diff, approbations, reprise de session."),
        ("Claude Code Quickstart", DOCS["claude_quickstart"], "Première connexion, commandes et premiers changements."),
        ("Claude Pro / Max", DOCS["claude_pro_max"], "Connexion de Claude Code au plan et usage partagé."),
        ("Claude Plans", DOCS["claude_plan"], "Prix Free, Pro, Max 5x, Max 20x à vérifier officiellement."),
        ("Claude limites", DOCS["claude_limits"], "Modèles, usage, `/clear`, `/compact`, contexte et coûts."),
        ("Claude extensions", DOCS["claude_extend"], "`CLAUDE.md`, skills, MCP, hooks et contexte projet."),
    ]
    body = ""
    for label, url, note in rows:
        body += f"""
          <tr>
            <td class="border-2 border-slate-950 bg-white px-4 py-3 font-black text-slate-950">{e(label)}</td>
            <td class="border-2 border-slate-950 bg-white px-4 py-3"><a class="font-semibold text-blue-700 underline decoration-2 underline-offset-4" href="{e(url)}" target="_blank" rel="noreferrer">{e(url)}</a></td>
            <td class="border-2 border-slate-950 bg-white px-4 py-3 text-sm leading-6 text-slate-700">{e(note)}</td>
          </tr>
        """
    return f"""
    <section id="sources" class="mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      <div class="border-2 border-slate-950 bg-white p-6 shadow-neo sm:p-8">
        <div class="mb-5 inline-flex border-2 border-slate-950 bg-blue-600 px-4 py-2 font-mono text-xs font-black uppercase tracking-[.18em] text-white shadow-neo-sm">Sources vérifiées · 3 juin 2026</div>
        <h2 class="font-display text-4xl font-black text-slate-950 sm:text-6xl">Liens officiels à garder</h2>
        <p class="mt-5 max-w-4xl text-lg leading-8 text-slate-700">Les accès, les prix et les commandes changent. Les liens ci-dessous sont volontairement visibles pour que vous puissiez vérifier avant une installation, un achat ou une formation répétée.</p>
        <div class="mt-7 max-w-full overflow-x-auto">
          <table class="w-full min-w-[920px] border-collapse">
            <thead>
              <tr>
                <th class="border-2 border-slate-950 bg-blue-100 px-4 py-3 text-left text-xs uppercase tracking-[.14em]">Source</th>
                <th class="border-2 border-slate-950 bg-violet-100 px-4 py-3 text-left text-xs uppercase tracking-[.14em]">Lien</th>
                <th class="border-2 border-slate-950 bg-cyan-100 px-4 py-3 text-left text-xs uppercase tracking-[.14em]">À quoi ça sert</th>
              </tr>
            </thead>
            <tbody>{body}</tbody>
          </table>
        </div>
      </div>
    </section>
    """


def custom_style() -> str:
    return """
    <style>
      :root { color-scheme: light; }
      html { scroll-behavior: smooth; }
      body { background: #ffffff; color: #0f172a; }
      .progress-bar { transform-origin: left; transform: scaleX(0); }
      .reveal { opacity: 0; transform: translateY(24px); transition: opacity .55s ease, transform .55s ease; }
      .reveal.is-visible { opacity: 1; transform: translateY(0); }
      .section-block { scroll-margin-top: 90px; }
      .nav-chip.is-active { background: #2563eb; color: #fff; transform: translateY(-2px); }
      .copy-btn.is-copied { background: #cffafe; color: #0f172a; }
      .focus-mode .section-block:not(.is-focused) { opacity: .42; }
      .focus-mode .section-block.is-focused { outline: 4px solid #7c3aed; outline-offset: 8px; }
      .spark { position: fixed; width: 8px; height: 8px; border: 2px solid #0f172a; background: #7c3aed; pointer-events: none; z-index: 60; animation: spark .55s ease forwards; }
      @keyframes spark { to { transform: translate(var(--dx), var(--dy)) rotate(180deg); opacity: 0; } }
      @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }
        .reveal { opacity: 1; transform: none; }
      }
    </style>
    """


def script() -> str:
    return """
    <script>
      const progress = document.querySelector('.progress-bar');
      const chips = [...document.querySelectorAll('.nav-chip')];
      const sections = [...document.querySelectorAll('.section-block')];

      function setProgress() {
        const max = document.documentElement.scrollHeight - window.innerHeight;
        const value = max > 0 ? window.scrollY / max : 0;
        progress.style.transform = `scaleX(${value})`;
      }

      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            sections.forEach((section) => section.classList.toggle('is-focused', section === entry.target));
            const id = '#' + entry.target.id;
            chips.forEach((chip) => chip.classList.toggle('is-active', chip.getAttribute('href') === id));
          }
        });
      }, { rootMargin: '-25% 0px -55% 0px', threshold: 0.01 });
      sections.forEach((section) => observer.observe(section));
      window.addEventListener('scroll', setProgress, { passive: true });
      setProgress();

      document.querySelectorAll('.copy-btn').forEach((button) => {
        button.addEventListener('click', async () => {
          const code = button.closest('.code-panel')?.querySelector('code')?.innerText || '';
          await navigator.clipboard.writeText(code);
          button.textContent = 'Copié';
          button.classList.add('is-copied');
          setTimeout(() => { button.textContent = 'Copier'; button.classList.remove('is-copied'); }, 1200);
        });
      });

      document.querySelector('img[alt="Logo Denem Academy"]')?.addEventListener('dblclick', () => {
        document.body.classList.toggle('focus-mode');
      });

      document.addEventListener('click', (event) => {
        if (!event.altKey) return;
        for (let i = 0; i < 8; i++) {
          const spark = document.createElement('span');
          spark.className = 'spark';
          spark.style.left = event.clientX + 'px';
          spark.style.top = event.clientY + 'px';
          spark.style.setProperty('--dx', `${Math.cos(i) * 70}px`);
          spark.style.setProperty('--dy', `${Math.sin(i) * 70}px`);
          document.body.appendChild(spark);
          setTimeout(() => spark.remove(), 620);
        }
      });
    </script>
    """


def render() -> str:
    sections = all_sections()
    section_html = "\n".join(render_section(item, index) for index, item in enumerate(sections, 1))
    html = f"""<!doctype html>
<html lang="fr" id="top">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Denem Academy · Séance 2 · Codex vs Claude Code</title>
    <meta name="description" content="Support technique séance 2 : comparaison Codex et Claude Code avec un parcours concret autour du Comptoir Bleu.">
    <link rel="icon" href="logo-denem.jpeg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&family=Space+Grotesk:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/tailwind-s2.css">
    {custom_style()}
  </head>
  <body class="font-sans antialiased">
    <div class="fixed left-0 right-0 top-0 z-50 h-2 border-b-2 border-slate-950 bg-white">
      <div class="progress-bar h-full bg-violet-600"></div>
    </div>
    {intro(sections)}
    <main>
      {section_html}
      {sources_block()}
    </main>
    <footer class="border-t-2 border-slate-950 bg-white px-4 py-10 sm:px-6 lg:px-8">
      <div class="mx-auto flex max-w-7xl flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div class="flex items-center gap-3">
          <img class="h-10 w-10 border-2 border-slate-950 object-cover shadow-neo-sm" src="logo-denem.jpeg" alt="Logo Denem Academy">
          <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-slate-700">Denem Academy · Séance 2 · Codex vs Claude Code</p>
        </div>
        <a class="border-2 border-slate-950 bg-white px-4 py-2 text-sm font-black text-slate-950 no-underline shadow-neo-sm transition hover:-translate-y-0.5 hover:bg-blue-600 hover:text-white" href="#top">Retour en haut</a>
      </div>
    </footer>
    {script()}
  </body>
</html>
"""
    return clean_public_copy(html)


def main() -> None:
    html = render()
    if len(all_sections()) != 80:
        raise SystemExit(f"Expected 80 sections, got {len(all_sections())}")
    OUT.write_text(html, encoding="utf-8")
    INDEX_OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.name} and index.html with {len(all_sections())} sections")


if __name__ == "__main__":
    main()
