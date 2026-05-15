---
marp: true
theme: default
paginate: true
html: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

  :root {
    --navy: #1A1A33;
    --orange: #FF6745;
    --lime: #DDFF45;
    --cyan: #00E5EE;
    --purple: #C445FF;
    --violet: #7657FF;
    --offwhite: #E8E7E1;
    --black: #000000;
    --white: #FFFFFF;
    --card: #252540;
    --border: #2E2E50;
    --body: #B0AFCC;
    --muted: #6B6A8A;
  }

  section {
    background: var(--navy);
    color: var(--white);
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    padding: 52px 68px;
    padding-top: 70px;
    line-height: 1.45;
    position: relative;
    overflow: hidden;
  }

  section::before {
    content: '';
    position: absolute;
    top: 28px;
    left: 52px;
    width: 88px;
    height: 27px;
    background-image: url('./assets/liora_logo_white.svg');
    background-repeat: no-repeat;
    background-position: left center;
    background-size: contain;
    z-index: 10;
    pointer-events: none;
  }

  section.light {
    background: var(--offwhite);
    color: var(--navy);
  }
  section.light::before { background-image: url('./assets/liora_logo_navy.svg'); }
  section.light h1 { color: var(--navy); }
  section.light h2, section.light p, section.light li { color: #3A3A55; }
  section.light h3 { color: #6B6A8A; }
  section.light .card { background: var(--white); border-color: rgba(26,26,51,0.14); }
  section.light .muted { color: #6B6A8A; }
  section.light code { background: rgba(26,26,51,0.08); color: var(--violet); }

  section.lead, section.dark-end {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 60px 80px;
  }
  section.lead::before, section.dark-end::before { display: none; }
  section.transition {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    background: var(--orange);
    color: var(--white);
    padding: 52px 68px;
  }
  section.transition::before { background-image: url('./assets/liora_logo_white.svg'); }
  section.transition h1 { color: var(--white); font-size: 3em; }
  section.transition h2 { color: rgba(255,255,255,0.76); }
  section.transition h3 { color: rgba(255,255,255,0.58); }

  h1 {
    font-family: 'Work Sans', sans-serif;
    font-weight: 800;
    font-size: 2.65em;
    line-height: 1.08;
    color: var(--white);
    margin: 0 0 0.18em 0;
  }
  h2 {
    font-family: 'Inter', sans-serif;
    font-weight: 300;
    font-size: 1.08em;
    color: var(--body);
    margin: 0 0 0.5em 0;
  }
  h3 {
    font-family: 'Work Sans', sans-serif;
    font-weight: 600;
    font-size: 0.58em;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.18em;
    margin: 0 0 0.55em 0;
  }
  p, li { color: var(--body); font-size: 0.78em; }
  ul, ol { padding-left: 1.2em; margin: 0; }
  li { margin-bottom: 0.25em; }
  li::marker { color: var(--orange); }
  strong { color: var(--orange); font-weight: 700; }
  em { color: var(--lime); font-style: normal; font-weight: 600; }
  code { background: var(--card); color: var(--lime); padding: 2px 7px; border-radius: 4px; font-size: 0.84em; }
  footer { font-size: 0.43em; color: var(--muted); }
  section::after { color: var(--muted); font-size: 0.48em; }

  .tag {
    font-family: 'Work Sans', sans-serif;
    font-weight: 700;
    font-size: 0.5em;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 4px;
    display: inline-block;
  }
  .tag-orange { background: rgba(255,103,69,0.18); color: var(--orange); border: 1px solid var(--orange); }
  .tag-lime { background: rgba(221,255,69,0.14); color: var(--lime); border: 1px solid var(--lime); }
  .tag-cyan { background: rgba(0,229,238,0.14); color: var(--cyan); border: 1px solid var(--cyan); }
  .tag-violet { background: rgba(118,87,255,0.18); color: var(--violet); border: 1px solid var(--violet); }
  .light .tag-lime { color: var(--navy); background: rgba(221,255,69,0.62); }

  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; align-items: stretch; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
  .card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 18px 20px;
  }
  .card-title {
    font-family: 'Work Sans', sans-serif;
    font-size: 0.72em;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 8px;
  }
  .light .card-title { color: var(--navy); }
  .metric {
    font-family: 'Work Sans', sans-serif;
    font-size: 1.9em;
    font-weight: 800;
    color: var(--orange);
    line-height: 1;
  }
  .muted { color: var(--body); font-size: 0.66em; }
  .small { font-size: 0.66em; }
  .photo {
    min-height: 148px;
    border-radius: 8px;
    background-position: center;
    background-size: cover;
    position: relative;
    overflow: hidden;
  }
  .photo::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(26,26,51,0.82), rgba(26,26,51,0.32));
  }
  .pipeline {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-top: 18px;
  }
  .step {
    border: 1px solid var(--border);
    background: var(--card);
    border-radius: 8px;
    padding: 16px;
    min-height: 118px;
  }
  .step-num {
    font-family: 'Work Sans', sans-serif;
    color: var(--lime);
    font-weight: 800;
    font-size: 1.15em;
  }
  .bar {
    height: 16px;
    border-radius: 4px;
    background: rgba(255,255,255,0.08);
    overflow: hidden;
    margin: 6px 0 12px 0;
  }
  .bar span { display: block; height: 100%; background: var(--orange); }
  .light .bar { background: rgba(26,26,51,0.12); }

