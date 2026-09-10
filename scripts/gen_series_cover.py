import os, sys, subprocess, argparse, shutil, re

def generate_cover(title, en_title, motif, tagline, author="著 / 宇龙", output_path=None):
    prompt = f"""请调用 image_gen 生成一张 3:4 比例的纯正面平视图书封面（2D Flat Front View，纯正面垂直视角，不要任何立体透视或旋转角度）：
1. 构图与外框：纯正面垂直视角，四周必须有一圈干净优雅的白色精装书边框（white outer border）；
2. 封面版心：纯正高饱和活力爱马仕亮橙色（Hermes Orange），极简现代科技风，留白高级；
3. 封面文字工整、清晰印在封面上：
   - 顶部英文小标：THE ORANGE PAPER SERIES
   - 主标题特粗黑体：{title}
   - 副标题：AI SKILL 橙皮书
   - 英文副标：{en_title}
   - 中间视觉：小巧精致的几何微光 {motif}
   - 核心定位语：{tagline}
   - 底部作者署名：{author}
请直接生成完整图书封面，并告诉我保存路径。"""

    print(f"[*] Submitting Grok Imagine task for '{title}'...")
    cmd = ["grok", "--always-approve", "-p", prompt]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=r"D:\repos\wechat-viral-orange-paper")
    
    output = res.stdout + res.stderr
    print("[*] Grok response summary:")
    print(output[-500:] if len(output) > 500 else output)
    
    match = re.search(r'([A-Za-z]:\\[^\n\r]+\.(?:jpg|png))', output)
    if match:
        img_path = match.group(1).strip('`" ')
        if os.path.exists(img_path):
            print(f"[+] Found generated image at: {img_path}")
            if output_path:
                shutil.copy2(img_path, output_path)
                print(f"[+] Saved to: {output_path}")
            return img_path
    
    match_rel = re.search(r'images[\\/]\d+\.(?:jpg|png)', output)
    if match_rel:
        rel_p = match_rel.group(0)
        print(f"[+] Found relative path: {rel_p}")
        return rel_p
        
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Series Orange Paper Cover")
    parser.add_argument("--title", required=True, help="Book Title")
    parser.add_argument("--en", required=True, help="English Subtitle")
    parser.add_argument("--motif", required=True, help="Center Motif Description")
    parser.add_argument("--tagline", default="AI 工业化工程手册", help="Tagline")
    parser.add_argument("--author", default="著 / 宇龙", help="Author Signature")
    parser.add_argument("--out", default=None, help="Output image path")
    
    args = parser.parse_args()
    generate_cover(args.title, args.en, args.motif, args.tagline, args.author, args.out)
