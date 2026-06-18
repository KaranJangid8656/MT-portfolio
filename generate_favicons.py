from PIL import Image, ImageDraw, ImageFont
import os

out = 'favicon'
os.makedirs(out, exist_ok=True)

sizes = {
    'favicon-16x16.png': 16,
    'favicon-32x32.png': 32,
    'favicon-96x96.png': 96,
    'android-chrome-192x192.png': 192,
    'android-chrome-512x512.png': 512,
    'web-app-manifest-192x192.png': 192,
    'web-app-manifest-512x512.png': 512,
    'apple-touch-icon.png': 180,
}

BG_COLOR = (17, 24, 39, 255)
BORDER_COLOR = (249, 115, 22, 255)
TEXT_COLOR = (255, 255, 255, 255)


def render_icon(size):
    img = Image.new('RGBA', (size, size), BG_COLOR)
    draw = ImageDraw.Draw(img)
    margin = max(4, size // 16)
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=size // 8,
        fill=BORDER_COLOR,
    )

    text = 'MT'
    font_size = int(size * 0.55)
    try:
        font = ImageFont.truetype('arial.ttf', font_size)
    except Exception:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    draw.text(
        ((size - text_w) / 2, (size - text_h) / 2 - size * 0.02),
        text,
        font=font,
        fill=TEXT_COLOR,
    )
    return img


if __name__ == '__main__':
    for name, size in sizes.items():
        render_icon(size).save(os.path.join(out, name))

    ico = render_icon(64)
    ico.save(os.path.join(out, 'favicon.ico'), format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print('Generated favicon assets in', out)
