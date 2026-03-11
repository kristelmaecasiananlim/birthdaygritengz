// ============================
// QUESTION & INPUT HANDLING
// ============================

let cakeHasBeenBlown = false;
let particleCanvas, particleCtx;
let particles = [];

const validAnswers = [
    'lim',
    'kristel',
    'kristel mae',
    'kristel mae c. lim',
    'kristel mae c lim',
    'kristel mae lim'
];

// ============================
// INITIALIZE
// ============================

document.addEventListener('DOMContentLoaded', () => {
    initializeParticles();
    setupAnswerInput();
    updateStatus('');
});

function setupAnswerInput() {
    const answerInput = document.getElementById('answerInput');
    const submitBtn = document.getElementById('submitBtn');
    
    answerInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            checkAnswer();
        }
    });

    submitBtn.addEventListener('click', checkAnswer);

    answerInput.focus();
}

// ============================
// ANSWER VALIDATION
// ============================

function checkAnswer() {
    if (cakeHasBeenBlown) return;

    const answerInput = document.getElementById('answerInput');
    const submitBtn = document.getElementById('submitBtn');
    const userAnswer = answerInput.value.trim().toLowerCase();

    if (!userAnswer) {
        updateStatus('Please enter your answer!');
        return;
    }

    // Check if answer matches any of the valid answers
    const isCorrect = validAnswers.some(validAnswer => userAnswer === validAnswer);

    if (isCorrect) {
        updateStatus('✨ Correct! Happy Birthday Sheena! ✨');
        answerInput.disabled = true;
        submitBtn.disabled = true;
        triggerBirthdayTransition();
    } else {
        updateStatus(`Hmm, that's not quite right. Try again!`);
        answerInput.value = '';
        answerInput.focus();
    }
}

// ============================
// BIRTHDAY TRANSITION
// ============================

function triggerBirthdayTransition() {
    cakeHasBeenBlown = true;

    // Extinguish flames
    const flames = document.querySelectorAll('.flame');
    flames.forEach((flame, index) => {
        setTimeout(() => {
            flame.classList.add('extinguished');
        }, index * 100);
    });

    // Hide cake after delay
    setTimeout(() => {
        const cakeSection = document.getElementById('cakeSection');
        cakeSection.classList.add('hidden');

        // Show bouquet
        const bouquetSection = document.getElementById('bouquetSection');
        bouquetSection.classList.remove('hidden');

        // Generate bouquet with images
        generateBouquetWithImages();

        // Update footer
        document.getElementById('footerMessage').textContent = 'Click the petals to see your memories together';

        // Trigger celebration particles
        triggerCelebration();
    }, 1200);
}

// ============================
// BOUQUET WITH IMAGE PETALS
// ============================

const petalMessages = [
    "My ride or die",
    "You're my person",
    "Forever grateful",
    "You get me",
    "My soul sister",
    "Best decision ever",
    "Always here for me",
    "You make me better",
    "Life without you? Nope",
    "My day just started",
    "You're everything",
    "Happy Birthday, bestie"
];

function generateBouquetWithImages() {
    const petalsContainer = document.getElementById('petalsContainer');
    petalsContainer.innerHTML = '';

    const petalCount = 12;
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
        'sheena_photos/ef5cbad5-95ac-4e7a-8203-0247716b268e.jpg',
    ];

    for (let i = 0; i < petalCount; i++) {
        const petal = document.createElement('div');
        petal.className = 'petal';

        const angle = (i / petalCount) * Math.PI * 2;
        
        // Responsive radius based on screen size
        let radius = 210;
        if (window.innerWidth < 768) {
            radius = 170;
        }
        if (window.innerWidth < 480) {
            radius = 140;
        }
        
        const x = Math.cos(angle) * radius;
        const y = Math.sin(angle) * radius;

        const imageUrl = imageUrls[i % imageUrls.length];

        petal.innerHTML = `<img src="${imageUrl}" alt="Memory ${i + 1}">`;
        petal.style.translate = `${x}px ${y}px`;

        petal.addEventListener('click', () => onPetalClick(petal, i));
        petal.addEventListener('mouseenter', () => {
            if (!petal.classList.contains('expanded')) {
                petal.style.translate = `${x}px ${y}px`;
                petal.style.transform = `scale(1.1)`;
            }
        });
        petal.addEventListener('mouseleave', () => {
            if (!petal.classList.contains('expanded')) {
                petal.style.transform = `scale(1)`;
            }
        });

        petalsContainer.appendChild(petal);
    }
}

