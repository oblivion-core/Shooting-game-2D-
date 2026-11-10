# TP N°1 – Methods and Technologies of Implementation (M1 GSI)

## Folder layout
```
tp1/
├── part1/  part1_basics.py  part1_text_fixed.py  data.txt
├── part2/  part2_csv.py  modules.csv  (modules.json + modules.html are generated)
├── homework/  game.py
└── README.md
```

## Step-by-step

### Step 0 – Setup
1. Install Python 3.10+ (python.org) and VS Code (or PyCharm).
2. `pip install pygame` (needed for the homework only).
3. Create a GitHub repo, add your partner (max 2 people), clone it, and copy this folder in.

### Step 1 – Part 1: run the basics
`cd part1 && python part1_basics.py`
Be able to explain: dynamic typing, `%s`/`%d` substitution, lists + `append`, `if/elif/else`, `in`, `for`.

### Step 2 – Part 1: fix the buggy program
Run `part1_text_fixed.py`. The errors in the original listing (list them in the report):

| Line | Error | Fix |
|---|---|---|
| 2-4, 11-13, 16-18, 25-27, 36-38, 51 | docstrings with mismatched quotes | use `"""..."""` |
| 5 | unterminated string `punct` | close the quote and escape `\'` |
| 6, 10, 15, 30, 32, 35, 41, 50, 54 | missing `:` | add colon |
| 7 | `replace(p,")` | `replace(p, "")` |
| 14 | `split( )` fine but spaces/newlines | `split()` |
| 19 | `\s+` not a string | `r"\s+"` |
| (top) | `re`, `sys` never imported | `import re, sys` |
| 21 | `return word` | `return words` |
| 39 | `frequent =` empty | `frequent = None` |
| 53 | `text = "'` | remove it |
| 57 | `print(Can't open file, ...)` | `print("Can't open file", filename)` |
| 60-61 | `read()` then `readlines()` returns empty | keep only `read()` |
| 65-70 | `""` opening a multi-line string | use `"""` |
| 78 | `"data.txt)` | `"data.txt"` |
| 86 | `print(most frequent word is ', ...)` | `print("most frequent word is", ...)` |

### Step 3 – Part 2: CSV → dictionaries
`cd part2 && python part2_csv.py`
- Level 1-2: `data[semester][unit] = [modules]` (`csv_to_nested_dict`)
- Level 3: `data[semester][unit][module_name] = {...}` (`csv_to_nested_dict3`)
- JSON: `json.dumps(data, indent=4, ensure_ascii=False)`
- HTML: `modules_to_html` → open `modules.html` in a browser.

Two traps in the lab handout:
1. The CSV is **tab-separated** → `delimiter="\t"`.
2. Percentages are already `20`, `40`, `60` → do **not** multiply by 100 in the HTML.

### Step 4 – Homework: Pygame prototype
`cd homework && python game.py`
Map of the requested tasks → code:

| Task | Where |
|---|---|
| Player moves in the game area | `Player.move` (+ boundary clamp) |
| Monster moves | `Monster.update` (pursues the player) |
| Main loop | `Game.run` |
| Input handling | `Game.handle_events` |
| Object updates | `Game.update` |
| Rendering | `Game.draw` |
| Bullet/monster/reward/collisions/score/health | bonus, already included |

You must be able to **explain and modify** it (AI use is allowed only on that condition). Practice: change player speed, bullet damage, add a second monster type, change the story/colors.

### Step 5 – GitHub (graded)
```
git checkout -b part2
git add part2/ && git commit -m "Part 2: nested dict + JSON + HTML"
git push -u origin part2     # then open a Pull Request
```
Commit progressively, one commit per task, both partners commit, keep the README updated.

### Step 6 – Report (pair, printed, clamps only, no colors needed)
- **Cover page**: names (pair), specialty & group, module (MTI), "TP N°1 – Python / <your game title>".
- **1. Introduction**: problem + questions (Python basics, CSV → structured data, game loop).
- **2. Methodology**: nested dictionaries, `csv.DictReader`, JSON serialization, HTML generation, game loop (input → update → render), circle collision.
- **3. Tools**: Python, `csv`, `json`, Pygame, Git/GitHub. *(Do not re-explain tools already seen in class.)*
- **4. Tests and results**: screenshots of terminal output, the JSON, the HTML table, the game screen.
- **Appendix**: commented source code.
- Submit on the platform before the deadline.