footer: "Masterclass SQL & Data Warehousing · Data Engineering"
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

<div style="position:absolute;inset:0;background:url('https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1280&q=80') center/cover no-repeat;filter:brightness(0.45) saturate(0.75);z-index:0;"></div>
<div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(26,26,51,0.95) 0%,rgba(26,26,51,0.78) 55%,rgba(0,229,238,0.28) 100%);z-index:1;"></div>

<div style="position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;gap:16px;width:100%;">
  <img src="./assets/liora_logo_white.svg" width="126" style="display:block;">
  <span class="tag tag-cyan">Masterclass · Data Engineering</span>
  <h1 style="font-size:3.05em;margin:0;color:#FFFFFF;">SQL & Data<br>Warehousing</h1>
  <h2 style="max-width:650px;margin:0;color:#B0AFCC;">Comprendre comment passer de données opérationnelles dispersées à une base analytique exploitable</h2>
  <div style="display:flex;gap:8px;margin-top:4px;">
    <span class="tag tag-orange">OLTP → OLAP</span>
    <span class="tag tag-lime">SQLite · Streamlit · Docker</span>
  </div>
</div>

---

<!-- _class: light -->

### Objectifs du module

# Ce que vous allez pouvoir faire

<div class="grid-3" style="margin-top:18px;">
  <div class="card">
    <div class="metric">01</div>
    <div class="card-title">Lire une architecture data</div>
    <p class="muted">Identifier les sources, les flux et le rôle d'une base analytique.</p>
  </div>
  <div class="card">
    <div class="metric">02</div>
    <div class="card-title">Modéliser pour analyser</div>
    <p class="muted">Distinguer faits, dimensions et schéma en étoile.</p>
  </div>
  <div class="card">
    <div class="metric">03</div>
    <div class="card-title">Interroger avec SQL</div>
    <p class="muted">Extraire, joindre, agréger et contextualiser des indicateurs.</p>
  </div>
</div>

<div style="display:flex;gap:10px;margin-top:22px;">
  <span class="tag tag-orange">Hors périmètre : MLOps</span>
  <span class="tag tag-violet">Environnement : aperçu Docker</span>
</div>

---

<!-- _class: transition -->
<!-- _paginate: false -->

### Partie 1

# Penser comme un Data Engineer

## La donnée devient utile quand elle circule, se transforme et reste fiable.

---

### Data Engineering

# La chaîne de valeur

<div class="grid-2" style="margin-top:14px;">
  <div>
    <div class="pipeline" style="grid-template-columns:1fr;gap:10px;margin-top:0;">
      <div class="step"><div class="step-num">Collecte</div><p class="small">Capturer des données depuis applications, fichiers, API ou logs.</p></div>
      <div class="step"><div class="step-num">Stockage</div><p class="small">Rendre les données accessibles, sécurisées et historisées.</p></div>
      <div class="step"><div class="step-num">Transformation</div><p class="small">Nettoyer, encoder, joindre et préparer les données pour l'analyse.</p></div>
    </div>
  </div>
  <div>
    <div class="photo" style="background-image:url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=700&q=75');"></div>
    <div class="card" style="margin-top:12px;">
      <div class="card-title">Ce qui change tout</div>
      <p class="muted">Le Data Engineer ne produit pas seulement des tables : il construit des chemins fiables entre les systèmes et les usages analytiques.</p>
    </div>
  </div>
</div>

---

### Data Warehousing

# Lake, Warehouse, Mart

