from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "public"
OUT.mkdir(parents=True, exist_ok=True)
PALETTE = [(10, 10, 15), (139, 92, 246), (6, 182, 212), (16, 185, 129)]


def neon(size: int) -> Image.Image:
    img = Image.new("RGB", (size, size), PALETTE[0])
    dr = ImageDraw.Draw(img)
    for i in range(size):
        r = i / size
        c = tuple(int(PALETTE[1][j] * (1 - r) + PALETTE[2][j] * r) for j in range(3))
        dr.line([(0, i), (size, i)], fill=c)
    for r in range(0, size, max(1, size // 32)):
        alpha = max(0, 120 - int(120 * (r / size)))
        glow = Image.new("RGBA", (size, size), (*PALETTE[3], alpha))
        img = Image.alpha_composite(img.convert("RGBA"), glow)
    return img.convert("RGBA")


def text(img: Image.Image, label: str, scale: float = 0.5) -> Image.Image:
    dr = ImageDraw.Draw(img)
    w, h = img.size
    try:
        font = ImageFont.truetype("arial.ttf", int(h * scale * 0.4))
    except Exception:
        font = ImageFont.load_default()
    tw, th = dr.textsize(label, font=font)
    pos = ((w - tw) // 2, (h - th) // 2)
    dr.text(pos, label, fill=(255, 255, 255, 230), font=font)
    return img


def save_png(name: str, size: int, label: str) -> None:
    img = text(neon(size), label)
    path = OUT / name
    img.save(path, format="PNG")
    print(f"saved {path}")


def save_og(name: str = "og-image.png") -> None:
    w, h = 1200, 630
    img = neon(max(w, h)).resize((w, h))
    dr = ImageDraw.Draw(img)
    try:
        f1 = ImageFont.truetype("arial.ttf", 96)
        f2 = ImageFont.truetype("arial.ttf", 36)
    except Exception:
        f1 = ImageFont.load_default()
        f2 = ImageFont.load_default()
    dr.text((60, 200), "SUNFIXER", font=f1, fill=(255, 255, 255, 255))
    dr.text((60, 320), "NEUROFUNK ARCHITECT", font=f2, fill=(139, 92, 246, 255))
    path = OUT / name
    img.save(path, format="PNG")
    print(f"saved {path}")


def main():
    save_png("icon-192.png", 192, "SF")
    save_png("icon-512.png", 512, "SF")
    save_og()


if __name__ == "__main__":
    main()
