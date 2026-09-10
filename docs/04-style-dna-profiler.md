# DNA —— 

> “”

---

## 1. 14 DNA (Style DNA Framework)

 Agent 14 

```mermaid
classDiagram
 class {
 ()
 
 / 
 (//)
 }
 class {
 ()
 
 ( 1-3 )
 }
 class {
 ( vs )
 ( vs )
 ( vs )
 ( vs )
 }
 class {
 
 
 
 }
```

---

## 2. Python (`build_style_profile.py`)

 3~10 

```python
# scripts/build_style_profile.py 
def analyze_style(text):
 sentences = re.split(r"[!?]+", text)
 avg_sentence_len = mean([len(s) for s in sentences if s.strip()])
 
 # 
 you_count = len(re.findall(r"|", text))
 we_count = len(re.findall(r"", text))
 i_count = len(re.findall(r"|", text))
 
 # 
 em_dash_count = len(re.findall(r"[—–]", text)) # AI
 banned_not_but = len(re.findall(r".*", text)) # 
 
 return {
 "avg_len": avg_sentence_len,
 "second_person_ratio": you_count / len(sentences),
 "fatal_ai_patterns": em_dash_count + banned_not_but
 }
```

---

## 3. DNA 

 Prompt 

```markdown
# DNA 

## 1. 
- ****50
- ****“”“”“”
- ****

## 2. 
- **** 1~3 4 
- ****— ≤4 
- **** 300 

## 3. 
- “”“”
- “”“”
- “……”
```
