---
name: mp-draft-push
description: """""publish to draft"""
homepage: https://github.com/bbwdadfg/wechat-ai-publisher
metadata: {"openclaw":{"emoji":"","requires":{"bins":["bash","curl","jq"]}}}
---

# mp-draft-push

## ****AI 

---

## Skill

| | | | |
|------|------|------|------|
| `title` | string | [] | 64 21 |
| `digest` | string | [] | |
| `content_html` | string | [] | HTML |
| `cover_image_path` | string | [] | URL |

---

## ```
1. 
 ↓
2. access_token
 ↓
3. thumb_media_id
 ↓
4. 
 ↓
5. 
```

---

## - **AppID**: `WECHAT_APPID`
- **AppSecret**: `WECHAT_SECRET`
- ****: `WECHAT_AUTHOR` `koo AI`

** AppID AppSecret**
1. [](https://developers.weixin.qq.com/platform/)
2. [ → /](https://developers.weixin.qq.com/platform/apps/subscription)
3. AppID AppSecret

> **** AppSecret
> / [ → ](https://mp.weixin.qq.com) 

---

## Step 1: 

****

 `cover_image_path`
1. ** `gen_image` ** `gen_image` 900×383 2.35:1 `/tmp/wechat_cover_generated.png`
2. `gen_image` `DEFAULT_COVER_URL` `/tmp/wechat_cover_default.png` 
3. `thumb_media_id` 

---

## Step 2 & 3: 



```bash
source ./scripts.sh
```

### access_token

```bash
TOKEN=$(get_wechat_token)
```

### ```bash
MEDIA_RESPONSE=$(upload_wechat_image "$TOKEN" "$cover_image_path")
THUMB_MEDIA_ID=$(echo "$MEDIA_RESPONSE" | jq -r '.media_id')
```

### JSON 

`content_html` 
- `style="..."` `<style>` 
- `mmbiz.qpic.cn` 
- JSON `ensure_ascii=False`

```bash
DRAFT_JSON="/tmp/draft_$(date +%Y%m%d%H%M%S).json"
jq -n \
 --arg title "$title" \
 --arg author "${WECHAT_AUTHOR:-koo AI}" \
 --arg digest "$digest" \
 --arg content "$content_html" \
 --arg thumb_media_id "$THUMB_MEDIA_ID" \
 '{
 articles: [{
 title: $title,
 author: $author,
 digest: $digest,
 content: $content,
 thumb_media_id: $thumb_media_id,
 need_open_comment: 1,
 only_fans_can_comment: 0
 }]
 }' > "$DRAFT_JSON"

DRAFT_RESPONSE=$(create_draft "$TOKEN" "$DRAFT_JSON")
DRAFT_MEDIA_ID=$(echo "$DRAFT_RESPONSE" | jq -r '.media_id')
rm -f "$DRAFT_JSON"
```

 `DRAFT_MEDIA_ID` `null` `DRAFT_RESPONSE` 

---

## Step 4: 



```
[] 

 
- {title}
- {digest}
- media_id{DRAFT_MEDIA_ID}

 
 https://mp.weixin.qq.com →

 
1. 
2. 
3. 
4. ""
```

> API 

---

## HTML 

```html
<section style="font-family: -apple-system, sans-serif; line-height: 1.8; color: #333; padding: 15px;">
 <p style="margin-bottom: 20px;"></p>

 <h2 style="border-bottom: 1px solid #eee; padding-bottom: 8px;"></h2>

 <p style="text-align: center; margin: 25px 0;">
 <img src="{mmbiz_img_url}" style="max-width: 100%; border-radius: 6px;">
 </p>

 <blockquote style="background: #f6f8fa; border-left: 4px solid #ddd; padding: 12px 16px;">
 
 </blockquote>
</section>
```

---

## 1. ****JSON `ensure_ascii=False``jq` 
2. **** 64 21 
3. **access_token** 2 
4. **** `mmbiz.qpic.cn` URL
