import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday Sheena Marie</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="phase-night">
    
    <!-- Background Environments -->
    <div class="sky-container">
        <!-- Night elements -->
        <div class="stars" id="stars"></div>
        
        <!-- Day elements -->
        <div class="clouds day-element">
            <!-- Simplified vector clouds matching the image -->
            <svg class="cloud c1" viewBox="0 0 120 60"><path fill="#ffffff" d="M20,40 Q20,20 40,20 Q45,5 65,10 Q85,0 100,20 Q115,20 115,35 Q115,50 100,50 L30,50 Q10,50 20,40 Z" opacity="0.6"/></svg>
            <svg class="cloud c2" viewBox="0 0 120 60"><path fill="#ffffff" d="M20,40 Q20,20 40,20 Q45,5 65,10 Q85,0 100,20 Q115,20 115,35 Q115,50 100,50 L30,50 Q10,50 20,40 Z" opacity="0.4"/></svg>
            <svg class="cloud c3" viewBox="0 0 120 60"><path fill="#ffffff" d="M20,40 Q20,20 40,20 Q45,5 65,10 Q85,0 100,20 Q115,20 115,35 Q115,50 100,50 L30,50 Q10,50 20,40 Z" opacity="0.5"/></svg>
        </div>
        
        <!-- Butterflies in the day sky -->
        <div class="butterflies day-element" id="butterflies"></div>
    </div>

    <!-- UI Overlay container -->
    <div class="ui-layer">
        
        <!-- Phase 1: Input -->
        <div class="central-card active-phase" id="inputPhase">
            <h1 class="serif-title">Sheena Marie</h1>
            <p class="subtitle">Who is your best friend?</p>
            
            <div class="input-wrapper">
                <input type="text" id="answerInput" placeholder="Your answer..." autocomplete="off">
                <button id="submitBtn">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </button>
            </div>
            <p id="statusMessage" class="status-msg"></p>
        </div>

        <!-- Phase 2: Cake -->
        <div class="cake-container hidden-phase" id="cakePhase">
            <div class="cake">
                <div class="plate"></div>
                <div class="layer layer-bottom"></div>
                <div class="layer layer-top"></div>
                <!-- Candles injected here -->
                <div class="candles" id="candlesContainer"></div>
            </div>
            <p class="instruction-text">Make a wish and blow out the candles.</p>
        </div>
        
        <!-- Phase 3: Field Instruction -->
        <div class="field-instruction hidden-phase" id="fieldInstruction">
            <p class="serif-title small">Click each tulip</p>
            <p class="subtitle">to bloom your memories.</p>
        </div>

    </div>
    
    <!-- Phase 3: The Tulip Field -->
    <div class="flower-field day-element" id="flowerField"></div>

    <!-- Memory Modal -->
    <div class="modal hidden" id="imageModal">
        <div class="modal-bg" id="modalBg"></div>
        <div class="modal-content">
            <button class="close-btn" id="closeBtn">&times;</button>
            <img id="modalImg" src="" alt="Memory">
            <p id="modalTxt" class="serif-title small italic mt-4"></p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

