#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aayush Ranjan profile
=====================

ONE file that builds an entire animated GitHub profile.

Every asset lives inside this script: the animated terminal card, the
ASCII portrait, the boot sequence, the tech-stack loader, the project
cards, the credentials timeline, the travelling signal-wave dividers,
and the README that ties them all together.

USAGE
-----
    1. Drop this file into your profile repository
       (github.com/Aayush-Ranjan-26/Aayush-Ranjan-26).
    2. Run it:           python3 "Aayush Ranjan profile.py"
    3. Push it:          git add -A && git commit -m "profile" && git push

It writes README.md and assets/*.svg beside itself. No dependencies, no
network, no build step - standard library only.

OPTIONS
-------
    --out DIR      write somewhere else (default: this file's folder)
    --dry-run      list what would be written, write nothing
    --no-clobber   never overwrite a file that already exists

Every SVG is hand-written SMIL, so the animation plays on GitHub with no
JavaScript. Re-theme the whole profile by editing GREEN and BLUE below
and re-running.
"""

import argparse
import os
import sys

GREEN = "#3fb950"
BLUE = "#58a6ff"


def build_wave(bars=100, width=1000, height=32):
    """The divider: 100 bars, each nudged slightly later than the last, so
    the wave appears to travel across the page forever."""
    rows = []
    for i in range(bars):
        x = 4 + i * 10
        delay = round(i * 0.045, 3)
        rows.append(
            '    <rect x="{x}" y="14" width="5" height="4" rx="2" fill="url(#wg)">'
            '<animate attributeName="height" values="4;20;4" dur="2.4s" begin="{d}s" repeatCount="indefinite"/>'
            '<animate attributeName="y" values="14;6;14" dur="2.4s" begin="{d}s" repeatCount="indefinite"/>'
            '<animate attributeName="opacity" values="0.35;1;0.35" dur="2.4s" begin="{d}s" repeatCount="indefinite"/>'
            "</rect>".format(x=x, d=delay)
        )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        'role="img" aria-label="animated signal divider">\n'
        "  <defs>\n"
        '    <linearGradient id="wg" x1="0" y1="0" x2="1" y2="0">\n'
        '      <stop offset="0%" stop-color="{g}"/>\n'
        '      <stop offset="100%" stop-color="{b}"/>\n'
        "    </linearGradient>\n"
        "  </defs>\n"
        "{rows}\n"
        "</svg>\n"
    ).format(w=width, h=height, g=GREEN, b=BLUE, rows="\n".join(rows))


# ==========================================================================
# EMBEDDED FILES
# ==========================================================================

# --- README.md ---------------------------------------------------
FILE_README_MD = r"""<p align="center">
  <img src="./assets/aayush-terminal-card.svg" width="100%" alt="Aayush Ranjan — animated terminal profile card">
</p>

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2800&pause=800&color=3FB950&center=true&vCenter=true&width=700&lines=B.Tech+AI%2FML+%C2%B7+3rd+Year+%C2%B7+SRM+Ghaziabad;NLP+%C2%B7+Computer+Vision+%C2%B7+Predictive+Modeling;Local-first+AI+with+Ollama%2C+n8n+and+MCP;Research+is+only+finished+when+it+deploys." alt="Typing SVG">

<a href="https://www.linkedin.com/in/aayush-ranjan-dev/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="mailto:Aayushranjan26092006@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
<a href="https://github.com/Aayush-Ranjan-26"><img src="https://img.shields.io/badge/GitHub-0d1117?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
<img src="https://img.shields.io/badge/Ghaziabad,_India-0d1117?style=for-the-badge&logo=googlemaps&logoColor=3fb950" alt="Location">
<img src="https://komarev.com/ghpvc/?username=Aayush-Ranjan-26&style=for-the-badge&color=3fb950&label=PROFILE+VIEWS" alt="Views">

</div>

<img src="./assets/wave.svg" width="100%" alt="">

### `>` INITIATING BOOT SEQUENCE

<img src="./assets/boot.svg" width="100%" alt="animated CLI boot sequence">

<img src="./assets/wave.svg" width="100%" alt="">

<table>
<tr>
<td width="34%" align="center">

<img src="./assets/ascii-portrait.svg" width="100%" alt="ASCII-art portrait">

</td>
<td width="66%" valign="top">

### `$ whoami`

```yaml
name:        Aayush Ranjan
handle:      "@Aayush-Ranjan-26"
role:        B.Tech — AI & Machine Learning (3rd year)
college:     SRM, Ghaziabad NCR  ·  CGPA 8.2
experience:  Software/IT Automation Intern, STPI-HQ
focus:       Applied ML | Local AI | Automation
domains:     NLP · Computer Vision · Predictive Modeling
open_to:     ML | Data Science | AI Engineering internships
```

```
$ cat ./mission.log
# ─────────────────────────────────────────────
> I design and evaluate end-to-end ML pipelines,
  then put them behind real interfaces.
> Local-first AI with Ollama; agentic automation
  with n8n and MCP.
> Grounded in statistical learning, Python-based
  development and system design.
> Research is only finished when it deploys.
# ─────────────────────────────────────────────
$ _
```

</td>
</tr>
</table>

<img src="./assets/wave.svg" width="100%" alt="">

### `>` INSTALLING TECH STACK

<img src="./assets/stack.svg" width="100%" alt="animated tech-stack loading bars">

<div align="center">
<img src="https://skillicons.dev/icons?i=python,c,cpp,sklearn,js,html,css,nodejs,supabase,docker,git,github,vercel,netlify,linux,vscode&theme=dark&perline=8" alt="Tech stack icons">
</div>

<table>
<tr><th width="26%" align="left">Layer</th><th align="left">Tools</th></tr>
<tr>
<td><b>Languages</b></td>
<td>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="">
<img src="https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white" alt="">
<img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="">
<img src="https://img.shields.io/badge/DSA_·_DAA_·_OOPS-30363d?style=flat-square" alt="">
</td>
</tr>
<tr>
<td><b>ML / Data</b></td>
<td>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="">
<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="">
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="">
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="">
</td>
</tr>
<tr>
<td><b>Local AI / Automation</b></td>
<td>
<img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white" alt="">
<img src="https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white" alt="">
<img src="https://img.shields.io/badge/MCP-4B32C3?style=flat-square" alt="">
</td>
</tr>
<tr>
<td><b>Web</b></td>
<td>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="">
<img src="https://img.shields.io/badge/REST_APIs-6e7681?style=flat-square" alt="">
<img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white" alt="">
</td>
</tr>
<tr>
<td><b>Tools / Deploy</b></td>
<td>
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="">
<img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white" alt="">
<img src="https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black" alt="">
<img src="https://img.shields.io/badge/Netlify-00C7B7?style=flat-square&logo=netlify&logoColor=white" alt="">
</td>
</tr>
</table>

<img src="./assets/wave.svg" width="100%" alt="">

### `$ ls ~/projects --detail`

<img src="./assets/projects.svg" width="100%" alt="animated project cards">

<table>
<tr>
<td width="50%" valign="top">

#### 🔍 CryptoSleuth &nbsp;<img src="https://img.shields.io/badge/SIH26183-3fb950?style=flat-square&logoColor=white" alt="">

Real-time identification of fraud-linked crypto exchanges from victim-reported
wallet addresses. **I own the blockchain analysis & transaction tracing engine.**

`Python` `blockchain` `graph analysis`

</td>
<td width="50%" valign="top">

#### 🎬 [TubeTome](https://github.com/Aayush-Ranjan-26/TubeTome)

Full-stack automation bridge that imports YouTube playlists into NotebookLM.

`React` `Express` `Playwright` `Supabase` `YouTube API`

</td>
</tr>
<tr>
<td valign="top">

#### 🏠 [Boston House Price Prediction](https://github.com/Aayush-Ranjan-26/Boston-House-Price-Prediction)

Regression model with scikit-learn pipelines, feature scaling via `scaler.pkl`,
and model persistence for real-time inference through `run.py`.

`scikit-learn` `regression` `MLOps`

</td>
<td valign="top">

#### 💰 Finance Tracker

Full-stack personal finance app — RESTful backend APIs, interactive UI and an
automated test suite with structured reports.

`full-stack` `REST` `testing`

</td>
</tr>
<tr>
<td valign="top">

#### 🛡️ PulseGuard

Automated infrastructure health sentinel and incident response pipeline.

`monitoring` `automation`

</td>
<td valign="top">

#### 📄 DocuFlow AI &nbsp;·&nbsp; 🌱 [GreenPulse](https://github.com/Aayush-Ranjan-26/greenpulse)

Local document summarizer & organizer, plus a responsive sustainability web app
built during a hackathon.

`local AI` `web`

</td>
</tr>
</table>

<div align="center">
<a href="https://github.com/Aayush-Ranjan-26?tab=repositories"><img src="https://img.shields.io/badge/browse_all_repositories-0d1117?style=for-the-badge&logo=github&logoColor=3fb950" alt="All repos"></a>
</div>

<img src="./assets/wave.svg" width="100%" alt="">

### `$ cat ./credentials.log`

<img src="./assets/credentials.svg" width="100%" alt="animated education and certifications timeline">

<table>
<tr><th width="22%" align="left">When</th><th align="left">What</th><th width="26%" align="left">Where</th></tr>
<tr><td><b>2024 — 2028</b></td><td><b>B.Tech — Artificial Intelligence & Machine Learning</b> · CGPA 8.2</td><td>SRM, Ghaziabad NCR</td></tr>
<tr><td><b>2024</b></td><td>Higher Secondary — Science (PCM), First Division</td><td>Kendriya Vidyalaya, INA</td></tr>
<tr><td>Feb 2026</td><td>SnowStoorm Hackathon</td><td>—</td></tr>
<tr><td>Oct 2025</td><td>Oracle Certified Foundations Associate</td><td>Oracle</td></tr>
<tr><td>Aug 2025</td><td>Python (Basic)</td><td>HackerRank</td></tr>
<tr><td>Jun 2025</td><td>Solutions Architecture Job Simulation</td><td>Forage</td></tr>
<tr><td>Jan 2025</td><td>Python: Zero to Hero Bootcamp</td><td>Devtown</td></tr>
</table>

<img src="./assets/wave.svg" width="100%" alt="">

<div align="center">

### `>` GITHUB TELEMETRY

<img src="https://github-readme-stats.vercel.app/api?username=Aayush-Ranjan-26&show_icons=true&count_private=true&hide_border=true&bg_color=0d1117&title_color=3fb950&icon_color=58a6ff&text_color=c9d1d9" height="170" alt="Stats">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Aayush-Ranjan-26&layout=compact&langs_count=8&hide_border=true&bg_color=0d1117&title_color=3fb950&text_color=c9d1d9" height="170" alt="Top languages">

<img src="https://streak-stats.demolab.com?user=Aayush-Ranjan-26&hide_border=true&background=0d1117&stroke=21304a&ring=3fb950&fire=58a6ff&currStreakLabel=3fb950&sideLabels=c9d1d9&dates=6e7681" width="70%" alt="Streak">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=Aayush-Ranjan-26&bg_color=0d1117&color=c9d1d9&line=3fb950&point=58a6ff&area=true&area_color=3fb950&hide_border=true" width="100%" alt="Activity graph">

<img src="https://github-profile-trophy.vercel.app/?username=Aayush-Ranjan-26&theme=matrix&no-frame=true&no-bg=true&margin-w=6&column=7" alt="Trophies">

</div>

<p align="center">
  <img src="./assets/contribution-heatmap.svg" width="100%" alt="animated contribution heatmap">
</p>

<img src="./assets/wave.svg" width="100%" alt="">

### `$ ./connect.sh`

```
aayush@dev:~$ ./connect.sh --establish-uplink

  [ github   ]  https://github.com/Aayush-Ranjan-26
  [ linkedin ]  https://www.linkedin.com/in/aayush-ranjan-dev
  [ email    ]  Aayushranjan26092006@gmail.com
  [ location ]  Ghaziabad, India
  [ open-to  ]  ML · Data Science · AI Engineering internships

  > channel open. say hi anytime.
aayush@dev:~$ _
```

<img src="./assets/wave.svg" width="100%" alt="">

<p align="center"><code>// thanks for dropping into my terminal — may your builds be green and your bugs be few //</code></p>
"""

# --- assets/aayush-terminal-card.svg -----------------------------
FILE_ASSETS_AAYUSH_TERMINAL_CARD_SVG = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" width="1000" height="500" role="img" aria-label="Aayush Ranjan — animated terminal profile card">
  <defs>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#3fb950" stop-opacity="0.55"/>
      <stop offset="50%" stop-color="#58a6ff" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#3fb950" stop-opacity="0.55"/>
      <animate attributeName="x1" values="0;1;0" dur="9s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="1;2;1" dur="9s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#58a6ff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#58a6ff" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="#58a6ff" stop-opacity="0"/>
    </linearGradient>

    <clipPath id="c0"><rect x="76" y="128" width="0" height="26"><animate attributeName="width" values="0;120" dur="0.5s" begin="0.3s" fill="freeze"/></rect></clipPath>
    <clipPath id="c1"><rect x="76" y="170" width="0" height="26"><animate attributeName="width" values="0;640" dur="0.75s" begin="1.0s" fill="freeze"/></rect></clipPath>
    <clipPath id="c2"><rect x="76" y="212" width="0" height="26"><animate attributeName="width" values="0;640" dur="0.75s" begin="1.85s" fill="freeze"/></rect></clipPath>
    <clipPath id="c3"><rect x="76" y="254" width="0" height="26"><animate attributeName="width" values="0;640" dur="0.75s" begin="2.7s" fill="freeze"/></rect></clipPath>
    <clipPath id="c4"><rect x="76" y="296" width="0" height="26"><animate attributeName="width" values="0;680" dur="0.75s" begin="3.55s" fill="freeze"/></rect></clipPath>
    <clipPath id="c5"><rect x="76" y="338" width="0" height="26"><animate attributeName="width" values="0;660" dur="0.75s" begin="4.4s" fill="freeze"/></rect></clipPath>
    <clipPath id="panel"><rect width="1000" height="500" rx="16"/></clipPath>

    <style>
      .m { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; }
      .k { fill: #3fb950; font-size: 19px; }
      .v { fill: #e6edf3; font-size: 19px; }
      .p { fill: #58a6ff; font-size: 19px; }
    </style>
  </defs>

  <g clip-path="url(#panel)">
    <rect width="1000" height="500" rx="16" fill="#0d1117"/>
    <rect x="0.75" y="0.75" width="998.5" height="498.5" rx="16" fill="none" stroke="url(#edge)" stroke-width="1.5"/>

    <rect x="34" y="60" width="932" height="340" rx="12" fill="#161b22"/>
    <path d="M34 72 a12 12 0 0 1 12 -12 h908 a12 12 0 0 1 12 12 v34 h-932 Z" fill="#1c232e"/>
    <line x1="34" y1="106" x2="966" y2="106" stroke="#21262d"/>

    <circle cx="60" cy="83" r="7" fill="#ff5f57"><animate attributeName="opacity" values="1;0.55;1" dur="3.2s" repeatCount="indefinite"/></circle>
    <circle cx="82" cy="83" r="7" fill="#febc2e"><animate attributeName="opacity" values="1;0.55;1" dur="3.2s" begin="0.4s" repeatCount="indefinite"/></circle>
    <circle cx="104" cy="83" r="7" fill="#28c840"><animate attributeName="opacity" values="1;0.55;1" dur="3.2s" begin="0.8s" repeatCount="indefinite"/></circle>

    <text x="500" y="89" text-anchor="middle" class="m" font-size="16" fill="#8b949e">aayush@github: ~/applied-ai</text>

    <g class="m">
      <g clip-path="url(#c0)"><text x="76" y="148" class="p">$ whoami</text></g>
      <g clip-path="url(#c1)">
        <text x="76" y="190" class="k">role</text>
        <text x="216" y="190" class="v">Third-year B.Tech AI/ML student</text>
      </g>
      <g clip-path="url(#c2)">
        <text x="76" y="232" class="k">focus</text>
        <text x="216" y="232" class="v">Applied ML | Local AI | Automation</text>
      </g>
      <g clip-path="url(#c3)">
        <text x="76" y="274" class="k">experience</text>
        <text x="216" y="274" class="v">Software/IT Automation Intern, STPI-HQ</text>
      </g>
      <g clip-path="url(#c4)">
        <text x="76" y="316" class="k">stack</text>
        <text x="216" y="316" class="v">Python | scikit-learn | Pandas | n8n | Ollama | MCP</text>
      </g>
      <g clip-path="url(#c5)">
        <text x="76" y="358" class="k">open_to</text>
        <text x="216" y="358" class="v">ML | Data Science | AI Engineering internships</text>
      </g>
      <text x="76" y="382" class="p" opacity="0">$<animate attributeName="opacity" values="0;1" dur="0.2s" begin="5.2s" fill="freeze"/></text>
    </g>

    <rect x="76" y="130" width="11" height="0" fill="#58a6ff">
      <animate attributeName="height" values="0;24" dur="0.01s" begin="0.3s" fill="freeze"/>
      <animate attributeName="x"
               values="76;196;76;716;76;716;76;716;76;756;76;736;96"
               keyTimes="0;0.06;0.12;0.21;0.27;0.35;0.41;0.49;0.55;0.63;0.69;0.77;0.88"
               dur="6.5s" begin="0.3s" fill="freeze"/>
      <animate attributeName="y"
               values="130;130;172;172;214;214;256;256;298;298;340;340;376"
               keyTimes="0;0.06;0.12;0.21;0.27;0.35;0.41;0.49;0.55;0.63;0.69;0.77;0.88"
               dur="6.5s" begin="0.3s" fill="freeze"/>
      <animate attributeName="opacity" values="1;0;1" dur="1.1s" begin="6.8s" repeatCount="indefinite"/>
    </rect>

    <text x="500" y="452" text-anchor="middle" class="m" font-size="16" fill="#c9d1d9" opacity="0">
      Building practical Machine Learning, local AI workflows, and automation systems.
      <animate attributeName="opacity" values="0;1" dur="0.9s" begin="5.6s" fill="freeze"/>
    </text>

    <rect x="0" y="-120" width="1000" height="120" fill="url(#scan)">
      <animate attributeName="y" values="-120;500" dur="7s" begin="6s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
"""

# --- assets/boot.svg ---------------------------------------------
FILE_ASSETS_BOOT_SVG = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="Boot sequence">
  <defs>
    <linearGradient id="bfill" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3fb950"/><stop offset="100%" stop-color="#58a6ff"/>
    </linearGradient>
    <clipPath id="bp"><rect width="1000" height="300" rx="14"/></clipPath>
    <style>
      .m { font-family: "SFMono-Regular", Consolas, Menlo, monospace; font-size: 14px; }
      .ok { fill: #3fb950; }
      .txt { fill: #c9d1d9; }
      .dim { fill: #6e7681; }
    </style>
  </defs>

  <g clip-path="url(#bp)">
    <rect width="1000" height="300" rx="14" fill="#0d1117"/>
    <rect x="0.5" y="0.5" width="999" height="299" rx="14" fill="none" stroke="#21304a"/>

    <text x="32" y="38" class="m dim">aayush@github:~$ ./boot --profile applied-ai</text>

    <g class="m">
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.2s" begin="0.4s" fill="freeze"/>
        <text x="32" y="70" class="ok">[  OK  ]</text><text x="118" y="70" class="txt">loading python3 &#183; pandas &#183; numpy &#183; scikit-learn</text></g>
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.2s" begin="0.7s" fill="freeze"/>
        <text x="32" y="96" class="ok">[  OK  ]</text><text x="118" y="96" class="txt">initialising ML pipelines &#8212; NLP &#183; computer vision &#183; predictive modeling</text></g>
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.2s" begin="1.0s" fill="freeze"/>
        <text x="32" y="122" class="ok">[  OK  ]</text><text x="118" y="122" class="txt">mounting C / C++ &#183; DSA &#183; DAA &#183; OOPS fundamentals</text></g>
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.2s" begin="1.3s" fill="freeze"/>
        <text x="32" y="148" class="ok">[  OK  ]</text><text x="118" y="148" class="txt">starting local AI runtime (Ollama) + n8n / MCP automation layer</text></g>
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.2s" begin="1.6s" fill="freeze"/>
        <text x="32" y="174" class="ok">[  OK  ]</text><text x="118" y="174" class="txt">connecting REST APIs &#183; Supabase &#183; Docker &#183; Vercel</text></g>
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.2s" begin="1.9s" fill="freeze"/>
        <text x="32" y="200" class="ok">[  OK  ]</text><text x="118" y="200" class="txt">attaching blockchain tracing engine &#8212; CryptoSleuth (SIH26183)</text></g>
    </g>

    <rect x="32" y="224" width="820" height="10" rx="5" fill="#161b22"/>
    <rect x="32" y="224" width="0" height="10" rx="5" fill="url(#bfill)">
      <animate attributeName="width" values="0;820" dur="2.3s" begin="0.4s" fill="freeze"/>
    </rect>
    <text x="870" y="234" class="m dim" opacity="0">100%<animate attributeName="opacity" values="0;1" dur="0.3s" begin="2.7s" fill="freeze"/></text>

    <text x="32" y="268" class="m" fill="#58a6ff" opacity="0">
      system ready &#8212; open to ML, Data Science &amp; AI Engineering internships.
      <animate attributeName="opacity" values="0;1" dur="0.4s" begin="2.8s" fill="freeze"/>
    </text>
    <rect x="512" y="257" width="8" height="14" fill="#58a6ff" opacity="0">
      <animate attributeName="opacity" values="0;1;0" dur="1.1s" begin="2.8s" repeatCount="indefinite"/>
    </rect>

    <rect x="-200" y="0" width="200" height="300" fill="#3fb950" opacity="0.04">
      <animate attributeName="x" values="-200;1000" dur="5s" begin="3s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
"""

# --- assets/ascii-portrait.svg -----------------------------------
FILE_ASSETS_ASCII_PORTRAIT_SVG = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 460" width="420" height="460" role="img" aria-label="ASCII-art portrait">
  <defs>
    <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#3fb950"/><stop offset="100%" stop-color="#58a6ff"/>
    </linearGradient>
    <clipPath id="pp"><rect width="420" height="460" rx="14"/></clipPath>
    <style>
      .a { font-family: "SFMono-Regular", Consolas, Menlo, monospace; font-size: 17px; letter-spacing: 1px; fill: #3fb950; }
      .dim { fill: #1f6f34; }
      .blue { fill: #58a6ff; }
      .m { font-family: "SFMono-Regular", Consolas, Menlo, monospace; }
    </style>
  </defs>

  <g clip-path="url(#pp)">
    <rect width="420" height="460" rx="14" fill="#0d1117"/>
    <rect x="0.5" y="0.5" width="419" height="459" rx="14" fill="none" stroke="#21304a"/>

    <text x="22" y="34" class="m" font-size="13" fill="#8b949e">$ render --ascii ./me.png</text>

    <g transform="translate(210 250)">
      <circle r="150" fill="none" stroke="url(#ring)" stroke-width="1.2" stroke-dasharray="4 16" opacity="0.4">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="30s" repeatCount="indefinite"/>
      </circle>
    </g>

    <g class="a" xml:space="preserve">
      <text x="60" y="76"  opacity="0">   ▄▄██████████▄▄   <animate attributeName="opacity" values="0;1" dur="0.25s" begin="0.2s" fill="freeze"/></text>
      <text x="60" y="98"  opacity="0"> ▄██▀▀        ▀▀██▄ <animate attributeName="opacity" values="0;1" dur="0.25s" begin="0.35s" fill="freeze"/></text>
      <text x="60" y="120" opacity="0">▐█▌  ▄▄▄▄▄▄▄▄▄▄  ▐█▌<animate attributeName="opacity" values="0;1" dur="0.25s" begin="0.5s" fill="freeze"/></text>
      <text x="60" y="142" opacity="0">▐█▌ ██        ██ ▐█▌<animate attributeName="opacity" values="0;1" dur="0.25s" begin="0.65s" fill="freeze"/></text>
      <text x="60" y="164" opacity="0">▐█▌ █  ▄▄▄  ▄▄▄  █ ▐█▌<animate attributeName="opacity" values="0;1" dur="0.25s" begin="0.8s" fill="freeze"/></text>

      <!-- eye row: open / blinking variants -->
      <g>
        <text x="60" y="186" opacity="0">▐█▌ █ █ ● █ █ ● █ █ ▐█▌
          <animate attributeName="opacity" values="0;1" dur="0.25s" begin="0.95s" fill="freeze"/>
          <animate attributeName="opacity" values="1;1;0;1;1;1;0;1;1" keyTimes="0;0.3;0.33;0.36;0.66;0.7;0.73;0.76;1" dur="5.5s" begin="1.3s" repeatCount="indefinite"/>
        </text>
        <text x="60" y="186" opacity="0">▐█▌ █ █ ▬ █ █ ▬ █ █ ▐█▌
          <animate attributeName="opacity" values="0;0;1;0;0;0;1;0;0" keyTimes="0;0.3;0.33;0.36;0.66;0.7;0.73;0.76;1" dur="5.5s" begin="1.3s" repeatCount="indefinite"/>
        </text>
      </g>

      <text x="60" y="208" opacity="0">▐█▌ █  ▀▀▀  ▀▀▀  █ ▐█▌<animate attributeName="opacity" values="0;1" dur="0.25s" begin="1.1s" fill="freeze"/></text>
      <text x="60" y="230" opacity="0">▐█▌ █      ▲     █ ▐█▌<animate attributeName="opacity" values="0;1" dur="0.25s" begin="1.25s" fill="freeze"/></text>
      <text x="60" y="252" opacity="0">▐█▌ █   ╲_____╱   █ ▐█▌<animate attributeName="opacity" values="0;1" dur="0.25s" begin="1.4s" fill="freeze"/></text>
      <text x="60" y="274" opacity="0"> ▀█▄ ██        ██ ▄█▀ <animate attributeName="opacity" values="0;1" dur="0.25s" begin="1.55s" fill="freeze"/></text>
      <text x="60" y="296" opacity="0">   ▀█▄▄██████████▄▄█▀ <animate attributeName="opacity" values="0;1" dur="0.25s" begin="1.7s" fill="freeze"/></text>
      <text x="60" y="318" opacity="0" class="a dim">      ▄████████▄      <animate attributeName="opacity" values="0;1" dur="0.25s" begin="1.85s" fill="freeze"/></text>
      <text x="60" y="340" opacity="0" class="a dim">  ▄████████████████▄  <animate attributeName="opacity" values="0;1" dur="0.25s" begin="2s" fill="freeze"/></text>
      <text x="60" y="362" opacity="0" class="a dim">▄████████████████████▄<animate attributeName="opacity" values="0;1" dur="0.25s" begin="2.15s" fill="freeze"/></text>
    </g>

    <!-- headphone cup indicators -->
    <rect x="66" y="150" width="4" height="120" rx="2" fill="#58a6ff" opacity="0">
      <animate attributeName="opacity" values="0;0.9;0.25;0.9" dur="2.4s" begin="2.3s" repeatCount="indefinite"/>
    </rect>
    <rect x="350" y="150" width="4" height="120" rx="2" fill="#58a6ff" opacity="0">
      <animate attributeName="opacity" values="0;0.25;0.9;0.25" dur="2.4s" begin="2.3s" repeatCount="indefinite"/>
    </rect>

    <text x="22" y="410" class="m" font-size="13" fill="#8b949e" opacity="0">
      resolution: 22x13 · palette: mono
      <animate attributeName="opacity" values="0;1" dur="0.4s" begin="2.4s" fill="freeze"/>
    </text>
    <text x="22" y="434" class="m" font-size="13" fill="#3fb950" opacity="0">
      $ _
      <animate attributeName="opacity" values="0;1;0.2;1" dur="1.2s" begin="2.6s" repeatCount="indefinite"/>
    </text>

    <rect x="0" y="-70" width="420" height="70" fill="#58a6ff" opacity="0.05">
      <animate attributeName="y" values="-70;460" dur="6s" begin="2.5s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
"""

# --- assets/stack.svg --------------------------------------------
FILE_ASSETS_STACK_SVG = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 310" width="1000" height="310" role="img" aria-label="Tech stack loading">
  <defs>
    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3fb950"/><stop offset="100%" stop-color="#58a6ff"/>
    </linearGradient>
    <clipPath id="sp"><rect width="1000" height="310" rx="14"/></clipPath>
    <style>
      .m { font-family: "SFMono-Regular", Consolas, Menlo, monospace; }
      .l { fill: #c9d1d9; font-size: 13.5px; }
      .s { fill: #6e7681; font-size: 11.5px; }
      .p { fill: #8b949e; font-size: 12px; }
    </style>
  </defs>

  <g clip-path="url(#sp)">
  <rect width="1000" height="310" rx="14" fill="#0d1117"/>
  <rect x="0.5" y="0.5" width="999" height="309" rx="14" fill="none" stroke="#21304a"/>

  <text x="32" y="38" class="m" font-size="14" fill="#8b949e">$ pip install --upgrade ./stack</text>

  <g class="m">
    <text x="32" y="76" class="l">Python &#183; ML</text>
    <text x="32" y="92" class="s">pandas &#183; numpy &#183; scikit-learn</text>
    <rect x="300" y="66" width="570" height="9" rx="4.5" fill="#161b22"/>
    <rect x="300" y="66" width="0" height="9" rx="4.5" fill="url(#bar)">
      <animate attributeName="width" values="0;530" dur="1.3s" begin="0.2s" fill="freeze"/>
    </rect>
    <text x="892" y="76" class="p" opacity="0">93%<animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.4s" fill="freeze"/></text>

    <text x="32" y="124" class="l">CS fundamentals</text>
    <text x="32" y="140" class="s">C &#183; C++ &#183; DSA &#183; DAA &#183; OOPS</text>
    <rect x="300" y="114" width="570" height="9" rx="4.5" fill="#161b22"/>
    <rect x="300" y="114" width="0" height="9" rx="4.5" fill="url(#bar)">
      <animate attributeName="width" values="0;496" dur="1.3s" begin="0.35s" fill="freeze"/>
    </rect>
    <text x="892" y="124" class="p" opacity="0">87%<animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.55s" fill="freeze"/></text>

    <text x="32" y="172" class="l">Local AI &#183; Automation</text>
    <text x="32" y="188" class="s">Ollama &#183; n8n &#183; MCP</text>
    <rect x="300" y="162" width="570" height="9" rx="4.5" fill="#161b22"/>
    <rect x="300" y="162" width="0" height="9" rx="4.5" fill="url(#bar)">
      <animate attributeName="width" values="0;467" dur="1.3s" begin="0.5s" fill="freeze"/>
    </rect>
    <text x="892" y="172" class="p" opacity="0">82%<animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.7s" fill="freeze"/></text>

    <text x="32" y="220" class="l">Web development</text>
    <text x="32" y="236" class="s">HTML &#183; CSS &#183; JavaScript &#183; REST APIs</text>
    <rect x="300" y="210" width="570" height="9" rx="4.5" fill="#161b22"/>
    <rect x="300" y="210" width="0" height="9" rx="4.5" fill="url(#bar)">
      <animate attributeName="width" values="0;433" dur="1.3s" begin="0.65s" fill="freeze"/>
    </rect>
    <text x="892" y="220" class="p" opacity="0">76%<animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.85s" fill="freeze"/></text>

    <text x="32" y="268" class="l">Tools &#183; Platforms</text>
    <text x="32" y="284" class="s">Git &#183; Docker &#183; Supabase &#183; Vercel &#183; Render &#183; Netlify</text>
    <rect x="300" y="258" width="570" height="9" rx="4.5" fill="#161b22"/>
    <rect x="300" y="258" width="0" height="9" rx="4.5" fill="url(#bar)">
      <animate attributeName="width" values="0;410" dur="1.3s" begin="0.8s" fill="freeze"/>
    </rect>
    <text x="892" y="268" class="p" opacity="0">72%<animate attributeName="opacity" values="0;1" dur="0.3s" begin="2s" fill="freeze"/></text>
  </g>

  <rect x="-200" y="0" width="200" height="310" fill="#58a6ff" opacity="0.035">
    <animate attributeName="x" values="-200;1000" dur="5.5s" begin="2.4s" repeatCount="indefinite"/>
  </rect>
  </g>
</svg>
"""

# --- assets/projects.svg -----------------------------------------
FILE_ASSETS_PROJECTS_SVG = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" width="1000" height="360" role="img" aria-label="Project cards">
  <defs>
    <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3fb950" stop-opacity="0"/>
      <stop offset="50%" stop-color="#3fb950" stop-opacity="0.13"/>
      <stop offset="100%" stop-color="#3fb950" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="p"><rect width="1000" height="360" rx="14"/></clipPath>
    <style>
      .m { font-family: "SFMono-Regular", Consolas, Menlo, monospace; }
      .t { fill: #e6edf3; font-size: 15.5px; font-weight: 700; }
      .d { fill: #8b949e; font-size: 12px; }
      .g { fill: #3fb950; font-size: 10.5px; }
    </style>
  </defs>

  <g clip-path="url(#p)">
    <rect width="1000" height="360" rx="14" fill="#0d1117"/>
    <rect x="0.5" y="0.5" width="999" height="359" rx="14" fill="none" stroke="#21304a"/>

    <text x="32" y="38" class="m" font-size="14" fill="#8b949e">$ ls ~/projects --detail</text>
    <rect x="228" y="27" width="8" height="14" fill="#58a6ff"><animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></rect>

    <g class="m">
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.45s" begin="0.25s" fill="freeze"/>
        <rect x="32" y="58" width="456" height="82" rx="10" fill="#161b22" stroke="#21304a"/>
        <rect x="32" y="58" width="3.5" height="82" rx="2" fill="#3fb950"/>
        <text x="52" y="84" class="t">CryptoSleuth &#183; SIH26183</text>
        <text x="52" y="104" class="d">Real-time identification of fraud-linked crypto exchanges</text>
        <text x="52" y="122" class="d">from victim-reported wallets. I own the tracing engine.</text>
        <text x="390" y="84" class="g">blockchain &#183; ML</text>
      </g>

      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.45s" begin="0.5s" fill="freeze"/>
        <rect x="512" y="58" width="456" height="82" rx="10" fill="#161b22" stroke="#21304a"/>
        <rect x="512" y="58" width="3.5" height="82" rx="2" fill="#58a6ff"/>
        <text x="532" y="84" class="t">TubeTome</text>
        <text x="532" y="104" class="d">Full-stack bridge importing YouTube playlists into</text>
        <text x="532" y="122" class="d">NotebookLM. React, Express, Playwright, Supabase, YT API.</text>
        <text x="862" y="84" class="g" fill="#58a6ff">automation</text>
      </g>

      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.45s" begin="0.75s" fill="freeze"/>
        <rect x="32" y="152" width="456" height="82" rx="10" fill="#161b22" stroke="#21304a"/>
        <rect x="32" y="152" width="3.5" height="82" rx="2" fill="#d29922"/>
        <text x="52" y="178" class="t">Boston House Price Prediction</text>
        <text x="52" y="198" class="d">Regression model with scikit-learn pipelines, feature</text>
        <text x="52" y="216" class="d">scaling and model persistence for real-time inference.</text>
        <text x="410" y="178" class="g" fill="#d29922">ML</text>
      </g>

      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.45s" begin="1.0s" fill="freeze"/>
        <rect x="512" y="152" width="456" height="82" rx="10" fill="#161b22" stroke="#21304a"/>
        <rect x="512" y="152" width="3.5" height="82" rx="2" fill="#a371f7"/>
        <text x="532" y="178" class="t">Finance Tracker</text>
        <text x="532" y="198" class="d">Full-stack personal finance app &#8212; RESTful backend,</text>
        <text x="532" y="216" class="d">interactive UI and an automated test suite.</text>
        <text x="856" y="178" class="g" fill="#a371f7">full-stack</text>
      </g>

      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.45s" begin="1.25s" fill="freeze"/>
        <rect x="32" y="246" width="456" height="82" rx="10" fill="#161b22" stroke="#21304a"/>
        <rect x="32" y="246" width="3.5" height="82" rx="2" fill="#f778ba"/>
        <text x="52" y="272" class="t">PulseGuard</text>
        <text x="52" y="292" class="d">Automated infrastructure health sentinel and</text>
        <text x="52" y="310" class="d">incident response pipeline.</text>
        <text x="392" y="272" class="g" fill="#f778ba">monitoring</text>
      </g>

      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.45s" begin="1.5s" fill="freeze"/>
        <rect x="512" y="246" width="456" height="82" rx="10" fill="#161b22" stroke="#21304a"/>
        <rect x="512" y="246" width="3.5" height="82" rx="2" fill="#39d0d8"/>
        <text x="532" y="272" class="t">DocuFlow AI &#183; GreenPulse</text>
        <text x="532" y="292" class="d">Local document summarizer &amp; organizer, plus a</text>
        <text x="532" y="310" class="d">responsive sustainability web app built at a hackathon.</text>
        <text x="856" y="272" class="g" fill="#39d0d8">local AI &#183; web</text>
      </g>
    </g>

    <rect x="-220" y="0" width="220" height="360" fill="url(#sweep)">
      <animate attributeName="x" values="-220;1000" dur="5.5s" begin="1.9s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
"""

# --- assets/credentials.svg --------------------------------------
FILE_ASSETS_CREDENTIALS_SVG = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 330" width="1000" height="330" role="img" aria-label="Education and certifications timeline">
  <defs>
    <linearGradient id="spine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3fb950"/><stop offset="100%" stop-color="#58a6ff"/>
    </linearGradient>
    <clipPath id="cp"><rect width="1000" height="330" rx="14"/></clipPath>
    <style>
      .m { font-family: "SFMono-Regular", Consolas, Menlo, monospace; }
      .h { fill: #e6edf3; font-size: 14.5px; font-weight: 700; }
      .s { fill: #8b949e; font-size: 12px; }
      .y { fill: #3fb950; font-size: 11.5px; }
      .d { fill: #6e7681; font-size: 13px; }
    </style>
  </defs>

  <g clip-path="url(#cp)">
    <rect width="1000" height="330" rx="14" fill="#0d1117"/>
    <rect x="0.5" y="0.5" width="999" height="329" rx="14" fill="none" stroke="#21304a"/>

    <text x="32" y="36" class="m d">$ cat ./credentials.log</text>

    <!-- spine draws in -->
    <line x1="60" y1="60" x2="60" y2="300" stroke="url(#spine)" stroke-width="2"
          stroke-dasharray="240" stroke-dashoffset="240">
      <animate attributeName="stroke-dashoffset" values="240;0" dur="1.6s" begin="0.2s" fill="freeze"/>
    </line>

    <g class="m">
      <!-- education -->
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="0.6s" fill="freeze"/>
        <circle cx="60" cy="76" r="6" fill="#0d1117" stroke="#3fb950" stroke-width="2.5">
          <animate attributeName="r" values="6;8;6" dur="2.6s" begin="0.6s" repeatCount="indefinite"/>
        </circle>
        <text x="88" y="72" class="h">B.Tech &#8212; Artificial Intelligence &amp; Machine Learning</text>
        <text x="88" y="92" class="s">SRM, Ghaziabad NCR &#183; C.G.P.A 8.2 (till 2nd year)</text>
        <text x="850" y="72" class="y">2024 &#8212; 2028</text>
      </g>

      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="0.9s" fill="freeze"/>
        <circle cx="60" cy="128" r="6" fill="#0d1117" stroke="#58a6ff" stroke-width="2.5"/>
        <text x="88" y="124" class="h">Higher Secondary &#8212; Science (PCM)</text>
        <text x="88" y="144" class="s">Kendriya Vidyalaya, INA Market &#183; First Division</text>
        <text x="850" y="124" class="y" fill="#58a6ff">2024</text>
      </g>

      <!-- certifications -->
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.2s" fill="freeze"/>
        <circle cx="60" cy="180" r="5" fill="#3fb950"/>
        <text x="88" y="184" class="s" fill="#c9d1d9">Oracle Certified Foundations Associate</text>
        <text x="850" y="184" class="y">Oct 2025</text>
      </g>
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.4s" fill="freeze"/>
        <circle cx="60" cy="210" r="5" fill="#3fb950"/>
        <text x="88" y="214" class="s" fill="#c9d1d9">Python (Basic) &#8212; HackerRank</text>
        <text x="850" y="214" class="y">Aug 2025</text>
      </g>
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.6s" fill="freeze"/>
        <circle cx="60" cy="240" r="5" fill="#3fb950"/>
        <text x="88" y="244" class="s" fill="#c9d1d9">Solutions Architecture Job Simulation &#8212; Forage</text>
        <text x="850" y="244" class="y">Jun 2025</text>
      </g>
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.8s" fill="freeze"/>
        <circle cx="60" cy="270" r="5" fill="#3fb950"/>
        <text x="88" y="274" class="s" fill="#c9d1d9">Python: Zero to Hero Bootcamp &#8212; Devtown</text>
        <text x="850" y="274" class="y">Jan 2025</text>
      </g>
      <g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="2.0s" fill="freeze"/>
        <circle cx="60" cy="300" r="5" fill="#58a6ff">
          <animate attributeName="opacity" values="1;0.35;1" dur="2.2s" begin="2s" repeatCount="indefinite"/>
        </circle>
        <text x="88" y="304" class="s" fill="#c9d1d9">SnowStoorm Hackathon</text>
        <text x="850" y="304" class="y" fill="#58a6ff">Feb 2026</text>
      </g>
    </g>

    <rect x="-180" y="0" width="180" height="330" fill="#58a6ff" opacity="0.035">
      <animate attributeName="x" values="-180;1000" dur="6s" begin="2.4s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
"""


FILES = {
    "README.md": FILE_README_MD,
    "assets/aayush-terminal-card.svg": FILE_ASSETS_AAYUSH_TERMINAL_CARD_SVG,
    "assets/boot.svg": FILE_ASSETS_BOOT_SVG,
    "assets/ascii-portrait.svg": FILE_ASSETS_ASCII_PORTRAIT_SVG,
    "assets/stack.svg": FILE_ASSETS_STACK_SVG,
    "assets/projects.svg": FILE_ASSETS_PROJECTS_SVG,
    "assets/credentials.svg": FILE_ASSETS_CREDENTIALS_SVG,
}


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Build the Aayush Ranjan GitHub profile from this single file.")
    parser.add_argument("--out", default=os.path.dirname(os.path.abspath(__file__)),
                        help="output directory (default: this file's folder)")
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would be written, write nothing")
    parser.add_argument("--no-clobber", action="store_true",
                        help="skip files that already exist")
    args = parser.parse_args(argv)

    payload = dict(FILES)
    payload["assets/wave.svg"] = build_wave()

    written = skipped = 0
    for relpath in sorted(payload):
        target = os.path.join(args.out, relpath)
        exists = os.path.exists(target)

        if args.dry_run:
            note = "  (would overwrite)" if exists else ""
            print("  would write   " + relpath + note)
            continue

        if exists and args.no_clobber:
            print("  skipped       " + relpath + "  (already exists)")
            skipped += 1
            continue

        parent = os.path.dirname(target)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(target, "w", encoding="utf-8") as handle:
            handle.write(payload[relpath])
        size = len(payload[relpath].encode("utf-8"))
        print("  wrote         {0}  ({1:,} bytes)".format(relpath, size))
        written += 1

    if args.dry_run:
        print("\ndry run - nothing written.")
        return 0

    print("\n{0} file(s) written, {1} skipped, into {2}".format(written, skipped, args.out))
    print("note: assets/contribution-heatmap.svg is produced by your existing")
    print("      GitHub Action, so this script leaves it alone.")
    print('next: git add -A && git commit -m "profile" && git push')
    return 0


if __name__ == "__main__":
    sys.exit(main())
