from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "img" / "interface-s2"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#0f172a"
BLUE = "#2563eb"
VIOLET = "#7c3aed"
CYAN = "#cffafe"
GREEN = "#dcfce7"
YELLOW = "#fef3c7"
ROSE = "#ffe4e6"
WHITE = "#ffffff"
SOFT = "#f8fafc"
TERMINAL = "#090d1f"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Courier New Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Courier New.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


F_HERO = font(54, True)
F_TITLE = font(38, True)
F_BODY = font(25)
F_BODY_BOLD = font(25, True)
F_MONO = font(22)
F_MONO_BOLD = font(22, True)
F_SMALL = font(18)
F_SMALL_BOLD = font(18, True)


def shadow(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: str, outline: str = INK, size: int = 10) -> None:
    x1, y1, x2, y2 = xy
    draw.rectangle((x1 + size, y1 + size, x2 + size, y2 + size), fill=INK)
    draw.rectangle(xy, fill=fill, outline=outline, width=3)


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, fnt: ImageFont.ImageFont, fill: str = INK) -> None:
    draw.text(xy, value, font=fnt, fill=fill)


def wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    value: str,
    width: int,
    fnt: ImageFont.ImageFont,
    fill: str = INK,
    gap: int = 9,
) -> int:
    x, y = xy
    avg = max(9, int(getattr(fnt, "size", 20) * 0.52))
    chars = max(18, width // avg)
    for line in wrap(value, chars):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += getattr(fnt, "size", 20) + gap
    return y


def header(draw: ImageDraw.ImageDraw, title: str, subtitle: str, badge: str) -> None:
    shadow(draw, (54, 50, 310, 104), BLUE, size=7)
    text(draw, (76, 67), badge.upper(), F_SMALL_BOLD, WHITE)
    text(draw, (54, 130), title, F_HERO, INK)
    wrapped(draw, (58, 202), subtitle, 820, F_BODY, "#334155", 10)


def terminal(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, rows: list[tuple[str, str]]) -> None:
    x1, y1, x2, y2 = xy
    shadow(draw, xy, TERMINAL, size=12)
    draw.rectangle((x1, y1, x2, y1 + 58), fill="#111827", outline=INK, width=0)
    for i, color in enumerate(["#fb7185", "#facc15", "#34d399"]):
        draw.ellipse((x1 + 24 + i * 30, y1 + 20, x1 + 42 + i * 30, y1 + 38), fill=color)
    text(draw, (x1 + 128, y1 + 17), title, F_SMALL_BOLD, "#f8fafc")
    y = y1 + 90
    for prompt, body in rows:
        color = "#67e8f9" if prompt in {"$", "codex", "claude"} else "#c4b5fd"
        text(draw, (x1 + 30, y), prompt, F_MONO_BOLD, color)
        y = wrapped(draw, (x1 + 118, y), body, x2 - x1 - 155, F_MONO, "#f8fafc", 7)
        y += 8


def browser(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, blocks: list[tuple[str, str, str]]) -> None:
    x1, y1, x2, y2 = xy
    shadow(draw, xy, WHITE, size=12)
    draw.rectangle((x1, y1, x2, y1 + 62), fill=SOFT, outline=INK, width=3)
    for i, color in enumerate(["#fb7185", "#facc15", "#34d399"]):
        draw.ellipse((x1 + 24 + i * 30, y1 + 22, x1 + 42 + i * 30, y1 + 40), fill=color)
    draw.rectangle((x1 + 130, y1 + 16, x2 - 28, y1 + 46), fill=WHITE, outline=INK, width=2)
    text(draw, (x1 + 148, y1 + 21), title, F_SMALL_BOLD, "#334155")
    card_w = (x2 - x1 - 92) // max(1, len(blocks))
    for i, (tone, label, body) in enumerate(blocks):
        bx = x1 + 28 + i * (card_w + 18)
        by = y1 + 102
        shadow(draw, (bx, by, bx + card_w, y2 - 36), tone, size=6)
        text(draw, (bx + 22, by + 24), label, F_BODY_BOLD, INK)
        wrapped(draw, (bx + 22, by + 74), body, card_w - 42, F_SMALL, "#334155", 7)


def comparison(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], rows: list[tuple[str, str, str]]) -> None:
    x1, y1, x2, y2 = xy
    shadow(draw, xy, WHITE, size=12)
    col = (x2 - x1) // 3
    headers = [("Situation", "#dbeafe"), ("Codex", "#ede9fe"), ("Claude Code", "#cffafe")]
    for i, (label, tone) in enumerate(headers):
        draw.rectangle((x1 + i * col, y1, x1 + (i + 1) * col, y1 + 64), fill=tone, outline=INK, width=3)
        text(draw, (x1 + i * col + 24, y1 + 20), label, F_SMALL_BOLD, INK)
    row_h = (y2 - y1 - 64) // len(rows)
    for r, row in enumerate(rows):
        for c, value in enumerate(row):
            cell = (x1 + c * col, y1 + 64 + r * row_h, x1 + (c + 1) * col, y1 + 64 + (r + 1) * row_h)
            draw.rectangle(cell, fill=WHITE, outline=INK, width=2)
            wrapped(draw, (cell[0] + 18, cell[1] + 15), value, col - 36, F_SMALL, "#334155", 5)