css_content = """/* ============================
   DESIGN SYSTEM
   ============================ */
:root {
    /* Night Palette */
    --night-bg: #0a0f1a;
    --night-card: rgba(15, 20, 35, 0.4);
    --night-border: rgba(255, 255, 255, 0.08);
    --text-main: #fcfcfc;
    --text-muted: #9ca3af;
    
    /* Day Palette (Matching Image) */
    --sky-day-top: #65b3e3;
    --sky-day-mid: #9bcdef;
    --sky-day-bot: #cbe6f8;
    
    /* Typography */
    --font-sans: 'Outfit', sans-serif;
    --font-serif: 'Playfair Display', serif;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    font-family: var(--font-sans);
    color: var(--text-main);
    background-color: var(--night-bg);
    transition: background-color 2.5s ease-in-out;
}

body.phase-day {
    background-color: var(--sky-day-bot);
}

/* ============================
   ENVIRONMENT
   ============================ */
.sky-container {
    position: absolute;
    inset: 0;
    z-index: 1;
    pointer-events: none;
}

body.phase-day .sky-container {
    background: linear-gradient(180deg, var(--sky-day-top) 0%, var(--sky-day-mid) 40%, var(--sky-day-bot) 100%);
}

.stars {
    position: absolute;
    inset: 0;
    background-image: 
        radial-gradient(1px 1px at 15% 25%, white, transparent),
        radial-gradient(1.5px 1.5px at 35% 55%, rgba(255,255,255,0.8), transparent),
        radial-gradient(1px 1px at 65% 15%, rgba(255,255,255,0.9), transparent),
        radial-gradient(2px 2px at 85% 45%, rgba(255,255,255,0.6), transparent),
        radial-gradient(1px 1px at 45% 85%, white, transparent),
        radial-gradient(1.5px 1.5px at 75% 75%, rgba(255,255,255,0.7), transparent);
    background-size: 250px 250px;
    opacity: 1;
    transition: opacity 2s ease;
}

body.phase-day .stars {
    opacity: 0;
}

.day-element {
    opacity: 0;
    visibility: hidden;
    transition: opacity 2s ease 0.5s, visibility 2s ease 0.5s;
}

body.phase-day .day-element {
    opacity: 1;
    visibility: visible;
}

/* Clouds matching the flat vector style */
.cloud {
    position: absolute;
    animation: drift linear infinite;
}
.c1 { top: 12%; left: 10%; width: 140px; animation-duration: 45s; }
.c2 { top: 22%; left: 50%; width: 180px; animation-duration: 65s; animation-delay: -10s; }
.c3 { top: 8%; left: 80%; width: 120px; animation-duration: 35s; animation-delay: -5s; }

@keyframes drift {
    0% { transform: translateX(100vw); }
    100% { transform: translateX(-200px); }
}

/* Butterflies */
.butterflies {
    position: absolute;
    inset: 0;
    z-index: 10;
}
.butterfly {
    position: absolute;
    width: 20px;
    height: 18px;
    transform-origin: center;
    animation: flutterFly var(--dur) ease-in-out infinite alternate;
}
.b-wing {
    position: absolute;
    top: 0;
    width: 10px;
    height: 18px;
    background-color: #f8fafc;
    border-radius: 50% 50% 10% 80%;
    transform-origin: right center;
    animation: flapWing 0.15s infinite alternate ease-in-out;
    box-shadow: inset -1px 0 3px rgba(0,0,0,0.1);
}
.b-wing.right {
    left: 10px;
    border-radius: 50% 50% 80% 10%;
    transform-origin: left center;
}

@keyframes flapWing {
    0% { transform: rotateY(10deg); }
    100% { transform: rotateY(70deg); }
}
@keyframes flutterFly {
    0% { transform: translate(0, 0) rotate(10deg) scale(0.8); }
    100% { transform: translate(80px, -40px) rotate(-10deg) scale(1.1); }
}

/* ============================
   UI & TYPOGRAPHY
   ============================ */
.ui-layer {
    position: relative;
    z-index: 20;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none; /* Let clicks pass to field */
}

/* Phases */
.active-phase {
    opacity: 1;
    transform: translateY(0);
    pointer-events: auto;
    transition: all 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.hidden-phase {
    opacity: 0 !important;
    transform: translateY(20px) !important;
    pointer-events: none !important;
    position: absolute;
}

/* Text Styles */
.serif-title {
    font-family: var(--font-serif);
    font-size: 3.5rem;
    font-weight: 400;
    letter-spacing: -0.02em;
    margin-bottom: 0.25rem;
    color: #fff;
}
.serif-title.small {
    font-size: 2.2rem;
}
.serif-title.italic {
    font-style: italic;
    color: #1e293b;
}

.subtitle {
    font-size: 1.1rem;
    color: var(--text-muted);
    font-weight: 300;
    margin-bottom: 2.5rem;
    letter-spacing: 0.05em;
}

/* Phase 1: Clean Glass Card */
.central-card {
    background: var(--night-card);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--night-border);
    padding: 3.5rem 4rem;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 30px 60px rgba(0,0,0,0.4);
}

.input-wrapper {
    display: flex;
    align-items: center;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 6px;
    transition: border-color 0.3s;
}
.input-wrapper:focus-within {
    border-color: rgba(255,255,255,0.3);
    background: rgba(255,255,255,0.05);
}

input[type="text"] {
    background: transparent;
    border: none;
    color: #fff;
    font-size: 1.05rem;
    padding: 10px 16px;
    width: 240px;
    outline: none;
    font-family: var(--font-sans);
    font-weight: 300;
}
input[type="text"]::placeholder {
    color: rgba(255,255,255,0.3);
}

#submitBtn {
    background: #fff;
    color: #000;
    border: none;
    border-radius: 8px;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: transform 0.2s, background 0.2s;
}
#submitBtn:hover {
    transform: scale(1.05);
    background: #f0f0f0;
}
#submitBtn:active {
    transform: scale(0.95);
}

.status-msg {
    margin-top: 1rem;
    height: 20px;
    font-size: 0.9rem;
    color: #f87171;
    font-weight: 400;
}

/* ============================
   CAKE PHASE (Minimal & Elegant)
   ============================ */
.cake-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.cake {
    position: relative;
    width: 220px;
    height: 160px;
    margin-bottom: 2rem;
}

.plate {
    position: absolute;
    bottom: -15px;
    left: 50%;
    transform: translateX(-50%);
    width: 260px;
    height: 12px;
    background: #2a2c35;
    border-radius: 50%;
    box-shadow: 0 15px 30px rgba(0,0,0,0.5);
}

.layer {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    background: #e2e8f0;
    border-radius: 8px;
}
.layer::after {
    content: '';
    position: absolute;
    top: -5px;
    left: 0;
    width: 100%;
    height: 10px;
    background: #f8fafc;
    border-radius: 50%;
}
.layer-bottom {
    width: 200px;
    height: 70px;
    bottom: 0;
}
.layer-top {
    width: 150px;
    height: 60px;
    bottom: 70px;
    background: #cbd5e1;
}

.candles {
    position: absolute;
    bottom: 130px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 25px;
    z-index: 5;
}

.candle {
    position: relative;
    width: 8px;
    height: 45px;
    background: #fef08a; /* Yellowish candle */
    border-radius: 4px;
    cursor: pointer;
}

.flame {
    position: absolute;
    top: -22px;
    left: -4px;
    width: 16px;
    height: 24px;
    background: #fcd34d;
    border-radius: 50% 50% 20% 20%;
    box-shadow: 0 0 15px 2px rgba(252, 211, 77, 0.6);
    animation: flicker 0.12s infinite alternate ease-in-out;
    transform-origin: bottom center;
}

.flame.out {
    animation: putOut 0.5s forwards ease-out;
}

@keyframes flicker {
    0% { transform: scale(1) rotate(-2deg); }
    100% { transform: scale(1.05) rotate(2deg); opacity: 0.9; }
}

@keyframes putOut {
    0% { opacity: 1; transform: scale(1) translateY(0); filter: grayscale(0%); }
    100% { opacity: 0; transform: scale(0) translateY(-10px); filter: grayscale(100%); }
}

.instruction-text {
    font-size: 1.05rem;
    color: rgba(255,255,255,0.7);
    letter-spacing: 0.02em;
}

/* ============================
   TULIP FIELD PHASE
   ============================ */
.field-instruction {
    text-align: center;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem 3rem;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.05);
}

.field-instruction .serif-title {
    color: #1e293b;
}

.field-instruction .subtitle {
    color: #475569;
    margin-bottom: 0;
}

.flower-field {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100vw;
    height: 50vh; /* Bottom half of screen */
    z-index: 10;
    display: flex;
    align-items: flex-end;
    justify-content: space-evenly;
    pointer-events: auto;
}

.tulip-wrapper {
    position: relative;
    transform-origin: bottom center;
    cursor: pointer;
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tulip-wrapper:hover {
    transform: scale(1.05) translateY(-5px);
}

.tulip-wrapper.bloomed {
    transform: scale(1.1);
    z-index: 50 !important;
}

/* Flat Vector Tulip Styles (Matching Reference) */
.t-stem {
    fill: #7dae59; /* lively green */
}
.t-leaf {
    fill: #689947; 
}
.t-leaf-front {
    fill: #85ba5f;
}

/* Base petals */
.t-petal-back { fill: currentColor; filter: brightness(0.85); }
.t-petal-main { fill: currentColor; }
.t-petal-left { fill: currentColor; filter: brightness(0.95); }
.t-petal-right { fill: currentColor; filter: brightness(0.9); }

/* Color classes mapping to specific HEX matching image */
.c-red { color: #e94b4b; }
.c-pink { color: #f28bab; }
.c-yellow { color: #f8c946; }
.c-orange { color: #f08b3e; }
.c-purple { color: #a46abf; }
.c-white { color: #f8fbfb; }

/* Memory Bubble Animation */
.memory-node {
    position: absolute;
    top: 15%;
    left: 50%;
    transform: translate(-50%, 0) scale(0);
    width: 70px;
    height: 70px;
    border-radius: 50%;
    overflow: hidden;
    border: 3px solid #fff;
    box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    opacity: 0;
    transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    z-index: 10;
}

.bloomed .memory-node {
    transform: translate(-50%, -90px) scale(1);
    opacity: 1;
}

.memory-node img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* ============================
   MODAL
   ============================ */
.modal {
    position: fixed;
    inset: 0;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: auto;
}

.modal-bg {
    position: absolute;
    inset: 0;
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    transition: opacity 0.4s ease;
}

.modal-content {
    position: relative;
    background: #fff;
    padding: 1.5rem;
    border-radius: 16px;
    box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 90vw;
    max-height: 90vh;
    transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.hidden.modal {
    pointer-events: none;
}
.hidden .modal-bg {
    opacity: 0;
}
.hidden .modal-content {
    transform: scale(0.9);
    opacity: 0;
}

#modalImg {
    max-width: 100%;
    max-height: 65vh;
    border-radius: 8px;
    object-fit: contain;
}

.mt-4 { margin-top: 1.5rem; }

.close-btn {
    position: absolute;
    top: -15px;
    right: -15px;
    width: 36px;
    height: 36px;
    background: #1e293b;
    color: #fff;
    border: none;
    border-radius: 50%;
    font-size: 20px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.2s;
}
.close-btn:hover {
    transform: scale(1.1);
}

/* ============================
   RESPONSIVE
   ============================ */
@media (max-width: 768px) {
    .central-card { padding: 2.5rem 2rem; }
    .serif-title { font-size: 2.8rem; }
    .input-wrapper input { width: 180px; }
    .flower-field { height: 40vh; }
    .tulip-wrapper { transform: scale(0.85); transform-origin: bottom center; }
    .tulip-wrapper:hover { transform: scale(0.9) translateY(-2px); }
    .tulip-wrapper.bloomed { transform: scale(0.95); }
}
"""

