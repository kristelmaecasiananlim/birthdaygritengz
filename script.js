// Data
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