def folder(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, files: list[tuple[str, str]]) -> None:
    x1, y1, x2, y2 = xy
    shadow(draw, xy, WHITE, size=12)
    draw.rectangle((x1, y1, x2, y1 + 62), fill="#dbeafe", outline=INK, width=3)
    text(draw, (x1 + 24, y1 + 20), title, F_SMALL_BOLD, INK)
    y = y1 + 100
    for kind, name in files:
        draw.rectangle((x1 + 32, y - 10, x2 - 32, y + 46), fill=SOFT, outline=INK, width=2)
        text(draw, (x1 + 52, y + 4), kind, F_SMALL_BOLD, BLUE if kind == "DIR" else VIOLET)
        text(draw, (x1 + 130, y + 4), name, F_SMALL, INK)
        y += 70


def kanban(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], cols: list[tuple[str, str, list[str]]]) -> None:
    x1, y1, x2, y2 = xy
    shadow(draw, xy, WHITE, size=12)
    col_w = (x2 - x1 - 68) // 3
    for i, (title, tone, items) in enumerate(cols):
        cx = x1 + 24 + i * (col_w + 22)
        draw.rectangle((cx, y1 + 28, cx + col_w, y2 - 28), fill=tone, outline=INK, width=3)
        text(draw, (cx + 20, y1 + 52), title, F_BODY_BOLD, INK)
        y = y1 + 105
        for item in items:
            draw.rectangle((cx + 18, y, cx + col_w - 18, y + 74), fill=WHITE, outline=INK, width=2)
            wrapped(draw, (cx + 32, y + 15), item, col_w - 64, F_SMALL, "#334155", 4)
            y += 92


def pill(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], label: str, fill: str = "#f4f4f5", bold: bool = False) -> None:
    draw.rounded_rectangle(xy, radius=18, fill=fill, outline="#e5e7eb", width=2)
    text(draw, (xy[0] + 18, xy[1] + 10), label, F_SMALL_BOLD if bold else F_SMALL, INK)


def codex_home_ui(draw: ImageDraw.ImageDraw) -> None:
    x1, y1, x2, y2 = 54, 315, 1380, 835
    shadow(draw, (x1, y1, x2, y2), WHITE, size=12)
    draw.rectangle((x1, y1, x1 + 230, y2), fill="#eef2f7", outline=INK, width=3)
    for i, color in enumerate(["#ef4444", "#facc15", "#22c55e"]):
        draw.ellipse((x1 + 18 + i * 28, y1 + 18, x1 + 36 + i * 28, y1 + 36), fill=color)
    side_items = ["Nouveau clavardage", "Recherche", "Modules d'extension", "Automatisations"]
    for i, label in enumerate(side_items):
        text(draw, (x1 + 34, y1 + 72 + i * 44), label, F_SMALL, "#3f3f46")
    text(draw, (x1 + 34, y1 + 265), "Projets", F_SMALL, "#a1a1aa")
    for i, label in enumerate(["06-leads-gratuits...", "Trouver un MCP de ...", "Nettoyer dossier le...", "Préparer base CRM..."]):
        text(draw, (x1 + 34, y1 + 310 + i * 42), label, F_SMALL, "#52525b")
    text(draw, (x1 + 34, y2 - 50), "Paramètres", F_SMALL, "#3f3f46")
    cx = x1 + 230
    text(draw, (cx + 340, y1 + 165), "Sur quoi devrait-on travailler?", F_TITLE, "#18181b")
    draw.rounded_rectangle((cx + 210, y1 + 250, cx + 880, y1 + 380), radius=24, fill=WHITE, outline="#e5e7eb", width=2)
    text(draw, (cx + 235, y1 + 278), "Posez n'importe quelle question", F_BODY, "#a1a1aa")
    text(draw, (cx + 235, y1 + 345), "+", F_BODY_BOLD, "#71717a")
    pill(draw, (cx + 295, y1 + 335, cx + 430, y1 + 376), "Accès complet", "#fff7ed", True)
    text(draw, (cx + 785, y1 + 345), "5.5  Très approfondi", F_SMALL, "#71717a")
    draw.rounded_rectangle((cx + 220, y1 + 385, cx + 870, y1 + 430), radius=16, fill="#f5f5f5", outline="#f5f5f5", width=1)
    text(draw, (cx + 245, y1 + 398), "Travailler sur un projet", F_SMALL, "#71717a")
    draw.rounded_rectangle((cx + 210, y1 + 505, cx + 880, y1 + 620), radius=20, fill=WHITE, outline="#e5e7eb", width=2)
    text(draw, (cx + 260, y1 + 535), "Activer le mode Fast", F_SMALL_BOLD, "#18181b")
    wrapped(draw, (cx + 260, y1 + 565), "Codex estime le temps gagné et propose un mode plus rapide quand le travail s'y prête.", 520, F_SMALL, "#71717a", 6)
    pill(draw, (cx + 700, y1 + 545, cx + 845, y1 + 585), "Activer maintenant", "#18181b", True)


