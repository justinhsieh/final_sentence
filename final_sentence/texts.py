"""Typing passages and rule text used by Final Sentence."""

#遊戲文本(可擴充)
PREDEFINED_TEXTS = [
    "Tomatoes\nTomatos\nTomatoss\nTomattos\nTomattoes\nTomattoess\nTommattoess\nTommattoes\nTommatos\nTommatoss\nThe word was guessed: Tomatoes\n",
    "Cucumbers\nCucumbers\nCucmubers\nCucumbars\nCucumbirs\nCucumbors\nCucumburs\nCucmumbers\nCucumberss\nCucumbersz\nThe word was guessed: Cucumbers\n",
    "Potatoes\nPotatos\nPotattos\nPotattos\nPotatoos\nPotatoos\nPottatoes\nPottatoes\nPotattoes\nPotatoos\nThe word was guessed: Potatoes\n",
    "It's-been three? four? days-\nThey said there'd be time to speak.\nI sleep. I eat. I wait. I'm fine.\nI keep thinking this is all... not yet real.\n",
    "I saw her face again-no-no I didn't-\njust her hands-one hand-shaking.\nI looked away. WHY did I look away?\nIt was over too fast. That's worse.\n",
    "I THOUGHT I-\nI thought I had time to change?\nTo fix something. to-undo-to stop it.\nBut I just stood there. I DID NOTHING.\n",
    "I HEARD THEM-I DID-I JUST-\nplease god please I didn't want to-\nI DID! I KNOW I DID!\ndon't let them hang me without-\n",
    "I'm sorry.\nI'm sorry.\nI remember it all. Every sound.\nTell them I said it. Tell them I said it.\n",
    "All your base are belong to us\nI can haz cheeseburger?\nLeeroy Jenkins!\nDo a barrel roll!\n",
    "Press F to pay respects\nOne does not simply walk into Mordor\nHide yo kids, hide yo wife\nThis is fine\n",
    "I am your father\nBut I never told you\nThis is SPARTA!\nWhy you heff to me mad?\n",
    "Here comes dat boi!\nO shit waddup!\nI see what you did there\nAm I a joke to you?\n",
    "Observer: D. Thorne\nLocation: Sector North-East, Ridge 7-B\nPage 14\n",
    "Specimen ID: 042\nCoordinates: 54d12'N, 13d44'E\nDate - Time: 7.04 at 09:36\nObserved Traits:\n- Hexapod, est, 4.1 cm, weight under 2 g\n- Exoskeleton: green-black, iridescent\n- Emerged from shale surface\n- Clicking sound when handled\nStatus: Sample secured, vial C3\n",
    "Specimen ID: 057\nCoordinates: 54d13'N, 13d46'E\nDate - Time: 7.04 at 13:12\nObserved Traits:\n- Quadruped, est, 37 cm, weight 1.2 kg\n- Facial mark: full black oval \"mask\"\n- Fur: pale gold, grey-blue underlayer\n- Hind legs highly articulated\nStatus: Avoided capture\n",
    "Specimen ID: 063\nCoordinates: 54d15'N, 13d49'E\nDate - Time: 7.04 at 16:08\nObserved Traits:\n- Solitary bird, wingspan est. 62 cm\n- Plumage: copper with soot-black bands\n- No vocal call; throat vibrates visibly\n- Eyes front-facing, unblinking\nStatus: Observeed only\n",
    "First text finished.\nCongratulations.\nNow let's add commas. dashes. dots.\n",
    "The timer on the table shows time left.\nIf it hits zero - bang bang.\nThe man in the black coat shoots.\n",
    "Numbers first.\n1234567890\nLetters next\nqwertyuiop\nasdfghjkl\nzxcvbnm\nNow symbols\n---\n'''\n...\n,,,\n;;;\n:::\n!!!\n???\n",
    "end line with enter or space\nshift is optional for CAPITALS\nround one cleared well done\nempty line ends a round\nPractice ends when this text is finished.\nGet ready for the real thing.\n"
]

def format_article_text(raw_text, prefix_spaces):
    # Format raw passage text for gameplay.
    lines = raw_text.strip().split('\n')
    formatted_lines = [prefix_spaces + line.strip() + " " for line in lines]
    return "\n".join(formatted_lines) + "\n"

#多人規則說明
MULTIPLAYER_RULES = (
    "Multiplayer Rules\n"
    "1. All players type the same five passages at the same time.\n"
    "2. Every player has a 240-second timer for each passage.\n"
    "3. A wrong key resets the current line and adds one strike.\n"
    "4. Three strikes trigger Russian Roulette; a loaded chamber eliminates that player.\n"
    "5. The first player to finish all passages wins. If everyone else dies first, the last survivor wins.\n"
    "6. This Socket version supports private LAN lobbies: one player hosts, others join by IP.\n"
)