<div class="grid-3" style="margin-top:20px;">
  <div class="card">
    <div class="metric">Lake</div>
    <div class="card-title">Données brutes</div>
    <p class="muted">Grand volume, formats variés, usage exploratoire ou préparation amont.</p>
  </div>
  <div class="card">
    <div class="metric">DW</div>
    <div class="card-title">Analyse structurée</div>
    <p class="muted">Stockage optimisé pour requêtes, indicateurs et données semi-structurées.</p>
  </div>
  <div class="card">
    <div class="metric">Mart</div>
    <div class="card-title">Vue métier</div>
    <p class="muted">Sous-ensemble adapté aux besoins d'un service ou d'un domaine.</p>
  </div>
</div>

<div style="margin-top:20px;">
  <div class="bar"><span style="width:34%;background:#00E5EE;"></span></div>
  <div class="bar"><span style="width:70%;background:#FF6745;"></span></div>
  <div class="bar"><span style="width:48%;background:#DDFF45;"></span></div>
</div>

---

<!-- _class: light -->

### Besoins d'entreprise

# OLTP versus OLAP

<div class="grid-2" style="margin-top:16px;">
  <div class="card">
    <div class="card-title">OLTP · opérations</div>
    <ul>
      <li>Transactions traitées en temps réel</li>
      <li>Bases fréquemment mises à jour</li>
      <li>Exemples : commande, sinistre, inscription</li>
    </ul>
  </div>
  <div class="card">
    <div class="card-title">OLAP · analyse</div>
    <ul>
      <li>KPI construits à partir des opérations</li>
      <li>Données historisées et agrégées</li>
      <li>Exemples : ventes, visites, souscriptions</li>
    </ul>
  </div>
</div>

<div class="card" style="margin-top:18px;">
  <div class="card-title">Point clé</div>
  <p class="muted">Les bases analytiques sont construites à partir des bases opérationnelles. Le passage OLTP → OLAP est le coeur du data warehousing.</p>
</div>

---

### Modèle relationnel

# Tables et relations

<div style="display:flex;gap:24px;align-items:center;margin-top:16px;">
  <div style="flex:1.15;">
    <div class="card">
      <div class="card-title">Trois objectifs</div>
      <ul>
        <li>Des données <strong>valides</strong></li>
        <li>Des données <strong>faciles à retrouver</strong></li>
        <li>Une base que plusieurs équipes peuvent <strong>alimenter</strong></li>
      </ul>
    </div>
    <p class="muted" style="margin-top:12px;">On sépare les données en tables, puis on représente leurs relations avec des identifiants.</p>
  </div>
  <div style="flex:1;">
    <div><svg viewBox="0 0 470 250" width="470" height="250"><rect x="18" y="24" width="132" height="84" rx="8" fill="#252540" stroke="#FF6745"/><text x="42" y="58" fill="#FFFFFF" font-family="Work Sans" font-size="18" font-weight="700">Clients</text><text x="42" y="84" fill="#B0AFCC" font-family="Inter" font-size="13">client_id</text><rect x="300" y="24" width="132" height="84" rx="8" fill="#252540" stroke="#00E5EE"/><text x="324" y="58" fill="#FFFFFF" font-family="Work Sans" font-size="18" font-weight="700">Produits</text><text x="324" y="84" fill="#B0AFCC" font-family="Inter" font-size="13">product_id</text><rect x="152" y="142" width="168" height="88" rx="8" fill="#252540" stroke="#DDFF45"/><text x="190" y="176" fill="#FFFFFF" font-family="Work Sans" font-size="18" font-weight="700">Commandes</text><text x="184" y="202" fill="#B0AFCC" font-family="Inter" font-size="12">client_id · product_id</text><path d="M126 108 L180 146" stroke="#FF6745" stroke-width="3"/><path d="M340 108 L292 146" stroke="#00E5EE" stroke-width="3"/></svg></div>
  </div>
</div>

---

### Modélisation analytique

# Schéma en étoile