def codex_plugins_ui(draw: ImageDraw.ImageDraw) -> None:
    x1, y1, x2, y2 = 54, 315, 1380, 835
    shadow(draw, (x1, y1, x2, y2), WHITE, size=12)
    pill(draw, (x1 + 30, y1 + 22, x1 + 150, y1 + 60), "Plugiciels", "#f4f4f5", True)
    text(draw, (x1 + 170, y1 + 32), "Compétences", F_SMALL, "#9ca3af")
    text(draw, (x1 + 470, y1 + 100), "Adaptez Codex à vos besoins", F_TITLE, "#18181b")
    draw.rounded_rectangle((x1 + 260, y1 + 170, x1 + 845, y1 + 210), radius=14, fill=WHITE, outline="#e5e7eb", width=2)
    text(draw, (x1 + 285, y1 + 181), "Rechercher des modules d'extension", F_SMALL, "#9ca3af")
    pill(draw, (x1 + 860, y1 + 170, x1 + 1010, y1 + 210), "Built by OpenAI", "#f4f4f5", False)
    pill(draw, (x1 + 1025, y1 + 170, x1 + 1105, y1 + 210), "Tout", "#f4f4f5", False)
    draw.rounded_rectangle((x1 + 260, y1 + 235, x1 + 1110, y1 + 465), radius=22, fill="#dbeafe", outline="#c7d2fe", width=2)
    draw.rounded_rectangle((x1 + 410, y1 + 325, x1 + 940, y1 + 395), radius=20, fill="#f8fafc", outline="#c7d2fe", width=2)
    text(draw, (x1 + 435, y1 + 346), "Gmail  Rédiger des réponses aux courriels", F_BODY, "#18181b")
    pill(draw, (x1 + 565, y1 + 425, x1 + 835, y1 + 470), "Essayer dans le clavardage", "#18181b", True)
    text(draw, (x1 + 260, y1 + 525), "Featured", F_BODY_BOLD, "#18181b")
    items = [("Spreadsheets", "Create and edit spreadsheet files"), ("Presentations", "Create and edit presentations"), ("GitHub", "Triage PRs, issues, CI, and flows"), ("Slack", "Read and manage Slack"), ("Notion", "Research and manage docs"), ("Linear", "Find and reference issues")]
    for i, (name, desc) in enumerate(items):
        col = i % 2
        row = i // 2
        ix = x1 + 280 + col * 470
        iy = y1 + 575 + row * 70
        draw.rounded_rectangle((ix, iy, ix + 48, iy + 48), radius=12, fill=WHITE, outline="#e5e7eb", width=2)
        text(draw, (ix + 65, iy + 4), name, F_SMALL_BOLD, "#18181b")
        text(draw, (ix + 65, iy + 28), desc, F_SMALL, "#71717a")


