// Configuração do ScrollReveal
const sr = ScrollReveal({
    distance: '50px',
    duration: 1500,
    easing: 'cubic-bezier(0.5, 0, 0, 1)',
    reset: false // Animação ocorre apenas uma vez
});

// Animação dos elementos da página
sr.reveal('.home-text', { origin: 'left' });
sr.reveal('.home-image', { origin: 'right', delay: 200 });

sr.reveal('h2', { origin: 'top' });

sr.reveal('.project-card', { interval: 200, origin: 'bottom' });
sr.reveal('.skills-grid', { origin: 'bottom', delay: 200 });
sr.reveal('.about-content', { origin: 'left' });
sr.reveal('.contact-content', { origin: 'right' });

sr.reveal('.quote', { scale: 0.85 });