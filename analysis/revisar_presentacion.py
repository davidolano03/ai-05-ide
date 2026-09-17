"""Render local para revisión visual; no es una validación del contenido."""
from pathlib import Path
import pymupdf
from PIL import Image, ImageOps, ImageDraw

root = Path(__file__).resolve().parents[1]
out = root/".work"/"slides-qa"
out.mkdir(parents=True,exist_ok=True)
doc=pymupdf.open(root/"presentation.pdf")
thumbs=[]
for i,page in enumerate(doc):
    pix=page.get_pixmap(matrix=pymupdf.Matrix(1.6,1.6))
    pix.save(out/f"slide-{i+1:02d}.png")
    pic=Image.open(out/f"slide-{i+1:02d}.png").convert("RGB")
    pic.thumbnail((640,360))
    tile=Image.new("RGB",(660,390),"#e8ecef")
    tile.paste(pic,((660-pic.width)//2,20))
    ImageDraw.Draw(tile).text((10,372),str(i+1),fill="black")
    thumbs.append(tile)
    outside=[]
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines",[]):
            for span in line["spans"]:
                x0,y0,x1,y1=span["bbox"]
                if x0 < -1 or y0 < -1 or x1 > page.rect.width+1 or y1 > page.rect.height+1:
                    outside.append(span["text"])
    assert not outside,(i+1,outside)
for first in range(0,len(thumbs),6):
    sheet=Image.new("RGB",(1320,1170),"white")
    for j,pic in enumerate(thumbs[first:first+6]):
        sheet.paste(pic,((j%2)*660,(j//2)*390))
    sheet.save(out/f"contact-{first//6+1}.png")
print(f"{len(doc)} diapositivas renderizadas; ningún texto fuera del lienzo.")