def codex_automations_ui(draw: ImageDraw.ImageDraw) -> None:
    x1, y1, x2, y2 = 54, 315, 1380, 835
    shadow(draw, (x1, y1, x2, y2), WHITE, size=12)
    text(draw, (x1 + 245, y1 + 85), "Automatisations", F_TITLE, "#18181b")
    text(draw, (x1 + 245, y1 + 142), "Lancez des clavardages selon un horaire ou quand vous en avez besoin.", F_BODY, "#8b8b91")
    pill(draw, (x2 - 345, y1 + 28, x2 - 190, y1 + 68), "Voir les modèles", WHITE, False)
    pill(draw, (x2 - 178, y1 + 28, x2 - 22, y1 + 68), "Créer par clavardage", "#18181b", True)
    draw.rounded_rectangle((x1 + 610, y1 + 310, x1 + 715, y1 + 410), radius=45, fill=WHITE, outline="#18181b", width=8)
    text(draw, (x1 + 652, y1 + 337), ">_", F_BODY_BOLD, "#18181b")
    text(draw, (x1 + 485, y1 + 485), "Créez votre première automatisation", F_BODY_BOLD, "#18181b")
    chips = ["Bilan quotidien", "Revue hebdomadaire", "Suivi de projet"]
    for i, label in enumerate(chips):
        pill(draw, (x1 + 390 + i * 205, y1 + 555, x1 + 570 + i * 205, y1 + 600), label, WHITE, False)


def save(name: str, title: str, subtitle: str, badge: str, draw_fn) -> None:
    image = Image.new("RGB", (1440, 900), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, title, subtitle, badge)
    draw_fn(draw)
    image.save(OUT / name, quality=94)