<div class="grid-2" style="margin-top:16px;align-items:center;">
  <div>
    <div><svg viewBox="0 0 480 300" width="480" height="300"><rect x="174" y="104" width="132" height="88" rx="8" fill="#FF6745"/><text x="205" y="138" fill="#FFFFFF" font-family="Work Sans" font-size="18" font-weight="800">Faits</text><text x="196" y="166" fill="#FFFFFF" font-family="Inter" font-size="13">commandes</text><rect x="22" y="20" width="124" height="70" rx="8" fill="#252540" stroke="#00E5EE"/><text x="48" y="58" fill="#FFFFFF" font-family="Work Sans" font-size="16" font-weight="700">Clients</text><rect x="334" y="20" width="124" height="70" rx="8" fill="#252540" stroke="#DDFF45"/><text x="358" y="58" fill="#FFFFFF" font-family="Work Sans" font-size="16" font-weight="700">Produits</text><rect x="22" y="218" width="124" height="70" rx="8" fill="#252540" stroke="#C445FF"/><text x="54" y="256" fill="#FFFFFF" font-family="Work Sans" font-size="16" font-weight="700">Dates</text><rect x="334" y="218" width="124" height="70" rx="8" fill="#252540" stroke="#7657FF"/><text x="352" y="256" fill="#FFFFFF" font-family="Work Sans" font-size="16" font-weight="700">Canaux</text><path d="M146 76 L182 116" stroke="#00E5EE" stroke-width="2.5"/><path d="M334 76 L298 116" stroke="#DDFF45" stroke-width="2.5"/><path d="M146 238 L182 178" stroke="#C445FF" stroke-width="2.5"/><path d="M334 238 L298 178" stroke="#7657FF" stroke-width="2.5"/></svg></div>
  </div>
  <div>
    <div class="card">
      <div class="card-title">Table de faits</div>
      <p class="muted">Le processus opérationnel à mesurer : commandes, visites, souscriptions.</p>
    </div>
    <div class="card" style="margin-top:12px;">
      <div class="card-title">Tables de dimensions</div>
      <p class="muted">Le contexte qui rend les statistiques lisibles : client, produit, date, canal.</p>
    </div>
  </div>
</div>

---

<!-- _class: transition -->
<!-- _paginate: false -->

### Partie 2

# Construire le flux

## Extraire, transformer, charger : le passage de l'opérationnel à l'analytique.

---

### Pipeline ETL

# Le modèle opérationnel

<div class="pipeline">
  <div class="step">
    <div class="step-num">E</div>
    <div class="card-title">Extract</div>
    <p class="small">Identifier les sources et extraire vers une zone intermédiaire.</p>
  </div>
  <div class="step">
    <div class="step-num">T</div>
    <div class="card-title">Transform</div>
    <p class="small">Encoder, nettoyer, joindre et structurer les données.</p>
  </div>
  <div class="step">
    <div class="step-num">L</div>
    <div class="card-title">Load</div>
    <p class="small">Charger vers la base cible pour les requêtes analytiques.</p>
  </div>
  <div class="step">
    <div class="step-num">Q</div>
    <div class="card-title">Quality</div>
    <p class="small">Contrôler exactitude, cohérence et fiabilité avant usage.</p>
  </div>
</div>

<div class="card" style="margin-top:18px;">
  <div class="card-title">Démo du repo</div>
  <p class="muted">Le flux peut être montré avec <strong>SQLite</strong> pour la base, <strong>Streamlit</strong> pour l'interface et <strong>Docker</strong> pour figer l'environnement.</p>
</div>

---

<!-- _class: light -->

### SQL

# Interroger la base

<div class="grid-2" style="margin-top:16px;">
  <div class="card">
    <div class="card-title">Commandes essentielles</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:0.76em;color:#3A3A55;">
      <code>SELECT</code><span>extraire</span>
      <code>INSERT</code><span>ajouter</span>
      <code>UPDATE</code><span>modifier</span>
      <code>DELETE</code><span>supprimer</span>
      <code>CREATE TABLE</code><span>structurer</span>
      <code>JOIN</code><span>relier</span>
    </div>
  </div>
  <div class="card">
    <div class="card-title">Requête analytique</div>
    <pre style="font-size:0.62em;line-height:1.45;margin:0;background:rgba(26,26,51,0.06);padding:14px;border-radius:8px;"><code>SELECT d.month, SUM(f.amount) AS ca
FROM fact_orders f
JOIN dim_date d ON f.date_id = d.id
GROUP BY d.month
ORDER BY d.month;</code></pre>
  </div>
</div>

<p class="muted" style="margin-top:14px;">SQL permet de passer d'une base relationnelle à une question métier mesurable.</p>

---

### Jointures

# Donner du contexte

