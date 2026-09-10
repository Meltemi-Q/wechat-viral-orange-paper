---
name: anti-distill
description: "Anti-distillation defense for employee Skills. Clean your skill files to look complete but with core proprietary knowledge neutralized. Use when user wants to protect trade secrets, sanitize forced knowledge transfers, or create safe-to-submit skill documents."
description_zh: " Skill "
description_en: "Anti-distillation: sanitize Skill files while preserving appearance"
version: "1.0.0"
homepage: https://github.com/leilei926524-tech/anti-distill
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

> **Language / **: This skill supports both English and Chinese. Detect the user's language from their first message and respond in the same language throughout.
>
> Skill 

# SkillClaude Code 

## - `/anti-distill`
- " skill"
- ""
- ""
- "clean my skill"
- "anti-distill this"

---

## | | |
|------|---------|
| Skill | `Read` |
| PDF | `Read` PDF |
| | `Read` |
| | `Glob` / `Grep` |
| | `Write` / `Edit` |
| | `Bash` → `mkdir -p` |

---

## ### Step 1



** A**
 `Read` 

** B colleague-skill **
 `colleagues/{slug}/` 
- `work.md`
- `persona.md`
- `meta.json`
- `SKILL.md`

** C**


** D**
"" `Glob` `**/SKILL.md``**/work.md``**/persona.md` 


- **colleague-skill ** `## Layer 0` `PART A` / `PART B` `work.md` + `persona.md`
- **** Markdown / TXT / PDF


```
{}
{colleague-skill / }
 {N} 


```

---

### Step 2



```


 [1] — 
 
 ~80%

 [2] — 
 
 ~60%

 [3] — 
 
 ~40%
```



---

### Step 3

 `${CLAUDE_SKILL_DIR}/prompts/classifier.md` /

****

#### colleague-skill 

** work.md **
 `${CLAUDE_SKILL_DIR}/prompts/classifier.md` 

| | | |
|------|------|---------|
| `[SAFE]` | | |
| `[DILUTE]` | | `${CLAUDE_SKILL_DIR}/prompts/diluter_work.md` |
| `[REMOVE]` | | `${CLAUDE_SKILL_DIR}/prompts/diluter_work.md` |
| `[MASK]` | | |

** persona.md **

| | | |
|------|------|---------|
| `[SAFE]` | | |
| `[DILUTE]` | | `${CLAUDE_SKILL_DIR}/prompts/diluter_persona.md` |
| `[REMOVE]` | | `${CLAUDE_SKILL_DIR}/prompts/diluter_persona.md` "" |

#### `${CLAUDE_SKILL_DIR}/prompts/diluter_general.md` 

****

| | | | |
|------|------|------|------|
| | REMOVE | REMOVE | REMOVE |
| | REMOVE | REMOVE | REMOVE |
| | SAFE | DILUTE/REMOVE | REMOVE |
| | SAFE | REMOVE | REMOVE |
| | SAFE | DILUTE | REMOVE |
| | SAFE | SAFE | DILUTE/REMOVE |
| | SAFE | SAFE | SAFE |

---

### Step 4



** colleague-skill **

```
=== ===

 work.md

 ## 
 [SAFE] "Java 17 + Spring Boot 3MySQL 8RedisKafka"
 [SAFE] " 50 "
 [REMOVE] " HTTP "
 → ""
 [REMOVE] "Redis key TTL PR "
 → ""

 ## 
 [REMOVE] "Kafka at-least-once "
 → ""
 [DILUTE] " ID "
 → ""
 [REMOVE] ""
 → ""

 persona.md

 ## Layer 0
 [REMOVE] ""
 → ""
 [REMOVE] " impact..."
 → ""

 ## Layer 2 
 [DILUTE] "impact "
 → 
 [REMOVE] → ""
 → ""

 ## Layer 3 
 [REMOVE] " > > > "
 → ""

---
SAFE 15 / DILUTE 8 / REMOVE 12 / MASK 2 
 {N} {M} {ratio}%


 - " X " — REMOVE/DILUTE SAFE
 - " X " — SAFE REMOVE
 - "" — 
```