SCENES = [
    ("hero-codex-claude.png", "Deux agents, un projet", "La séance compare Codex et Claude Code avec le même dossier et la même mission business.", "séance 2", lambda d: browser(d, (54, 360, 1380, 810), "restaurant-comptoir-bleu", [(CYAN, "Dossier", "Une page simple de restaurant sert de terrain commun."), ("#ede9fe", "Codex", "On observe comment il planifie, modifie et vérifie."), ("#dbeafe", "Claude Code", "On regarde la même demande dans le même contexte.")]),),
    ("codex-home-screen.png", "Accueil Codex", "L’écran de départ sert à poser une demande, choisir un projet, un niveau d’accès et un mode de raisonnement.", "codex", lambda d: codex_home_ui(d),),
    ("codex-plugiciels-screen.png", "Plugiciels Codex", "Les plugiciels adaptent Codex à vos outils : GitHub, Notion, Linear, Slack, Gmail et autres connexions.", "codex", lambda d: codex_plugins_ui(d),),
    ("codex-automatisations-screen.png", "Automatisations Codex", "Les automatisations lancent des clavardages selon un horaire ou un besoin récurrent.", "codex", lambda d: codex_automations_ui(d),),
    ("codex-install.png", "Installer Codex", "La route officielle propose une application, une extension IDE, le CLI et le cloud.", "codex", lambda d: terminal(d, (54, 350, 1380, 820), "Installation Codex CLI", [("$", "curl -fsSL https://chatgpt.com/codex/install.sh | sh"), ("PS", 'powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"'), ("$", "npm install -g @openai/codex"), ("$", "brew install --cask codex")]),),
    ("codex-login.png", "Connexion Codex", "Codex démarre dans le terminal puis demande une connexion ChatGPT ou une clé API.", "codex", lambda d: terminal(d, (54, 350, 1380, 820), "Première session Codex", [("$", "cd restaurant-comptoir-bleu"), ("$", "codex"), ("codex", "Sign in with ChatGPT ou API key"), ("codex", "Local sélectionné : Codex travaille sur votre machine.")]),),
    ("claude-install.png", "Rappel Claude Code", "Claude Code a déjà été vu en séance 1. Ici il sert seulement de point de comparaison.", "claude", lambda d: terminal(d, (54, 350, 1380, 820), "Rappel rapide", [("$", "cd restaurant-comptoir-bleu"), ("$", "claude"), ("claude", "Même dossier, même brief, même vérification."), ("→", "Pas de réinstallation ici : on compare seulement la méthode.")]),),
    ("same-folder.png", "Même dossier", "La comparaison ne vaut rien si les deux outils ne partent pas du même contexte.", "terrain", lambda d: folder(d, (54, 350, 1380, 820), "restaurant-comptoir-bleu", [("DIR", "img/"), ("FILE", "index.html"), ("FILE", "README.md"), ("FILE", "AGENTS.md"), ("FILE", "CLAUDE.md")]),),
    ("same-brief.png", "Même brief", "On donne la même demande aux deux outils pour comparer le raisonnement, pas l’humeur du moment.", "brief", lambda d: terminal(d, (54, 350, 1380, 820), "Brief commun", [(">", "Ajoute une formule midi à la page du Comptoir Bleu."), (">", "Garde fond blanc, bleu et violet. Vérifie mobile."), (">", "Liste les fichiers modifiés et les tests à faire.")]),),
    ("agents-md.png", "AGENTS.md", "Codex lit les consignes de projet dans AGENTS.md quand elles existent dans le dossier.", "codex", lambda d: folder(d, (54, 350, 1380, 820), "AGENTS.md", [("RULE", "Fond blanc, accents bleu et violet"), ("RULE", "Toujours vérifier mobile"), ("RULE", "Ne pas ajouter de dépendance sans demander"), ("RULE", "Résumer les fichiers modifiés")]),),
    ("claude-md.png", "CLAUDE.md", "Claude Code peut garder les conventions du projet dans CLAUDE.md.", "claude", lambda d: folder(d, (54, 350, 1380, 820), "CLAUDE.md", [("RULE", "Français simple et direct"), ("RULE", "Page restaurant fictive"), ("RULE", "Bouton Réserver visible"), ("RULE", "Pas de secret ni clé API")]),),
    ("first-comparison.png", "Premier verdict", "La première comparaison porte sur le plan proposé avant de toucher aux fichiers.", "plan", lambda d: comparison(d, (54, 330, 1380, 835), [("Lire le dossier", "Explique vite les fichiers et les risques", "Explique le contexte et propose une boucle"), ("Créer la formule", "Peut proposer un diff direct", "Demande souvent une validation claire"), ("Vérifier", "Insiste sur git et commandes", "Insiste sur permissions et rendu")]),),
    ("codex-plan.png", "Plan Codex", "Codex sert bien de deuxième regard structuré avant une modification.", "codex", lambda d: kanban(d, (54, 350, 1380, 820), [("Comprendre", "#dbeafe", ["Lire index.html", "Repérer la zone menu"]), ("Modifier", "#ede9fe", ["Ajouter formule midi", "Garder CTA visible"]), ("Vérifier", CYAN, ["Comparer le diff", "Tester mobile"])]),),
    ("claude-plan.png", "Plan Claude Code", "Claude Code sert à dérouler la tâche dans le terminal avec validations visibles.", "claude", lambda d: kanban(d, (54, 350, 1380, 820), [("Observer", CYAN, ["Lister les fichiers", "Lire les règles"]), ("Agir", "#ede9fe", ["Créer la section", "Adapter les textes"]), ("Contrôler", "#dbeafe", ["Ouvrir la page", "Relire le bouton"])]),),
    ("diff-codex.png", "Diff Codex", "Le diff montre exactement ce qui change. On ne valide pas une phrase, on valide des lignes.", "diff", lambda d: terminal(d, (54, 350, 1380, 820), "Résumé des changements", [("codex", "+ section formule-midi"), ("codex", "+ bouton Voir la formule"), ("codex", "~ styles responsive"), ("$", "git diff -- index.html")]),),
    ("diff-claude.png", "Diff Claude Code", "Claude Code vous laisse relire la modification avant de l’accepter.", "diff", lambda d: terminal(d, (54, 350, 1380, 820), "Modification proposée", [("claude", "Je vais modifier index.html"), ("claude", "Section ajoutée : Formule midi"), ("claude", "Souhaitez-vous appliquer ce changement ?"), (">", "Lire puis accepter ou refuser")]),),
    ("browser-preview.png", "Aperçu navigateur", "Le vrai test n’est pas la réponse de l’outil. Le vrai test est la page ouverte.", "test", lambda d: browser(d, (54, 330, 1380, 835), "Le Comptoir Bleu", [("#dbeafe", "Hero", "Le nom et le bouton sont visibles dès le début."), ("#ede9fe", "Formule midi", "Prix fictif, plats courts, texte facile à lire."), (CYAN, "Contact", "Adresse, horaires et réservation restent accessibles.")]),),
    ("mobile-check.png", "Version mobile", "Une page de restaurant se consulte souvent sur téléphone. La comparaison inclut ce test.", "mobile", lambda d: browser(d, (300, 300, 1110, 835), "Mobile 390px", [(WHITE, "Menu compact", "Le titre ne déborde pas."), ("#dbeafe", "Bouton", "Réserver reste visible."), ("#ede9fe", "Section", "Formule midi se lit sans zoom.")]),),
    ("git-status.png", "État Git", "Avant de juger un agent, on regarde les fichiers qu’il a réellement touchés.", "git", lambda d: terminal(d, (54, 350, 1380, 820), "git status", [("$", "git status --short"), ("→", "M index.html"), ("→", "?? img/interface-s2/mobile-check.png"), ("?", "Est-ce attendu pour cette tâche ?")]),),
    ("approval-modes.png", "Permissions", "Les modes de permission changent le niveau de contrôle avant les commandes et les éditions.", "sécurité", lambda d: comparison(d, (54, 330, 1380, 835), [("Début", "Read-only ou auto avec vigilance", "Default ou plan mode"), ("Projet isolé", "Auto peut aller plus vite", "Accept edits peut aider"), ("Client réel", "Lire les commandes avant accord", "Garder les validations importantes")]),),
    ("pricing-comparison.png", "Accès et budget", "Les plans évoluent. Le bon réflexe est de vérifier les pages officielles avant de décider.", "budget", lambda d: comparison(d, (54, 330, 1380, 835), [("Codex", "Inclus dans les plans ChatGPT éligibles", "Limites selon plan et usage agentique"), ("Claude Code", "Plan Pro ou Max possible", "Limites partagées avec Claude"), ("Décision", "Tester sur un vrai besoin", "Payer plus seulement si la limite bloque le travail")]),),
    ("local-vs-cloud.png", "Local ou cloud", "Codex peut être utilisé en local ou dans le cloud. Claude Code a aussi des surfaces locales et web.", "surface", lambda d: comparison(d, (54, 330, 1380, 835), [("Local", "Travaille dans le dossier de la machine", "Terminal et dossier courant"), ("Cloud", "Environnement lié à un dépôt", "Tâches web avec GitHub selon accès"), ("À retenir", "Contexte et permissions à vérifier", "Compte, dépôt et limites à vérifier")]),),
    ("business-task.png", "Tâche business", "On ne compare pas les outils avec une question vague, mais avec une demande utile pour vendre.", "business", lambda d: terminal(d, (54, 350, 1380, 820), "Mission du jour", [(">", "La formule midi doit être plus visible."), (">", "Le bouton Réserver doit mener au contact."), (">", "La page doit rester sérieuse sur mobile."), (">", "À la fin, dites quel agent a été le plus clair.")]),),
    ("prompt-bad-good.png", "Prompt utile", "Un prompt comparatif doit donner contexte, sortie, limites et vérification attendue.", "prompt", lambda d: comparison(d, (54, 330, 1380, 835), [("Trop vague", "améliore le site", "risque de tout changer"), ("Correct", "ajoute formule midi", "zone et résultat clairs"), ("Bon", "ajoute, garde style, vérifie mobile", "comparaison propre")]),),
    ("debug-flow.png", "Déboguer", "Quand un bouton ne marche pas, le bon agent est celui qui explique et corrige sans casser le reste.", "debug", lambda d: kanban(d, (54, 350, 1380, 820), [("Symptôme", ROSE, ["Le bouton ne descend pas", "Lien #contact absent"]), ("Diagnostic", YELLOW, ["Chercher l'id contact", "Lire le href du bouton"]), ("Correction", GREEN, ["Créer l'ancre", "Tester le clic"])]),),
    ("review-other-agent.png", "Deuxième regard", "Un agent peut relire le travail de l’autre. C’est souvent plus utile qu’une compétition.", "review", lambda d: terminal(d, (54, 350, 1380, 820), "Revue croisée", [("codex", "Relis les changements faits par Claude Code."), ("codex", "Signale seulement les risques réels."), ("claude", "Relis le diff Codex et propose 3 corrections utiles."), ("→", "Vous gardez la décision finale.")]),),
    ("parallel-workflow.png", "Travail en parallèle", "Codex peut servir au second avis pendant que Claude Code déroule une tâche locale, ou l’inverse.", "routine", lambda d: kanban(d, (54, 350, 1380, 820), [("Claude Code", "#dbeafe", ["Créer la section", "Tester le rendu"]), ("Codex", "#ede9fe", ["Relire le diff", "Chercher risque mobile"]), ("Décision", CYAN, ["Garder le meilleur", "Refuser le superflu"])]),),
    ("daily-routine.png", "Routine quotidienne", "La comparaison devient utile quand elle crée une méthode simple à refaire tous les jours.", "routine", lambda d: browser(d, (54, 350, 1380, 820), "Routine 15 minutes", [(CYAN, "1. Brief", "Une tâche concrète et vérifiable."), ("#ede9fe", "2. Agent", "Choisir Codex, Claude Code, ou les deux."), ("#dbeafe", "3. Vérif", "Ouvrir la page, relire le diff, tester mobile.")]),),
    ("decision-matrix.png", "Matrice de choix", "Le bon choix dépend de la situation, pas d’un outil préféré.", "choix", lambda d: comparison(d, (54, 330, 1380, 835), [("Installer", "Simple avec CLI ou app", "Simple avec terminal et compte Claude"), ("Comparer", "Très utile en review", "Très utile en exécution guidée"), ("Livrer", "Bon pour checklist et diff", "Bon pour corrections terminal")]),),
    ("risk-table.png", "Risques terrain", "Les vrais problèmes viennent souvent du mauvais dossier, du mauvais compte ou d’une demande trop large.", "risques", lambda d: comparison(d, (54, 330, 1380, 835), [("Mauvais dossier", "lit le mauvais projet", "modifie au mauvais endroit"), ("Compte confus", "limites ou accès inattendus", "API au lieu d’abonnement"), ("Demande large", "trop de changements", "trop de contexte")]),),
    ("source-check.png", "Sources officielles", "Les prix, commandes et accès changent. Les pages officielles restent la référence.", "sources", lambda d: browser(d, (54, 350, 1380, 820), "Docs à vérifier", [("#dbeafe", "OpenAI", "Quickstart, pricing, AGENTS.md, CLI."), ("#ede9fe", "Anthropic", "Quickstart, Pro/Max, limites, CLAUDE.md."), (CYAN, "Décision", "Mettre la date de vérification dans vos notes.")]),),
    ("handoff-summary.png", "Résumé final", "Une livraison claire explique ce qui a été fait, par qui, comment vérifier et quoi faire ensuite.", "livraison", lambda d: terminal(d, (54, 350, 1380, 820), "Résumé de livraison", [(">", "Objectif : comparer Codex et Claude Code sur la formule midi."), (">", "Fichiers : index.html, AGENTS.md, CLAUDE.md."), (">", "Vérifications : desktop, mobile, bouton, diff."), (">", "Choix : outil à garder selon la prochaine tâche.")]),),
    ("easter-egg.png", "Détail caché", "Le petit bouton de thème et le raccourci de progression rendent la page plus vivante sans gêner la lecture.", "design", lambda d: browser(d, (54, 350, 1380, 820), "Micro-interactions", [("#dbeafe", "Progression", "La barre suit la lecture."), ("#ede9fe", "Copier", "Les blocs pratiques se copient."), (CYAN, "Mode focus", "Un détail discret active un style de lecture.")]),),
    ("codex-app.png", "Application Codex", "Codex existe aussi en application locale sur macOS et Windows.", "codex", lambda d: browser(d, (54, 350, 1380, 820), "Codex app · Local", [("#dbeafe", "Projet", "Sélectionner un dossier local."), ("#ede9fe", "Message", "Demander une tâche concrète."), (CYAN, "Diff", "Lire et appliquer les changements.")]),),
    ("claude-web.png", "Claude Code web", "Claude Code peut aussi lancer des tâches web liées à GitHub selon l’accès disponible.", "claude", lambda d: browser(d, (54, 350, 1380, 820), "Claude Code on the web", [("#dbeafe", "Dépôt", "Connecter le dépôt GitHub."), ("#ede9fe", "Tâche", "Créer une branche de travail."), (CYAN, "Revue", "Vérifier le changement avant fusion.")]),),
    ("final-map.png", "Carte finale", "À la fin, la séance donne une méthode de choix, pas une opinion figée.", "fin", lambda d: kanban(d, (54, 350, 1380, 820), [("Comprendre", "#dbeafe", ["Ce que fait chaque outil", "Comment installer"]), ("Comparer", "#ede9fe", ["Même brief", "Même dossier", "Même test"]), ("Choisir", CYAN, ["Tâche locale", "Review", "Budget", "Habitude"])]),),
]


def main() -> None:
    for scene in SCENES:
        save(*scene)


if __name__ == "__main__":
    main()
