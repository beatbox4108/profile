import yaml
import jinja2
from urllib.request import urlopen
from pathlib import Path
import cairosvg
import base64

with open(Path(__file__).parent/"stat.yml","r",encoding="utf-8")as f:
    stat=yaml.safe_load(f)

with open(Path(__file__).parent/"card.svg.j2","r",encoding="utf-8")as f:
    template=jinja2.Template(f.read())
with urlopen(stat["icon"]["url"])as res:
    image_dataurl=f"data:image/png;base64,{base64.b64encode(res.read()).decode('utf-8')}"
#image_dataurl=stat["icon"]["url"]
with open(Path(__file__).parent/"card.svg","w",encoding="utf-8")as f:
    svg=template.render(**stat,image_dataurl=image_dataurl)
    f.write(svg)
cairosvg.svg2png(url=str(Path(__file__).parent/"card.svg"),write_to=str(Path(__file__).parent/"card.png"))
with open("./information.html.j2","r",encoding="utf-8")as f:
    html_template=jinja2.Template(f.read())
with open(Path(__file__).parent/"information.html","w",encoding="utf-8")as f:
    f.write(html_template.render(**stat,service="プロジェクトセカイ",service_url="rhythm_game/pjsekai"))