function onPetalClick(petal, index) {
    // Remove previous expanded state
    document.querySelectorAll('.petal.expanded').forEach(p => {
        p.classList.remove('expanded');
    });
    document.querySelectorAll('.petal-message').forEach(msg => {
        msg.remove();
    });

    // Expand the clicked petal
    petal.classList.add('expanded');
    petal.style.transform = `scale(1.4)`;

    // Show message
    const message = petalMessages[index];
    const messageEl = document.createElement('div');
    messageEl.className = 'petal-message';
    messageEl.textContent = message;

    const rect = petal.getBoundingClientRect();
    messageEl.style.left = (rect.left + rect.width / 2 - 75) + 'px';
    messageEl.style.top = (rect.top - 80) + 'px';

    document.body.appendChild(messageEl);

    // Create particle burst
    createPetalBurst(petal);

    // Hide message after 3 seconds
    setTimeout(() => {
        messageEl.style.animation = 'fadeOut 0.4s ease forwards';
        setTimeout(() => {
            messageEl.remove();
            petal.classList.remove('expanded');
        }, 400);
    }, 3000);
}

// ============================
// PARTICLE SYSTEM
// ============================

function initializeParticles() {
    particleCanvas = document.getElementById('particleCanvas');
    particleCtx = particleCanvas.getContext('2d');

    particleCanvas.width = window.innerWidth;
    particleCanvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
        particleCanvas.width = window.innerWidth;
        particleCanvas.height = window.innerHeight;
    });

    animateParticles();
}

function createPetalBurst(element) {
    const rect = element.getBoundingClientRect();
    const x = rect.left + rect.width / 2;
    const y = rect.top + rect.height / 2;

    const colors = ['#dc2626', '#db2777', '#7c3aed', '#2563eb', '#059669', '#ca8a04'];

    for (let i = 0; i < 12; i++) {
        const angle = (i / 12) * Math.PI * 2;
        const velocity = 2 + Math.random() * 4;

        particles.push({
            x: x,
            y: y,
            vx: Math.cos(angle) * velocity,
            vy: Math.sin(angle) * velocity,
            life: 1,
            size: 4 + Math.random() * 4,
            color: colors[Math.floor(Math.random() * colors.length)]
        });
    }
}

function triggerCelebration() {
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;

    const colors = ['#dc2626', '#db2777', '#7c3aed', '#2563eb', '#059669', '#fbbf24'];

    for (let i = 0; i < 50; i++) {
        const angle = (Math.random()) * Math.PI * 2;
        const velocity = 3 + Math.random() * 6;

        particles.push({
            x: centerX,
            y: centerY,
            vx: Math.cos(angle) * velocity,
            vy: Math.sin(angle) * velocity,
            life: 1,
            size: 6 + Math.random() * 6,
            color: colors[Math.floor(Math.random() * colors.length)]
        });
    }
}

function animateParticles() {
    particleCtx.clearRect(0, 0, particleCanvas.width, particleCanvas.height);

    particles = particles.filter(p => p.life > 0);

    particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.15; // gravity
        p.life -= 0.015;

        particleCtx.globalAlpha = p.life;
        particleCtx.fillStyle = p.color;
        particleCtx.beginPath();
        particleCtx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        particleCtx.fill();
    });

    particleCtx.globalAlpha = 1;
    requestAnimationFrame(animateParticles);
}

// ============================
// UI HELPERS
// ============================

function updateStatus(message) {
    const statusEl = document.getElementById('status');
    if (statusEl) {
        statusEl.textContent = message;
    }
}

// ============================
// ANIMATIONS
// ============================

const style = document.createElement('style');
style.textContent = `
    @keyframes petalClick {
        0% {
            transform: scale(1);
            opacity: 1;
        }
        50% {
            transform: scale(1.15);
            opacity: 0.9;
        }
        100% {
            transform: scale(1);
            opacity: 1;
        }
    }
    
    @keyframes fadeOut {
        from {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
        to {
            opacity: 0;
            transform: scale(0.9) translateY(-20px);
        }
    }
`;
document.head.appendChild(style);