js_content = """// Data
const validAnswers = ['lim', 'kristel', 'kristel mae', 'kristel mae c. lim', 'kristel mae c lim', 'kristel mae lim'];

// Tulip Colors matching reference: Red, Pink, Yellow, White, Purple, Orange
const tulipFieldDesign = [
    { msg: "Best titang ina", color: "c-red", scale: 0.9, height: 220 },
    { msg: "Best driver", color: "c-pink", scale: 1.0, height: 250 },
    { msg: "Best table tennis player", color: "c-yellow", scale: 0.85, height: 200 },
    { msg: "Best dancer (murag si Niana)", color: "c-white", scale: 1.1, height: 260 },
    { msg: "Best teacher", color: "c-purple", scale: 0.95, height: 230 },
    { msg: "Best runner", color: "c-orange", scale: 0.85, height: 210 },
    { msg: "Best listener", color: "c-red", scale: 1.0, height: 240 },
    { msg: "Best yapper", color: "c-yellow", scale: 0.9, height: 220 },
    { msg: "Best daughter", color: "c-white", scale: 1.05, height: 255 },
    { msg: "Best sister", color: "c-orange", scale: 0.95, height: 230 },
    { msg: "Best silingan", color: "c-purple", scale: 0.85, height: 200 },
    { msg: "And the best best friend!", color: "c-white", scale: 1.1, height: 270 }
];

const imageUrls = [
    'sheena_photos/17729b7b-5448-4660-bc4a-1dbb4039db44.jpg',
    'sheena_photos/2050014f-2911-438f-a066-027cbe2b50bf.jpg',
    'sheena_photos/2794e4a1-d7b9-4de8-94cf-93c13568b6e2.jpg',
    'sheena_photos/4582b689-e309-428d-8a34-ac5e96a153df.jpg',
    'sheena_photos/6c07251e-40fd-4286-948d-4d08509ef4c4.jpg',
    'sheena_photos/80602776-5e96-4646-b243-d54234560f0f.jpg',
    'sheena_photos/8f54b507-f192-4a52-9235-cb8ec120af20.jpg',
    'sheena_photos/a183e4ea-b861-493e-8959-7760a688ce72.jpg',
    'sheena_photos/b4d64ad0-99b2-452d-a7dd-85369c58dab6.jpg',
    'sheena_photos/b6ca4881-96d1-411f-8f02-8e7245f6ebf7.jpg',
    'sheena_photos/e342aae9-90ba-469e-bd60-5757c23c5128.jpg',
    'sheena_photos/ef5cbad5-95ac-4e7a-8203-0247716b268e.jpg'
];

let cakeBlown = false;

document.addEventListener('DOMContentLoaded', () => {
    initInputPhase();
    generateButterflies();
    generateCandles(2);
});

/* =================================
   PHASE 1: INPUT
   ================================= */
function initInputPhase() {
    const btn = document.getElementById('submitBtn');
    const input = document.getElementById('answerInput');
    
    input.focus();
    
    btn.addEventListener('click', checkAnswer);
    input.addEventListener('keypress', e => {
        if (e.key === 'Enter') checkAnswer();
    });
}

function checkAnswer() {
    const input = document.getElementById('answerInput');
    const msg = document.getElementById('statusMessage');
    const ans = input.value.trim().toLowerCase();
    
    if (!ans) {
        msg.textContent = "Please enter an answer.";
        return;
    }
    
    if (validAnswers.includes(ans)) {
        msg.textContent = "";
        goToCakePhase();
    } else {
        msg.textContent = "Hmm, that's not quite right. Try again!";
        input.value = "";
        input.focus();
    }
}

/* =================================
   PHASE 2: CAKE
   ================================= */
function goToCakePhase() {
    document.getElementById('inputPhase').classList.replace('active-phase', 'hidden-phase');
    document.getElementById('cakePhase').classList.replace('hidden-phase', 'active-phase');
    
    // Auto blow setup
    setTimeout(() => {
        document.body.addEventListener('click', blowAllCandles, { once: true });
    }, 1000);
}

function generateCandles(count) {
    const container = document.getElementById('candlesContainer');
    container.innerHTML = '';
    for (let i = 0; i < count; i++) {
        container.innerHTML += `
            <div class="candle" onclick="blowCandle(this)">
                <div class="flame"></div>
            </div>
        `;
    }
}

function blowCandle(el) {
    if (el.dataset.blown) return;
    el.dataset.blown = 'true';
    el.querySelector('.flame').classList.add('out');
    checkAllBlown();
}

function blowAllCandles() {
    if (cakeBlown) return;
    document.querySelectorAll('.candle').forEach(c => blowCandle(c));
}

function checkAllBlown() {
    if (cakeBlown) return;
    const total = document.querySelectorAll('.candle').length;
    const blown = document.querySelectorAll('.candle[data-blown="true"]').length;
    
    if (total === blown) {
        cakeBlown = true;
        setTimeout(goToFieldPhase, 1200);
    }
}

/* =================================
   PHASE 3: FIELD & DAYTIME
   ================================= */
function goToFieldPhase() {
    document.getElementById('cakePhase').classList.replace('active-phase', 'hidden-phase');
    document.body.classList.replace('phase-night', 'phase-day');
    
    // Show instruction briefly
    const instr = document.getElementById('fieldInstruction');
    instr.classList.replace('hidden-phase', 'active-phase');
    setTimeout(() => {
        instr.classList.replace('active-phase', 'hidden-phase');
    }, 4000);
    
    generateField();
}

function generateField() {
    const field = document.getElementById('flowerField');
    field.innerHTML = '';
    
    tulipFieldDesign.forEach((item, index) => {
        const wrap = document.createElement('div');
        wrap.className = `tulip-wrapper ${item.color}`;
        
        // Z-index to layer them organically based on scale
        const z = Math.floor(item.scale * 10);
        wrap.style.zIndex = z;
        wrap.style.transform = `scale(${item.scale})`;

        // Flat Vector Design SVG matching the attached image style
        wrap.innerHTML = `
            <svg width="60" height="${item.height}" viewBox="0 0 60 ${item.height}" style="overflow:visible;">
                <!-- Stem -->
                <rect x="27" y="60" width="6" height="${item.height - 60}" class="t-stem" />
                
                <!-- Leaves (Vector style pointing up) -->
                <!-- Left Leaf -->
                <path d="M27 120 C 15 100, 5 60, 10 50 C 15 65, 25 80, 27 100 Z" class="t-leaf"/>
                <!-- Right Leaf -->
                <path d="M33 130 C 45 110, 55 70, 50 60 C 45 75, 35 90, 33 110 Z" class="t-leaf-front"/>

                <!-- Tulip Head -->
                <g transform="translate(10, 10)">
                    <!-- Back part of cup -->
                    <path d="M 5,20 C 5,50  35,50 35,20 C 25,10 15,10 5,20 Z" class="t-petal-back"/>
                    <!-- Main Cup -->
                    <path d="M 0,25 C 0,55  40,55 40,25 C 40,15 30,5 20,5 C 10,5 0,15 0,25 Z" class="t-petal-main"/>
                    <!-- Left Petal detail -->
                    <path d="M 0,25 C 0,50  20,55 20,25 C 20,15 10,5 0,15 Z" class="t-petal-left"/>
                    <!-- Right Petal detail -->
                    <path d="M 40,25 C 40,50 20,55 20,25 C 20,15 30,5 40,15 Z" class="t-petal-right"/>
                </g>
            </svg>
            <div class="memory-node">
                <img src="${imageUrls[index % imageUrls.length]}" alt="Memory">
            </div>
        `;
        
        wrap.addEventListener('click', () => {
            wrap.classList.add('bloomed');
            setTimeout(() => {
                openModal(imageUrls[index % imageUrls.length], item.msg);
                wrap.classList.remove('bloomed');
            }, 500);
        });

        field.appendChild(wrap);
    });
}

function generateButterflies() {
    const container = document.getElementById('butterflies');
    for (let i=0; i<4; i++) {
        const b = document.createElement('div');
        b.className = 'butterfly';
        b.style.left = (20 + Math.random() * 60) + 'vw';
        b.style.top = (10 + Math.random() * 30) + 'vh';
        b.style.setProperty('--dur', (5 + Math.random() * 3) + 's');
        b.innerHTML = '<div class="b-wing left"></div><div class="b-wing right"></div>';
        container.appendChild(b);
    }
}

/* =================================
   MODAL
   ================================= */
const modal = document.getElementById('imageModal');
const mImg = document.getElementById('modalImg');
const mTxt = document.getElementById('modalTxt');

function openModal(src, text) {
    mImg.src = src;
    mTxt.textContent = text;
    modal.classList.remove('hidden');
}

function closeModal() {
    modal.classList.add('hidden');
    setTimeout(() => mImg.src = '', 400); 
}

document.getElementById('closeBtn').addEventListener('click', closeModal);
document.getElementById('modalBg').addEventListener('click', closeModal);
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css_content)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Rewrite done with highly aesthetic vector field")