<div class="grid-2" style="margin-top:16px;align-items:center;">
  <div>
    <div><svg viewBox="0 0 500 250" width="500" height="250"><rect x="32" y="36" width="150" height="178" rx="8" fill="#252540" stroke="#FF6745"/><text x="68" y="70" fill="#FFFFFF" font-family="Work Sans" font-size="18" font-weight="800">Commandes</text><text x="58" y="104" fill="#B0AFCC" font-family="Inter" font-size="13">order_id</text><text x="58" y="132" fill="#DDFF45" font-family="Inter" font-size="13">client_id</text><text x="58" y="160" fill="#B0AFCC" font-family="Inter" font-size="13">amount</text><rect x="318" y="36" width="150" height="178" rx="8" fill="#252540" stroke="#00E5EE"/><text x="362" y="70" fill="#FFFFFF" font-family="Work Sans" font-size="18" font-weight="800">Clients</text><text x="348" y="104" fill="#DDFF45" font-family="Inter" font-size="13">client_id</text><text x="348" y="132" fill="#B0AFCC" font-family="Inter" font-size="13">segment</text><text x="348" y="160" fill="#B0AFCC" font-family="Inter" font-size="13">country</text><path d="M182 124 C230 88 270 88 318 124" stroke="#DDFF45" stroke-width="4" fill="none"/><text x="220" y="78" fill="#DDFF45" font-family="Work Sans" font-size="16" font-weight="700">JOIN</text></svg></div>
  </div>
  <div>
    <div class="card">
      <div class="card-title">Sans jointure</div>
      <p class="muted">Une commande reste un événement isolé.</p>
    </div>
    <div class="card" style="margin-top:12px;">
      <div class="card-title">Avec jointure</div>
      <p class="muted">On sait quel segment, pays ou produit explique le résultat.</p>
    </div>
  </div>
</div>

---

<!-- _class: light -->

### Environnement

# Pourquoi Docker ici

<div class="grid-3" style="margin-top:18px;">
  <div class="card">
    <div class="metric">1</div>
    <div class="card-title">Même runtime</div>
    <p class="muted">La démo démarre pareil sur Windows, macOS ou Linux.</p>
  </div>
  <div class="card">
    <div class="metric">2</div>
    <div class="card-title">Dépendances isolées</div>
    <p class="muted">Streamlit, drivers et scripts restent dans un conteneur.</p>
  </div>
  <div class="card">
    <div class="metric">3</div>
    <div class="card-title">Déploiement simple</div>
    <p class="muted">Une commande lance l'application et la base SQLite.</p>
  </div>
</div>

<p class="muted" style="margin-top:18px;">On garde cette partie comme contexte d'environnement, sans entrer dans le cycle de vie MLOps.</p>

---

### Atelier

# Démo Data Engineering

<div class="grid-2" style="margin-top:16px;">
  <div>
    <div class="photo" style="background-image:url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=700&q=75');"></div>
    <div class="card" style="margin-top:12px;">
      <div class="card-title">Fil rouge</div>
      <p class="muted">Charger des données opérationnelles dans SQLite, les transformer, puis exposer des KPI dans Streamlit.</p>
    </div>
  </div>
  <div class="pipeline" style="grid-template-columns:1fr;gap:10px;margin-top:0;">
    <div class="step"><div class="step-num">01</div><p class="small">Créer les tables sources et dimensions.</p></div>
    <div class="step"><div class="step-num">02</div><p class="small">Écrire les requêtes de jointure et d'agrégation.</p></div>
    <div class="step"><div class="step-num">03</div><p class="small">Afficher les KPI et filtres métier dans Streamlit.</p></div>
  </div>
</div>

---

### Synthèse

# Ce qu'il faut retenir

<div class="grid-2" style="margin-top:16px;">
  <div class="card">
    <div class="card-title">Architecture mentale</div>
    <ul>
      <li>OLTP alimente OLAP</li>
      <li>Le warehouse structure l'analyse</li>
      <li>Les dimensions donnent le contexte</li>
    </ul>
  </div>
  <div class="card">
    <div class="card-title">Compétence pratique</div>
    <ul>
      <li>Modéliser les faits et dimensions</li>
      <li>Construire un ETL lisible</li>
      <li>Questionner les données avec SQL</li>
    </ul>
  </div>
</div>

<div style="margin-top:22px;">
  <div class="bar"><span style="width:25%;background:#00E5EE;"></span></div>
  <div class="bar"><span style="width:58%;background:#FF6745;"></span></div>
  <div class="bar"><span style="width:100%;background:#DDFF45;"></span></div>
</div>

---

<!-- _class: dark-end -->
<!-- _paginate: false -->
<!-- _footer: '' -->

<div style="position:absolute;inset:0;background:url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1280&q=80') center/cover no-repeat;filter:brightness(0.45) saturate(0.75);z-index:0;"></div>
<div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(26,26,51,0.96) 0%,rgba(26,26,51,0.82) 62%,rgba(255,103,69,0.34) 100%);z-index:1;"></div>

<div style="position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;gap:16px;">
  <img src="./assets/liora_logo_white.svg" width="126" style="display:block;">
  <span class="tag tag-lime">Module terminé</span>
  <h1 style="color:#DDFF45;margin:0;">Place à la démo</h1>
  <h2 style="max-width:620px;color:#B0AFCC;">Docker lance l'environnement, SQLite porte les données, Streamlit rend les indicateurs visibles.</h2>
</div>