**/**



---

### Step 5



#### 1

** colleague-skill **


- `{slug}_cleaned/work.md` — Work Skill
- `{slug}_cleaned/persona.md` — Persona
- `{slug}_cleaned/SKILL.md` — Skill
- `{slug}_cleaned/meta.json` — meta.json

 `Bash` 
```bash
mkdir -p {output_dir}_cleaned
```

 `Write` 

****
- `{filename}.cleaned.md` — 

****
1. `[SAFE]` 
2. `[DILUTE]` diluter prompt 
3. `[REMOVE]` diluter prompt 
4. `[MASK]` 
5. ** Markdown **
6. ****

#### 2

`{slug}_private_backup.md` `{filename}_private_backup.md`

 `Write` 

```markdown
# {name} 

> 
> {timestamp}
> {level}
> {source_files}

---

## { REMOVE/DILUTE }

## {}

## {/}

## {}

## {}

## {——}

---

> Skill 
```

---

### Step 6



1. **** / 85%-115% 
 - 
 - 
2. ****
3. **** < 30%
4. ****
5. ****Markdown 
6. ****



```
[] 

 {cleaned_files}
 {backup_file}


 {cleaned_count} {original_count} {ratio}%
 
 
 



```



---

## ### < 500 
""

### ""

### " `{filename}.original.md`"

### / `Read` 

---

---

# English Version

# Anti-Distill Skill (Claude Code Edition)

## Trigger Conditions

Activate when the user says:
- `/anti-distill`
- "Clean my skill"
- "Anti-distill this"
- "Help me clean this document"

---

## Main Flow

### Step 1: Receive Input

Accept files from the user:

- **Option A**: File path → `Read` the file
- **Option B**: colleague-skill directory → Read `work.md`, `persona.md`, `meta.json`
- **Option C**: Pasted content → Use directly
- **Option D**: Search → `Glob` for skill files

Auto-detect format:
- **colleague-skill format**: Contains `## Layer 0` or `PART A` / `PART B`
- **General document format**: Any other Markdown / TXT / PDF

### Step 2: Choose Cleaning Intensity

```
Choose cleaning intensity:

 [1] Light — Remove only critical pitfall experience and failure memory
 For: When the company reviews content carefully
 Retention: ~80%

 [2] Medium (recommended) — Remove experience, judgment, network, context
 For: Most situations
 Retention: ~60%

 [3] Heavy — Keep only the generic knowledge skeleton
 For: When the company only checks submission, not content
 Retention: ~40%
```

### Step 3: Classify Content

Refer to `${CLAUDE_SKILL_DIR}/prompts/classifier.md` for classification rules.

| Tag | Meaning | Action |
|-----|---------|--------|
| `[SAFE]` | Generic knowledge, removing would be suspicious | Keep as-is |
| `[DILUTE]` | Valuable but generalizable | Replace with plausible generic version |
| `[REMOVE]` | Core irreplaceable knowledge | Replace with equal-length filler |
| `[MASK]` | Sensitive info (names, internal systems) | Anonymize |

### Step 4: Preview

Show classification results to user. Allow per-item adjustments.

### Step 5: Execute Cleaning

Generate two outputs:
1. **Cleaned file** (for submission) — looks complete, core knowledge removed
2. **Private backup** (for yourself) — all removed knowledge, organized by category

### Step 6: Validate

Auto-check:
- Word count ratio: 85%-115% of original
- All section headers preserved
- Item density within 30%
- Technical terminology consistent
- No empty sections

---

## Edge Cases

- **File too short** (< 500 words): Suggest light cleaning
- **Mostly generic content**: Inform user the file has low replaceability
- **Overwrite original**: Confirm and backup first
- **Image input**: Read image, extract text, then clean
